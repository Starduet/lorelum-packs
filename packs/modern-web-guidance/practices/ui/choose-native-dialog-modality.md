---
anti_patterns:
  - description: A blocking confirmation is implemented as a positioned div with a hand-written focus trap and Escape listener, while background controls remain interactive.
    id: modern-web-guidance.ui.custom-modal-overlay
    name: Custom modal overlay without native modality
    severity: warn
applies_when: implementing a dialog that either blocks interaction with the page or remains open while the page is usable
id: modern-web-guidance.ui.choose-native-dialog-modality
severity: warn
stage: implementation
tech_stack:
  - html
  - javascript
title: Choose Native Dialog Modality and Dismissal
---

Use a named `<dialog>` opened with `showModal()` for a blocking confirmation or form. The browser puts it in the top layer, makes the rest of the document inert, manages focus and handles Escape. Provide an explicit close or cancel control; focus the safe action in a destructive confirmation. Do not recreate the focus trap or open a modal with the `open` attribute or `show()`.

```html
<button type="button" id="delete">Delete</button>
<dialog id="confirm" aria-labelledby="title">
  <h2 id="title">Delete this item?</h2>
  <form method="dialog">
    <button value="cancel" autofocus>Cancel</button>
    <button value="delete">Delete</button>
  </form>
</dialog>
<script>
  const dialog = document.querySelector('#confirm');
  document.querySelector('#delete').addEventListener('click', () => dialog.showModal());
  dialog.addEventListener('close', () => {
    const choice = dialog.returnValue;
    dialog.returnValue = '';
    if (choice === 'delete') console.log('Confirmed');
  });
</script>
```

Reset `returnValue` after each close so a later Escape cannot reuse a previous answer. A non-modal inspector can use `dialog.show()` or, where supported, `<dialog popover>`; include a visible close button and do not make the page inert. Menus and tooltips are not dialogs and need their own semantics.

`closedby` and declarative invoker commands have narrower support than the native modal. If unsaved changes must be protected, handle the `cancel` event rather than relying on `closedby="none"` alone; explain a prevented close and offer a safe way to discard or continue. Treat click-outside dismissal and backdrop scroll containment as enhancements, not guarantees in every browser. Check the project's browser targets before using invoker commands or popovers; provide a working script or appropriate polyfill where they are required.

Source: [Dialog, v1.0.0, commit 4dd9683](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-components/dialog.md).
