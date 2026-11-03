---
anti_patterns:
  - description: A server render writes per-request or per-user data into a module-level variable, so concurrent requests can overwrite or read each other's values.
    id: react.server.module-state-per-request
    name: Request data kept in module scope
    severity: warn
applies_when: server-rendered code needs to share request-scoped data across components or helpers, and the sharing mechanism is being chosen
id: react.server.no-module-request-state
severity: warn
stage: implementation
tech_stack:
  - react
  - next
title: Keep Request Data Out of Module Scope
---

## When to apply

When several parts of one request need the current user, request ID, or locale, keep that data
separate from other requests. This applies to server components, SSR'd client components, route
handlers, and server actions; choose a place to store the value that preserves that separation.

## Guidance

Treat module scope on the server as process-wide shared memory. Concurrent renders run in the same
process, so a module-level variable written by request A is read by request B, and the last writer
wins: races, cross-request contamination, and one user's data appearing in another's response all
follow from that.

Pass request data through the render tree instead — as arguments and props from the entry point, or
through a request-scoped memo when several components need the same lookup:

```tsx
export default async function OrderPage({ orderId }: { orderId: string }) {
  const user = await getCurrentUser(token);
  const order = await getOrder(orderId);
  return <OrderSummary user={user} order={order} />;
}
```

Reserve module scope for immutable configuration read once, constants, and caches deliberately
designed for cross-request reuse with correct keys and size bounds. For any request context, ask
whether two concurrent requests could need different values. If so, one shared variable cannot hold
it safely. Use framework request objects or request-scoped storage rather than hand-rolled globals.

## Anti-pattern

A dashboard page assigns the authenticated user to a module-level `currentUser` and a nested
component reads it. Two overlapping requests interleave: request B overwrites `currentUser` between
request A's assignment and A's render of the nested component, and A's page shows B's account name.

## Why

Concurrent requests can share the same module instance. If one request replaces a module-level value
before another request reads it, the second request can render the wrong user's data. Keeping each
request's values separate prevents that interleaving from changing its response.

## Exceptions and boundaries

- Immutable static configuration and code constants are safe at module scope; they cannot differ
  between requests.
- An intentionally shared cache is safe only with keys that include every axis the data varies on
  (user, tenant, locale) plus eviction and size bounds; designing one is its own decision, and
  per-request sharing needs no such machinery.
- This Practice concerns mutable request-scoped data; module-level singletons that hold no
  per-request state, such as a database client, are a different pattern with different constraints.
- Within-request duplication of a lookup is a performance decision handled by
  `react.server.request-dedup-cache`; this Practice governs where the result may live.

## Example

An order page resolves its request-scoped values at the entry point and passes them down. Every
concurrent request renders against its own values.

```tsx
import { getCurrentUser } from "./session";

export default async function OrderPage({
  orderId,
  token,
}: {
  orderId: string;
  token: string | null;
}) {
  const user = await getCurrentUser(token);
  const order = await getOrder(orderId, user);
  return (
    <section>
      <OrderTitle order={order} />
      <OrderItems order={order} />
      <SupportContact user={user} />
    </section>
  );
}
```

`user` and `order` exist only inside this request's render tree; the only module-level objects
involved are the imported functions and read-only configuration. Two overlapping requests for
different orders cannot observe each other's data, because there is no shared variable to observe.
