---
id: modern-web-guidance.css.choose-clip-or-scroll-for-overflow
title: Keep Overflowing Content Reachable
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: long text or other content is clipped or overflows a small panel or constrained box, or a visual effect needs clipping
anti_patterns:
  - id: modern-web-guidance.css.choose-clip-or-scroll-for-overflow.counterexample
    name: Hide overflow without deciding how content is accessed
    description: Clipping a box to hide a layout defect can make content or controls unreachable.
    severity: warn
---

## Guidance

First identify the overflowing element and axis in the actual layout. Check for fixed dimensions, a non-wrapping flex row, a flex item held at its intrinsic minimum, or a long unbreakable string. Let items wrap, allow the relevant item to shrink with `min-inline-size: 0`, and wrap text where appropriate. Shrinking the box alone does not make its contents wrap. Do not hide the symptom with clipping.

When a bounded region genuinely needs to retain more content than fits, use `overflow: auto` and a real size constraint; content must remain reachable. A nested scroll region may need a focusable, named region so keyboard users can discover and scroll it, particularly when it contains no focusable descendants. Use `scrollbar-gutter: stable` if reserving space for a classic scrollbar prevents disruptive layout shifts. Add `overscroll-behavior: contain` only when stopping scroll handoff to the parent is intentional; otherwise leave normal chaining intact.

When the excess is purely decorative, `overflow: clip` cuts it off without creating a scroll container. Unlike `hidden`, `clip` also prevents programmatic scrolling and does not establish a formatting context by itself. If the existing layout relies on either behavior, provide it separately or choose another design. Keep interactive content and focus outlines outside the clipping boundary.

## Examples

For a constrained results region, the focusable named region exposes keyboard access even when its contents are plain text:

```html
<section class="results" tabindex="0" aria-label="Search results">
  <p>Results content…</p>
</section>
```

```css
.results { max-block-size: 25rem; overflow: auto; scrollbar-gutter: stable; }
```

For decorative spill only, choose the fallback based on whether strict clipping or preserving the visual effect matters more:

```css
.decoration { overflow: hidden; overflow: clip; }
@supports (overflow-clip-margin: 1rem) {
  .decoration { overflow-clip-margin: 1rem; }
}
```

Here `hidden` preserves the boundary in older browsers but creates a scroll container and may cut off shadows. Use `visible` as the fallback instead if preserving the effect matters more than clipping. `overflow-clip-margin` can allow a shadow to bleed beyond the clipping edge without changing layout size; it requires `clip`, has more limited support, and must not be relied on to keep essential content accessible.

## Validation

Test the actual region with enough content to overflow, then with little content. At narrow widths and enlarged text, verify no accidental page-level horizontal overflow; scroll to both ends with pointer and keyboard and confirm all content and focus indicators remain visible. Check sticky elements and any scripted scrolling after changing `hidden` to `clip`. If a needed item or focus indicator is cut off, or the fallback changes required scrolling behavior, change the layout or fallback rather than accepting the clip.

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [css-layout.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/css-layout.md)
- [overflow-clipping-control.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/overflow-clipping-control.md)
