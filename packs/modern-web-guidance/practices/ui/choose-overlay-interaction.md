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

Check whether the background must be operable, whether the items are navigation or an arrow-key composite, and whether dismissal would lose work. Also check the target browsers for the individual features used; top-layer placement, anchoring and keyboard semantics are separate concerns.

- **Interrupt and block the page**, such as a delete confirmation: prefer a named `<dialog>` opened with `showModal()` when supported by the target browsers. The browser places it in the top layer, makes the rest of the document inert, contains focus, handles Escape and returns focus on close. Include a visible cancel or close control and initially focus the safe action for destructive choices. If a custom modal is necessary, provide equivalent modality, keyboard and focus behavior; `show()` or the `open` attribute alone does not make a dialog modal.
- **Keep working in the page**, such as a find panel: a named non-modal `<dialog>` is one option; include a visible close button. Use `show()` when it need not be in the top layer, or `<dialog popover>` where supported when popover dismissal is wanted. Do not make the page inert.
- **Choose a command or destination**: a short dropdown traversed with Tab is ordinary navigation, not an ARIA menu. Use a button for an action and an `<a href>` for a destination. Use menu semantics only for a composite widget: name the menu and, if present, its trigger; expose the trigger's expanded state, move keyboard focus into the menu on keyboard opening, support arrows and Home/End, allow Tab to leave, and close on Escape with focus returned to the trigger or, for a triggerless context menu, the prior focus target. Nested menus close one level at a time; a submenu trigger should not also run a separate command.
- **Explain a control**: associate descriptive tooltip text with its trigger and make it accessible without a mouse. A tooltip is not a dialog; keep it from obscuring focused controls and dismiss or reposition it when no longer relevant.

For example, a delete dialog can use `<form method="dialog">` with Cancel and Delete buttons. Read `dialog.returnValue` on `close` and reset it to `''` so a subsequent Escape cannot reuse the previous answer. If closing could discard edits, route Escape and every cancel or close control through the same confirmation logic. `requestClose()` requests a cancellable close and fires `cancel`; a `method="dialog"` submission or direct `close()` bypasses that guard. Where `requestClose()` or declarative `request-close` is unsupported, have the control invoke the same confirmation logic in script, then close only after the user allows discarding. Explain a prevented close and offer a safe discard or continue path; do not rely on `closedby="none"` alone.

### Modal confirmation pattern

This example only reports the user's choice; the caller must perform its own authorized deletion. It uses script rather than newer declarative invoker commands:

```html
<button id="ask" type="button">Delete item</button>
<dialog id="confirm" aria-labelledby="confirm-title">
  <h2 id="confirm-title">Delete this item?</h2>
  <form method="dialog">
    <button value="cancel" autofocus>Cancel</button>
    <button value="delete">Delete</button>
  </form>
</dialog>
<p id="result" role="status"></p>
<script>
  const dialog = document.getElementById('confirm');
  document.getElementById('ask').addEventListener('click', () => dialog.showModal());
  dialog.addEventListener('close', () => {
    const choice = dialog.returnValue;
    dialog.returnValue = '';
    document.getElementById('result').textContent =
      choice === 'delete' ? 'Deletion confirmed.' : 'Deletion cancelled.';
  });
</script>
```

If the design requires containing background scrolling, the following progressive enhancement can prevent scroll chaining within the modal and over its backdrop:

```css
dialog:modal { overscroll-behavior: contain; }
dialog::backdrop { overflow: hidden; overscroll-behavior: contain; }
```

Some target browsers do not contain scrolling on non-scrollable containers even though `CSS.supports()` accepts the property. In those browsers background scrolling may remain; `showModal()` still provides inertness and focus behavior. Do not claim the syntax check proves scroll containment, or hide root overflow without assessing layout shifts and sticky positioning.

The close event is not a cancellation guard; a dirty editor needs a `cancel` handler that prevents the close request while offering explicit Discard and Continue actions. Repeated Escape prevention alone is not a dependable guard without user activation. Reserve space for the explanation and place the destructive action so an ensuing pointer click cannot accidentally activate it. If the invoker has been removed or disabled on close, explicitly move focus to a logical surviving target; otherwise rely on native focus return.

### Menu and tooltip boundaries

For a composite menu with a trigger, synchronize `aria-expanded` from actual open/close events, including light dismiss and nested closure, not only the trigger's click. Keyboard opening enters the first item; Arrow Up/Down move among items, Home/End reach the ends, Enter or Space activates, and Tab leaves rather than trapping focus. For a submenu, Right enters it and Left or Escape closes that level and restores its trigger; a top-level Escape restores the original trigger, or the previous focus target for a triggerless context menu. Pointer opening need not move focus into an item. A plain link list instead uses normal Tab order and does not claim menu roles.

Tooltip content must be available on focus as well as hover, remain available when the pointer moves onto it, and be dismissible with Escape without moving focus. Keep interactive content out of a tooltip; use an appropriate popover or dialog for that. Do not let a tooltip cover the newly focused control.

Popover, invoker commands, anchor positioning and `focusgroup` have independent browser support. Where required behavior is unsupported, use a working script or conditionally loaded polyfill; a popup still needs usable positioning, dismissal and keyboard access. In particular, a menu without `focusgroup` needs explicit menu roles and keyboard focus management. Treat animation as an enhancement, not a prerequisite for reading or operating the overlay.

## Verify before shipping

For a modal, use keyboard only to check initial focus, Tab and Shift+Tab containment, Escape and focus return. If reusing a dialog's return value, reopen after confirming and press Escape to ensure the old choice is not reused. If scroll containment is required, test wheel and touch scrolling over the backdrop and at both dialog scroll boundaries in target browsers, and address unsupported behavior. For dirty content, try every close route, including repeated Escape and any backdrop dismissal; edits must not disappear without the explicit discard choice. For the chosen non-modal, menu or tooltip interaction, check background access and the applicable pointer, touch and keyboard behaviors above. At narrow widths and zoom, check that controls remain visible and focus is not obscured. Where enhancements are used, check their fallback in the target browsers; stop if a required action, close path or focus target is unavailable.

Sources: [Dialog](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-components/dialog.md), [Modal background scrolling](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-behaviors/prevent-page-scroll-under-modal-dialog.md), [Popup menu](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-components/menu.md), and [Position aware tooltips](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-atoms/position-aware-tooltips.md), upstream commit `4dd9683`.
