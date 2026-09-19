#!/usr/bin/env python3
"""Reproducible, dependency-free audit for the sanitized Livora case data."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Iterable


EVENT_ORDER = [
    "PageView",
    "ViewContent",
    "AddToCart",
    "InitiateCheckout",
    "AddPaymentInfo",
    "Purchase",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def as_number(value: str | None) -> float | None:
    if value in (None, ""):
        return None
    return float(value)


def sitewide_rates(rows: Iterable[dict[str, str]]) -> list[dict[str, float | str | None]]:
    counts = {row["event"]: int(row["count"]) for row in rows}
    output: list[dict[str, float | str | None]] = []
    previous_event = None
    for event in EVENT_ORDER:
        count = counts.get(event)
        rate = None
        if previous_event and count is not None and counts.get(previous_event):
            rate = round(count / counts[previous_event] * 100, 2)
        output.append({"event": event, "count": count, "stage_rate_percent": rate})
        previous_event = event
    return output


def campaign_summary(rows: Iterable[dict[str, str]]) -> list[dict[str, object]]:
    output = []
    for row in rows:
        impressions = int(row["impressions"])
        clicks = int(row["link_clicks"])
        calculated_ctr = round(clicks / impressions * 100, 2) if impressions else None
        output.append(
            {
                "campaign": row["campaign"],
                "reported_ctr_percent": as_number(row["link_ctr"]),
                "calculated_ctr_percent": calculated_ctr,
                "reported_cpc_aed": as_number(row["cpc_aed"]),
                "link_clicks": clicks,
                "purchases": int(row["purchases"]),
            }
        )
    return output


def build_report(data_dir: Path) -> dict[str, object]:
    sitewide = sitewide_rates(read_csv(data_dir / "sitewide_pixel_funnel.csv"))
    campaigns = campaign_summary(read_csv(data_dir / "campaign_results.csv"))
    warnings = [
        "Site-wide Pixel totals and campaign-attributed totals have different reporting scopes.",
        "Rounded screenshot totals should not be used for precise financial forecasting.",
        "The featured campaign records zero attributed purchases; profitability is not established.",
    ]
    return {
        "project": "Livora UAE e-commerce measurement audit",
        "sitewide_pixel_funnel": sitewide,
        "campaign_summary": campaigns,
        "warnings": warnings,
    }


def validate(report: dict[str, object]) -> list[str]:
    errors: list[str] = []
    funnel = report["sitewide_pixel_funnel"]
    if not funnel or funnel[0]["event"] != "PageView":
        errors.append("The site-wide funnel must start with PageView.")
    for row in funnel:
        if row["count"] is None or row["count"] < 0:
            errors.append(f"Invalid count for {row['event']}.")
    for row in report["campaign_summary"]:
        if row["calculated_ctr_percent"] is None:
            errors.append(f"Cannot calculate CTR for {row['campaign']}.")
    return errors


def print_report(report: dict[str, object]) -> None:
    print("Livora UAE — measurement audit")
    print("\nSite-wide Pixel funnel:")
    for row in report["sitewide_pixel_funnel"]:
        rate = "baseline" if row["stage_rate_percent"] is None else f"{row['stage_rate_percent']:.2f}% of previous stage"
        print(f"  {row['event']:<18} {row['count']:>6}  ({rate})")
    print("\nCampaign checks:")
    for row in report["campaign_summary"]:
        print(
            f"  {row['campaign']}: {row['link_clicks']} clicks, "
            f"reported CTR {row['reported_ctr_percent']:.2f}%, "
            f"calculated CTR {row['calculated_ctr_percent']:.2f}%, "
            f"purchases {row['purchases']}"
        )
    print("\nInterpretation guardrails:")
    for warning in report["warnings"]:
        print(f"  - {warning}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="print the report as JSON")
    parser.add_argument("--check", action="store_true", help="return a non-zero exit code for invalid data")
    parser.add_argument("--data-dir", type=Path, default=Path(__file__).parents[1] / "data")
    args = parser.parse_args()

    report = build_report(args.data_dir)
    errors = validate(report)
    if args.json:
        print(json.dumps({"report": report, "errors": errors}, indent=2))
    else:
        print_report(report)
        if errors:
            print("\nValidation errors:")
            for error in errors:
                print(f"  - {error}")
    return 1 if args.check and errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
