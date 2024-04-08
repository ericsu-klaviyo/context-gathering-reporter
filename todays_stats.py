import argparse
import os
import constants as c

from datetime import date
from report_parser import parse_report
from tabulate import tabulate, SEPARATING_LINE

class TodaysStatsReporter:
    def __init__(self, date_stamp: str, summary=False, suppress=False):
        self.date_stamp = date_stamp
        self.summary = summary
        self.suppress = suppress
        self.team_names = [
            c.FLOWS_INTERFACE_TEAM_NAME,
            c.FLOWS_IMS_TEAM_NAME,
            c.FLOWS_PLATFORM_TEAM_NAME
        ]

    def get_report_path(self, team: str):
        path = f"reports/{self.date_stamp}/{team}.json"
        if not os.path.exists(path) and not self.suppress:
            raise FileNotFoundError(f"File not found: {path}")

        return path

    def find_duplicate_domains(self):
        domains = set()
        duplicate_domains = set()
        for name in self.team_names:
            team_table_data = parse_report(self.get_report_path(name.lower()), silent=True)
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
        for names in self.team_names:
            print(tabulate([names]))
            parse_report(self.get_report_path(names.lower()))

    def print_summary_report(self):
        top_level_table_data = []

        if len(self.team_names) == 0:
            return

        try:
            for name in self.team_names:
                top_level_table_data.extend(
                    parse_report(
                        self.get_report_path(name.lower()),
                        summary=True,
                        summary_domain_name=name,
                        silent=True
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
    args = parser.parse_args()

    stats_reporter = TodaysStatsReporter(
        date.today().isoformat() if not args.date else args.date,
        args.summary,
        args.suppress
    )

    stats_reporter.get_reports()
    if args.duplicates:
        stats_reporter.find_duplicate_domains()


