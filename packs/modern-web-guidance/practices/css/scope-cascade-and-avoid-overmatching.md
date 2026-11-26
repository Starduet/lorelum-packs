---
id: modern-web-guidance.css.scope-cascade-and-avoid-overmatching
title: Make Cascade Priority and Selector Intent Explicit
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: designing CSS rules that otherwise require specificity escalation or reset overrides
anti_patterns:
  - id: modern-web-guidance.css.scope-cascade-and-avoid-overmatching.counterexample
    name: Make Cascade Priority and Selector Intent Explicit counterexample
    description: A generic hover rule followed by a disabled override becomes incorrect when the rules are reordered.
    severity: warn
---

## Guidance

When a declaration wins unexpectedly, inspect the element's matched rules and computed property in browser developer tools. Check whether the rule matches the intended element and state first; then compare origin and importance, layer priority, specificity, scope proximity where applicable, and finally source order. Inheritance matters when no declaration wins on the element itself. Fix the source of competition rather than adding another higher-specificity reset.

Exclude fundamentally irrelevant states instead of styling them and undoing the value later. For example:

```css
button:hover:not(:disabled) { background: var(--color-blue); }
button:disabled { background: var(--color-neutral); }
```

The hover rule no longer matches a disabled native button even if the rules change order. An `aria-disabled` custom control is not matched by `:disabled`: handle its semantics and state separately. Conversely, a base button style followed by a primary-button style is legitimate specialization, not necessarily overmatching.

## Layers and scope

If rules repeatedly compete across parts of the stylesheet, first inventory existing layered and unlayered rules, imports, and `!important` declarations. An explicit order such as `@layer base, components, utilities;` makes later layers win for normal declarations; normal unlayered author rules still outrank all normal layered author rules. For important declarations layer order reverses, and important layered rules outrank important unlayered rules. Moving only one existing rule into a layer can therefore change its winner. Migrate deliberately rather than wrapping a single file and assuming its old priority remains.

Within the intended layer, `:where()` gives its arguments zero specificity, useful for overridable defaults or incidental filters. It does not erase specificity outside the function: `.card :where(a)` still has the class selector's specificity. Follow existing naming conventions instead of escalating selectors.

For a nested subtree boundary, `@scope` can express a scope root and limit more reliably than a long descendant `:not()` selector:

```css
@scope (.card) to (.card__content) {
  h2 { margin-block: 0; }
}
```

This applies to headings in the card scope outside the limited content subtree. Check browser support against the project's target before relying on `@scope`; an unsupported block is ignored, so provide a separate safe fallback if the style is essential. Scope proximity is considered only after higher-priority cascade criteria such as layer and specificity; it is not a universal override.

## Validation

Inspect computed styles and matched rules for the states affected by the change. For the button example, include enabled, hovered and disabled controls; the disabled button should not match the hover rule regardless of source order. For layered changes, inspect representative existing overrides and `!important` rules before and after migration; for scoped rules, exercise the relevant nested and excluded subtrees and any fallback required by the project's browser target. If an unrelated component's winning value changes unexpectedly, adjust the scope or layer plan rather than adding an arbitrary override.

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [css.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/css.md)
