---
id: modern-web-guidance.css.query-component-container-size
title: Adapt a Reusable Component to Its Available Space
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: a reusable component needs different layouts in narrow and wide regions
anti_patterns:
  - id: modern-web-guidance.css.query-component-container-size.counterexample
    name: Tie a reusable component to viewport width
    description: A viewport breakpoint can make a narrow sidebar card use the layout intended for a wide main-content card.
    severity: warn
---

## Guidance

Start with a usable narrow layout. Set `container-type: inline-size` on a sized ancestor and query it from the component; name the container when nested contexts could otherwise select the wrong ancestor. Choose the breakpoint where the component content needs more room, not by device name. Use media queries instead for page-level changes and user preferences.

## Exceptions and boundaries

A container cannot query itself. Size containment affects intrinsic sizing; use `container-type: size` only when both axes need querying and the block size is provided. The narrow base must remain usable without container queries. Check reflow at 200% text resize.

## Example

```css
.card-slot { container: card / inline-size; }
.card { display: flex; flex-direction: column; gap: 1rem; }
@container card (inline-size > 30rem) {
  .card { flex-direction: row; }
}
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [size-aware-styling.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/size-aware-styling.md)
- [css-layout.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/css-layout.md)
- [responsive-design.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/responsive-design.md)
