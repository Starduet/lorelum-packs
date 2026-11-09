---
id: code-review.concurrency.protect-critical-sections
title: Check Locks Against the Invariant They Protect
stage: review
severity: critical
tech_stack: [code-review]
applies_when: a diff changes mutex Lock or Unlock, lock ordering, SELECT FOR UPDATE, a Redis lease, or shared read-modify-write protection
anti_patterns:
  - id: code-review.concurrency.unprotected-invariant
    name: Critical operation escapes its protection
    description: Concurrent work can violate a shared invariant or wait indefinitely because lock scope or ordering changed.
    severity: critical
---

## When to apply

A diff changes a lock, shared mutable state, critical section, or a wait inside one. Determine whether the actual synchronization still protects the relevant invariant and allows progress.

## Guidance

Compare every participant's lock scope and acquisition order against the protected shared invariant. A finding needs a reachable interleaving or wait cycle that survives the actual atomic or distributed protections.

Check concrete protection boundaries:

- A process-local mutex does not serialize requests in other processes or replicas; a shared atomic update or distributed coordination may nevertheless protect the invariant.
- A Redis lease can expire while its former holder is still executing. Check renewal failure, ownership-checked release, and whether the protected resource rejects stale holders with fencing where required.
- `SELECT ... FOR UPDATE` protects rows only within the transaction holding those locks; a later update outside that transaction can race. Also check whether the query actually locks the relevant rows.
- Opposite lock acquisition order creates a potential cycle only when both paths can run concurrently and each waits while holding its first lock.
- A read-modify-write sequence protected by different locks, or an `await` that permits another writer to enter after a lock is released, may break an otherwise atomic invariant.

## Anti-pattern

A handler holds a mutex while waiting for a worker that must acquire the same mutex to complete. Both wait indefinitely. Merely seeing an `await` while holding a lock, without showing that the awaited path needs the lock or otherwise harms the contract, does not prove a deadlock.

## Why

Mutual exclusion protects only the operations actually covered by the same synchronization. Waiting can also extend lock ownership into work that cannot complete until the lock is released.

## Exceptions and boundaries

A lock may intentionally span asynchronous work when the awaited path does not require it and the latency tradeoff is accepted. Inspect actual callers rather than assuming concurrent access. Task cancellation ownership and stale state transitions are distinct decisions, though a single change can require both reviews.

## Example

An order handler acquires `inventoryLock`, starts a reservation worker, and awaits its result before releasing the lock. The worker must acquire `inventoryLock` to decrement stock and signal completion. Both paths are reachable in the same request, so the new await forms a wait cycle and checkout never completes. If the worker uses an independent resource and no caller needs the lock to make progress, the same syntax is not evidence of that cycle.
