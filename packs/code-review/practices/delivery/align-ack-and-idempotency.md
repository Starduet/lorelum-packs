---
id: code-review.delivery.align-ack-and-idempotency
title: Trace Commit, Delivery, and Acknowledgement Together
stage: review
severity: warn
tech_stack: [code-review]
applies_when: a change moves a database commit, message publish, acknowledgement, retry, or deduplication boundary in a durable workflow
anti_patterns:
  - id: code-review.delivery.partial-success-window
    name: Delivery and durable state diverge
    description: A failure between state mutation and delivery or acknowledgement loses an event or repeats a non-idempotent effect.
    severity: warn
---

## When to apply

A change affects a durable write and message publication or consumption. Determine what remains true if the process crashes between commit, publish, business effect, and acknowledgement.

## Guidance

1. Establish the broker's actual delivery and acknowledgement semantics and the business contract for loss, duplicates, ordering, and recovery. Do not assume exactly-once delivery.
2. Lay out transaction commits, outbox writes, publishing, side effects, acknowledgements, retries, and crash boundaries. Trace the actual consumer and producer, not only the changed statement.
3. At each reachable partial-success window, check whether the existing transaction, durable outbox, deduplication key, or idempotent effect closes it. Idempotency must cover the actual repeated effect and key scope; an acknowledgement alone is not deduplication.
4. Report a concrete loss or duplicate sequence that violates the contract, anchored to the change. Stop when the relevant windows and real protections are accounted for; do not prescribe an outbox without establishing a gap.

## Anti-pattern

A consumer acknowledges a message before committing its non-repeatable business update. If it crashes after ack but before the commit and the broker does not redeliver acknowledged messages, the work is lost. Conversely, an existing transactional inbox and atomic business update may already protect a repeated delivery.

## Why

A database, broker, and external service do not automatically share one atomic boundary. A crash between two successful steps can leave only one visible, and retry can repeat a step that already happened.

## Exceptions and boundaries

Some workloads explicitly permit loss or duplicate effects; judge against their actual contract. A durable outbox helps only when its write shares the business transaction and the downstream path handles retries appropriately. This Practice unifies queue and transaction reasoning; it does not infer the need for exactly-once semantics.

## Example

An order service commits an order, then publishes an event directly. Its contract requires every accepted order to reach fulfillment, and no recovery process scans committed orders. A crash after commit but before publish leaves a paid order with no fulfillment event. The changed publish boundary is reportable. If the order and a durable outbox record are committed atomically and a worker safely retries publication, that crash window is closed; inspect consumer idempotency separately before claiming duplicates.

Before conducting a review, explicitly load the [review execution contract and workflow](resource:references/review-workflow.md); retrieval does not load it. The designated reviewer makes the substantive judgment.
