# software-license-expiry-tracker

Read a CSV of software licences (`software,vendor,expiry_date` with
`YYYY-MM-DD` dates) and list the ones expiring within N days, soonest first.

## How to run

```bash
python3 main.py --csv licences.csv --within-days 30
```

## Example output (sample from test fixture data)

```text
Tool A (Vendor A) expires 2026-11-01 in 6 day(s)
Tool B (Vendor B) expires 2026-11-10 in 15 day(s)
```

Standard library only. No network access.
