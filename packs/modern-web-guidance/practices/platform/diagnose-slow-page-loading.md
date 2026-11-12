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

Measure the affected route with a representative viewport, device, connection and cache state; compare field data when available with a reproducible browser performance recording. Locate the actual Largest Contentful Paint (LCP) element in the trace, and note that it can differ by viewport, content or visit. For an image candidate, inspect the document and image requests in the network waterfall together with the rendering timeline:

1. **Document response:** If time to first byte dominates, inspect redirects, server response and cache behavior before changing image priority.
2. **Resource load delay:** Compare the document response with the image request start. Check whether the image is present in the initial HTML, discovered only after a stylesheet or script runs, or marked lazy. Expose the actual image in initial markup and remove lazy loading when feasible. For a CSS background or script-discovered image that must remain late-discovered, consider an early preload matching the eventual URL, responsive selection and request mode; a mismatch can fetch an unused or duplicate resource.
3. **Resource load duration:** Inspect transfer size, response and request priority, connection setup and competing requests. Serve an appropriately sized image and consider raising priority for the actual LCP image or reducing competition, rather than marking all images high priority. A hint cannot fix an intrinsically slow response or guarantee a scheduling order.
4. **Element render delay:** If the image has finished loading but paints much later, inspect render-blocking CSS, script execution, layout, image decoding, and whether the element is hidden pending application work. Defer noncritical scripts only when their ordering and behavior remain correct; reduce the measured blocking work. If LCP is text, inspect its markup, fonts and rendering path instead of prioritizing an unrelated hero image.

For an identified critical image in initial markup, a possible change is:

```html
<img src="/images/hero.webp" alt="Product in use"
     width="1200" height="600" fetchpriority="high">
```

The image is eager by default; use real dimensions and meaningful alternative text for the content. `fetchpriority` is a hint and unsupported browsers use their normal priority. Lazy-load ordinary offscreen images and reserve their dimensions; use low priority selectively for initially hidden competing images, not automatically for every lazy image that must load promptly on scrolling. Preloads and high-priority hints consume shared bandwidth, so remove those that do not help the actual critical path.

Re-record the same route and conditions, including relevant viewport and cache variants. Verify the LCP candidate, request start and completion, final paint, and competing resource timings; check that no duplicate fetch, missing content, ordering regression or layout shift was introduced. Stop adding hints when the measured bottleneck is elsewhere or the user-visible result does not improve.

Sources: [Performance](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/performance/performance.md) and [Optimize image priority](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/performance/optimize-image-priority.md), upstream commit `4dd9683`.
