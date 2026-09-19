# E-commerce measurement implementation checklist

Use this checklist when auditing a live Shopify store. It is deliberately written as an implementation-ready checklist, not as a claim that every item was completed in the Livora test.

## Tracking foundation

- [ ] Document the store domain, checkout domain, timezone, currency, and consent behavior.
- [ ] Record Pixel, dataset, Google Tag Manager, and analytics IDs privately—not in this repository.
- [ ] Confirm one canonical event naming scheme across browser and server sources.
- [ ] Add UTMs to every paid-social destination URL.

## Meta Pixel / server events

- [ ] Verify PageView and ViewContent on the intended templates.
- [ ] Verify AddToCart fires once per meaningful cart action.
- [ ] Verify InitiateCheckout and AddPaymentInfo match the actual checkout flow.
- [ ] Verify Purchase includes order ID, value, currency, and event ID.
- [ ] Check browser/server deduplication in Events Manager diagnostics.
- [ ] Compare event counts across the same date range and attribution window.

## Shopify funnel

- [ ] Test product page, cart, checkout, payment, and COD confirmation on mobile and desktop.
- [ ] Check broken links, loading states, shipping visibility, and validation messages.
- [ ] Confirm the order confirmation page cannot be refreshed into duplicate Purchase events.
- [ ] Record where a visitor can abandon the flow and what evidence supports that diagnosis.

## Reporting

- [ ] Separate delivery metrics, traffic metrics, funnel events, and revenue metrics.
- [ ] Label rounded screenshots as directional evidence.
- [ ] Never infer ROAS without verified spend and revenue in the same scope.
- [ ] Keep an audit log of every change to tracking or campaign settings.
