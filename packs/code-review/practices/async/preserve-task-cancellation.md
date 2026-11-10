---
id: code-review.async.preserve-task-cancellation
title: Make Sure Background Work Knows When to Stop
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

A request or job starts a task, timer, subscription, or stream. Check what happens to that work when the request finishes, fails, or is cancelled.

## Guidance

Find who is responsible for the work after it starts. If the request goes away, should the work stop or keep running? Check who stops it when needed, waits for it to finish, and handles errors.

Starting a task without awaiting it is not a bug by itself. Report it when the actual lifetime or error handling breaks a requirement.

The answer depends on the runtime:

- Python `asyncio.create_task` needs a strong reference for reliable detached work; the event loop keeps weak references. A task group or supervising collection may already own it.
- `asyncio.shield` prevents cancellation of the awaiting caller from propagating to the inner task, but the caller still receives `CancelledError`; direct cancellation of the inner task still works. Check the cleanup path rather than assuming shielding guarantees completion.
- JavaScript `void somePromise()` does not observe rejection; check a rejection handler or supervisor and the host's unhandled-rejection policy.
- In Go, cancelling a `context.Context` signals cancellation; it does not kill goroutines. Check whether blocking operations and loops select on `ctx.Done()` or otherwise terminate.
- A shutdown hook that initiates cancellation but never joins workers can close resources while they are still in use. Conversely, joining a worker that ignores cancellation can prevent shutdown.

## Anti-pattern

A JavaScript handler starts an optional background refresh with `void refresh()` and assumes the runtime will report its rejection to the request's error handler. The request has already returned and no supervisor observes the rejected promise, so the failure is unhandled. A deliberately detached promise with a real rejection handler is different.

## Why

Returning from a request doesn't necessarily stop the work it started. If nobody is responsible for that work, it may keep running, leave resources open, or fail without anyone handling the error.

## Exceptions and boundaries

A deliberately detached task with a real owner and appropriate error handling is not defective merely because the caller does not await it. This Practice concerns task lifetime; stale results overwriting a newer state are a separate state-transition decision, even if both arise from the same task.

## Example

An asyncio handler creates a worker and awaits it through `asyncio.shield`. The request contract requires cancellation to stop and join that worker before request cleanup. Cancelling the handler does not cancel the shielded worker, and there is no `finally` cleanup or supervisor. The shielded await is a finding because the worker continues past cleanup. If a `finally` block cancels and joins it, shielding alone is not evidence of a leak.
