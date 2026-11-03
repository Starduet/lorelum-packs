---
anti_patterns:
  - description: Several components in one server render each perform the same authentication or database lookup, multiplying latency and backend load although one lookup would serve the whole request.
    id: react.server.duplicate-request-lookups
    name: Request-scoped lookups repeated within a render
    severity: warn
applies_when: one server render calls the same request-scoped async work, such as session or record lookup, from more than one component or helper
id: react.server.request-dedup-cache
severity: warn
stage: implementation
tech_stack:
  - react
  - next
title: Deduplicate Request-Scoped Lookups with React cache
---

## When to apply

A layout, page, and sidebar may each look up the same authenticated user during one server render.
When several components or helpers independently fetch the same request-scoped user, tenant setting,
or record, share that lookup within the request.

## Guidance

Wrap the lookup in React's `cache()`. Within one server request, calls to the same cached function
with matching arguments share one execution and result. The cached results are not reused by the
next request:

```ts
import { cache } from "react";

export const getCurrentUser = cache(async (token: string | null) => {
  if (!token) return null;
  return loadUserByToken(token);
});
```

`cache()` compares each argument with `Object.is`. Matching primitive values reuse the result; fresh
object literals do not, even if their contents match. Pass primitive keys, or reuse one stable
reference across calls when an object argument is unavoidable.

Do not reach for `cache()` where the framework already deduplicates: in Next.js, identical `fetch`
calls in one request are memoized automatically, so `cache()` earns its keep on non-fetch work —
database and ORM queries, authentication checks, file reads, expensive pure computation. And do not
expect it to share anything across requests: deduplication across requests, users, or instances is a
different decision with invalidation and isolation consequences that `cache()` deliberately does not
make.

## Anti-pattern

A layout fetches the session user, the page fetches it again for the heading, and a sidebar
component fetches it a third time for the avatar. One page render issues three identical database
queries; under load, that multiplies backend work by component count.

## Why

Several components can need the same user or record during one server render. Without request-scoped
memoization, each component repeats the lookup. `cache()` reuses matching lookups within that
request without sharing their results with another request or user.

## Exceptions and boundaries

- If the lookup already runs exactly once per request, `cache()` cannot remove any duplicate work.
- Arguments that cannot be expressed as primitives or stable references defeat the cache; reshape
  the signature rather than passing fresh object literals.
- Matching calls reuse the cached result for the request's lifetime. Use this for data the request
  treats as constant, not for a value that must be fetched again immediately after a mutation.
- Module-level or cross-request caching is a separate decision with its own invalidation, tenancy,
  and memory design; see `react.server.no-module-request-state` for the isolation boundary that
  motivates keeping per-request data out of module scope.

## Example

Two independent server components on one account page each need the authenticated user. Both call
the same `cache()`-wrapped lookup; within the request it loads once. The declared helpers stand in
for the data layer.

```tsx
import { getCurrentUser } from "./session";

export async function AccountHeader({ token }: { token: string | null }) {
  const user = await getCurrentUser(token);
  return <header>{user?.name}</header>;
}

export async function BillingNotice({ token }: { token: string | null }) {
  const user = await getCurrentUser(token);
  return user?.plan === "trial" ? <p>Trial ends soon.</p> : null;
}
```

One render of a page composing both components issues one `loadUserByToken` call, no matter how many
components need the user. A second request — even the same user reloading — runs the lookup again,
because nothing survives the request.
