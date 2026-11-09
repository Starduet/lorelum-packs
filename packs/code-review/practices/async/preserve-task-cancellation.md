---
id: code-review.async.preserve-task-cancellation
title: Trace Task Ownership and Cancellation
stage: review
severity: warn
tech_stack: [code-review]
applies_when: a change starts or detaches work via create_task, go func, or a Promise, or changes cancellation, joining, or exception observation
anti_patterns:
  - id: code-review.async.unowned-work
    name: Work outlives its owner without a contract
    description: A request stops while its task continues without the required cancellation, error observation, or cleanup.
    severity: warn
---

## When to apply

A change creates a task, subscription, timer, or stream, or changes its parent lifecycle. Determine who owns it and what must happen when its owner finishes, fails, or is cancelled.

## Guidance

Identify the owner of each spawned task and check what actually stops, joins, and observes it when the owner exits. Report a concrete lifecycle violation, not mere detachment.

Inspect the actual runtime, not a generic notion of cancellation:

- Python `asyncio.create_task` needs a strong reference for reliable detached work; the event loop keeps weak references. A task group or supervising collection may already own it.
- `asyncio.shield` prevents cancellation of the awaiting caller from propagating to the inner task, but the caller still receives `CancelledError`; direct cancellation of the inner task still works. Check the cleanup path rather than assuming shielding guarantees completion.
- JavaScript `void somePromise()` does not observe rejection; check a rejection handler or supervisor and the host's unhandled-rejection policy.
- In Go, cancelling a `context.Context` signals cancellation; it does not kill goroutines. Check whether blocking operations and loops select on `ctx.Done()` or otherwise terminate.
- A shutdown hook that initiates cancellation but never joins workers can close resources while they are still in use. Conversely, joining a worker that ignores cancellation can prevent shutdown.

## Anti-pattern

A JavaScript handler starts an optional background refresh with `void refresh()` and assumes the runtime will report its rejection to the request's error handler. The request has already returned and no supervisor observes the rejected promise, so the failure is unhandled. A deliberately detached promise with a real rejection handler is different.

## Why

Starting work does not establish who observes its failure or how it ends. Cancellation often affects the caller and the spawned task differently.

## Exceptions and boundaries

A deliberately detached task with a real owner and appropriate error handling is not defective merely because the caller does not await it. This Practice concerns task lifetime; stale results overwriting a newer state are a separate state-transition decision, even if both arise from the same task.

## Example

An asyncio handler creates a worker and awaits it through `asyncio.shield`. The request contract requires cancellation to stop and join that worker before request cleanup. Cancelling the handler does not cancel the shielded worker, and there is no `finally` cleanup or supervisor. The shielded await is a finding because the worker continues past cleanup. If a `finally` block cancels and joins it, shielding alone is not evidence of a leak.
