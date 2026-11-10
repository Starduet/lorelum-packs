---
id: code-review.side-effects.isolate-noncritical-failures
title: Don't Let Optional Work Hold Up the Main Job
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

The code has done what the user asked, but still needs to send a notification, write a log, or update a cache. Check whether that extra work can keep the user waiting or make the completed job look like a failure.

## Guidance

Find out when the main job actually finishes. If a later notification, log, thumbnail, or cache update fails or takes too long, what does the caller see? Trace the error or delay back to the response.

Check what the extra work is supposed to guarantee. Some work is best effort; other work must be saved and retried even if the caller doesn't wait for it. Don't suggest simply dropping it without checking.

Watch for these situations:

- A transaction commits before a notification or cache invalidation throws; a 500 response can cause a retry of already-completed work.
- `Promise.all` rejects when any member rejects, so a nonessential telemetry promise can fail a response even while the primary promise succeeds.
- An awaited network call with no bounded timeout can exhaust the primary request deadline even if its errors are caught.
- A framework background task may run only after a response is sent or may be cancelled on process shutdown; verify the actual framework and whether required work survives restart.
- A synchronous log exporter or full queue can make the request thread wait. Check whether the configured exporter or queue blocks, drops messages, or reports an error.

## Anti-pattern

A successful file upload waits for a best-effort email. The mail service hangs beyond the gateway deadline, so the client sees a timeout even though the file was stored. Retrying may create another upload. A mandatory durable notification would require a different contract analysis.

## Why

If an order was saved but the response says it failed, the customer may try again and place a second order. An optional call that never returns can cause the same confusion through a timeout.

## Exceptions and boundaries

Some work really must finish before the caller gets a success response. Authorization, audit records, and other required records depend on the actual contract. If you don't know the contract, find it before reporting a bug. This Practice covers non-billing work; use `code-review.llm.account-for-all-usage` for usage and billing.

## Example

An endpoint commits an order and then awaits an analytics service before returning 201. The service throws on network errors, and the endpoint turns uncaught exceptions into 500. The product contract says analytics failure must not affect ordering. The changed await is reportable: an analytics outage makes a successfully placed order look failed. If the endpoint instead uses a non-throwing best-effort handoff and returns 201, this failure claim is not supported.
