import argparse
import json
import os

from constants import TABLE_HEADERS, TABLE_COLALIGN, TOTAL_STR, DOMAIN_OWNERSHIP
from tabulate import tabulate, SEPARATING_LINE

def printable_percent(numerator, denominator):
    return round((numerator / denominator) * 100)

def print_report_table(table_data):
    print(
        tabulate(
            table_data,
            headers=TABLE_HEADERS,
            colalign=TABLE_COLALIGN
        )
    )

def parse_report(filepath, summary=False, summary_domain_name=TOTAL_STR, silent=False):
    if not filepath or not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    total_keys = 0
    total_missing = 0

    domain_high_level_stats = {}
    domain_table_data = []

    team_name_lower = os.path.basename(filepath).replace('.json', '')

    with open(filepath, 'r') as report_file:
        report_json = json.load(report_file)

        # files key:
        # client/shared/i18n/translations/{DOMAIN}/en-US/translations.json
        for translation_filepath, data in report_json.get('files', {}).items():
            domain = translation_filepath.replace('client/shared/i18n/translations/', '').replace('/en-US/translations.json', '')
            if domain in DOMAIN_OWNERSHIP and DOMAIN_OWNERSHIP[domain] != team_name_lower:
                continue

            num_found = data.get('stats', {}).get('foundCount', 0)
            total_keys += num_found
            num_missing = data.get('stats', {}).get('missingCount', 0)
            total_missing += num_missing
            total_keys += num_missing

            domain_total = num_found + num_missing

            domain_high_level_stats[domain] = {
                'num_found': num_found,
                'num_missing': num_missing,
                'pct_missing': 1 if domain_total == 0 else printable_percent(num_missing, domain_total),
            }
            if not summary:
                domain_table_data.append([domain, num_missing, f"{domain_high_level_stats[domain]['pct_missing']}%"])
        
        if not summary:
            domain_table_data.append(SEPARATING_LINE)
        domain_table_data.append([summary_domain_name, total_missing, f"{printable_percent(total_missing, total_keys)}%"])
    
    if total_keys > 0:
        if not silent:
            print_report_table(domain_table_data)
    else:
        print("Error. Cannot divide by zero: No keys counted.")
    
    return domain_table_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse a context gathering report.")
    parser.add_argument("filepath", help="The path to the report file.")
    parser.add_argument("--summary", action="store_true", help="Print a high-level summary of the report.")
    parser.add_argument("--date", help="The date of the report.")
    parser.add_argument("--silent", action="store_true", help="Do not print the report.")
    args = parser.parse_args()

    if args.date and not args.silent:
        print(f"{args.date}\n")
    parse_report(args.filepath, args.summary, args.silent)



