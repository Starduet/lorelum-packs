---
anti_patterns:
  - description: A JSX conditional guards rendering with `&&` on a numeric or string expression whose falsy domain includes renderable values, so `0` or `NaN` appears in the interface.
    id: react.rendering.falsy-left-operand-rendered
    name: Falsy left operand rendered by `&&`
    severity: warn
applies_when: a conditional render uses `&&` on an expression that can be `0`, `NaN`, or another falsy value that is not boolean
id: react.rendering.boolean-render-guards
severity: warn
stage: implementation
tech_stack:
  - react
title: Make Render Conditions Actually Boolean
---

## When to apply

Apply while writing or reviewing `{value && <Thing />}`. Check what happens when `value` is falsy:
does React receive a value it ignores, such as `false`, or a number it displays, such as `0`?

## Guidance

`&&` returns its left operand when falsy, and JSX renders numbers — so `{count && <Badge />}` shows
the text `0` whenever the count is zero. When the condition's type is not genuinely boolean, reduce
it to one first:

```tsx
{error.code > 0 && <ErrorBanner code={error.code} />}
```

Use an explicit comparison, `Boolean(...)`, or a ternary with a `null` branch to state when the
element should appear. Handle `NaN` and empty strings deliberately too; in particular, `NaN`, like
`0`, can appear as text if passed through as the left operand.

Keep `&&` when the left operand is already boolean — a flag, comparison, or predicate call.
`{isOpen && <Panel />}` is idiomatic and correct. Check whether a falsy result could be displayed
instead of hidden; this is about the expression's type, not a preference for one JSX style.

## Anti-pattern

An error banner is guarded by `{error.code && <Banner ... />}` where `code` is `0` on success and a
nonzero code on failure. On every success path the page renders a stray `0` next to the form,
because zero is falsy but still a number JSX displays.

## Why

When the left operand is falsy, `&&` returns that operand, not necessarily `false`. React displays
numbers such as `0` and `NaN`, but ignores boolean children. A boolean condition therefore separates
the decision to show the element from the value that should be displayed.

## Exceptions and boundaries

- Genuinely boolean conditions need no change; adding `Boolean()` around a `bool` is noise.
- If zero is a meaningful display value, the ternary form makes that intent explicit — this Practice
  does not say zero must never render, only that its rendering must be chosen.
- TypeScript narrows some of this: a typed `boolean` left operand cannot leak a number, so the
  failure mode lives at untyped boundaries, API responses, and arithmetic results.
- This Practice governs render conditions only; it does not cover truthiness in non-JSX logic, where
  `if (items.length)` may be perfectly clear.

## Example

A search results header shows the match count only when there is at least one result. The comparison
makes the zero case explicit; the previous `resultCount && ...` shape rendered the text `0` under
the heading whenever the result set came back empty.

```tsx
function ResultsHeader({ resultCount }: { resultCount: number }) {
  return (
    <header>
      <h1>Results</h1>
      {resultCount > 0 && (
        <p>
          {resultCount} match{resultCount === 1 ? "" : "es"}
        </p>
      )}
    </header>
  );
}
```

An empty result set now renders the heading alone. If the product decision were to show "0 matches"
instead, the ternary form would say so — the point of the Practice is that the zero case's meaning
appears in the code rather than falling out of a coercion.
