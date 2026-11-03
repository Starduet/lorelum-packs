---
anti_patterns:
  - description: A value computed from current props and state is copied into another piece of state and refreshed by an effect, adding an extra render per change and a version that can drift from its inputs.
    id: react.rendering.mirroring-derived-value
    name: Derived value mirrored into state
    severity: warn
applies_when: a render value can be computed from current props or state, and a decision is needed between deriving it and storing it
id: react.rendering.derive-dont-mirror
severity: warn
stage: implementation
tech_stack:
  - react
title: Derive Render Values; Do Not Mirror Props into State
---

## When to apply

If a displayed total, label, or other value always follows from current props and state, there is
usually no need to store it separately and refresh it in an effect. First check whether the user or
an external system can change it independently; if not, calculate it from its current inputs.

## Guidance

If the value is a pure function of current props and state, compute it during render and delete the
state and the effect:

```tsx
const totalWithTax = subtotal + subtotal * taxRate;
```

The stored copy can be stale in the render before the effect updates it. It can also stay stale if
the effect misses an input change. Computing the value during render avoids maintaining a second
copy and scheduling another state update.

Keep these different cases separate:

- The value starts from a prop but the user edits it: that is an editable draft with its own
  lifecycle; initialize from the prop and own it thereafter.
- The value must reset when an identity changes (a form bound to a different record): reset
  explicitly with a `key` at the identity boundary, not by watching props in an effect.
- The computation is expensive: still derive the value, and memoize the calculation if measurement
  justifies it. Caching does not fix the problem of maintaining a second copy.

Apply the same test to an effect that sets state whenever a prop changes. Effects may synchronize
with external systems; what should go is an effect that merely copies or recalculates a value from
props inside the same render tree.

## Anti-pattern

An invoice editor keeps `total` in state and recomputes it in an effect after line items or tax rate
change. Changing an item first renders the old total, then the effect schedules another render. If
the effect's dependencies omit an input changed by bulk import, the total can remain out of sync
with the imported items.

## Why

A derived value stored in state is a second copy of a calculation. Its effect cannot update that
copy until after the render that used the changed inputs. Calculating during render uses the current
inputs immediately, so there is no copy to synchronize and no extra state update for that value.

## Exceptions and boundaries

- Values with genuine user ownership or independent lifetimes stay in state; this Practice does not
  shrink state, it removes duplicated state.
- Deriving values during render must stay pure: no side effects, no writes, even for expensive
  derivations.
- Memoizing a derivation with `useMemo` uses memory and requires correct dependencies to save
  computation. Decide whether that pays off through measurement, taking React Compiler into account.
- Reading and adjusting DOM in effects for layouts React cannot express is external-system
  synchronization, not value mirroring.

## Example

An invoice summary derives both figures from its inputs during render. There is no second state to
fall out of sync and no effect to forget.

```tsx
function InvoiceSummary({ lines, taxRate }: { lines: InvoiceLine[]; taxRate: number }) {
  const subtotal = lines.reduce((sum, line) => sum + line.amount, 0);
  const totalWithTax = subtotal + subtotal * taxRate;

  return (
    <dl>
      <dt>Subtotal</dt>
      <dd>{subtotal}</dd>
      <dt>Total with tax</dt>
      <dd>{totalWithTax}</dd>
    </dl>
  );
}
```

Adding, removing, or editing a line updates both figures in the same render that shows the change.
If profiling ever shows the reduction matters on very large invoices, `useMemo` wraps this exact
derivation — the shape of the code does not change, only its caching.
