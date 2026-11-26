---
id: backend-engineering.state.guard-current-generation-writes
title: Guard Writes Against the Current Generation
stage: design
severity: warn
tech_stack: [backend]
applies_when: an asynchronous result, callback, or retry can update state after a newer operation, terminal transition, or record replacement
anti_patterns:
  - id: backend-engineering.state.stale-result-overwrite
    name: Let an obsolete result overwrite current state
    description: A completion from an older operation updates a record even though its generation, identity, or allowed state no longer matches.
    severity: warn
---

## Decision

Check the final write, not just an earlier read or a check before an `await`. Put the expected version or generation, operation identity, and allowed current state into the atomic write predicate wherever each is needed to enforce the transition. An equivalent transaction or serialization mechanism can also protect the transition if it covers all relevant writers and holds through the write. Reading under a lock in one transaction does not protect a later independent write.

## Handle rejected transitions

Inspect the affected-row count or returned record and interpret zero rows according to the actual write and driver contract. The target may have moved on, been deleted, or already applied the operation. Distinguish stale work, an idempotent replay, and a missing target as the caller contract requires. Do not claim success solely because the statement did not throw, and do not retry without the guard. If the operation is still appropriate, read the current state and decide again under the same atomic protection.

A reused record ID and reset generation can make a delayed callback appear current after deletion and recreation. Include an incarnation or operation identity that is not reused while stale writers can still arrive. Update fields that form one invariant together: atomic status and result writes in separate transactions can still expose a new terminal status with an old result.

## Example and limits

Run A finishes after run B starts and is cancelled. If A writes `succeeded` by job ID alone, it can replace B's `cancelled` state. Require A's generation and a state that allows completion, write status and result together, and interpret a rejected write rather than issuing an unconditional retry. Test delayed completion after cancellation and after deletion and recreation. Explicit reopen transitions, an intentional last-write-wins policy, or existing equivalent atomic protection can make a different design correct. Judge severity by the actual invariant and consequence. Task cancellation and lock release are separate decisions.
