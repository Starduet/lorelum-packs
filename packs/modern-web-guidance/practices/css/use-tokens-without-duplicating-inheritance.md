---
id: modern-web-guidance.css.use-tokens-without-duplicating-inheritance
title: Use Design Tokens Without Duplicating Built-In Relationships
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: defining shared colors, spacing, and component design values
anti_patterns:
  - id: modern-web-guidance.css.use-tokens-without-duplicating-inheritance.counterexample
    name: Use Design Tokens Without Duplicating Built-In Relationships counterexample
    description: Creating a custom property for every inherited color and repeating its assignment on each child obscures the built-in relationship.
    severity: warn
---

## When to apply

Apply when defining shared colors, spacing, and component design values.

## Guidance

Reuse the project’s token conventions for shared decisions, with semantic aliases where they add meaning. Prefer `currentColor`, inheritance, or relative units when they already represent the relationship.

## Anti-pattern

Creating a custom property for every inherited color and repeating its assignment on each child obscures the built-in relationship.

## Why

A token captures a reusable design decision; built-in inheritance keeps dependent values synchronized without another source of truth.

## Exceptions and boundaries

Use only as many token tiers as the product needs; an isolated demo may need one. Dynamic data-driven inline values may be appropriate, but avoid embedding recurring design constants in markup.

## Example

```css
:root { --accent: rebeccapurple; }
.notice { color: var(--accent); border: 1px solid currentColor; }
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [css.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/css.md)
