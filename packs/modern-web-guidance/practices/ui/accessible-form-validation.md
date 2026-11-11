---
anti_patterns:
  - description: A registration form marks untouched required fields invalid, shows only a red border, or displays a server rejection without associating it with the affected field or directing the user to it.
    id: modern-web-guidance.ui.inaccessible-form-errors
    name: Form errors that users cannot find or resolve
    severity: warn
applies_when: implementing validation and error recovery for a registration or other data submission form
id: modern-web-guidance.ui.accessible-form-validation
severity: warn
stage: implementation
tech_stack:
  - html
  - javascript
  - accessibility
title: Make Form Validation and Errors Accessible
---

Use a real form with labeled controls, visible required indicators and appropriate native constraints such as `required` and `type="email"`. Keep format requirements available before an error and associate hints with their fields. Let users submit to discover errors instead of disabling submit merely because the form is incomplete. Browser constraints improve feedback, but the server must independently validate submitted data.

- **Choose when to show an error.** Avoid marking an untouched required field invalid on page load or announcing an incomplete value on every keystroke. Validate on submit, and optionally after an edited field is left or a control's change is committed; clear a displayed error as soon as it is resolved. `:user-invalid` can supply native interaction-aware visual timing; where the browser policy requires a fallback, track interaction and submit attempts in script. A submit attempt must expose errors for untouched required fields too.
- **Make the error discoverable at its field.** Show specific text explaining the problem and, when known, how to fix it; do not rely on color alone. Set `aria-invalid="true"` when an error is presented, and associate its text using `aria-describedby` while preserving existing hint IDs. Remove the error reference and update invalid state when that error is resolved; hidden text referenced by `aria-describedby` can still be announced. `:user-invalid` alone does not synchronize ARIA. The upstream guidance initializes `aria-invalid="false"` to avoid premature invalid announcements in some browser/screen-reader combinations; verify the behavior in the combinations the application supports.
- **Notify without competing for attention.** For an error newly appearing after blur or change, update an already-present polite live region with the field name and error; avoid a separate live region for every message and repeated announcements while typing. On a failed submit, use focus instead of announcing every field: native constraint validation normally focuses the first invalid control. If custom validation or `novalidate` takes over, focus the first invalid control, or for a long form focus an error summary with links to the relevant fields. Ensure the target and associated messages are present before moving focus. Test keyboard and screen-reader behavior, including duplicate or interrupted announcements.
- **Keep server errors distinct from client validity.** A syntactically valid email can still be rejected by the server. Map a field-specific rejection to that field's visible message, invalid state and description, then apply the same focus or summary approach after the response. Do not clear a server error just because native constraints pass; clear or recheck it when the relevant value changes or the server confirms resolution. Handle a submission-wide failure separately with an actionable form-level message, preserving entered data where appropriate; a network failure is not evidence that a particular field is invalid. Avoid exposing sensitive account or server details in error text.

Keep visual state, descriptions and announcements synchronized on input, change, invalid submission and reset. If custom validity is used, clear a stale `setCustomValidity()` message when its condition no longer applies. Check the browser and assistive-technology combinations used by the application rather than assuming a CSS selector or live region alone makes errors accessible.

Sources: [Forms](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/forms/forms.md), [Validate input after interaction](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/forms/validate-input-after-interaction.md), [Required field feedback](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/forms/required-field-feedback.md), and [Accessible error announcement](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/accessibility/accessible-error-announcement.md), upstream commit `4dd9683`.
