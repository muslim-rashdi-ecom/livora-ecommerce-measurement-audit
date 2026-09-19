# Livora UAE — E-commerce Measurement Audit

> A public portfolio repository documenting a self-directed Shopify e-commerce acquisition test and measurement audit for the UAE market.

This project is positioned as an **acquisition and diagnostics exercise**. It demonstrates campaign testing, event-funnel analysis, and reporting reconciliation. It is not presented as proof of profitability, ROAS, or recovered revenue.

## Project snapshot

| Field | Detail |
| --- | --- |
| Role | Technical Performance Marketer |
| Market | United Arab Emirates |
| Commerce platform | Shopify e-commerce store |
| Acquisition channel | Meta Ads |
| Measurement focus | Pixel event funnel, attribution scope, event-quality checks |
| Evidence window | 30 Jul–26 Aug 2025 for the site-wide Pixel overview |
| Repository status | Sanitized public portfolio version |

## Verified campaign signal

The featured Smart LED test produced low-cost traffic, but did not establish purchase conversion:

| Metric | Result |
| --- | ---: |
| Impressions | 15,134 |
| Link clicks | 1,065 |
| Link CTR | 7.04% |
| CPC link click | AED0.0734 |
| Website checkouts initiated | 2 |
| Attributed purchases | 0 |
| Reported spend | AED78.21 |

A second Wireless Camera Doorbell purchase test recorded 1,622 impressions, 53 link clicks, 3.27% CTR, AED1.48 CPC, 0 checkouts, and 0 purchases.

## Site-wide Pixel overview

The Events Manager screenshot showed rounded site-wide totals of:

```text
PageView         6.2K
ViewContent      5K
AddToCart        304
InitiateCheckout 55
AddPaymentInfo   24
Purchase         1
```

These totals are deliberately kept separate from campaign-attributed Ads Manager results. Scope, dates, attribution windows, timezone, and browser/server deduplication can differ, so the two views must not be treated as a one-to-one conversion report.

## What this project demonstrates

- Structuring low-budget Meta traffic tests for a UAE e-commerce offer.
- Reading campaign delivery metrics without confusing clicks with landing-page views.
- Mapping a Shopify-style event funnel from PageView through Purchase.
- Identifying a reporting-scope mismatch before recommending more spend.
- Turning screenshots and rounded dashboard totals into a reproducible audit note.
- Writing a small, dependency-free Python utility to calculate stage rates and flag scope limitations.

## Repository map

```text
.
├── analysis/
│   ├── funnel_audit.py          # Reproducible standard-library analysis
│   └── test_funnel_audit.py     # Small regression test suite
├── data/
│   ├── campaign_results.csv     # Sanitized campaign-level metrics
│   └── sitewide_pixel_funnel.csv
├── docs/
│   ├── measurement-audit.md     # Written case-study analysis
│   ├── event-taxonomy.md        # Event definitions and validation fields
│   ├── implementation-checklist.md
│   ├── skills-and-evidence.md   # Demonstrated vs. future evidence
│   └── sanitization-checklist.md
└── .github/workflows/validate.yml
```

## Run the analysis

The analysis uses only the Python standard library.

```bash
python analysis/funnel_audit.py
python analysis/funnel_audit.py --json
python -m unittest discover -s analysis -p 'test_*.py'
```

## Evidence and claim hygiene

The public repository intentionally distinguishes between:

1. **Demonstrated in this case:** Meta Ads testing, Shopify-style event-funnel analysis, Pixel event monitoring, attribution reconciliation, and the Python audit utility included here.
2. **Implementation capabilities to validate on a live account:** Shopify/Liquid customization, GA4, Google Tag Manager, Triple Whale, Google Ads, TikTok Ads, and server-side CAPI implementation details.

This distinction keeps the portfolio strategically strong without implying a client result that the available evidence cannot verify.

## Privacy note

No customer records, access tokens, Pixel IDs, ad-account IDs, payment details, or private store credentials are included. The data in `data/` is sanitized and sourced from rounded dashboard screenshots.

## Author

**Syed Muslim Shah** — Technical Performance Marketer focused on Meta Ads, Shopify measurement, Pixel/CAPI diagnostics, acquisition testing, and funnel analysis.
