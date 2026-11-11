---
id: modern-web-guidance.css.fit-viewport-layout-to-browser-chrome
title: Fit Viewport Layout to Mobile Browser Chrome
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: sizing a page region to the visible mobile viewport
anti_patterns:
  - id: modern-web-guidance.css.fit-viewport-layout-to-browser-chrome.counterexample
    name: Fit Viewport Layout to Mobile Browser Chrome counterexample
    description: A fixed `100vh` region can be taller than the visible area when mobile browser controls are present.
    severity: warn
---

## When to apply

Apply when sizing a page region to the visible mobile viewport.

## Guidance

Use a dynamic viewport unit for a region that must track the changing visible viewport, with an ordinary viewport-unit fallback. For a normal full-width block, prefer `inline-size: 100%` to viewport width.

## Anti-pattern

A fixed `100vh` region can be taller than the visible area when mobile browser controls are present.

## Why

Dynamic units respond as browser chrome expands or collapses; percentages size a normal block against its container.

## Exceptions and boundaries

Dynamic units can resize during scrolling; use a small viewport unit if a stable minimum visible size is the real requirement. Check target support and keep a fallback. Do not assume viewport width units exclude scrollbars.

## Example

```css
.screen { min-block-size: 100vh; min-block-size: 100dvb; }
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [responsive-design.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/responsive-design.md)
- [css-layout.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/css-layout.md)
