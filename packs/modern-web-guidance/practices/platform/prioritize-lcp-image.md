---
id: modern-web-guidance.platform.prioritize-lcp-image
title: Prioritize the Actual LCP Image
stage: implementation
severity: warn
applies_when: optimizing image loading for a page whose likely Largest Contentful Paint element is an image
tech_stack:
  - html
  - web
anti_patterns:
  - id: modern-web-guidance.platform.lazy-load-lcp-image
    name: Lazy-loading the LCP image
    severity: warn
    description: The likely LCP image is deferred as offscreen content or competes with many other high-priority images.
---

Identify the likely Largest Contentful Paint (LCP) image using measurements across relevant pages and viewports. Make it discoverable in the initial markup, avoid `loading="lazy"`, and consider `fetchpriority="high"` to hint its importance. Reserve high priority for at most one or two critical images so other resources are not starved. Hints do not guarantee scheduling or replace measurement.

Use `loading="lazy"` for ordinary below-the-fold images without also lowering their fetch priority; they should load normally when approached. `fetchpriority="low"` can help for initially hidden images such as inactive carousel slides or menu promotions. Preserve dimensions and appropriate alternative text.

The source identifies fetch priority as Baseline newly available in October 2024. Unsupported browsers ignore the hint and use their own heuristics; lazy loading support and image choice also depend on target browsers and layout. If LCP is text or varies by viewport, do not blindly elevate a hero image.

Source: [Optimize image priority](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/performance/optimize-image-priority.md), v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`.
