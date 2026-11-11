---
id: modern-web-guidance.css.feature-detect-the-required-css-capability
title: Feature Detect the CSS Capability Actually Needed
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: an enhancement depends on support for a specific CSS selector, value, or at-rule
anti_patterns:
  - id: modern-web-guidance.css.feature-detect-the-required-css-capability.counterexample
    name: Feature Detect the CSS Capability Actually Needed counterexample
    description: Testing `@container` by name does not establish that style queries or another specific container query syntax work.
    severity: warn
---

## When to apply

Apply when an enhancement depends on support for a specific CSS selector, value, or at-rule.

## Guidance

Keep a functional base style, then detect the relevant selector or declaration with `@supports`. Use `at-rule()` only when its own support meets the browser target and at-rule name detection is sufficient.

## Anti-pattern

Testing `@container` by name does not establish that style queries or another specific container query syntax work.

## Why

Support for a feature family does not imply support for every descriptor or nested syntax.

## Exceptions and boundaries

Unknown at-rules are already ignored; do not wrap an at-rule only to hide it. `container-type: style` is not a valid style-query support test. A parser support test is not proof of correct behavior; test the rendered result when necessary.

## Example

```css
.card { display: block; }
@supports (container-type: inline-size) {
  .slot { container-type: inline-size; }
}
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [atrule-support-conditionals.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/atrule-support-conditionals.md)
