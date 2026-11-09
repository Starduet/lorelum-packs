---
id: code-review.frontend.control-render-and-load-cost
title: Trace Added Work on a User Interaction
stage: review
severity: warn
tech_stack: [code-review]
applies_when: a frontend diff changes list rendering, fetchPage versus fetchAll, asset imports, or sequential independent fetches on a visible interaction
anti_patterns:
  - id: code-review.frontend.unbounded-interaction-work
    name: Repeated work grows with user data
    description: A changed interaction repeatedly performs expensive or unbounded work on a path the user waits for.
    severity: warn
---

## When to apply

A frontend diff changes render dependencies, list processing, data loading, or asset loading on an interaction or navigation path. Decide whether the change adds material work or delay for a reachable workload.

## Guidance

Compare the old and new UI critical path at a realistic list size and interaction frequency. Identify the added network waterfall, bundle work, or repeated computation; quantify only when measured.

Inspect where work is introduced:

- New object or function identities in effect dependencies can cause repeated effect execution; establish whether this actually triggers costly work, not just an extra development-only Strict Mode cycle.
- Awaiting independent data requests in sequence creates a network waterfall; verify the inputs, connection limits, and error semantics before suggesting parallelism.
- Mapping or sorting an entire large list on every keystroke, including before virtualization, can still block the main thread even if only a few rows render.
- Importing a heavy editor or chart in the initial bundle can move its download and evaluation onto navigation even when the feature is not opened; check the actual build and loading boundary.
- A cache key or invalidation change can defeat request deduplication and refetch on each mount; inspect library settings and real reuse rather than assuming every fetch reaches the network.

## Anti-pattern

A changed search field triggers a full unpaginated dataset fetch on every keystroke; real users have large datasets and wait for the result. In contrast, adding a small calculation over a fixed ten-item page is not a performance defect merely because it lacks `useMemo`.

## Why

A small source change can repeat work along a frequent interaction or serialize independent network waits. The cost depends on actual frequency, dataset size, caching, and user-visible critical path.

## Exceptions and boundaries

A deliberate sequential dependency, bounded list, cached request, or accepted loading tradeoff can make the apparent regression harmless. Do not assign a numeric slowdown without a measurement. An old response replacing a newer one is a correctness issue covered by request ordering, not automatically a performance issue.

## Example

An account screen previously fetched a bounded page once on navigation. A change moves the same uncached request into a handler called on every typed character. The server returns all records, and the repository's documented workload includes large accounts; each request blocks updated results. The repeated unbounded fetch is a concrete regression. If the handler instead filters a locally cached ten-item page, the proposed network finding is unsupported.
