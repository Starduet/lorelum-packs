---
id: code-review.delivery.align-ack-and-idempotency
title: Trace Commit, Delivery, and Acknowledgement Together
stage: review
severity: critical
tech_stack: [code-review]
applies_when: a change moves message ack, offset commit, publish, outbox, transaction commit, or deduplication around a durable effect
anti_patterns:
  - id: code-review.delivery.partial-success-window
    name: Delivery and durable state diverge
    description: A failure between state mutation and delivery or acknowledgement loses an event or repeats a non-idempotent effect.
    severity: critical
---

## When to apply

A change affects a durable write and message publication or consumption. Determine what remains true if the process crashes between commit, publish, business effect, and acknowledgement.

## Guidance

Compare ack or offset commit, business transaction, outbox and external effects at each crash boundary. A deduplication key must cover the actual logical effect and retention window; ack alone cannot prevent duplicates.

Broker-specific checks expose different windows:

- Kafka automatic offset commits can advance independently of application side-effect completion; inspect consumer configuration, polling, batching, rebalance, and actual commit timing.
- An SQS visibility timeout shorter than processing can allow another consumer to receive the same message; even an unexpired timeout does not absolutely prevent duplicates for standard queues. Check extension and idempotent effects.
- An outbox written in a separate transaction from the business row still permits one to commit without the other. Publishing an outbox entry and crashing before marking it sent can also publish twice.
- A deduplication key scoped incorrectly can collide across tenants or fail to identify retries of the same logical operation. Verify uniqueness over the actual effect and retention window, rather than assuming global uniqueness is always required.
- Committing a database inbox key before an external API call can suppress retries after a crash; recording it after the call can repeat the external effect. Inspect the external idempotency contract.

## Anti-pattern

A consumer acknowledges a message before committing its non-repeatable business update. If it crashes after ack but before the commit and the broker does not redeliver acknowledged messages, the work is lost. Conversely, an existing transactional inbox and atomic business update may already protect a repeated delivery.

## Why

A database, broker, and external service do not automatically share one atomic boundary. A crash between two successful steps can leave only one visible, and retry can repeat a step that already happened.

## Exceptions and boundaries

Some workloads explicitly permit loss or duplicate effects; judge against their actual contract. A durable outbox helps only when its write shares the business transaction and the downstream path handles retries appropriately. This Practice unifies queue and transaction reasoning; it does not infer the need for exactly-once semantics.

## Example

An order service commits an order, then publishes an event directly. Its contract requires every accepted order to reach fulfillment, and no recovery process scans committed orders. A crash after commit but before publish leaves a paid order with no fulfillment event. The changed publish boundary is reportable. If the order and a durable outbox record are committed atomically and a worker safely retries publication, that crash window is closed; inspect consumer idempotency separately before claiming duplicates.
