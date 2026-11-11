---
id: modern-web-guidance.css.animate-intrinsic-sizes-progressively
title: Animate Intrinsic Sizes as Progressive Enhancement
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: expanding or collapsing an element to its content-driven size
anti_patterns:
  - id: modern-web-guidance.css.animate-intrinsic-sizes-progressively.counterexample
    name: Animate Intrinsic Sizes as Progressive Enhancement counterexample
    description: Animating a hardcoded maximum height either clips larger content or takes a visibly inconsistent duration.
    severity: warn
---

## When to apply

Apply when expanding or collapsing an element to its content-driven size.

## Guidance

For a transition between a length and `auto`, opt into `interpolate-size: allow-keywords` on the element or an ancestor. Use `calc-size()` only if the intrinsic size needs arithmetic, with a preceding ordinary size fallback.

## Anti-pattern

Animating a hardcoded maximum height either clips larger content or takes a visibly inconsistent duration.

## Why

The browser can interpolate the actual intrinsic size without measuring it in JavaScript.

## Exceptions and boundaries

Support is limited in the pinned upstream snapshot; unsupported browsers should switch sizes instantly. Two intrinsic keywords cannot be interpolated directly. Respect reduced motion; synchronize expanded state and remove closed content from keyboard and assistive-technology access. Size animation triggers layout.

## Example

```css
.panel { interpolate-size: allow-keywords; block-size: 0; overflow: clip; visibility: hidden; transition: block-size .2s, visibility .2s; }
.panel.open { block-size: auto; visibility: visible; }
@media (prefers-reduced-motion: reduce) { .panel { transition: none; } }
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [animate-to-intrinsic-sizes.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/animate-to-intrinsic-sizes.md)
- [calculate-with-intrinsic-sizes.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/calculate-with-intrinsic-sizes.md)
