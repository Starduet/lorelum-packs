---
id: modern-web-guidance.css.derive-sibling-position-progressively
title: Derive Sibling Position Without Duplicated Indices
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: decorative styling varies with an element’s sibling index or sibling count
anti_patterns:
  - id: modern-web-guidance.css.derive-sibling-position-progressively.counterexample
    name: Derive Sibling Position Without Duplicated Indices counterexample
    description: Hardcoded per-item indices become stale when children are inserted or removed.
    severity: warn
---

## When to apply

Apply when decorative styling varies with an element’s sibling index or sibling count.

## Guidance

Use `sibling-index()` and `sibling-count()` for per-sibling CSS calculations when supported, with a usable static base style. Feature-detect the exact expressions before any necessary index fallback.

## Anti-pattern

Hardcoded per-item indices become stale when children are inserted or removed.

## Why

The browser computes index and count from the current sibling structure.

## Exceptions and boundaries

These functions count siblings, not only elements matching a class; a script fallback must match that semantics and update after DOM changes. If the variation is essential, provide and maintain an equivalent fallback; otherwise a static visual fallback is simpler. Confirm actual browser support for the deployment target.

## Example

```css
.swatch { background: steelblue; }
@supports (width: calc(sibling-index() * 1px)) and (width: calc(sibling-count() * 1px)) {
  .swatch { background: hsl(calc(360deg / sibling-count() * sibling-index()) 70% 50%); }
}
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [dynamic-sibling-styling.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/dynamic-sibling-styling.md)
