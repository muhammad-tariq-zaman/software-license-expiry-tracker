import datetime
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import main


class TestLicences(unittest.TestCase):
    def test_sorted_and_windowed(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "lic.csv")
            open(p, "w").write("software,vendor,expiry_date\n"
                               "Tool B,Vendor B,2026-11-10\n"
                               "Tool A,Vendor A,2026-11-01\n"
                               "Tool C,Vendor C,2027-06-01\n")
            rows = main.expiring(p, 30, datetime.date(2026, 10, 26))
            self.assertEqual([r["software"] for r in rows], ["Tool A", "Tool B"])
            self.assertEqual(rows[0]["days_left"], 6)


if __name__ == "__main__":
    unittest.main()
