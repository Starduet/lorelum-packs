---
id: modern-web-guidance.css.choose-clip-or-scroll-for-overflow
title: Choose Clipping or Scrolling Deliberately
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: content overflows a box or decoration needs a controlled clip boundary
anti_patterns:
  - id: modern-web-guidance.css.choose-clip-or-scroll-for-overflow.counterexample
    name: Choose Clipping or Scrolling Deliberately counterexample
    description: "Applying `overflow: hidden` to mask an unexplained layout gap can hide focus indicators or content and creates a scroll container."
    severity: warn
---

## When to apply

Apply when content overflows a box or decoration needs a controlled clip boundary.

## Guidance

Use `overflow: auto` when content must remain scrollable, and `overflow: clip` when it must not create a scroll container. Use `overflow-clip-margin` to allow intentional visual spill beyond the clip edge.

## Anti-pattern

Applying `overflow: hidden` to mask an unexplained layout gap can hide focus indicators or content and creates a scroll container.

## Why

Scrolling, clipping, and layout repair have different semantics; masking the cause can make content inaccessible.

## Exceptions and boundaries

Fix unintended overflow at its source first. Clipped essential content needs another accessible means of access. Where `clip` is unsupported, choose a tested fallback deliberately: `hidden` is programmatically scrollable and not equivalent.

## Example

```css
.decoration { overflow: hidden; overflow: clip; overflow-clip-margin: 0.5rem; }
.results { max-block-size: 20rem; overflow: auto; }
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [overflow-clipping-control.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/overflow-clipping-control.md)
- [css-layout.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/css-layout.md)
