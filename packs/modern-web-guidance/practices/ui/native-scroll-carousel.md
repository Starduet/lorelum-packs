---
anti_patterns:
  - description: A carousel replaces native scrolling with a scripted transform and cloned slides, while unlabeled controls and changing indexes make the content inaccessible.
    id: modern-web-guidance.ui.script-only-carousel
    name: Script-only carousel with duplicated slides
    severity: warn
applies_when: building a finite carousel of related items with previous next or direct slide navigation
id: modern-web-guidance.ui.native-scroll-carousel
severity: warn
stage: implementation
tech_stack:
  - html
  - css
  - accessibility
title: Build Carousel Navigation on Native Scrolling
---

Make the track natively scrollable and use CSS scroll snap; keep its content usable even if script does not run. Provide named HTML buttons for previous, next, and direct slide selection. For a meaningful carousel section, name its region, use `aria-roledescription="carousel"`, and give each slide a localized position label and slide description. Keep the slides available to assistive technology. Show a visible focus indicator and never intercept keys used by controls inside a slide.

Wire controls to the actual scroll position, not an independent index that can drift when users swipe. Keep the current marker synchronized as scrolling happens, and announce a changed settled slide through a polite status region without announcing the initial load. Respect reduced motion for smooth scrolling. Use `scrollend` when available and a debounced scroll listener otherwise; do not run both settled handlers. When continuous looping is not required, finite navigation with disabled end buttons is a simpler valid choice.

The upstream looping approach requires additional parking, focus and scroll-compensation logic and support for `sibling-index()`; in unsupported browsers leave the list finite. Do not duplicate slide DOM as a shortcut because IDs and assistive-technology content would be duplicated. Scroll snap and smooth scrolling are separately supported, and effects must remain optional; check target browsers before depending on newer scroll events or effects.

Source: [Carousel, v1.0.0, commit 4dd9683](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-components/carousel.md).
