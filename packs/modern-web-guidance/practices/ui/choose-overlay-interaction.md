---
anti_patterns:
  - description: A blocking confirmation is built as a positioned div with a hand-written focus trap while background controls remain interactive, or ordinary navigation links are given menu roles without menu keyboard behavior.
    id: modern-web-guidance.ui.overlay-semantics-mismatch
    name: Overlay semantics that do not match the interaction
    severity: warn
applies_when: choosing and implementing a popup for a confirmation, an inspector, a list of actions or links, or contextual help
id: modern-web-guidance.ui.choose-overlay-interaction
severity: warn
stage: design
tech_stack:
  - html
  - javascript
  - accessibility
title: Choose an Overlay by Its Interaction
---

Start with what the user needs to do, not the word “popup” or a positioning API:

- **Interrupt and block the page**, such as a delete confirmation: use a named `<dialog>` and `showModal()`. The browser places it in the top layer, makes the rest of the document inert, contains focus, handles Escape and returns focus on close. Include a visible cancel or close control and initially focus the safe action for destructive choices. Do not replace native modality with `show()`, the `open` attribute, a custom focus trap or redundant ARIA.
- **Keep working in the page**, such as a find panel: use a named non-modal `<dialog>` with a visible close button. Use `show()` when it need not be in the top layer, or `<dialog popover>` where supported when popover dismissal is wanted. Do not make the page inert.
- **Choose a command or destination**: a short dropdown traversed with Tab is ordinary navigation, not an ARIA menu. Use a button for an action and an `<a href>` for a destination. Use menu semantics only for a composite widget: name the trigger and menu, expose the expanded state, move keyboard focus into the menu on keyboard opening, support arrows and Home/End, allow Tab to leave, and close on Escape with focus returned to the trigger. Nested menus close one level at a time; a submenu trigger should not also run a separate command.
- **Explain a control**: associate descriptive tooltip text with its trigger and make it accessible without a mouse. A tooltip is not a dialog; keep it from obscuring focused controls and dismiss or reposition it when no longer relevant.

For example, a delete dialog can use `<form method="dialog">` with Cancel and Delete buttons. Read `dialog.returnValue` on `close` and reset it to `''` so a subsequent Escape cannot reuse the previous answer. If closing could discard edits, intercept `cancel`, explain why closing was prevented, and provide a safe discard or continue path; do not rely on `closedby="none"` alone in browsers that lack it.

Popover, invoker commands, anchor positioning and `focusgroup` have independent browser support. Where required behavior is unsupported, use a working script or conditionally loaded polyfill; a popup still needs usable positioning, dismissal and keyboard access. In particular, a menu without `focusgroup` needs explicit menu roles and keyboard focus management. Treat animation as an enhancement, not a prerequisite for reading or operating the overlay.

Sources: [Dialog](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-components/dialog.md), [Popup menu](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-components/menu.md), and [Position aware tooltips](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-atoms/position-aware-tooltips.md), upstream commit `4dd9683`.
