---
id: frontend-engineering.performance.bound-interaction-work
title: Bound the Work Users Wait For
stage: design
severity: warn
tech_stack: [ui]
applies_when: deciding what data, computation, or follow-up work must finish before a UI interaction shows useful feedback, or whether repeated work on that path grows with data or input frequency
anti_patterns:
  - id: frontend-engineering.performance.unbounded-interaction-work
    name: Repeated work grows with user data
    description: A frequent interaction performs growing work on the path to visible feedback without a practical bound.
    severity: warn
---

## When to apply

Identify the action and the next useful feedback, such as acknowledging a saved setting or showing the first page. Decide what must finish before that milestone and what can complete later under the product contract.

## Guidance

Trace the same action and visible milestone in the base and changed versions. For representative data sizes, identify what actually triggers, how often it runs, how much data each invocation touches, and what must finish before the user sees feedback. Separate local processing and rendering from network round trips and resource download and evaluation. Measure under representative conditions before claiming a numeric slowdown or improvement.

Keep required feedback truthful: wait for the save before claiming it succeeded. An independent analytics call or a refresh not needed for that confirmation should not hold it up. Keep any required delivery or failure handling for the deferred work; moving an `await` does not make its effects optional.

- Bound data at the source when possible. Fetching all records on every keystroke increases both frequency and volume; a virtualized list still pays for a full sort or filter done before row selection. Check the workload before choosing pagination, a bounded local dataset, or a change to the trigger.
- Trace duplicate work to real triggers. A newly created object or callback used as a React Effect dependency can restart costly work; an extra development-only Strict Mode setup and cleanup is not evidence of production repetition. Check cache key stability, invalidation, and actual reuse on mount or repeated input. A fetch call is not necessarily a network round trip.
- Check which requests truly depend on earlier results and which merely start later. Verify concurrency limits and failure behavior before changing their order. For a heavy editor or chart, inspect the built artifact and actual load path: did navigation now pay for code needed only on a later action, or would deferral move the wait onto a more important action?

For React-specific implementation decisions, use `react.async.parallel-independent-work` for independent I/O and `react.bundle.defer-heavy-loads` for heavy code-loading boundaries.

## Anti-pattern

A search handler fetches an entire uncached account dataset on every keystroke and waits for it to update results. Rendering only visible rows does not bound that fetch or the full-list work preceding it.

## Why

Even cheap work can delay feedback when multiplied by a frequent trigger or large dataset. Conversely, work off the waiting path is not by itself evidence that the interaction became slower.

## Exceptions and boundaries

A fixed small list, genuine dependency, verified cache reuse, or an accepted tradeoff between initial and later loading can make an apparent problem harmless. Do not infer a regression from a render count alone. An obsolete result taking over a newer operation is a correctness issue; see `frontend-engineering.async.preserve-result-ownership`.

## Example

The base account screen loads one bounded page on entry. The new search fetches and sorts every record on each typed character before it shows updated results. Compare request count, records processed, and time to results for the same typing sequence and a representative large account. If the changed handler instead filters a cached ten-item page, the alleged network regression does not follow.
