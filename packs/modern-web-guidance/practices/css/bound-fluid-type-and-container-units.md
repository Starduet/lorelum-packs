---
id: modern-web-guidance.css.bound-fluid-type-and-container-units
title: Bound Fluid Typography and Define Its Container
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: scaling component or page typography continuously with available space
anti_patterns:
  - id: modern-web-guidance.css.bound-fluid-type-and-container-units.counterexample
    name: Bound Fluid Typography and Define Its Container counterexample
    description: Sizing text only with `vw` can make it illegible on small screens and fail to respond adequately to zoom.
    severity: warn
---

## When to apply

Apply when scaling component or page typography continuously with available space.

## Guidance

Use `clamp()` with font-relative bounds and a mixed font-relative and viewport or container-relative preferred value. For component units, establish a qualifying ancestor container and ensure it receives a usable size.

## Anti-pattern

Sizing text only with `vw` can make it illegible on small screens and fail to respond adequately to zoom.

## Why

Font-relative bounds protect minimum readability; a qualifying container makes `cqi` reflect component space instead of a viewport fallback.

## Exceptions and boundaries

Upstream recommends a maximum no more than 2.5 times the minimum; still test 200% text resize and reflow because this ratio alone does not guarantee accessibility. Container units fall back to the small viewport when no eligible container exists. Provide a fixed font-size first for browsers lacking required syntax.

## Example

```css
.panel { container-type: inline-size; }
.panel h2 { font-size: 1.25rem; font-size: clamp(1.25rem, 1rem + 2cqi, 2rem); }
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [fluid-scaling.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/fluid-scaling.md)
- [responsive-design.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/responsive-design.md)
