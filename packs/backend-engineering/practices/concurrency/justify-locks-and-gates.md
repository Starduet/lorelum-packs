---
id: backend-engineering.concurrency.justify-locks-and-gates
title: Justify a Lock or Gate Against Real Conflicts and Release Paths
stage: design
severity: warn
tech_stack: [backend]
applies_when: deciding whether to add, retain, remove, or change a mutex, lock, busy flag, semaphore, queue, or other gate around backend operations, shared state, or a state-machine transition
anti_patterns:
  - id: backend-engineering.concurrency.guard-imagined-conflicts
    name: Guard normal work against an unestablished race
    description: A global lock or busy gate serializes or rejects independent requests because concurrency seems risky, without identifying a reachable conflict or the invariant it protects.
    severity: warn
  - id: backend-engineering.concurrency.guard-without-release
    name: Acquire a gate without a complete release path
    description: An error, cancellation, early return, missing callback, or wait cycle leaves a lock or gate held and prevents subsequent work from progressing.
    severity: warn
---

## Start without a new gate

Do not add a lock, busy flag, queue, or semaphore just because calls can overlap. Name two reachable callers, the resource they share, and the order of operations that would break a specific invariant. A real capacity or ordering requirement can also justify a guard. If you cannot establish either need, leave the normal path alone; if a fact is missing, inspect it rather than adding protection on speculation.

Check what already prevents the conflict: ownership, an existing queue, a conditional write, a uniqueness constraint, or a transaction. Keep working protection. If a gap remains, protect the smallest resource and interval that cover all actual writers. A process-local lock does not cover other replicas. For a database lock, check the actual SQL, isolation level, rows locked, and transaction end; a protected read does not cover a later independent write, and a query finding no row does not by itself protect an insert.

## Check who gets blocked and who releases

Walk a normal second request through the proposed guard. Can an unrelated job still run? Does a same-resource caller wait, receive `busy`, or get dropped, and does the contract allow that? For a queue, distinguish admission from execution. Reserve on admission only if the invariant includes queued work or otherwise requires early reservation. Check whether an admitted job can prevent existing work from reaching completion.

For every acquisition, identify the owner and release path on success, early return, error, timeout, cancellation, and shutdown. Include work that never starts or never calls back. A success-only reset can leave the service permanently busy. Conversely, a cancellation signal is not proof the old worker stopped; releasing its protection while it still writes can let two owners act. For a lease, release only the current owner's lease and check whether the protected resource rejects stale writes after expiry.

If an operation waits while holding a guard, trace what the awaited work needs to finish. Report deadlock only when there is a reachable wait cycle; delay or rejection of normal work can be a separate defect without a cycle.

## Decide and verify

Leave independent work unguarded when no shared requirement exists. Keep a justified guard, but fix proven overreach or missing release rather than stacking another gate on it. Before accepting a change, check that independent work still proceeds, a real conflict is prevented, and the next eligible request can run after the first fails or is cancelled. In review, describe the reachable sequence and consequence; lack of explanation alone warrants a question, not a defect finding.

For example, a service-wide `busy` flag rejects a different job while the first waits on a remote call. If the jobs share neither state nor a capacity limit, do not add the flag. A device that accepts one command at a time does need serialization; keep it and verify that a failed command does not leave later commands permanently blocked.
