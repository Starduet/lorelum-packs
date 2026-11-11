---
id: modern-web-guidance.css.query-component-container-size
title: Query the Component Container for Responsive Layout
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: a reusable component needs different layouts in narrow and wide available space
anti_patterns:
  - id: modern-web-guidance.css.query-component-container-size.counterexample
    name: Query the Component Container for Responsive Layout counterexample
    description: A viewport media query assumes a card in a narrow sidebar has the same width as a card in the main column.
    severity: warn
---

## When to apply

Apply when a reusable component needs different layouts in narrow and wide available space.

## Guidance

Put `container-type: inline-size` on an ancestor wrapper and query that ancestor from its descendants. Name the container when nested query contexts could be ambiguous. Start with a usable narrow layout outside the query.

## Anti-pattern

A viewport media query assumes a card in a narrow sidebar has the same width as a card in the main column.

## Why

A container query follows the space actually allocated to the component, rather than the viewport.

## Exceptions and boundaries

Use media queries for page-level layout or user preferences. Size containment changes intrinsic sizing; `container-type: size` contains both axes and needs a definite block size. A container cannot query itself. Test target browsers and retain the base layout where queries are unsupported.

## Example

```css
.card-slot { container: card / inline-size; }
.card { display: block; }
@container card (inline-size > 30rem) {
  .card { display: flex; gap: 1rem; }
}
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [size-aware-styling.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/size-aware-styling.md)
- [css-layout.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/css-layout.md)
- [responsive-design.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/responsive-design.md)
