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

For a native disclosure, the browser owns `open` and the summary's keyboard behavior. A custom heading-based disclosure instead needs one update path for both button activation and any programmatic reveal: set the panel's hidden state and `aria-expanded` together, and never leave focus inside a panel that is being hidden. If an “Expand all” control is offered, derive its state from the items after individual toggles too; in a mixed state its action should expand all. Do not add a landmark for every small section.

When a tab widget suits switching between alternative panels on the **same page**, give the tablist an accessible name, use button tabs and named `tabpanel` elements associated with their tabs; other on-page content need not be turned into tabs. Use links for navigation between pages. Render the initial state in HTML: one selected tab and one visible panel. Keep selected state, visible panel, keyboard entry point and visible indicator synchronized. Arrow keys move through tabs; selection following focus works when panels are instant and have no costly side effects. Require activation instead if selection is slow, changes history, starts media or otherwise has a noticeable cost. Make the selected state recognizable without color alone, including in forced colors. Prefer a scrollable single row to wrapped tabs.

### Tab state and keyboard contract

For a scripted fallback without `focusgroup`, give the container `role="tablist"`, each button `role="tab"`, and each panel `role="tabpanel"` with `aria-labelledby` pointing to its tab. In HTML, set the selected tab's `aria-selected="true"` and `tabindex="0"`; set other tabs to `aria-selected="false"` and `tabindex="-1"`, and hide their panels. Make a visible panel focusable with `tabindex="0"` when it has no focusable content. A single selection function should update all tabs, all panels and the roving entry point together; derive the visual underline from `aria-selected`.

For a horizontal tablist, Left and Right move focus among tabs, wrapping at the ends; Home and End can move to the first and last. Do not consume Up/Down, which users need to scroll. With automatic activation, each arrow movement also selects its tab; with manual activation, arrows move focus only and Enter or Space selects. Tab enters on the selected tab and then moves on to the active panel or its first focusable content. If a selection changes without focus, such as browser find, update the roving entry point as well. `focusgroup` can provide the arrow navigation where supported, but its support and polyfill behavior need checking; do not combine it with a second competing roving-tabindex implementation.

For example, in manual activation a user can arrow across three expensive report panels without fetching any; pressing Enter on the third selects it, hides the old panel and makes the third the entry point on the next visit. Keep the previously selected tab as the entry point while focus is only exploring other tabs.

If collapsed content must be discoverable by browser find or fragment navigation, check that requirement when selecting the control. Native `<details>` is a useful default for disclosures. For a custom panel, `hidden="until-found"` and `beforematch` can expose matches, but control state must be synchronized and support varies. Do not apply `display: none`, `contents`, or `inline` to that panel: these prevent reveal. Unlike ordinary hidden content, it can still generate a box; move padding, border, and background to a child and prevent hidden panels or parent gaps from consuming space, for example by placing tab panels in the same grid cell. If findability is essential on unsupported browsers, provide a searchable, visible presentation. Verify keyboard and assistive-technology behavior in target browsers.

## Verify the chosen pattern

For disclosures, use Tab and Enter/Space to open and close each section, confirm independent sections stay open when intended, and test shared-name exclusivity in the oldest supported browser if relied upon. For tabs, check one selected tab and one visible panel at load, arrow wrapping, manual or automatic activation as chosen, Tab exit and re-entry, and selection indication in forced colors. Where find or fragment reveal is supported by the chosen pattern, search for a unique word in hidden content and follow a fragment: the reveal must select or expand the correct control and hide any mutually exclusive panel. If findability is required, test the fallback in unsupported target browsers; do not silently make the content unsearchable. Check that zoom and narrow screens leave the controls reachable and the focus indicator visible.

Sources: [Accordion](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-components/accordion.md), [Tabbed interfaces](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-components/tabs.md), and [Search hidden content](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-behaviors/search-hidden-content.md), upstream commit `4dd9683`.
