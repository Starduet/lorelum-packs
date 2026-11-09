---
id: code-review.frontend.prevent-request-races
title: Check Whether an Old Response Can Replace Current UI State
stage: review
severity: warn
tech_stack: [code-review]
applies_when: frontend queryKey, useEffect cleanup, AbortController, setLoading, or response handlers change which request owns displayed state
anti_patterns:
  - id: code-review.frontend.stale-response-wins
    name: Older response wins a newer interaction
    description: An earlier request can finish last and replace the results for the user's current input.
    severity: warn
---

## When to apply

A changed component starts requests as input, navigation, or dependencies change, and multiple responses may write the same displayed state. Decide whether completion order can contradict the current interaction.

## Guidance

At every data, error, and loading-state write, check whether its request still owns the current input and cache key. A concrete overlapping completion or wrong-key reuse must remain possible after existing guards.

Check the framework's actual response ownership:

- React runs an effect's cleanup before rerunning it with changed dependencies and on unmount. Missing cleanup matters when stale callbacks can still write or subscriptions remain active.
- `AbortController.abort()` can abort an in-flight fetch or body consumption, but it cannot undo an already fulfilled promise or arbitrary asynchronous work in a later `.then`; guard the final state write as needed.
- SWR or TanStack Query cache keys must distinguish every input that changes the returned resource, including tenant or account where applicable. A shared key can reuse another parameter's data even without overlapping network requests.
- An old request's `finally` can clear a loading indicator for a newer request; guard error and loading writes as well as successful data.
- Resetting a request counter on remount or reusing an ID can let an old callback match a new request; check the identifier's lifetime.

## Anti-pattern

A dashboard changes accounts while the old account's balance request is still running. The new balance loads first, then the old callback writes into the shared balance state. A request-generation guard or correctly scoped query cache can rule out this sequence.

## Why

Network completion order does not preserve interaction order. A result valid for the previous input can be wrong for the current screen.

## Exceptions and boundaries

An application may intentionally show an older cached result with a visible stale indicator; use the actual contract. Aborting a request may not guarantee a response handler cannot run, so check the runtime and write guard. Rendering cost and load waterfalls are separate performance decisions.

## Example

The user types `ca`, then `cat`; two requests overlap. The new handler writes every response into the same `results` state without checking the request's query. If `cat` completes first and `ca` completes later, the displayed items no longer match the input. Report the changed write. If a current-request token prevents the older response from writing, do not report this sequence.
