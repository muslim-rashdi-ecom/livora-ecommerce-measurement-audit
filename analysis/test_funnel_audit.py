import unittest
from pathlib import Path

from funnel_audit import build_report, validate


DATA_DIR = Path(__file__).parents[1] / "data"


class FunnelAuditTests(unittest.TestCase):
    def setUp(self):
        self.report = build_report(DATA_DIR)

    def test_stage_rates_use_previous_event(self):
        funnel = self.report["sitewide_pixel_funnel"]
        self.assertEqual(funnel[0]["stage_rate_percent"], None)
        self.assertEqual(funnel[1]["stage_rate_percent"], 80.65)
        self.assertEqual(funnel[2]["stage_rate_percent"], 6.08)
        self.assertEqual(funnel[3]["stage_rate_percent"], 18.09)

    def test_campaign_ctr_is_recomputed(self):
        campaign = self.report["campaign_summary"][0]
        self.assertEqual(campaign["calculated_ctr_percent"], 7.04)

    def test_sanitized_dataset_passes_validation(self):
        self.assertEqual(validate(self.report), [])


if __name__ == "__main__":
    unittest.main()
