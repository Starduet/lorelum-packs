---
id: backend-engineering.side-effects.isolate-optional-work
title: Isolate Optional Work from the Primary Result
stage: design
severity: warn
tech_stack: [backend]
applies_when: a backend response depends on notifications, analytics, logging, cache work, or other ancillary operations
anti_patterns:
  - id: backend-engineering.side-effects.failure-controls-primary-result
    name: Make committed work look failed after an optional operation
    description: An ancillary exception or delay turns a completed primary operation into a failure or timeout and may induce a duplicate submission.
    severity: warn
---

## Decision

Locate the primary commit and classify the ancillary work by its contract. It may be best effort, required eventually, or required before reporting success. Do not classify audit, authorization, billing, or a cache update needed for consistency as optional merely because it runs outside the primary function.

## Isolate failure and waiting separately

Once the primary operation has committed, a best-effort failure should not become a failed primary response. Catching an exception handles rejection, not an operation that never returns. Give inline optional work a bounded share of the request deadline and define what happens to work still running after that budget. In JavaScript, `Promise.all` rejects when a member rejects without automatically cancelling the other work. The primary operation may already have committed or may still commit after the response fails.

Check what the configured exporter or full queue does: block, drop, or return an error. Define the overload behavior rather than assuming an enqueue or log call is cheap or non-throwing. An in-process framework background task is not by itself a durable handoff; check what survives worker shutdown, crash, or restart. Work that must happen eventually needs a reliable handoff with a recovery path, not just detachment. If acceptance depends on that handoff, arrange for it to be durable before reporting success and avoid a gap between the primary commit and recording the obligation.

## Example

An endpoint commits an order, awaits best-effort analytics, and returns an error when analytics rejects. Retrying the apparent failure can submit the order twice. Returning the committed result through a bounded, non-throwing best-effort path fixes that failure mode. If the secondary write is a required audit record, use the audit contract to choose between synchronous completion and durable handoff instead of discarding it.
