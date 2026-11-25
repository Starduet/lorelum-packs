---
id: code-review.navigation.backend
title: Navigate Backend Changes During Review
stage: review
severity: info
tech_stack: [code-review]
applies_when: a review involves backend request handling, persistent state, background tasks, messaging, or external service calls
anti_patterns:
  - id: code-review.navigation.backend-as-checklist
    name: Treat backend mechanisms as defects
    description: Report concurrency or asynchronous work without establishing the actual contract and effect.
    severity: warn
---

When changes affect backend behavior, understand the primary operation and its consumers first. Follow mechanisms affected by the change; unchanged code matters when it changes the outcome. Select relevant topics rather than checking every item.

Group the changed code by behavior, not file. A single diff can change several paths; do not let the first plausible concern stand in for the others. Once you see a changed boundary but have not judged it, state the engineering question using the affected operation, the changed mechanism, and what you need to determine. Query for that question without a review-stage filter. Read candidates that help answer the question and check their applicability against the code; a matching term alone is not enough.

**Admission, execution, and release.** Trace who can start or continue, when ownership or capacity changes hands, and what releases it on ordinary and exceptional paths. Admission and execution are different boundaries. A field that controls progress matters even when the code has no explicit lock.

**State writes.** Trace the final write predicate and the state or identity it expects. Checking whether a mutation can become stale does not tell you whether an otherwise valid caller can still proceed.

**Retries and recovery.** Trace operation identity, repeatable effects, and existing deduplication or recovery. The absence of a field named idempotency key does not prove missing protection.

**Main work and side products.** Follow the consumer, completion responsibility, delay, and failure of each result. Check the project contract before deciding whether a side effect can be dropped, must survive failure, or must complete before the caller proceeds.

**Persistent state and external work.** Trace writes, external calls, events, and acknowledgements across intermediate failure or process exit. Check actual transaction boundaries, atomic updates, and recovery; absence of one transaction is not alone a defect.

**Lifecycle.** When work moves to a background task or cancellation, timeout, or shutdown changes, identify who owns the task and observes completion or failure. Background execution is not itself durable.

