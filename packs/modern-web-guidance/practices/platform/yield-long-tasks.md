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

Record the affected interaction in a browser performance trace on a representative device and dataset. Follow the input through the main-thread flame chart and inspect task duration, call stacks, style recalculation, layout and paint; compare the delay before the handler runs with the work performed by the handler and rendering afterward. A long script stack suggests computation; repeated layout events between DOM reads and writes suggest forced synchronous layout. For the latter, batch reads such as `getBoundingClientRect()` before writes, and reduce the amount of DOM affected. Yielding a loop alone will not fix an expensive layout or paint.

Remove unnecessary work first. For CPU-heavy work independent of the DOM, consider a Web Worker: measure startup, copying or transferring data, and result delivery as well as computation. Workers cannot directly manipulate the DOM; transferables can avoid copies but transfer ownership, so the sender must not keep using a transferred buffer. Handle worker errors, and when requests can be cancelled or superseded, prevent obsolete results from being applied. If the operation needs the DOM, cannot justify worker overhead, or must run where workers are unavailable, split interruptible work on the main thread instead. Do not split an operation whose partial effects cannot safely be interrupted unless it can stage and commit them atomically.

Choose consistency safeguards for the operation: immutable input or work that cannot overlap with changes may need no snapshot or generation tracking. If input can change across yields, use a stable snapshot or another consistency mechanism when a coherent result is required. If cancellation or replacement can occur, check for it and discard obsolete results. For example, this operation supports both and stages an ordered result; the caller supplies a measured budget and increments its generation when starting a replacement or invalidating the input:

```js
async function buildResult(itemsSnapshot, budgetMs, signal, isCurrent) {
  const result = [];
  let deadline = performance.now() + budgetMs;
  for (const item of itemsSnapshot) {
    if (signal.aborted || !isCurrent()) return null;
    result.push(processItem(item)); // synchronous, without externally visible effects
    if (performance.now() >= deadline) {
      if (typeof globalThis.scheduler?.yield === "function") {
        await globalThis.scheduler.yield();
      } else {
        await new Promise(resolve => setTimeout(resolve, 0));
      }
      deadline = performance.now() + budgetMs;
    }
  }
  if (signal.aborted || !isCurrent()) return null;
  return result; // caller checks currency again immediately before committing
}
```

In this example the snapshot must actually remain unchanged during processing. Check cancellation and generation after every yield and immediately before a synchronous commit when those races are possible; discard staged data on cancellation or error rather than publishing partial output, and surface errors appropriately for the operation. Side effects such as writes to a server need their own cancellation, idempotency or rollback design when applicable; stopping a loop does not undo them. A single expensive item may itself need splitting or moving to a worker. `await Promise.resolve()` only schedules a microtask and does not reliably give input or paint a turn; the timeout fallback also lacks the scheduler continuation's priority.

The 50 ms long-task threshold is a diagnostic boundary, not a responsiveness target or a worker-selection rule. Choose a budget from measurements, not a fixed iteration count. Repeat the trace with the same input and device conditions: confirm input and paint can occur between chunks, long blocking work or layout has actually decreased, and the result remains correct, including after cancellation or replacement if supported. Stop adding yields if overhead outweighs the observed benefit or the remaining delay comes from another source.

Source: [Break Up Long Tasks](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/performance/break-up-long-tasks.md), v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`. At this snapshot `scheduler.yield()` has limited support, including no Safari support; feature-detect against the application's actual browser targets.
