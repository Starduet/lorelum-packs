---
id: code-review.state.prevent-stale-terminal-overwrites
title: Check Whether Older Work Can Overwrite Newer State
stage: review
severity: warn
tech_stack: [code-review]
applies_when: a changed asynchronous completion or state update may write a result after a newer operation or terminal transition
anti_patterns:
  - id: code-review.state.stale-result-overwrite
    name: Older completion overwrites current state
    description: A delayed completion writes an obsolete result after a newer state or terminal transition without a valid guard.
    severity: warn
---

## When to apply

A diff changes state writes, completion handlers, terminal status, or version checks. Determine whether an earlier operation can complete after a later operation and overwrite a state that the contract says must be retained.

## Guidance

1. Establish the actual state contract: legal transitions, terminal states, ownership of each result, and whether later attempts supersede earlier ones.
2. Trace the changed read and write through persistence and callers. Construct a feasible sequence in which an older result arrives after a newer write or cancellation.
3. Check version comparisons, conditional updates, generation identifiers, serialization, and other real protections at the write boundary. A guard checked only before an intervening wait may no longer protect the write.
4. Report only when the sequence remains possible and produces an invalid state or visible result. Identify the changed write and the contract it violates; stop if an existing guard excludes the sequence.

Examine the write boundary for these failure modes:

- A status or version check before an `await` is stale after the wait; put the expected version or allowed status into the atomic write predicate, or verify an equivalent protection.
- A zero-row conditional update is not success: follow its result to see whether the caller incorrectly publishes completion or retries with an unconditional update.
- Reusing a generation ID after deletion and recreation can make an old callback appear current; check identity lifetime as well as the counter.
- Multiple fields can form one invariant: updating status and result in separate transactions may expose `succeeded` with an old result, even when each write is individually atomic.
- Database isolation and transaction boundaries matter: a read guarded in one transaction does not protect an update performed after that transaction ends.

## Anti-pattern

An older background job writes `succeeded` after the user has cancelled its replacement, even though cancellation is terminal. Reporting every asynchronous write as a race without checking the update predicate would be equally misleading.

## Why

A result can be correct for the operation that produced it but obsolete for the current state. The ordering of completion is not necessarily the ordering of requests.

## Exceptions and boundaries

Some systems explicitly permit later results to replace earlier ones or reopen terminal states; use their actual contract rather than inventing a state machine. Cancellation and task cleanup are separate lifecycle questions; lock ownership is a separate critical-section question.

## Example

A job row holds a generation number. Starting a second run increments it; cancelling that run sets a terminal `cancelled` status. A changed callback from the first run updates the row by ID only and sets `succeeded`. If it finishes after cancellation, it overwrites the newer terminal status. The changed unconditional update is reportable. An atomic update constrained by the original generation and allowed current status excludes that sequence.
