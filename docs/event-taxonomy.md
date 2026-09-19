# Event taxonomy and validation map

This document describes the event path used for the audit. It is a validation map, not a claim that every field below was exported from the screenshots.

| Event | Funnel meaning | Fields to validate |
| --- | --- | --- |
| `PageView` | Page loaded | URL, timestamp, browser consent state |
| `ViewContent` | Product or offer viewed | `content_ids`, `content_type`, `value`, `currency` |
| `AddToCart` | Product added to cart | `content_ids`, `contents`, `value`, `currency` |
| `InitiateCheckout` | Checkout flow started | cart contents, value, currency |
| `AddPaymentInfo` | Payment details step reached | checkout ID, value, currency |
| `Purchase` | Order completion | order ID, `event_id`, value, currency |

## Browser/server consistency checks

- Use the same order identifier in browser and server Purchase payloads where deduplication requires it.
- Confirm that `event_id` is present and stable for the same event.
- Confirm currency is `AED` for UAE order values.
- Confirm Purchase is emitted only after the order-completion state is reached.
- Check that test orders and repeated refreshes are excluded from production reporting.

## Scope rule

Do not compare a site-wide Events Manager total with an Ads Manager campaign total as if both were the same denominator. Document the scope beside every exported metric.
