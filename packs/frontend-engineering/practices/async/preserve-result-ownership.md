---
id: frontend-engineering.async.preserve-result-ownership
title: Let Only the Current Operation Update UI State
stage: design
severity: warn
tech_stack: [ui]
applies_when: asynchronous UI work can outlive its input, selected account, view instance, or a newer operation targeting the same state
anti_patterns:
  - id: frontend-engineering.async.superseded-operation-writes
    name: Superseded operation writes current state
    description: An obsolete completion can replace current data, surface an irrelevant error, or clear another operation's loading state.
    severity: warn
---

## When to apply

A search, page change, account switch, retry, or view close can happen before earlier work finishes. Decide who may update each destination, including shared stores and cache entries that outlive the view.

## Guidance

Identify the resource inputs, the operation identity, the state slot being written, and the lifetime of its owner. For a slot meant to show the latest operation, revoke the old operation's authority when it is superseded or its owner is retired. Check the current owner and operation at the point that applies each write, including success, error, and loading updates in `finally`. A check before an asynchronous transform or before enqueueing a deferred update is not enough if ownership can change before the write is applied.

Choose an identity that cannot be reused while an old completion can still reach the destination. A per-view counter may suffice for isolated state; it can collide if a remounted view resets it and both views write to the same store. For that store, issue distinct tokens across owner lifetimes or compare both the owner and its generation. Input equality alone does not distinguish an A → B → A sequence or a retry of A.

Use a cache key and scope that distinguish all inputs that change the returned resource, including tenant or account where applicable. A correct key prevents cross-resource reuse, but does not by itself order two operations for the same key or guard writes outside the cache. Check what the data layer actually guarantees for the installed version, configuration, and destination.

For example, TanStack Query v5 uses serializable array keys; SWR associates the entire array key with the data, but passes it to the fetcher as one argument in 2.x and as spread arguments before 2.0. Check both the effective key and what the fetcher actually reads when reviewing a migration. Neither key contract covers writes to a separate UI store.

Cancel obsolete work where the API supports it, but keep cancellation separate from permission to publish. With web Fetch, aborting via the supplied signal can stop a pending fetch or interrupt response-body consumption even after the fetch promise fulfills. It cannot undo that fulfillment or automatically stop an unrelated async transform or continuation.

## Anti-pattern

A dashboard switches accounts while a balance request is pending. The old request writes an error or clears `loading` in a shared store while the new balance is still loading. Guarding only successful responses leaves this failure intact.

## Why

Completion order is not ownership order. The same check that keeps old data off the screen must also keep obsolete status changes from misleading the user.

## Exceptions and boundaries

Out-of-order completion is harmless when the destinations are independent or when a generation check or verified data-layer guarantee covers the actual writes. Showing an older cached result from the intended scope while it refreshes can be deliberate; judge it against the user-visible stale-data contract, not arrival order alone.

In React, `useEffect` cleanup runs before the next setup after changed dependencies and on unmount. It can revoke a setup's write permission; React does not automatically cancel work started by that setup. Derived state, functional updaters, and server-render request memoization do not establish client-side result ownership.

## Example

Start searches for `ca` and then `cat`. Let `ca` reject while `cat` is pending: the current view must stay loading and show no error for `ca`. In a second run let `cat` finish, then let `ca` succeed: the displayed results must still belong to `cat`. Repeat after closing and reopening the view if the results are stored outside it.
