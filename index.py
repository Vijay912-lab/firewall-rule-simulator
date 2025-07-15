import argparse
import csv
from log_analyzer import LogAnalyzer

def print_head(logs):
    for log in logs[:5]:
        print(log)

def deny_count(logs):
    denied_logs = [log for log in logs if log.action == 'Deny']
    print(f"{len(denied_logs)} log entries were denied.")

def country_count(logs, country_code):
    country_logs = [log for log in logs if log.country == country_code]
    print(f"{len(country_logs)} log entries from {country_code} were recorded.")

def parse(logs, month, export=False):
    filtered_logs = [log for log in logs if log.event_time.month == month]
    print(f"{len(filtered_logs)} log entries were recorded in month {month}.")

    if export:
        filename = f"2022_{str(month).zfill(2)}_logs.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=filtered_logs[0].__dict__.keys())
            writer.writeheader()
            writer.writerows([log.__dict__ for log in filtered_logs])
        print(f"Filtered log data exported to {filename}.")

def count_logs(logs, country_code=None):
    if country_code:
        country_logs = [log for log in logs if log.country == country_code]
        print(f"{len(country_logs)} log entries from {country_code} were recorded.")
    else:
        print(f"Total log entries: {len(logs)}")

def main():
    parser = argparse.ArgumentParser(description='Analyze Firewall Logs')
    parser.add_argument('--filename', '-f', required=True, help='CSV file to process')
    parser.add_argument('--action', '-a', required=True, 
                        choices=['head', 'deny', 'source', 'parse', 'count'], 
                        help='Action to perform')
    parser.add_argument('--country', '-c', help='Country code for filtering (used with action=source and count)')
    parser.add_argument('--month', '-m', type=int, help='Month for filtering (used with action=parse)')
    parser.add_argument('--export', '-e', choices=['Y', 'N'], help='Export filtered logs (used with action=parse)')

    args = parser.parse_args()
    analyzer = LogAnalyzer(args.filename)
    logs = analyzer.load_logs()

    if args.action == 'head':
        print_head(logs)
    elif args.action == 'deny':
        deny_count(logs)
    elif args.action == 'source':
        if not args.country:
            print("Error: --country argument is required for action=source")
        else:
            country_count(logs, args.country)
    elif args.action == 'parse':
        if not args.month or not (1 <= args.month <= 12):
            print("Error: --month argument must be between 1 and 12 for action=parse")
        else:
            export_flag = args.export == 'Y' if args.export else False
            parse(logs, args.month, export_flag)
    elif args.action == 'count':  
        count_logs(logs, args.country)  

if __name__ == "__main__":
    main()

