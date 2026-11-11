---
anti_patterns:
  - description: A page uses clickable divs for ordinary disclosures or changes a tab's CSS class without updating the selected state, visible panel and keyboard entry point.
    id: modern-web-guidance.ui.disclosure-state-drift
    name: Hidden content and controls out of sync
    severity: warn
applies_when: presenting related page content in expandable sections or switching among panels without leaving the page
id: modern-web-guidance.ui.choose-on-page-content-controls
severity: warn
stage: design
tech_stack:
  - html
  - javascript
  - accessibility
title: Choose and Synchronize On-Page Content Controls
---

Choose the interaction from the task. A FAQ or “read more” section normally needs independent disclosures: use `<details>` and `<summary>`, without custom arrow-key handling. Let multiple sections stay open so readers can compare them. A shared `name` makes a group exclusive where that constraint is genuinely needed, but check browser support and provide a fallback if exclusivity is essential. If each item must be a navigable heading, instead place a button in a heading and synchronize its `aria-expanded` with the panel's visibility; headings inside `summary` are not consistently exposed by screen readers.

Use a tab widget when users switch between alternative panels on the **same page**; use links for navigation between pages. Give the tablist an accessible name, use button tabs and named `tabpanel` elements associated with their tabs. Render the initial state in HTML: one selected tab and one visible panel. Keep selected state, visible panel, keyboard entry point and visible indicator synchronized. Arrow keys move through tabs; selection following focus works when panels are instant and have no costly side effects. Require activation instead if selection is slow, changes history, starts media or otherwise has a noticeable cost. Make the selected state recognizable without color alone, including in forced colors. Prefer a scrollable single row to wrapped tabs.

If collapsed content must be discoverable by browser find or fragment navigation, check that requirement when selecting the control. Native `<details>` is a useful default for disclosures. For a custom panel, `hidden="until-found"` and `beforematch` can expose matches, but the control state must be synchronized and support varies. If findability is essential on unsupported browsers, provide a searchable, visible presentation rather than pretending ordinary `display: none` content is discoverable. Verify keyboard and assistive-technology behavior in target browsers.

Sources: [Accordion](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-components/accordion.md), [Tabbed interfaces](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-components/tabs.md), and [Search hidden content](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-behaviors/search-hidden-content.md), upstream commit `4dd9683`.
