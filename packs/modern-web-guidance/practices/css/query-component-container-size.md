---
id: modern-web-guidance.css.query-component-container-size
title: Adapt a Reusable Component to Its Available Space
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: a reusable component needs different layouts in narrow and wide regions
anti_patterns:
  - id: modern-web-guidance.css.query-component-container-size.counterexample
    name: Tie a reusable component to viewport width
    description: A viewport breakpoint can make a narrow sidebar card use the layout intended for a wide main-content card.
    severity: warn
---

## Guidance

Use a container query when the same component can appear in differently sized regions of the same viewport. First inspect the embedding layout: identify an ancestor whose inline size is supplied by its parent and which actually wraps the component. Put `container-type: inline-size` on that ancestor, not on the element being styled: a size query selects a qualifying ancestor and cannot query the target itself. Name the container if intervening components may establish their own query containers.

Start with a usable stacked layout. Resize the actual slot with representative content and choose the threshold where a side-by-side layout has enough space, including for translated or enlarged text; the example's `30rem` is illustrative, not a device breakpoint. Use a media query for viewport-wide layout or user preferences instead.

## Example

The wrapper and card are distinct elements; the same card can be placed in a narrow sidebar or wide main region.

```html
<div class="card-slot">
  <article class="card">
    <div class="card__summary"><h2>Account</h2><p>Account details</p></div>
    <a href="/account">View account</a>
  </article>
</div>
```

```css
.card-slot { container: card / inline-size; }
.card { display: flex; flex-direction: column; gap: 1rem; }
.card__summary { min-inline-size: 0; overflow-wrap: anywhere; }
@container card (inline-size > 30rem) {
  .card { flex-direction: row; align-items: center; }
}
```

## Boundaries and validation

Inline-size containment changes intrinsic sizing: do not expect the wrapper's children to determine its intrinsic inline size. Ensure its parent gives it appropriate space, especially in a flex or intrinsically sized layout. `container-type: size` contains both axes; use it only if both are needed and the container has a suitable independent block size. `block-size` is not a valid container type. Container query units without an eligible ancestor fall back to small viewport units, so do not assume they always reflect the intended component.

If browsers in the project's support target lack size queries, choose a usable fallback for the component's actual placements: a stacked base may be enough, or a viewport-based fallback may work when the embedding layout makes viewport width a useful proxy for available space. It need not adapt to hypothetical placements, but must keep content and controls usable in supported ones. With the viewport held wide, compare the card in the narrow and wide slots where it is used, then resize across the chosen threshold. Check representative long or enlarged text for clipping. If the rule does not trigger, inspect the selected ancestor, its computed container name/type and its actual size before changing the breakpoint.

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [size-aware-styling.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/size-aware-styling.md)
- [css-layout.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/css-layout.md)
- [responsive-design.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/responsive-design.md)
