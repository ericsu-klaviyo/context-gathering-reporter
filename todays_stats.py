import argparse
import os

from constants import TABLE_HEADERS, TABLE_COLALIGN
from datetime import date
from report_parser import parse_report
from tabulate import tabulate

class TodaysStatsReporter:
    def __init__(self, date_stamp: str, summary=False, suppress=False):
        self.date_stamp = date_stamp
        self.summary = summary
        self.suppress = suppress
        self.team_names = [
            ("interface", "Interface"),
            ("flims", "FLIMS"),
            ("platform", "Platform")
        ]

    def get_report_path(self, team: str):
        path = f"reports/{self.date_stamp}/{team}.json"
        if not os.path.exists(path) and not self.suppress:
            raise FileNotFoundError(f"File not found: {path}")

        return path

    def print_full_report(self):
        for team in self.team_names:
            print(tabulate([team[1]]))
            parse_report(self.get_report_path(team[0]))
            print("\n")

    def print_summary_report(self):
        top_level_table_data = []

        if len(self.team_names) == 0:
            return

        try:
            for team_name, team_title in self.team_names:
                top_level_table_data.extend(
                    parse_report(
                        self.get_report_path(team_name),
                        summary=True,
                        summary_domain_name=team_title,
                        silent=True
                    )
                )
            
            print(tabulate(
                top_level_table_data,
                headers=TABLE_HEADERS,
                colalign=TABLE_COLALIGN,
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
    args = parser.parse_args()

    stats_reporter = TodaysStatsReporter(
        date.today().isoformat() if not args.date else args.date,
        args.summary,
        args.suppress
    )
    stats_reporter.get_reports()


