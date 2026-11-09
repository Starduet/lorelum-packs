---
id: code-review.side-effects.isolate-noncritical-failures
title: Check Whether a Side Effect Blocks the Main Result
stage: review
severity: warn
tech_stack: [code-review]
applies_when: a changed request or job waits for a non-billing side effect before reporting its primary result, or changes how that side effect fails
anti_patterns:
  - id: code-review.side-effects.failure-controls-primary-result
    name: Optional side effect controls a committed result
    description: A completed primary operation is reported as failed when a separately recoverable side effect fails.
    severity: warn
---

## When to apply

A change puts a notification, analytics event, cache update, or other non-billing work on the path to a request or job result. Determine whether its failure or latency may alter that result. Billing and usage settlement need their own accounting contract; do not treat them as disposable analytics.

## Guidance

1. Identify when the main operation takes effect and what the caller is promised. Trace the added side effect through waits, exceptions, timeouts, and response handling.
2. Find the actual contract for the side effect: whether it is required before success, must eventually be durable, or is best effort. Trace existing queues, recovery, and reconciliation rather than assuming fire-and-forget is safe.
3. For each reachable failure or slow response, compare the observable main result with that contract. Consider client retries after the primary work already committed.
4. Report only a changed path that violates the contract, with the side-effect failure, primary consequence, and a precise location. Stop when the path and existing protections explain the result; do not propose a queue merely because the call is synchronous.

## Anti-pattern

A paid order is committed, then an analytics request throws. The handler reports HTTP 500, although the accepted contract says analytics is optional. The customer retries and may submit the order twice. Reporting the analytics call as a mere style problem would miss the committed-order failure window.

## Why

A dependency placed after a commit can change the caller's perception of success without undoing the operation. Slow optional work can likewise increase response latency or cause a timeout.

## Exceptions and boundaries

Do not report synchronous work merely because it waits: a required audit, authorization, or durable record may be part of success. If the contract is unknown, investigate before claiming isolation is required. This Practice excludes billing; analyze usage and settlement with `code-review.llm.account-for-all-usage`. Task ownership and cancellation are separate decisions.

## Example

An endpoint commits an order and then awaits an analytics service before returning 201. The service throws on network errors, and the endpoint turns uncaught exceptions into 500. The product contract says analytics failure must not affect ordering. The changed await is reportable: an analytics outage makes a successfully placed order look failed. If the endpoint instead uses a non-throwing best-effort handoff and returns 201, this failure claim is not supported.

Before conducting a review, the caller must explicitly load the [review execution contract and workflow](resource:references/review-workflow.md); retrieval alone does not load it. The designated reviewer makes the substantive judgment.
