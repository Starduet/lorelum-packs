---
id: modern-web-guidance.css.reserve-space-for-media
title: Reserve Media Space Before Loading
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: laying out images or video whose dimensions are known
anti_patterns:
  - id: modern-web-guidance.css.reserve-space-for-media.counterexample
    name: Reserve Media Space Before Loading counterexample
    description: An unsized image loaded after surrounding text moves the page when its dimensions become known.
    severity: warn
---

## When to apply

Apply when laying out images or video whose dimensions are known.

## Guidance

Declare intrinsic image dimensions in HTML when available, or reserve the intended frame with CSS `aspect-ratio`; make the media responsive within that frame.

## Anti-pattern

An unsized image loaded after surrounding text moves the page when its dimensions become known.

## Why

An early aspect ratio lets the browser allocate space before the media is decoded, reducing layout shift.

## Exceptions and boundaries

Use the correct source or crop ratio and avoid forcing an inaccurate ratio onto arbitrary content. Supply an appropriate fallback or explicit dimensions for browsers outside the feature target.

## Example

```html
<img src="photo.jpg" width="1200" height="800" alt="A mountain lake">
```
```css
img { max-inline-size: 100%; block-size: auto; }
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [responsive-design.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/responsive-design.md)
- [css-layout.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/css-layout.md)
