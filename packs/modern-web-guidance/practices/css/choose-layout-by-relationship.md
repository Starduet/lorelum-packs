---
id: modern-web-guidance.css.choose-layout-by-relationship
title: Choose a Layout Mode by Its Relationship
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: choosing CSS layout for a row, grid, or nested alignment
anti_patterns:
  - id: modern-web-guidance.css.choose-layout-by-relationship.counterexample
    name: Choose a Layout Mode by Its Relationship counterexample
    description: Using a two-dimensional grid for every toolbar or fixed widths for every card ties layout to today’s content.
    severity: warn
---

## When to apply

Apply when choosing CSS layout for a row, grid, or nested alignment.

## Guidance

Use flexbox for a single content-driven row or column; use grid for a two-dimensional skeleton and subgrid when nested items must align with parent tracks. Use multicolumn for flowing prose. Prefer intrinsic sizes, flexible tracks and gap to fixed dimensions.

## Anti-pattern

Using a two-dimensional grid for every toolbar or fixed widths for every card ties layout to today’s content.

## Why

Flex distributes along one axis; grid describes tracks on both axes, while subgrid shares tracks instead of approximating their dimensions.

## Exceptions and boundaries

Subgrid needs a preceding explicit track fallback if the target includes browsers without support. Dense grid packing is not masonry and can change visual order; avoid it for interactive items. Preserve DOM order for keyboard users.

## Example

```css
.toolbar { display: flex; flex-wrap: wrap; gap: 1rem; }
.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr)); gap: 1rem; }
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [css-layout.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/css-layout.md)
