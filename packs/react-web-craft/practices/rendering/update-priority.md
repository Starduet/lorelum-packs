---
anti_patterns:
  - description: An input's keystroke triggers a synchronous expensive filter or render, so the control the user is typing into stutters even though the expensive result could lag behind without harm.
    id: react.rendering.urgent-input-blocked-by-heavy-render
    name: Urgent input blocked by heavy follow-up render
    severity: warn
applies_when: one interaction produces both an urgent visual update and an expensive derived render or data follow-up, and their priorities are being chosen
id: react.rendering.update-priority
severity: warn
stage: implementation
tech_stack:
  - react
title: Split Urgent Input Updates from Slow Follow-Up Renders
---

## When to apply

Typing, dragging a slider, or selecting a tab may also trigger work that cannot finish within one
frame. Keep the control's visible update immediate, and decide which follow-up content can safely
lag behind.

## Guidance

Choose based on whether you are deferring a derived value or scheduling a state update:

- The lag is in rendering a derived view of an input value (filtering a large list, re-rendering an
  expensive chart): defer the value. The control keeps its own immediate state, and the deferred
  value trails it while React keeps the input responsive:

  ```tsx
  const [query, setQuery] = useState("");
  const deferredQuery = useDeferredValue(query);
  const results = useMemo(
    () => filterEntries(corpus, deferredQuery),
    [corpus, deferredQuery],
  );
  const isStale = query !== deferredQuery;
  ```

- The lag is in a state update the user does not need synchronously (switching a tab whose content
  is heavy, navigating): wrap the update in `startTransition`, or use `useTransition` when the UI
  should show that the follow-up is in flight.

Show when the result is stale or pending, for example by dimming old results or adding a pending
indicator to the tab. This tells users that the control has updated but the content has not caught
up. A transition does not make high-frequency updates cheap and is not a scroll throttle.
`useDeferredValue` is not a network debounce and does not cancel a fetch. Transition `isPending`
tracks the transition's lifecycle; async follow-ups still need their own error and race handling.

## Anti-pattern

A pricing page's range slider writes its value to state, and every change re-filters and re-renders
a grid of two hundred cards synchronously. Dragging the slider drops frames on the thumb itself —
the one element that must track the pointer — even though the grid could happily lag a few frames
behind.

## Why

Concurrent rendering lets React interrupt lower-priority rendering, but the code must identify which
updates can wait. Keeping the control's update urgent lets React prioritize it over the derived
view. A stale or pending indicator explains why that view still shows older content.

## Exceptions and boundaries

- If the derived render is cheap enough to finish within the frame budget, adding deferral is
  ceremony; measure before reaching for it.
- If the expensive work is a network request rather than render cost, the split is about request
  lifecycle and caching, not render priority.
- If the follow-up changes what the user is looking at (not a lagging mirror but a navigation),
  decide with transitions at the navigation boundary; hidden-content timing is the
  `react.async.suspense-boundary-scope` decision.

## Example

A pricing page's range slider filters a grid of two hundred cards. The slider writes its own urgent
state; the grid reads a deferred value and dims while it trails.

```tsx
function PriceExplorer({ products }: { products: Product[] }) {
  const [maxPrice, setMaxPrice] = useState(500);
  const deferredMaxPrice = useDeferredValue(maxPrice);

  const visible = useMemo(
    () => products.filter((product) => product.price <= deferredMaxPrice),
    [products, deferredMaxPrice],
  );
  const isStale = maxPrice !== deferredMaxPrice;

  return (
    <>
      <input
        type="range"
        min={50}
        max={500}
        value={maxPrice}
        onChange={(event) => setMaxPrice(Number(event.currentTarget.value))}
      />
      <div style={{ opacity: isStale ? 0.6 : 1 }}>
        <ProductGrid products={visible} />
      </div>
    </>
  );
}
```

The slider's value updates urgently, while the grid uses the deferred value. React can prioritize
the control over the lower-priority render. Dimming the old results shows that the grid has not
caught up yet, rather than leaving users to guess whether the interaction was ignored.
