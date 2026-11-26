# Sources and synthesis

The Practices and examples are independently written under the Pack's CC-BY-4.0 license. References support specific platform and library claims; no source prose or code is reproduced.

## `frontend-engineering.async.preserve-result-ownership`

- [WHATWG DOM: Aborting ongoing activities](https://dom.spec.whatwg.org/#aborting-ongoing-activities) (Living Standard, accessed 2026-11-18) and [WHATWG Fetch: Abort a fetch call](https://fetch.spec.whatwg.org/commit-snapshots/2696300d95bb6ced34e47c5401dd74e1f944eca8/#abort-fetch): abort signals only affect work that observes them. Fetch abort can reject a pending fetch and error a still-readable response body, but cannot revert an already fulfilled fetch promise. Neither standard grants or revokes application state-write authority.
- [React `useEffect`](https://react.dev/reference/react/useEffect) (accessed 2026-11-18): cleanup runs before the next setup on changed dependencies and on unmount; the fetching example shows ignoring outdated results. This describes client Effects, not automatic cancellation or the lifetime of an external store.
- [SWR Arguments](https://swr.vercel.app/docs/arguments) (accessed 2026-11-18): the whole array key identifies the cached resource; SWR 2.x passes the array to the fetcher as one argument, whereas pre-2.0 spreads it. Object-like keys are automatically serialized from 1.1 onward. These are key and fetcher contracts, not a guarantee for arbitrary completion handlers.
- [TanStack Query v5 Query Keys](https://tanstack.com/query/v5/docs/framework/react/guides/query-keys) (accessed 2026-11-18): serializable array keys distinguish data and should include changing resource inputs. Keying alone does not establish write ordering in a shared store or cancellation of a caller's continuation.

## `frontend-engineering.performance.bound-interaction-work`

- [React `useEffect`](https://react.dev/reference/react/useEffect) (accessed 2026-11-18): dependencies are compared with `Object.is`; a changed object or function dependency can rerun setup. Strict Mode's extra development setup/cleanup cycle does not establish production interaction cost.
- [TanStack Query v5 Query Invalidation](https://tanstack.com/query/v5/docs/framework/react/guides/query-invalidation) (accessed 2026-11-18): invalidation can mark matching entries stale and trigger background refetching. Matching filters and refetch options matter; this is not a universal cache policy.
- For React implementation details, reuse `react.async.parallel-independent-work` and `react.bundle.defer-heavy-loads`; see the [React Web Craft source ledger](https://github.com/lorelum/lorelum-packs/blob/react-web-craft-v0.1.0/packs/react-web-craft/SOURCES.md) for provenance. The framework-independent cost comparison is a design method, not a benchmark result.
