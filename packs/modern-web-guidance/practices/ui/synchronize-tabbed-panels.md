---
anti_patterns:
  - description: Tabs render all panels until JavaScript starts, then change only CSS classes while keyboard focus and selected state drift apart.
    id: modern-web-guidance.ui.tabs-state-drift
    name: Unsynchronized tab selection and panels
    severity: warn
applies_when: implementing a tabbed widget that switches between panels on the same page rather than navigating to different pages
id: modern-web-guidance.ui.synchronize-tabbed-panels
severity: warn
stage: implementation
tech_stack:
  - html
  - javascript
  - accessibility
title: Keep Tab Focus Selection and Panels Synchronized
---

Use a named tablist, native button tabs, and named `tabpanel` elements associated with their tabs. Render the initial selected state in HTML: one tab has `aria-selected="true"`, and all other panels are hidden. Keep the selected tab, visible panel, keyboard entry point, and visible selection indicator in sync for every selection path. Indicate selection with a shape such as an underline as well as color, including in forced colors.

Arrow keys move through the tablist. Automatic selection on focus suits instantly available panels without side effects; require activation when changing panels loads data slowly, changes history, starts media, or otherwise has a noticeable cost. On narrow screens prefer a horizontally scrollable single row over wrapping, retaining access to every tab. Use links, not a tab widget, for navigation between pages.

The upstream uses `focusgroup="tablist nomemory"` and moves `focusgroupstart` with selection. Its pinned compatibility data lists support as limited to Chromium-based browsers; feature-detect and conditionally load a compatible focusgroup polyfill, or implement the ARIA tablist keyboard and focus pattern explicitly. Do not add a second competing focus system. `hidden="until-found"` allows browser search in supporting engines; synchronize selection on `beforematch`. Where unsupported it behaves as ordinary hidden content, so provide a separate searchable presentation if findability is required. Keep panel padding and borders on a child wrapper because until-found panels can retain their own box.

Source: [Tabbed interfaces, v1.0.0, commit 4dd9683](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-components/tabs.md).
