---
anti_patterns:
  - description: A page statically imports large modules that only conditional or rare paths use, so every visitor downloads them before the first interaction whether or not they are ever opened.
    id: react.bundle.initial-bundle-carries-deferrable-code
    name: Deferrable code shipped in the initial bundle
    severity: warn
applies_when: a large module, component, or third-party library is needed only after the initial render or only on a conditional path, and the loading mechanism is being chosen
id: react.bundle.defer-heavy-loads
severity: warn
stage: implementation
tech_stack:
  - react
  - next
title: Defer Heavy Non-Critical Loads Until They Are Needed
---

## When to apply

An editor, charting library, map widget, export dialog, or analytics script may be large relative to
the page but unnecessary for its initial paint or first interaction. In that case, load it when the
user reaches the feature rather than including it in the initial load.

## Guidance

Deferring a module postpones both downloading and executing it. A static import adds it to the
initial dependency graph even if its feature never renders. A dynamic import puts it in a separate
chunk, fetched when first rendered or called:

```tsx
const ReportBuilder = dynamic(() => import("./report-builder"), {
  loading: () => <p>Loading report builder…</p>,
});
```

Use the framework's component loader for components (in Next.js, `next/dynamic`), plain `import()`
for data and non-component modules, and the framework's script-loading strategy for third-party
scripts — analytics and chat widgets are usually scripts, not React components, and their loading
strategy is separate from component code splitting. Be clear about what `ssr: false` changes: it
keeps a component out of the server render, so the delivered HTML will not contain it. In the App
Router, use that option from a client component. Omitting a widget from the HTML is usually
appropriate; omitting content usually is not.

Keep import paths statically analyzable. A bundler cannot split what it cannot see: prefer an
explicit map of loader functions over composing a path string, and prefer literal file-system paths
in server code, where over-broad paths also widen Next.js output file tracing:

```ts
const REPORT_LOADERS = {
  sales: () => import("./reports/sales"),
  usage: () => import("./reports/usage"),
} as const;

const loadReport = REPORT_LOADERS[reportKind];
```

Correct one common misconception while deferring: a runtime guard such as
`typeof window !== "undefined"` prevents a module from executing on the server; it does not remove
the module from the server bundle. Bundle membership is decided by static imports and loader flags,
not by runtime checks.

## Anti-pattern

A settings page statically imports a full charting library that only the admin-only usage dialog
renders. Every visitor — including the ninety-nine percent who never open the dialog — downloads and
parses the library before the page becomes interactive.

## Why

Code in the initial bundle must be downloaded and parsed even by visitors who never use its feature.
A dynamic import puts that code in a separate chunk, so conditional features can load it when they
render or call it. Explicit loader maps tell the bundler which modules can be loaded, rather than
requiring it to include a broader set of possible paths.

## Exceptions and boundaries

- Do not defer code on the critical rendering or first-interaction path; a deferred critical
  component trades one cost for a worse one.
- Small modules are not worth splitting: the extra chunk request can cost more than the bytes saved;
  this is a cost boundary, not a style rule.
- `typeof window` guards and `ssr: false` answer different questions (execution versus inclusion);
  this Practice does not replace the browser-API and SSR boundary decisions of the rendering
  category.
- Deciding when a deferred chunk should be fetched ahead of its click is the
  `react.bundle.preload-on-intent` decision; excluding barrel-file entry points from imports is
  deferred in this Pack pending build-output evidence.

## Example

A settings page renders a usage section only for admins. The charting library is in a separate
chunk, so non-admin visitors do not need it. In this example, an admin renders `UsageCharts` even
while `<details>` is closed; expanding the section is not what triggers the load.

```tsx
"use client";

import dynamic from "next/dynamic";

const UsageCharts = dynamic(() => import("./usage-charts"), {
  loading: () => <p>Loading charts…</p>,
});

export function SettingsPage({ isAdmin }: { isAdmin: boolean }) {
  return (
    <main>
      <h1>Settings</h1>
      <ProfileForm />
      {isAdmin && (
        <details>
          <summary>Usage</summary>
          <UsageCharts />
        </details>
      )}
    </main>
  );
}
```

The charting library ships in the `usage-charts` chunk, fetched when `UsageCharts` first renders —
for most visitors, never. If several report kinds competed for the same slot, they would hang off a
loader map like the one above, each entry a literal `() => import(...)` so the bundler can enumerate
the split points instead of over-including a directory.
