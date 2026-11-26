---
id: backend-engineering.delivery.align-effects-and-acknowledgements
title: Align Durable Effects and Message Acknowledgements
stage: design
severity: warn
tech_stack: [backend]
applies_when: changing a business commit, external effect, publish, acknowledgement, offset commit, inbox, outbox, or deduplication rule
anti_patterns:
  - id: backend-engineering.delivery.partial-success-window
    name: Leave a crash window between delivery and the effect
    description: A retry loses required work or repeats an effect because acknowledgement and durable state advance independently without recovery.
    severity: warn
---

## Decision

Define the business operation that must survive retry, and whether loss or repetition is acceptable. A delivery ID is useful only if it identifies the intended effect across retries. Scope the deduplication key to that effect (including tenant or destination where needed), enforce uniqueness at the write boundary, and keep the record for the supported retry and replay window.

## Put a crash between each pair of steps

Trace database commit, external effect, publish, ack or offset commit, and inbox marking in their actual order. At each boundary, ask what survives, what will be retried, and what proves earlier success. Include lost responses: the external system or broker may have accepted the request even if the caller saw a timeout.

- Ack before the required commit can lose work; commit before ack can replay it. An inbox record and database effect in one transaction can make replay safe for that database effect.
- Write the outbox record in the same transaction as the business state when an accepted state change must produce an event. The relay can still publish twice if it crashes after publishing but before marking the row sent; give consumers a stable key or another way to tolerate the replay.
- Marking a local inbox before calling an external API can suppress work that never happened. Marking it after the call can repeat a completed action. Use the external API's actual idempotency contract, or design to reconcile ambiguous outcomes; a local marker alone does not make the external effect exactly once.

For Kafka, inspect the actual client and broker versions, auto/manual commit settings, `poll` and batching behavior, and what happens to in-flight work on rebalance. An offset must not get ahead of required effects for earlier records in its partition; consumed position is not proof of completion. For Amazon SQS, check queue type and the actual interval from receive to delete. Work can outlast visibility and be delivered again. Standard queues can duplicate even within visibility; extensions can help with long work but cannot replace idempotency.

## Example and limits

An order commits but the process dies before publishing the fulfillment event. If fulfillment is required and no recovery path discovers the order, use a transactional outbox or another recovery mechanism that closes that window. Verify replay after publish as well. Loss-tolerant signals, duplicate-tolerant effects, and paths with existing transactional protection, external idempotency, or reconciliation do not automatically need an outbox. Judge severity by what is actually lost or repeated.
