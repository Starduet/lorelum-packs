---
id: modern-web-guidance.css.use-style-queries-for-context-tokens
title: Use Style Queries for Contextual Component Tokens
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: a descendant component varies based on an ancestor’s semantic design token
anti_patterns:
  - id: modern-web-guidance.css.use-style-queries-for-context-tokens.counterexample
    name: Use Style Queries for Contextual Component Tokens counterexample
    description: A card hardcoded to `.featured .card` couples a reusable component to one particular producer of featured context.
    severity: warn
---

## When to apply

Apply when a descendant component varies based on an ancestor’s semantic design token.

## Guidance

Set a custom property on the context and query it with `@container style()` to style descendants, leaving the component independent of the context’s class name. When several selectors or media conditions produce the same context, resolve them into that token before querying it.

## Anti-pattern

A card hardcoded to `.featured .card` couples a reusable component to one particular producer of featured context.

## Why

The token describes the shared meaning; multiple contexts can provide it and multiple components can consume it.

## Exceptions and boundaries

Style queries query an ancestor, not the element being styled, and do not require size containment. For unsupported browsers, preserve a usable default or provide a selector-based fallback for essential variations; simple ancestor selectors can mishandle nested contexts. Check the actual target matrix rather than relying on a dated support snapshot.

## Example

```css
.featured { --surface: featured; }
.card { border: 1px solid gray; }
@container style(--surface: featured) { .card { border-width: 3px; } }
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [design-token-reactivity.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/design-token-reactivity.md)
- [usage-aware-component-variations.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/usage-aware-component-variations.md)
- [selector-atrule-combinations.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/selector-atrule-combinations.md)
