---
anti_patterns:
  - description: A sortable list changes CSS order during a pointer drag but offers no keyboard operation and leaves reading order unchanged.
    id: modern-web-guidance.ui.pointer-only-visual-reordering
    name: Pointer-only visual reordering
    severity: warn
applies_when: adding user-controlled reordering to a single-axis list or row of items
id: modern-web-guidance.ui.accessible-list-reordering
severity: warn
stage: implementation
tech_stack:
  - javascript
  - accessibility
title: Reorder Real List Items with Keyboard Alternatives
---

Reorder the existing DOM children, not just CSS `order`, so visual, keyboard, and reading order agree. Supply discoverable move buttons or an actions menu as a keyboard and single-pointer alternative to dragging. Name controls with the item and direction, disable invalid boundary moves, retain focus on an appropriate control, keep the moved item visible, and announce its new position in a polite live region. Arrow-key or grab–move–drop interactions can supplement controls but must not interfere with screen-reader navigation.

For pointer dragging, use a dedicated handle when items contain controls or selectable text. Restrict `touch-action: none` to the handle, capture the initiating pointer, ignore other pointers, handle cancellation and release, and show the proposed position without shifting the whole list on each move. Commit the DOM move on drop; do not clone items. Respect reduced motion for movement animations. A user must be able to move an item without performing a drag gesture.

Where supported, `container.moveBefore(item, reference)` preserves more state during a move. Feature-detect it; otherwise move the existing node with `reference.before(item)` or `container.append(item)` and restore focus because reinsertion can blur descendants. If moving during an active drag, account for lost pointer capture. A static list is an acceptable no-script fallback only when reordering is supplementary, not when order itself is essential data. This guidance covers a single axis, not grid sorting or moving between lists.

Source: [Rearrange Items with Drag and Drop, v1.0.0, commit 4dd9683](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-behaviors/drag-and-drop.md).
