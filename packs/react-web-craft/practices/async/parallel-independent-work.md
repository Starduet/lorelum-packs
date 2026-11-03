---
anti_patterns:
  - description: An async server function awaits unrelated I/O operations one after another, so its latency is the sum of all requests even though no result depends on an earlier one.
    id: react.async.sequential-independent-fetches
    name: Independent requests awaited in sequence
    severity: warn
applies_when: an async function performs several I/O operations whose results do not depend on one another, and a decision is needed about starting them together or in sequence
id: react.async.parallel-independent-work
severity: warn
stage: implementation
tech_stack:
  - react
title: Start Independent Async Work Together
---

## When to apply

When an async function makes several requests or performs other I/O, check what each operation needs
as input. If it does not need another operation's result, it can start without waiting for that
operation to finish.

## Guidance

Start independent operations together with `Promise.all`. An operation that needs another
operation's result as input must wait for that result. The returned results stay in call order, not
completion order.

`Promise.all` is all-or-nothing: it rejects as soon as one input rejects, and the batch's other
results are dropped. When the caller can make use of partial results, use `Promise.allSettled` and
inspect each status instead.

A dependency does not force serializing unrelated work. Create a dependent operation's promise from
its input's promise as soon as the input is started, and include the chained promise in the same
final `Promise.all`:

```ts
const customerPromise = getCustomer(customerId);
const paymentMethodsPromise = customerPromise.then((customer) =>
  getPaymentMethods(customer.id),
);

const [customer, taxRegion, template, paymentMethods] = await Promise.all([
  customerPromise,
  getTaxRegion(request.countryCode),
  getDefaultInvoiceTemplate(),
  paymentMethodsPromise,
]);
```

The payment-methods request waits only for the customer; the tax-region and template requests run
while that dependent pair completes.

For per-item work over a long list, cap the number of requests running at once instead of starting
every request together. `Promise.all` overlaps waiting on I/O; it does not parallelize CPU work, and
requests that share one connection pool or single-threaded resource may serialize anyway. Expect a
benefit for independent network requests, not an equal speedup for every kind of work.

## Anti-pattern

In an invoice builder where all four requests already have their inputs, the code still awaits
customer, tax region, template, and payment methods one by one. None needs an earlier result in this
version. Serial execution adds four round trips instead of waiting for the slowest independent
request. If payment methods need the customer result, that pair must instead stay chained as above.

## Why

An `await` before an unrelated request delays that request's start. Starting independent requests
together lets them wait on I/O at the same time. Start a dependent request as soon as its own input
resolves, rather than waiting for unrelated results too.

## Exceptions and boundaries

- If every operation genuinely feeds the next, the sequence is the dependency graph; this Practice
  does not ask to parallelize true dependents.
- `Promise.all`'s fail-fast behavior is usually correct for building one response; choose
  `Promise.allSettled` only when the caller has defined behavior for partial results.
- Third-party rate limits or per-request cost can make deliberate sequencing cheaper than maximal
  concurrency; cap or sequence explicitly when a quota exists.
- This Practice stays at the single-function level. Restructuring a component tree so slow data does
  not block the page shell is the `react.async.suspense-boundary-scope` decision, and per-item
  follow-up chaining over a list is `react.async.chain-nested-item-fetches`.

## Example

An invoice assembly service needs the customer, the tax region for the request, and the default
template independently; payment methods depend on the customer. The payment-methods request starts
as soon as the customer resolves, without waiting for the tax region or template. The declared
helpers stand in for the data layer.

```ts
type Customer = { id: string; name: string };
type TaxRegion = { code: string; rate: number };
type InvoiceTemplate = { id: string; headerHtml: string };
type PaymentMethod = { id: string; label: string };

declare function getCustomer(id: string): Promise<Customer>;
declare function getTaxRegion(countryCode: string): Promise<TaxRegion>;
declare function getDefaultInvoiceTemplate(): Promise<InvoiceTemplate>;
declare function getPaymentMethods(customerId: string): Promise<PaymentMethod[]>;

export async function buildInvoiceSummary(customerId: string, countryCode: string) {
  const customerPromise = getCustomer(customerId);
  const paymentMethodsPromise = customerPromise.then((customer) =>
    getPaymentMethods(customer.id),
  );

  const [customer, taxRegion, template, paymentMethods] = await Promise.all([
    customerPromise,
    getTaxRegion(countryCode),
    getDefaultInvoiceTemplate(),
    paymentMethodsPromise,
  ]);

  return { customer, taxRegion, template, paymentMethods };
}
```

Elapsed time is now the longest dependency chain —
`max(customer + paymentMethods, taxRegion, template)` — instead of the sum of four request times. If
a partial invoice were still renderable when one request fails, the final await would become
`Promise.allSettled` over the same four promises.
