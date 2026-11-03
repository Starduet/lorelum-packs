---
anti_patterns:
  - description: Deferred chunks are preloaded indiscriminately on mount, or not at all, so preload traffic competes with the current page or the deferred code is always paid as a wait at click time.
    id: react.bundle.preload-without-intent-signal
    name: Preloading without an intent signal
    severity: warn
applies_when: code or data has been deferred into a separate chunk, and a decision is needed about whether and when to fetch it ahead of the request that uses it
id: react.bundle.preload-on-intent
severity: warn
stage: implementation
tech_stack:
  - react
  - next
title: Preload Deferred Code When User Intent Signals It
---

## When to apply

If users open a dynamically imported feature through a button, tab, or predictable wizard step,
their actions may give you time to load its code before they need it. Choose which actions justify
starting that download before the click.

## Guidance

Use how clearly an action points to the feature, and the cost of a wrong guess, to choose a signal.
An explicit step toward it — a key press, completing the previous wizard stage, or a feature flag
known to enable it — is strongest. Hover and focus (`onMouseEnter`, `onFocus`) offer a small,
inexpensive head start. Preloading unconditionally on mount is the weakest signal and usually wrong.
Preload only the few chunks the current interface leads to, not the whole catalog:

```tsx
const preloadCheckout = () => {
  void import("./checkout-flow");
};

export function CheckoutEntry() {
  return (
    <button
      onMouseEnter={preloadCheckout}
      onFocus={preloadCheckout}
      onClick={() => void import("./checkout-flow").then((m) => m.openCheckout())}
    >
      Go to checkout
    </button>
  );
}
```

Repeated `import()` calls for the same module reuse its loading and module cache. The click handler
can call `import()` again to use the in-flight or already loaded module; it does not need a shared
state variable to track the preload.

Know what the framework already does. Next.js prefetches linked routes (production `<Link>`
prefetches on viewport entry), so intent-based preloading earns its keep mainly for dynamically
imported chunks and non-link targets — exactly the code the defer decision split off. Preloading is
bandwidth spent in advance: wrong guesses compete with the current page's own bytes, so treat the
preload list as a small, measured decision, not a default.

## Anti-pattern

A dashboard mounts and immediately preloads every panel's chunk — twelve heavy modules — because one
of them might be opened. On metered and mobile connections the preloads strangle the dashboard's own
data fetching; the panels most users open are no faster than without preloading.

## Why

Deferral avoids downloading a feature for visitors who never use it. Preloading on intent starts
that download before the click, reducing the remaining wait if the user proceeds. Preloading on
every mount instead spends bandwidth even when the user shows no interest in the feature.

## Exceptions and boundaries

- If the deferred feature is one tap from every session and small enough to be instant anyway, skip
  preloading; this is a cost boundary.
- Do not preload to compensate for deferring critical-path code; fix the deferral decision instead.
- Preloading code is not prefetching data: cached module code still fetches its own data on use, and
  data prefetching has its own staleness and privacy considerations outside this Practice.
- On the server, preload is meaningless — the guard question is execution, not inclusion; see
  `react.bundle.defer-heavy-loads`.

## Example

A checkout wizard renders each stage from its own deferred chunk and preloads the next stage's chunk
as soon as the user lands on the current one — an explicit step, the strongest signal. The two heavy
stages are deferred; `AddressForm` is a small local component that stays in the main bundle, because
splitting it would cost more than it saves.

```tsx
"use client";

import { useEffect } from "react";
import dynamic from "next/dynamic";

const ReviewStage = dynamic(() => import("./review-stage"));
const PaymentStage = dynamic(() => import("./payment-stage"));

export function CheckoutWizard({ stage }: { stage: "address" | "review" | "payment" }) {
  useEffect(() => {
    if (stage === "address") void import("./review-stage");
    if (stage === "review") void import("./payment-stage");
  }, [stage]);

  if (stage === "address") return <AddressForm />;
  if (stage === "review") return <ReviewStage />;
  return <PaymentStage />;
}
```

While the user fills the address form, the review chunk is already loading. If it finishes before
the next stage, that stage need not wait for the download. Only one next-stage chunk is preloaded
per step, based on the user's current stage.
