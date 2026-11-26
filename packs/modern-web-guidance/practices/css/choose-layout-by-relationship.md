---
id: modern-web-guidance.css.choose-layout-by-relationship
title: Build a Responsive Layout Around Content Relationships
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: building a page, toolbar, or card collection that must reflow with content and screen size
anti_patterns:
  - id: modern-web-guidance.css.choose-layout-by-relationship.counterexample
    name: Rigid or visually reordered layout
    description: Fixed card widths and visual reordering make narrow layouts overflow or keyboard order diverge from the visible sequence.
    severity: warn
---

## Guidance

Choose the layout **for each container**, not for the whole page. Inspect which dimensions must align and whether the number of items is known:

- Use flex for a single row or column whose items determine their own space, such as a toolbar. Set `flex-wrap: wrap` when controls can fit on another line; use `gap` for spacing. For a flex item containing a long URL or label, `min-inline-size: 0` permits shrinking, but the text still needs wrapping or an intentional scroll region. In a row, an auto inline-start margin can push one item to the far end; `justify-self` does not position an individual flex item.
- Use grid when rows and columns must be coordinated. For a known page structure, define tracks or named areas; for an unknown number of cards, use `repeat(auto-fit, minmax(..., 1fr))`. `auto-fit` collapses empty repeated tracks so occupied tracks can stretch; `auto-fill` retains them. The minimum comes from `minmax()`, not from the cards. Give the grid available inline space rather than relying on an intrinsically sized `inline-grid` or unsized flex item.
- Use subgrid when a nested grid must inherit parent tracks, such as aligning card titles and actions across siblings. The cards must span the parent tracks they share. If child counts vary, subgrid only the shared axis and allow implicit tracks on the other; ordinary grid is sufficient if cross-card alignment is not required.
- For continuous prose flowing into columns, consider multi-column layout rather than grid.

Keep controls in reading and keyboard order in the DOM. `order`, reverse flex directions and dense grid packing change visual order without changing sequential focus order; do not use them to reorder interactive content. Use logical sizing and spacing when they should follow writing mode, but retain physical directions for graphics that should not flip.

## Example

The toolbar wraps independently of the card grid. The illustrative `15rem` track minimum is capped at the available width, so it can still fit a narrower container; choose a minimum for the actual content.

```css
.toolbar { display: flex; flex-wrap: wrap; gap: 1rem; }
.toolbar__label { min-inline-size: 0; overflow-wrap: anywhere; }
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr));
  gap: 1rem;
}
```

For subgrid, a parent with two shared row tracks can use `.card { grid-row: span 2; display: grid; grid-template-rows: auto 1fr; grid-template-rows: subgrid; }`. The explicit rows are a fallback, not cross-card alignment in browsers without subgrid.

## Exceptions and validation

A toolbar may intentionally scroll instead of wrapping if every control remains reachable. Do not clip overflow to disguise an undersized layout. In the actual embedding context, check the supported range of widths, including a container narrower than the card's preferred minimum if that can occur; use representative long content and enlarged text. Verify no unintended horizontal overflow or lost content, and tab through controls to confirm focus follows the visible sequence. If target browsers need a subgrid fallback, check that it preserves any essential alignment.

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [css-layout.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/css-layout.md)
