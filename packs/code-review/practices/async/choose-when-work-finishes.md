---
id: code-review.async.choose-when-work-finishes
title: Check What Must Finish Before the Main Task Returns
stage: review
severity: warn
tech_stack: [code-review]
applies_when: a diff awaits, serializes, detaches, or moves work to the background, or changes the order of completion, commit, or response
anti_patterns:
  - id: code-review.async.wrong-completion-boundary
    name: Work crosses the wrong completion boundary
    description: Required results arrive too late or unrelated work blocks a completed task.
    severity: warn
---

Follow the main result and each side product to its consumer. Which must exist before the caller can continue, and which can finish later? Check the actual contract, not whether the code happens to use `await`.

Report a concrete case where required work or its result can be lost, associated with the wrong operation, or read too early; also report optional work that delays or fails an already-completed task when the contract permits separation. A task may run concurrently and be joined only where its result is needed.

Before reporting, check existing joins, ownership, error handling, cancellation, and durable handoff or reconciliation. A background task is not itself durable; neither logs nor usage records are automatically optional.

