---
id: modern-web-guidance.platform.yield-long-tasks
title: Yield Long Main-Thread Work
stage: implementation
severity: warn
applies_when: an export, save, large list, or other browser-side operation makes the interface slow or unresponsive by delaying interaction or rendering
tech_stack:
  - javascript
  - web
anti_patterns:
  - id: modern-web-guidance.platform.unbroken-main-thread-work
    name: Unbroken main-thread work
    severity: warn
    description: A large synchronous loop monopolizes the main thread and delays interaction and paint.
---

Measure the interaction on representative devices and identify the work occupying the main thread. Eliminate unnecessary work first; move CPU-heavy work that does not need the DOM to a worker when the transfer and coordination cost is justified. For work that must remain on the main thread and can be interrupted, process it in chunks and yield between chunks with `scheduler.yield()` when available, or `await new Promise(resolve => setTimeout(resolve, 0))` as a fallback.

For example, process a large list until a time budget expires, yield, then reset the deadline before continuing. The 50 ms long-task threshold is not a responsiveness target: choose and measure a budget suitable for the interaction. A single expensive item may need splitting too. `await Promise.resolve()` only schedules a microtask and does not reliably give input or paint a turn.

Yielding allows other work to interleave, so preserve required ordering and handle cancellation or state changes between chunks. The timeout fallback yields without the scheduler's continuation priority. Avoid adding yields to trivial work without evidence.

Source: [Break Up Long Tasks](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/performance/break-up-long-tasks.md), v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`. At this snapshot `scheduler.yield()` has limited support, including no Safari support; feature-detect against the application's actual browser targets.
