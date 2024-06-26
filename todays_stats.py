import argparse
import os
import constants as c

from datetime import date
from pathlib import Path
from report_parser import parse_report
from tabulate import tabulate, SEPARATING_LINE
from utils.naming import get_team_file_name, get_team_name_from_file_name

class TodaysStatsReporter:
    def __init__(self, date_stamp: str, summary=False, suppress=False, group=None):
        self.date_stamp = date_stamp
        self.summary = summary
        self.suppress = suppress

        self.group = group
        team_group = c.TEAM_GROUPS.get(group)
        if team_group is not None:
            self.file_names = list(map(lambda team: get_team_file_name(team), team_group))
        else:
            self.file_names = os.listdir(os.path.join(c.REPORTS_BASE_PATH, self.date_stamp))
        
        self.file_names.sort()

    def get_team_report_path(self, team: str):
        filename = get_team_file_name(team)
        path = os.path.join(c.REPORTS_BASE_PATH, self.date_stamp, filename)
        if not os.path.exists(path) and not self.suppress:
            raise FileNotFoundError(f"File not found: {path}")

        return path

    def find_duplicate_domains(self):
        domains = set()
        duplicate_domains = set()
        for file_name in self.file_names:
            team_table_data = parse_report(
                os.path.join(c.REPORTS_BASE_PATH, self.date_stamp, file_name),
                silent=True,
                suppress=self.suppress
            )
            for row in team_table_data:
                if row == SEPARATING_LINE:
                    continue
                domain = row[0].strip()
                if domain is None or domain == "" or domain == c.TOTAL_STR:
                    continue
                if domain in domains:
                    duplicate_domains.add(domain)
                else:
                    domains.add(domain)

        print("\nDuplicate domains:")
        for domain in duplicate_domains:
            print(f"- {domain}")
        print()

    def print_full_report(self):
        for file_name in self.file_names:
            print(tabulate([get_team_name_from_file_name(file_name)]))
            parse_report(
                os.path.join(c.REPORTS_BASE_PATH, self.date_stamp, file_name),
                silent=False,
                suppress=self.suppress
            )
            print()

    def print_summary_report(self):
        top_level_table_data = []

        if len(self.file_names) == 0:
            return

        try:
            for file_name in self.file_names:
                top_level_table_data.extend(
                    parse_report(
                        os.path.join(c.REPORTS_BASE_PATH, self.date_stamp, file_name),
                        summary=True,
                        summary_domain_name=get_team_name_from_file_name(file_name),
                        silent=True,
                        suppress=self.suppress
                    )
                )
            
            print(tabulate(
                top_level_table_data,
                headers=c.TABLE_HEADERS,
                colalign=c.TABLE_COLALIGN,
            ))
        except Exception as e_inner:
            if not self.suppress:
                raise e_inner

    def get_reports(self):
        print(f"{self.date_stamp}\n")

        if self.summary:
            self.print_summary_report()
        else:
            self.print_full_report()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse today's context gathering reports.")
    parser.add_argument("--summary", action="store_true", help="Print a high-level summary of the report.")
    parser.add_argument("--suppress", action="store_true", help="Suppress errors and return what is available.")
    parser.add_argument("--date", help="If not today, when?")
    parser.add_argument("--duplicates", action="store_true", help="Find duplicate domains.")
    parser.add_argument("--group", help="The group of teams to report on.")
    args = parser.parse_args()

    stats_reporter = TodaysStatsReporter(
        date.today().isoformat() if not args.date else args.date,
        args.summary,
        args.suppress,
        group=args.group
    )

    stats_reporter.get_reports()
    if args.duplicates:
        stats_reporter.find_duplicate_domains()


