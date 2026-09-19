# Measurement audit

## 1. Question

Can a low-budget Meta Ads test generate economical UAE e-commerce traffic, and can the event path from visit to purchase be trusted well enough to guide the next test?

## 2. Campaign evidence

| Campaign | Impressions | Link clicks | CTR | CPC | Checkouts | Purchases | Spend |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Smart LED Test — Sales — UAE | 15,134 | 1,065 | 7.04% | AED0.0734 | 2 | 0 | AED78.21 |
| Wireless Camera Doorbell — Purchase | 1,622 | 53 | 3.27% | AED1.48 | 0 | 0 | Not shown |

The featured test generated inexpensive link-click traffic. It did not establish purchase conversion or profitability.

## 3. Site-wide Pixel funnel

The Events Manager overview showed rounded totals for 30 Jul–26 Aug 2025:

| Event | Rounded total | Approximate stage rate |
| --- | ---: | ---: |
| PageView | 6.2K | Baseline |
| ViewContent | 5K | 5,000 ÷ 6,200 = 80.65% |
| AddToCart | 304 | 304 ÷ 5,000 = 6.08% |
| InitiateCheckout | 55 | 55 ÷ 304 = 18.09% |
| AddPaymentInfo | 24 | 24 ÷ 55 = 43.64% |
| Purchase | 1 | 1 ÷ 24 = 4.17% |

Because the dashboard values are rounded, these rates are directional rather than a precision analytics export.

## 4. Reconciliation finding

The featured Smart LED campaign reported 0 attributed add-to-carts and 0 purchases, while the site-wide Pixel overview showed 304 AddToCart events and 1 Purchase. These views cannot be reconciled one-to-one from screenshots alone. The next audit must align:

- date range and account timezone;
- campaign filters and attribution window;
- browser/server event deduplication IDs;
- event parameters, especially `value`, `currency`, and `event_id`;
- the difference between site-wide activity and campaign-attributed activity.

## 5. What the evidence supports

- Hands-on campaign setup and traffic testing.
- Low-cost link-click acquisition for the featured test.
- Practical event-funnel monitoring.
- Ability to identify a reporting-scope problem before scaling spend.

## 6. What the evidence does not support

- Profitability, ROAS, or recovered revenue.
- A statistically significant audience winner.
- A causal uplift from a specific language or creative variant.
- A claim that the reported Pixel totals were caused by the featured campaign.

## 7. Next validation sequence

1. Export identical date ranges from Ads Manager and Events Manager.
2. Compare campaign-attributed and site-wide event scopes separately.
3. Validate browser/server deduplication and Purchase parameters.
4. Walk through product page, checkout, payment, and COD handoff events.
5. Only then decide whether a new spend test is justified.
