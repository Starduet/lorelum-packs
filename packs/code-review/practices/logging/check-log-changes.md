---
id: code-review.logging.check-log-changes
title: Check the Effects of Changed Logs and Error Handling
stage: review
severity: warn
tech_stack: [code-review]
applies_when: a diff changes logging, error handling, audit events, log filters, or the order of middleware that produces logs
anti_patterns:
  - id: code-review.logging.log-leaks-or-hides-the-failure
    name: A log exposes data or hides a required failure
    description: A reachable log exposes protected data or a changed path removes a required diagnostic or audit event.
    severity: warn
---

Trace logged values to the actual sink and its redaction before reporting exposure. When an error or audit event changes, follow the affected path through middleware order, early returns, levels, filters, sampling, and upstream handlers: can the required event still be recorded, and does it describe what actually happened?

Report the reachable input or failure and its concrete exposure or operational consequence. Do not demand duplicate logs, treat every identifier as sensitive, or assume ordinary diagnostic logs have the same durability requirements as audit records.
