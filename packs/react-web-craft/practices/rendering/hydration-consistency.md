---
anti_patterns:
  - description: A server-rendered page reads browser-only state during render or patches divergent text with `suppressHydrationWarning`, so the first client render disagrees with server output and hydration either fails or silently papers over real mismatches.
    id: react.rendering.hydrating-over-divergent-output
    name: Hydrating over divergent output
    severity: warn
applies_when: a server-rendered tree contains values that can differ between server output and the first client render, and the treatment of that difference is being chosen
id: react.rendering.hydration-consistency
severity: warn
stage: implementation
tech_stack:
  - react
  - next
title: Keep the First Client Render Equal to Server Output
---

## When to apply

Times, locale and timezone formatting, random or per-instance identifiers, and browser storage can
produce different output on the server and in the browser. If a server-rendered component uses them,
decide how to keep its first client render consistent or handle a narrowly defined difference.

## Guidance

Make the server output and first client render equal by default. Initialize from values the server
knows rather than reading browser-only state during render. Choose when client-only values appear:

- If the value is decoration, initialize state from the server-known value and read the browser
  value in an effect after mount. The first render stays consistent; accept that the displayed value
  changes after hydration.
- If the value is knowingly different but visually irrelevant — a rendered timestamp, a per-instance
  id — keep the divergence and mark only that element with `suppressHydrationWarning`. It silences
  the warning for that element's text and attributes; React still patches nothing, so use it only
  where the two contents are both acceptable, never to hide structural mismatch (different element
  trees, missing children).
- If presentation must be correct before first paint, such as a theme class, use the framework or
  theme library's pre-hydration setup. A script may set that class before hydration, with
  `suppressHydrationWarning` narrowly applied to the affected attribute container. Suppression is
  not a repair mechanism: the server and client must still render the same React output. This does
  not establish authentication or authorize access to protected content.

Investigate each hydration warning before choosing suppression. React identifies the difference; a
mismatch in one leaf may come from browser-only code running during render elsewhere. Apply
suppression only after reviewing that specific, known difference, not as a general setting.

## Anti-pattern

A page renders `lastSaved.toLocaleTimeString()` during SSR and hydration. A developer responds by
adding `suppressHydrationWarning` to every element near a date, without identifying each difference.
One instance is added to a `<ul>` whose children differ between server and client. Suppression does
not fix that structural bug or cover the children's mismatches, so the attempted fix leaves the
underlying client-only list problem unresolved.

## Why

Hydration reuses the server-rendered DOM and expects the client's first render to match it.
Differences can cause warnings, recovery work, and visible changes. Suppression does not make the
two outputs equal or repair the known mismatch. Use it only for an isolated element whose server and
client contents are both acceptable; otherwise eliminate the difference or use the appropriate
pre-hydration setup.

## Exceptions and boundaries

- Streaming SSR shifts where the mismatch appears but not the rule: what a boundary's children
  render must match between server and client.
- `suppressHydrationWarning` is one level deep — it does not suppress warnings for that element's
  children, which is why it is safe only on leaves.
- Client-only subtrees that should never render on the server are a loading-boundary decision (see
  `react.async.suspense-boundary-scope`), not a suppression decision.
- This Practice does not cover error-decoded hydration repair APIs or framework nonce/CSP
  interactions with pre-hydration scripts.

## Example

A draft editor displays the last saved time, but server and browser timezones produce different
strings. `SavedAt` first shows the same neutral text on both sides, then formats the time after
mount. `SavedAtExact` instead permits a known mismatch on one text element, only when either
timezone's displayed time is acceptable.

```tsx
function SavedAt({ isoTimestamp }: { isoTimestamp: string }) {
  const [mounted, setMounted] = useState(false);
  useEffect(() => setMounted(true), []);

  return (
    <span>
      {mounted
        ? `Saved at ${new Date(isoTimestamp).toLocaleTimeString()}`
        : "Saved"}
    </span>
  );
}

function SavedAtExact({ isoTimestamp }: { isoTimestamp: string }) {
  return (
    <span suppressHydrationWarning>
      {new Date(isoTimestamp).toLocaleTimeString()}
    </span>
  );
}
```

`SavedAt` renders "Saved" on both sides first, then displays the browser-formatted time after
hydration. `SavedAtExact` leaves the known text difference on one element rather than asking React
to repair it. Neither uses suppression for a different element tree or missing children; unrelated
hydration mismatches must still be investigated.
