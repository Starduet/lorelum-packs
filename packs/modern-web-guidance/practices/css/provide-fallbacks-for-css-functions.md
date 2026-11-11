---
id: modern-web-guidance.css.provide-fallbacks-for-css-functions
title: Provide Fallbacks for CSS Custom Functions
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: reusing parameterized CSS value logic across several declarations
anti_patterns:
  - id: modern-web-guidance.css.provide-fallbacks-for-css-functions.counterexample
    name: Provide Fallbacks for CSS Custom Functions counterexample
    description: Using an unsupported custom function as the only background value leaves the component without the intended background.
    severity: warn
---

## When to apply

Apply when reusing parameterized CSS value logic across several declarations.

## Guidance

Use a dashed-name `@function` for genuinely repeated or complex runtime value logic, and declare a usable ordinary value before each function-dependent declaration.

## Anti-pattern

Using an unsupported custom function as the only background value leaves the component without the intended background.

## Why

An earlier valid declaration remains in effect when a browser cannot parse the newer declaration.

## Exceptions and boundaries

The pinned upstream reports limited support for CSS custom functions. Simple repeated values may be clearer as custom properties; static logic can be precompiled. An acceptable fallback must preserve essential contrast and layout, not merely parse.

## Example

```css
@function --card-background(--tone <color>) returns <color> { result: var(--tone); }
.card { background: steelblue; background: --card-background(steelblue); }
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [reduce-style-repetition.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/reduce-style-repetition.md)
