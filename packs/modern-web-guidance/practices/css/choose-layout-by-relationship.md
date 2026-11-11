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

Use flex for a content-driven row or column, grid for coordinated rows and columns, and subgrid when nested items must share parent tracks. Use flexible tracks and `gap`, not fixed card widths; use `auto-fit` to stretch occupied tracks or `auto-fill` to retain empty tracks. Allow flex items to wrap, and set `min-inline-size: 0` on an item that must shrink around long content; also make the text wrap or provide intentional scrolling.

Keep interactive elements in reading and keyboard order in the DOM. Avoid `order`, reverse flex directions, or dense grid packing when they would change their visual sequence. Use logical spacing and sizing when the direction should follow writing mode, but keep physical directions for intentionally fixed graphics.

## Exceptions and boundaries

Subgrid can align card internals across shared tracks; provide explicit tracks first if older target browsers need a fallback. A toolbar may intentionally scroll instead of wrapping, but its controls must remain reachable. Do not clip overflow to hide a sizing problem. Check narrow layouts, long unbreakable text, keyboard order, and text resizing.

## Example

```css
.toolbar { display: flex; flex-wrap: wrap; gap: 1rem; }
.toolbar__label { min-inline-size: 0; overflow-wrap: anywhere; }
.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr)); gap: 1rem; }
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [css-layout.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/css-layout.md)
