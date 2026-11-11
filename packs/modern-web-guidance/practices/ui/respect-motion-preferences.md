---
anti_patterns:
  - description: A global near-zero animation duration is used as the reduced-motion strategy, leaving essential state changes dependent on animation events or content hidden when motion is disabled.
    id: modern-web-guidance.ui.motion-disabled-state-loss
    name: Motion preference breaks the underlying interaction
    severity: warn
applies_when: adding or changing interface motion, including transitions, scrolling effects, loading indicators, and automatically moving content
id: modern-web-guidance.ui.respect-motion-preferences
severity: warn
stage: implementation
tech_stack:
  - css
  - javascript
  - accessibility
title: Respect Reduced Motion Preferences
---

Separate the task from its animation. For decorative spatial movement, zoom, rotation, parallax, or animated reveals, default to the complete static state and add motion only inside `@media (prefers-reduced-motion: no-preference)`. A static reveal must still show its content and focus and selection indicators. Keep useful non-spatial feedback such as link and button color transitions; reduced motion does not mean removing every visual state change.

Where motion conveys ongoing activity, retain the information rather than blindly removing the indicator: use a visible static loading label or indicator, or a gentler animation when appropriate. If an animation should remain but be adjusted, declare it normally and override its parameters under `@media (prefers-reduced-motion: reduce)`. Choose a suitable alternative case by case; slowing or shortening motion is not automatically comfortable. Do not globally force `animation-duration: 0.01ms`, which can make effects more jarring. Consider a static default with an explicit motion opt-in.

The preference is not a substitute for controls. Automatically moving, blinking, or scrolling content that starts automatically, lasts more than five seconds, and appears alongside other content needs a keyboard-operable pause, stop, or hide control unless the movement is essential. If its button alternates labels between “Pause” and “Play”, do not also use `aria-pressed`. Avoid rapid flashing regardless of preference; do not use a `no-preference` query as permission to exceed flash limits.

Apply reduced-motion handling to CSS transitions, keyframe and scroll-driven animations, view transitions, and motion started by JavaScript. For a view transition, disable or replace the snapshot animations under `reduce` while still updating the DOM and moving focus to the new context when necessary. A transition is an enhancement: never make navigation, removal, focus, or final state depend solely on `animationend` or `transitionend`, since neither fires when the effect does not run. Complete the state change immediately if there is no relevant animation; handle cancellation as well as normal completion when waiting for one.

Test both preference settings, including changing the operating-system setting while the page is open. CSS media queries update with the preference; JavaScript-driven motion should use `matchMedia('(prefers-reduced-motion: reduce)')`, check its current `matches` value, and respond to its `change` event where motion can continue or start later. Check that content, loading status, keyboard focus, navigation, and close/remove behavior remain usable with motion absent, and that persistent motion can still be paused. Test on target browsers and devices: a preference communicates a request to reduce motion, not a guarantee that every animation is safe or that the user's needs are identical.

Sources: [Motion](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-behaviors/motion.md) and [Same Document Transitions](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-behaviors/same-document-transitions.md), upstream commit `4dd9683`.
