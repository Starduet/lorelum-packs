---
id: code-review.frontend.prevent-request-races
title: Don't Show an Older Response for the User's New Input
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

A user changes a search term, account, or page while a request is still running. Check whether the old request can finish later and replace what the user should see now.

## Guidance

Follow each response to where it updates data, an error message, or a loading indicator. If the user starts a newer request first, can the old response still write there? Also check whether the cache key keeps data for different inputs apart.

Before reporting a bug, check any cancellation, request ID, or cache guard that may already prevent it:

- React runs an effect's cleanup before rerunning it with changed dependencies and on unmount. Missing cleanup matters when stale callbacks can still write or subscriptions remain active.
- `AbortController.abort()` can abort an in-flight fetch or body consumption, but it cannot undo an already fulfilled promise or arbitrary asynchronous work in a later `.then`; guard the final state write as needed.
- SWR or TanStack Query cache keys must distinguish every input that changes the returned resource, including tenant or account where applicable. A shared key can reuse another parameter's data even without overlapping network requests.
- An old request's `finally` can clear a loading indicator for a newer request; guard error and loading writes as well as successful data.
- Resetting a request counter on remount or reusing an ID can let an old callback match a new request; check the identifier's lifetime.

## Anti-pattern

A dashboard changes accounts while the old account's balance request is still running. The new balance loads first, then the old callback writes into the shared balance state. A request-generation guard or correctly scoped query cache can rule out this sequence.

## Why

The network doesn't promise that requests finish in the order they started. An earlier response can arrive last.

## Exceptions and boundaries

An application may intentionally show an older cached result with a visible stale indicator; use the actual contract. Aborting a request may not guarantee a response handler cannot run, so check the runtime and write guard. Rendering cost and load waterfalls are separate performance decisions.

## Example

The user types `ca`, then `cat`; two requests overlap. The new handler writes every response into the same `results` state without checking the request's query. If `cat` completes first and `ca` completes later, the displayed items no longer match the input. Report the changed write. If a current-request token prevents the older response from writing, do not report this sequence.
