---
id: modern-web-guidance.css.choose-clip-or-scroll-for-overflow
title: Keep Overflowing Content Reachable
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: content exceeds a constrained box or a visual effect needs clipping
anti_patterns:
  - id: modern-web-guidance.css.choose-clip-or-scroll-for-overflow.counterexample
    name: Hide overflow without deciding how content is accessed
    description: Clipping a box to hide a layout defect can make content or controls unreachable.
    severity: warn
---

## Guidance

First fix unintended overflow: let layouts wrap, allow flex items to shrink, and wrap long strings where appropriate. If content must remain accessible in a constrained region, use `overflow: auto`; consider `scrollbar-gutter: stable` to avoid shifts and `overscroll-behavior: contain` when a nested scroller should not hand scrolling to the page. If only decoration should be clipped, use `overflow: clip`, which does not create a scroll container.

## Exceptions and boundaries

Do not clip essential content without another accessible way to reach it. `overflow: hidden` can be scrolled programmatically and is not equivalent to `clip`; choose a deliberate fallback for browsers that lack `clip`. Scroll containment is not always desirable: retain scroll chaining when users should continue scrolling the parent. Check keyboard access and visible focus in constrained regions.

## Example

```css
.results { max-block-size: 25rem; overflow: auto; scrollbar-gutter: stable; overscroll-behavior: contain; }
.decoration { overflow: hidden; overflow: clip; }
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [css-layout.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/css-layout.md)
- [overflow-clipping-control.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/overflow-clipping-control.md)
