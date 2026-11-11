---
id: modern-web-guidance.platform.diagnose-slow-page-loading
title: Diagnose Slow Page Loading Before Prioritizing Resources
stage: implementation
severity: warn
applies_when: a page loads slowly or its main content takes too long to appear, particularly on mobile or slow connections
tech_stack:
  - html
  - web
anti_patterns:
  - id: modern-web-guidance.platform.guess-loading-bottleneck
    name: Prioritizing resources without identifying the bottleneck
    severity: warn
    description: A page marks many images high priority without checking which content is actually delayed or what blocks it.
---

Measure the affected route and representative viewport and connection; identify the Largest Contentful Paint (LCP) element and inspect the request and rendering timeline. First distinguish slow document delivery, late discovery or loading of a critical resource, and time spent rendering after it arrives. Fix the observed bottleneck rather than assuming every slow page needs an image hint.

When the LCP element is an image discovered late, expose it in initial markup where possible; do not lazy-load it. Consider `fetchpriority="high"` for the actual critical image, not every image. Use lazy loading for ordinary below-the-fold images and reserve their dimensions to reduce layout shift. If LCP is text, or changes across viewports, elevating a hero image can waste bandwidth.

If render-blocking CSS or JavaScript delays the content, inspect the critical path and defer noncritical scripts or reduce blocking work where safe. Preload a resource only when it is needed for the current render and otherwise discovered late; hints compete for bandwidth and do not guarantee scheduling. Re-measure the same user-facing scenario after the change.

Sources: [Performance](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/performance/performance.md) and [Optimize image priority](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/performance/optimize-image-priority.md), upstream commit `4dd9683`.
