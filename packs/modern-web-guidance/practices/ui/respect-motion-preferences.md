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

Separate the task from its animation. For decorative spatial movement, zoom, rotation, parallax, or animated reveals, choose a reduced-motion alternative appropriate to the effect; when removing motion, default to the complete static state and add motion inside `@media (prefers-reduced-motion: no-preference)`. A static reveal must still show its content and focus and selection indicators. Keep useful non-spatial feedback such as link and button color transitions; reduced motion does not mean removing every visual state change.

First identify what each effect communicates and where it runs: CSS, scripted animation, smooth scrolling, or a view transition. If it only decorates a state change, the complete static state is the fallback. If it communicates progress, preserve a visible status; if it moves continuously, also provide the applicable user control. Inspect the actual state update and focus flow rather than changing a global duration.

For example, a loading message remains readable when the decorative spinner is not moving:

```html
<p role="status"><span class="spinner" aria-hidden="true">◌</span> Loading results…</p>
```

```css
@keyframes spin { to { transform: rotate(1turn); } }
@media (prefers-reduced-motion: no-preference) {
  .spinner { display: inline-block; animation: spin 1s linear infinite; }
}
```

The application must replace the status with success or an actionable failure when the request finishes. The spinner is not the status itself, and this example does not make a long-running task cancellable.

Where motion conveys ongoing activity, retain the information rather than blindly removing the indicator: use a visible static loading label or indicator, or a gentler animation when appropriate. If an animation should remain but be adjusted, declare it normally and override its parameters under `@media (prefers-reduced-motion: reduce)`. Choose a suitable alternative case by case; slowing or shortening motion is not automatically comfortable. Do not globally force `animation-duration: 0.01ms`, which can make effects more jarring. Consider a static default with an explicit motion opt-in.

The preference is not a substitute for controls. Automatically moving, blinking, or scrolling content that starts automatically, lasts more than five seconds, and appears alongside other content needs a keyboard-operable pause, stop, or hide control unless the movement is essential. If its button alternates labels between “Pause” and “Play”, do not also use `aria-pressed`. Avoid rapid flashing regardless of preference; do not use a `no-preference` query as permission to exceed flash limits.

Apply reduced-motion handling to CSS transitions, keyframe and scroll-driven animations, view transitions, and motion started by JavaScript. For a view transition, disable or replace the snapshot animations under `reduce` while still updating the DOM and moving focus to the new context when necessary. A transition is an enhancement: never make navigation, removal, focus, or final state depend solely on `animationend` or `transitionend`, since neither fires when the effect does not run. Complete the state change immediately if there is no relevant animation; handle cancellation as well as normal completion when waiting for one.

For a same-document navigation using a view transition, apply the DOM update and focus the new context when appropriate whether or not `document.startViewTransition` exists. If using shared transition names, they must be unique in each captured state; clean up temporary names after the transition. With reduced motion, disable snapshot animations, not the DOM update:

```css
@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(*),
  ::view-transition-old(*),
  ::view-transition-new(*) { animation: none; }
}
```

When an exit effect needs to delay removal, scope the wait to that effect, not every animation on the page: a looping spinner must not hold the removal open. Handle both finish and cancellation and complete immediately if there is no relevant effect. If the preference changes during a scripted animation, stop or replace the effect and apply its intended end state; remove listeners when the component is disposed.

Test both preference settings and check that the affected content and interaction remain usable without motion. If scripted motion can continue or start later, use `matchMedia('(prefers-reduced-motion: reduce)')`, check its current `matches` value, and respond to its `change` event; test changing the operating-system setting while the page is open. CSS media queries update with the preference. Test on target browsers and devices: a preference communicates a request to reduce motion, not a guarantee that every animation is safe or that the user's needs are identical.

Where an open/close or navigation depends on an effect, exercise it with motion absent and, if it can be interrupted, while toggling the preference mid-effect. Verify the final state and focus without waiting indefinitely for an event. Where persistent motion requires a control, start and pause it using only the keyboard in both preference modes. For loading indicators, inspect their loading, failure and completion states. Stop if affected content remains invisible, focus is lost, an exit never completes, or automatic motion cannot be stopped where required.

Sources: [Motion](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-behaviors/motion.md) and [Same Document Transitions](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-behaviors/same-document-transitions.md), upstream commit `4dd9683`.
