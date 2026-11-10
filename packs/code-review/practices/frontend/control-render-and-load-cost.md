---
id: code-review.frontend.control-render-and-load-cost
title: Check Whether the Change Makes Users Wait Longer
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

A page or interaction now fetches data, renders a list, or loads code differently. Check whether users have to wait for more work than they did before.

## Guidance

Follow what happens when a user opens the page or performs the interaction. Compare it with the old code: does it make another network trip, download code earlier, or repeat a calculation for a large list?

Use a realistic amount of data and a realistic interaction. Don't claim a specific slowdown unless you measured it.

Look for work added in these places:

- New object or function identities in effect dependencies can cause repeated effect execution; establish whether this actually triggers costly work, not just an extra development-only Strict Mode cycle.
- Awaiting independent data requests in sequence creates a network waterfall; verify the inputs, connection limits, and error semantics before suggesting parallelism.
- Mapping or sorting an entire large list on every keystroke, including before virtualization, can still block the main thread even if only a few rows render.
- Importing a heavy editor or chart in the initial bundle can move its download and evaluation onto navigation even when the feature is not opened; check the actual build and loading boundary.
- A cache key or invalidation change can defeat request deduplication and refetch on each mount; inspect library settings and real reuse rather than assuming every fetch reaches the network.

## Anti-pattern

A changed search field triggers a full unpaginated dataset fetch on every keystroke; real users have large datasets and wait for the result. In contrast, adding a small calculation over a fixed ten-item page is not a performance defect merely because it lacks `useMemo`.

## Why

A short piece of code can run on every keystroke or make users wait for several requests in a row. Whether that matters depends on how often it runs, how much data it handles, and whether the result is cached.

## Exceptions and boundaries

A deliberate sequential dependency, bounded list, cached request, or accepted loading tradeoff can make the apparent regression harmless. Do not assign a numeric slowdown without a measurement. An old response replacing a newer one is a correctness issue covered by request ordering, not automatically a performance issue.

## Example

An account screen previously fetched a bounded page once on navigation. A change moves the same uncached request into a handler called on every typed character. The server returns all records, and the repository's documented workload includes large accounts; each request blocks updated results. The repeated unbounded fetch is a concrete regression. If the handler instead filters a locally cached ten-item page, the proposed network finding is unsupported.
