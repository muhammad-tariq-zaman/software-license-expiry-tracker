"""Software licence expiry tracker: list licences expiring within N days."""
import argparse
import csv
import datetime
import sys


def parse_date(text):
    return datetime.date.fromisoformat(text.strip())


def expiring(csv_path, within_days=30, today=None):
    today = today or datetime.date.today()
    rows = []
    with open(csv_path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            expiry = parse_date(row["expiry_date"])
            days = (expiry - today).days
            if 0 <= days <= within_days:
                rows.append({**row, "days_left": days})
    rows.sort(key=lambda r: r["days_left"])
    return rows


def main(argv=None):
    p = argparse.ArgumentParser(description="List licences expiring soon.")
    p.add_argument("--csv", required=True)
    p.add_argument("--within-days", type=int, default=30)
    p.add_argument("--today", default=None, help="YYYY-MM-DD, for testing/reporting")
    args = p.parse_args(argv)
    today = datetime.date.fromisoformat(args.today) if args.today else None
    for r in expiring(args.csv, args.within_days, today):
        print(f"{r['software']} ({r.get('vendor', '')}) expires {r['expiry_date']} in {r['days_left']} day(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
