---
anti_patterns:
  - description: A component exposes one `renderX` callback prop per slot, so callers compose structure through unfamiliar callback signatures while the component could have accepted children and slot elements directly.
    id: react.composition.render-props-for-static-slots
    name: Render props for static slots
    severity: warn
applies_when: a component's composition API is being designed and a choice is needed between children/slot elements and render-function props
id: react.composition.children-over-render-props
severity: warn
stage: design
tech_stack:
  - react
title: Compose with Children; Reserve Render Props for Data-Bound Slots
---

## When to apply

When callers fill a frame, card, toolbar, or dialog with content, they can often pass the elements
directly. Use this distinction to design its slots: does the caller already have what it needs to
render them, or must the component supply data first?

## Guidance

Accept headers, actions, and sections as `children` or named slot props containing elements when the
caller can write them directly at the call site. There is no need to wrap those elements in
functions for the component to call:

```tsx
<Card>
  <Card.Header title="Billing" />
  <PlanSummary plan={plan} />
  <Card.Footer>
    <Button onClick={openPortal}>Manage subscription</Button>
  </Card.Footer>
</Card>
```

Use a render function when the component must supply data for the caller to render the slot: each
row of a table, each item of a virtualized list, or measured dimensions. The callback receives that
data as an argument:

```tsx
<DataTable rows={invoices} renderRow={(invoice) => <InvoiceRow key={invoice.id} invoice={invoice} />} />
```

For each prop, ask whether the caller needs data from inside the component to render the slot. If
not, accept an element. A `renderHeader?: () => ReactNode` that receives no internal data requires
the caller to wrap an element in a function without gaining anything. Name data-receiving callbacks
`render*` and include the data in their parameters; use element props for the other slots.

## Anti-pattern

A toolbar component declares `renderLeft`, `renderRight`, and `renderOverflow` — all zero-argument.
Callers study the component's signature to compose plain buttons, each usage wraps static elements
in arrows, and none of the three slots can ever receive toolbar state, because the component never
passes any.

## Why

Children are declarative, tree-shaped, and already familiar; render functions add a call layer that
pays for itself only when the component supplies data per invocation. Keeping element props and
render props distinct also makes the component's contract self-describing: element props say "bring
structure", render props say "I will call you with my data".

## Exceptions and boundaries

- Zero-argument render props are occasionally justified for lazy mounting (deferring a heavy subtree
  until the slot renders); the deferral motive should be stated, and suspense boundaries usually
  express it better.
- Compound-component APIs (`<Toolbar.Left />`) are the shared-context evolution of slot elements;
  they add machinery that single-use slots do not need.
- Data-bound slots need key discipline and stable callbacks like any list rendering; this Practice
  covers the API shape, not list rendering semantics.
- Wrapping children to inject context is provider design, not a render prop; see
  `react.state.share-one-owner` for the ownership decision underneath.

## Example

A page header accepts its actions and filter input as elements, since neither needs data from inside
the header. `Button` and `FilterInput` stand in for real components.

```tsx
function PageHeader({ title, actions, children }: {
  title: string;
  actions?: React.ReactNode;
  children?: React.ReactNode;
}) {
  return (
    <header className="page-header">
      <h1>{title}</h1>
      {children}
      <div className="page-header-actions">{actions}</div>
    </header>
  );
}

<PageHeader
  title="Invoices"
  actions={<Button onClick={newInvoice}>New invoice</Button>}
>
  <FilterInput value={filter} onChange={setFilter} />
</PageHeader>
```

`actions` and `children` are elements: the caller composes real buttons and inputs with no callback
layer. A render prop would earn its place here only if the header had to hand the caller something
internal — say, which actions overflowed into a menu — and then the signature would say so:
`renderOverflow?: (items: Action[]) => ReactNode`, data as a parameter, not a zero-argument thunk.
