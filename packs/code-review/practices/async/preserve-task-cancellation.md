---
id: code-review.async.preserve-task-cancellation
title: Trace Task Ownership and Cancellation
stage: review
severity: warn
tech_stack: [code-review]
applies_when: a changed request or job starts or detaches asynchronous work, or changes who cancels, joins, and observes that work
anti_patterns:
  - id: code-review.async.unowned-work
    name: Work outlives its owner without a contract
    description: A request stops while its task continues without the required cancellation, error observation, or cleanup.
    severity: warn
---

## When to apply

A change creates a task, subscription, timer, or stream, or changes its parent lifecycle. Determine who owns it and what must happen when its owner finishes, fails, or is cancelled.

## Guidance

1. Identify the task owner and the contract for completion, cancellation, errors, shutdown, and cleanup. Determine whether the task is intentionally allowed to outlive its caller.
2. Trace creation, waiting, cancellation propagation, error observation, and resource release on normal completion and on each relevant failure or cancellation path. Check actual runtime semantics and existing supervisors.
3. Compare the reachable lifecycle with the contract. Report a changed path only when the missing ownership or cleanup produces a concrete effect, such as continued provider calls, leaked resources, or a lost failure.
4. Stop after establishing the owner and relevant terminal paths; do not demand that every asynchronous task be awaited by the initiating request.

## Anti-pattern

A request starts an independent worker, shields it from cancellation, and exits without a supervisor or cleanup. If the contract requires the worker to stop before request cleanup, the worker continues after its owner has gone. Flagging shielding without checking a `finally` block that cancels and joins it would instead be a false positive.

## Why

Starting work does not establish who observes its failure or how it ends. Cancellation often affects the caller and the spawned task differently.

## Exceptions and boundaries

A deliberately detached task with a real owner and appropriate error handling is not defective merely because the caller does not await it. This Practice concerns task lifetime; stale results overwriting a newer state are a separate state-transition decision, even if both arise from the same task.

## Example

An asyncio handler creates a worker and awaits it through `asyncio.shield`. The request contract requires cancellation to stop and join that worker before request cleanup. Cancelling the handler does not cancel the shielded worker, and there is no `finally` cleanup or supervisor. The shielded await is a finding because the worker continues past cleanup. If a `finally` block cancels and joins it, shielding alone is not evidence of a leak.

Before conducting a review, explicitly load the [review execution contract and workflow](resource:references/review-workflow.md); retrieval does not load it. The designated reviewer makes the substantive judgment.
