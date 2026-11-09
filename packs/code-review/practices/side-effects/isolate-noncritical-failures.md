---
id: code-review.side-effects.isolate-noncritical-failures
title: Check Whether a Side Effect Blocks the Main Result
stage: review
severity: warn
tech_stack: [code-review]
applies_when: a committed operation waits on optional analytics, notifications, thumbnails, cache invalidation, or telemetry before reporting success
anti_patterns:
  - id: code-review.side-effects.failure-controls-primary-result
    name: Optional side effect controls a committed result
    description: A completed primary operation is reported as failed when a separately recoverable side effect fails.
    severity: warn
---

## When to apply

A change puts a notification, analytics event, cache update, or other non-billing work on the path to a request or job result. Determine whether its failure or latency may alter that result. Billing and usage settlement need their own accounting contract; do not treat them as disposable analytics.

## Guidance

Compare the committed primary operation with the non-billing side effect's failure and latency contract. Check whether its error or delay changes the result, and whether existing recovery makes the required effect durable.

Look for these concrete coupling mechanisms:

- A transaction commits before a notification or cache invalidation throws; a 500 response can cause a retry of already-completed work.
- `Promise.all` rejects when any member rejects, so a nonessential telemetry promise can fail a response even while the primary promise succeeds.
- An awaited network call with no bounded timeout can exhaust the primary request deadline even if its errors are caught.
- A framework background task may run only after a response is sent or may be cancelled on process shutdown; verify the actual framework and whether required work survives restart.
- A synchronous log exporter or full queue can apply backpressure on the request thread. Check its configured blocking and overflow policy, not just the logging call's name.

## Anti-pattern

A successful file upload waits for a best-effort email. The mail service hangs beyond the gateway deadline, so the client sees a timeout even though the file was stored. Retrying may create another upload. A mandatory durable notification would require a different contract analysis.

## Why

A dependency placed after a commit can change the caller's perception of success without undoing the operation. Slow optional work can likewise increase response latency or cause a timeout.

## Exceptions and boundaries

Do not report synchronous work merely because it waits: a required audit, authorization, or durable record may be part of success. If the contract is unknown, investigate before claiming isolation is required. This Practice excludes billing; analyze usage and settlement with `code-review.llm.account-for-all-usage`. Task ownership and cancellation are separate decisions.

## Example

An endpoint commits an order and then awaits an analytics service before returning 201. The service throws on network errors, and the endpoint turns uncaught exceptions into 500. The product contract says analytics failure must not affect ordering. The changed await is reportable: an analytics outage makes a successfully placed order look failed. If the endpoint instead uses a non-throwing best-effort handoff and returns 201, this failure claim is not supported.
