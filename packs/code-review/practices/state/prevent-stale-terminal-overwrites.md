---
id: code-review.state.prevent-stale-terminal-overwrites
title: Don't Let an Old Result Undo a Newer Change
stage: review
severity: warn
tech_stack: [code-review]
applies_when: an update_state, save, version check, or asynchronous completion can write after a newer operation or terminal state
anti_patterns:
  - id: code-review.state.stale-result-overwrite
    name: Older completion overwrites current state
    description: A delayed completion writes an obsolete result after a newer state or terminal transition without a valid guard.
    severity: warn
---

## When to apply

One operation starts, then another changes the same record before the first operation finishes. Check whether the older result can overwrite the newer state, such as turning a cancelled job back into a running one.

## Guidance

Look at the final database or state write. Does it check that the version, generation, or status is still the one the operation started with? The check and write need to happen together, unless another protection prevents an intervening change. A check before an `await` is not enough on its own.

Assign finding severity from actual impact: a stale display may be minor, but a reachable overwrite of payment or order terminal state that causes financial loss or corrupts authoritative records can warrant critical severity.

Examine the write boundary for these failure modes:

- A status or version check before an `await` is stale after the wait; put the expected version or allowed status into the atomic write predicate, or verify an equivalent protection.
- A conditional update may affect zero rows because the state changed. Check whether the caller notices, rather than reporting success or retrying without the condition.
- Reusing a generation ID after deletion and recreation can make an old callback appear current; check identity lifetime as well as the counter.
- Multiple fields can form one invariant: updating status and result in separate transactions may expose `succeeded` with an old result, even when each write is individually atomic.
- Database isolation and transaction boundaries matter: a read guarded in one transaction does not protect an update performed after that transaction ends.

## Anti-pattern

An older background job writes `succeeded` after the user has cancelled its replacement, even though cancellation is terminal. Reporting every asynchronous write as a race without checking the update predicate would be equally misleading.

## Why

The first request to start isn't always the first to finish. Its result may have been right when it started but wrong by the time it is saved.

## Exceptions and boundaries

Some systems explicitly permit later results to replace earlier ones or reopen terminal states; use their actual contract rather than inventing a state machine. Cancellation and task cleanup are separate lifecycle questions; lock ownership is a separate critical-section question.

## Example

A job row holds a generation number. Starting a second run increments it; cancelling that run sets a terminal `cancelled` status. A changed callback from the first run updates the row by ID only and sets `succeeded`. If it finishes after cancellation, it overwrites the newer terminal status. The changed unconditional update is reportable. An atomic update constrained by the original generation and allowed current status excludes that sequence.
