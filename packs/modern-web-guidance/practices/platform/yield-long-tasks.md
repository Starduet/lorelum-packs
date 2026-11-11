---
id: modern-web-guidance.platform.yield-long-tasks
title: Yield Long Main-Thread Work
stage: implementation
severity: warn
applies_when: a browser-side loop or computation blocks input or rendering for long periods
tech_stack:
  - javascript
  - web
anti_patterns:
  - id: modern-web-guidance.platform.unbroken-main-thread-work
    name: Unbroken main-thread work
    severity: warn
    description: A large synchronous loop monopolizes the main thread and delays interaction and paint.
---

Break interruptible work into chunks and yield to the browser between them. A time budget can accommodate items with variable cost; 50 ms is the long-task threshold, not a guarantee of good responsiveness. Measure on representative devices and choose a smaller budget when needed.

```js
async function processItems(items) {
  let deadline = performance.now() + 30;
  for (const item of items) {
    processItem(item);
    if (performance.now() >= deadline) {
      if (globalThis.scheduler && typeof globalThis.scheduler.yield === 'function') {
        await globalThis.scheduler.yield();
      } else {
        await new Promise(resolve => setTimeout(resolve, 0));
      }
      deadline = performance.now() + 30;
    }
  }
}
```

A resolved promise alone yields to the microtask queue, not necessarily to rendering or input. The timeout fallback yields but does not reproduce scheduler continuation priority. One expensive item can still exceed the budget; split that item or consider a worker when appropriate. Yielding changes interleaving, so preserve ordering and account for state changes or cancellation across yields. Do not add yields to trivial work without evidence.

Source: [Break Up Long Tasks](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/performance/break-up-long-tasks.md), v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`. At this snapshot `scheduler.yield()` has limited support, including no Safari support; feature-detect against the application's actual browser targets.
