---
anti_patterns:
  - description: A site navigation dropdown receives menu roles without arrow-key navigation, making ordinary links behave like a composite widget only to assistive technology.
    id: modern-web-guidance.ui.menu-roles-on-navigation
    name: Menu semantics on ordinary navigation
    severity: warn
applies_when: choosing semantics and keyboard interaction for a popup list of commands or navigation links
id: modern-web-guidance.ui.choose-popup-menu-interaction
severity: warn
stage: design
tech_stack:
  - html
  - accessibility
  - javascript
title: Choose Menu Semantics from the Interaction Model
---

A popup is a menu when it behaves as a composite widget: one tab stop, arrow-key movement among items, and Escape to close and restore focus. Use a button for an action and an anchor with `href` for a destination, even inside a menu. A short dropdown of ordinary links traversed with Tab is navigation instead: keep links and normal navigation semantics, without menu or menuitem roles.

For a real menu, name the trigger and menu, expose the trigger's expanded state, enter the menu on keyboard opening, support arrow navigation and Home/End, and let Tab leave rather than trapping focus. Close nested menus one level at a time and return focus to the appropriate trigger. Maintain the same interaction when opened by keyboard or pointer; pointer activation need not move focus into the menu. Do not make one submenu trigger also execute an unrelated action.

Popover, invoker commands, CSS anchor positioning and `focusgroup` can reduce implementation work, but are separately supported features. The pinned upstream reports `focusgroup` as limited; conditionally polyfill it or supply explicit roles and roving-focus handling in unsupported browsers. Popover and anchor-positioning fallbacks must preserve opening, dismissal, keyboard access and usable positioning, not merely the appearance. Test the complete interaction against target browsers and assistive technologies.

Source: [Popup menu, v1.0.0, commit 4dd9683](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-components/menu.md).
