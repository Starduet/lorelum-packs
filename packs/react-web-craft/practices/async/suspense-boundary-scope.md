---
anti_patterns:
  - description: A page component awaits its slowest data source before returning any JSX, so header, navigation, and fast sections cannot render or stream until it resolves.
    id: react.async.shell-blocked-by-slowest-subtree
    name: Whole shell awaits one slow data source
    severity: warn
applies_when: a server component tree waits on one slow data source even though only one subtree's output depends on it
id: react.async.suspense-boundary-scope
severity: warn
stage: design
tech_stack:
  - react
  - next
title: Put Slow Subtrees Behind Their Own Suspense Boundaries
---

## When to apply

If one server component needs data that is much slower than the rest of the page's, avoid making
unrelated content wait for it. Find the subtree that uses that data and place its Suspense boundary
there.

## Guidance

An async component cannot return its JSX until its await completes. If the page awaits a slow
request before returning, even unrelated parts of the shell must wait. Move the slow fetch into the
child that needs it and wrap that child in `<Suspense>`. The shell can render — and, with a
streaming setup such as the Next.js App Router, stream to the client — while the child shows its
fallback until the data arrives.

A boundary around the whole page makes even fast content wait behind one fallback. Give each slow
subtree its own boundary so it can replace its fallback when ready, while fast, critical content
stays in the initial response. Usually, fast, layout-critical, or SEO-relevant content should stay
outside those boundaries; wrap only the genuinely slow subtrees.

Not awaiting in the parent is also what starts sibling fetches concurrently — the component
structure is the parallelism mechanism; there is no need for a parent-level `Promise.all` over
children the parent does not consume. When several consumers need the same data, start the promise
once and read it with React 19's `use()` inside each consumer under one boundary, so the request
happens once and they fall back together.

Consider how the page will feel to use, not just its profiling results. Showing the shell sooner
means some content arrives later through a fallback, which can shift the layout. Make that trade-off
deliberately for each part of the interface rather than adding boundaries by default.

## Anti-pattern

A product page awaits the reviews feed before returning any JSX. The title, price, and navigation
depend on none of it, yet they all wait for the slowest source; the browser shows nothing until
reviews resolve.

## Why

When only the slow child sits behind Suspense, its data request no longer prevents the shell from
rendering. Each separately wrapped subtree can replace its fallback when its own data arrives.
Keeping fast content outside those boundaries preserves it in the initial response, which matters
for perceived speed and for crawlers.

## Exceptions and boundaries

- Layout-critical data — content whose size or position determines the surrounding structure —
  belongs in the shell; hiding it behind a fallback causes reflow.
- SEO-critical above-the-fold content should remain in the initial response rather than arrive
  through a fallback.
- For cheap queries, fallback churn can cost more than the wait would; a boundary is a cost
  boundary, not a default wrapper.
- If a slow subtree must also start before the page renders (prefetching during navigation), that is
  a framework navigation decision this Practice does not cover.
- This Practice decides where timing is isolated in the component tree. Single-function sequencing
  is `react.async.parallel-independent-work` and `react.async.await-after-cheap-work`.

## Example

A product page keeps the fast catalog read in the shell — it is above the fold and SEO-relevant —
and isolates the two slow panes behind their own boundaries. The declared helpers stand in for the
data layer.

```tsx
import { Suspense } from "react";

type ProductSummary = { name: string; price: string };

declare function getProductSummary(id: string): Promise<ProductSummary>;
declare function getProductReviews(id: string): Promise<{ items: string[] }>;
declare function getCompatibilityChecks(id: string): Promise<{ rows: string[] }>;

async function ProductHead({ id }: { id: string }) {
  const product = await getProductSummary(id);
  return (
    <header>
      <h1>{product.name}</h1>
      <p>{product.price}</p>
    </header>
  );
}

async function ReviewsPane({ id }: { id: string }) {
  const reviews = await getProductReviews(id);
  return (
    <section>
      {reviews.items.map((item) => (
        <p key={item}>{item}</p>
      ))}
    </section>
  );
}

async function CompatibilityPane({ id }: { id: string }) {
  const checks = await getCompatibilityChecks(id);
  return (
    <aside>
      {checks.rows.map((row) => (
        <p key={row}>{row}</p>
      ))}
    </aside>
  );
}

export function ProductPage({ id }: { id: string }) {
  return (
    <main>
      <ProductHead id={id} />
      <Suspense fallback={<p>Loading reviews…</p>}>
        <ReviewsPane id={id} />
      </Suspense>
      <Suspense fallback={<p>Checking compatibility…</p>}>
        <CompatibilityPane id={id} />
      </Suspense>
    </main>
  );
}
```

`ProductPage` itself never awaits, so the head data ships in the initial response while each pane
resolves behind its own fallback. The two panes' fetches also start concurrently, because no parent
awaits them before rendering.
