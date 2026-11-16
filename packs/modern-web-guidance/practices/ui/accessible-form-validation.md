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

## Decide who owns validation

Inspect the actual form before adding handlers: which controls are required, which have persistent hints, which checks need a server response, and whether native interactive validation is enabled? Native validation prevents `submit` from firing when constraints fail; an `invalid` listener must use capture because that event does not bubble. Do not put the only error-rendering path in a `submit` listener and expect it to run for a blank required field. If choosing `novalidate`, the application instead owns checking every relevant control, blocking submission, rendering errors and routing focus; do not assume the browser will do those steps.

For an email field, the baseline markup can be:

```html
<label for="email">Email (required)</label>
<p id="email-hint">For example, you@example.com.</p>
<input id="email" name="email" type="email" autocomplete="email" required
       aria-describedby="email-hint" aria-invalid="false">
<p id="email-error" hidden></p>
```

For an application-rendered error, populate `email-error` with a specific message, unhide it, set `aria-invalid="true"` and set `aria-describedby="email-hint email-error"`. On resolution, hide and clear the error, restore `aria-describedby="email-hint"` and set `aria-invalid="false"`. This is a state contract, not a complete validation handler: if the application renders native, custom or server errors, synchronize their presentation while retaining their distinct causes. Native `type="email"` checks syntax, not whether the address exists or is accepted.

## Timing and recovery

- **Choose when to show an error.** Avoid marking an untouched required field invalid on page load or announcing an incomplete value on every keystroke. Validate on submit, and optionally after an edited field is left or a control's change is committed; clear a displayed error as soon as it is resolved. `:user-invalid` can supply native interaction-aware visual timing; where the browser policy requires a fallback, track interaction and submit attempts in script. A submit attempt must also identify invalid untouched required fields; native interactive validation may surface them one at a time.
- **Make the error discoverable at its field.** Show specific text explaining the problem and, when known, how to fix it; do not rely on color alone. Set `aria-invalid="true"` when an error is presented, and associate its text using `aria-describedby` while preserving existing hint IDs. Remove the error reference and update invalid state when that error is resolved; hidden text referenced by `aria-describedby` can still be announced. `:user-invalid` alone does not synchronize ARIA. The upstream guidance initializes `aria-invalid="false"` to avoid premature invalid announcements in some browser/screen-reader combinations; verify the behavior in the combinations the application supports.
- **Notify without competing for attention.** If an error appears after blur or change, ensure the user is notified; one option is to update an already-present polite live region with the field name and error. Avoid a separate live region for every message and repeated announcements while typing. On a failed submit, use focus instead of announcing every field: native constraint validation normally focuses the first invalid control. If custom validation or `novalidate` takes over, focus the first invalid control, or for a long form focus an error summary with links to the relevant fields. Ensure the target and associated messages are present before moving focus. Test keyboard and screen-reader behavior, including duplicate or interrupted announcements.
- **Keep server errors distinct from client validity.** A syntactically valid email can still be rejected by the server. Map a field-specific rejection to that field's visible message, invalid state and description, then apply the same focus or summary approach after the response. Do not clear a server error just because native constraints pass; clear or recheck it when the relevant value changes or the server confirms resolution. Handle a submission-wide failure separately with an actionable form-level message, preserving entered data where appropriate; a network failure is not evidence that a particular field is invalid. Avoid exposing sensitive account or server details in error text.

Keep visual state, descriptions and announcements synchronized on input, change, invalid submission and reset. If custom validity is used, clear a stale `setCustomValidity()` message when its condition no longer applies. Check the browser and assistive-technology combinations used by the application rather than assuming a CSS selector or live region alone makes errors accessible.

For a concrete server response, associate “Enter an email address in the format you@example.com” with a malformed email; an availability rejection can instead say the address cannot be used, without revealing whether an account exists. When a request is in flight, a second submission may be temporarily prevented, but restore the submit control after a recoverable failure. If the user edits while a request is pending, do not attach a response for the old value to the new value: compare against the submitted value or discard obsolete responses. Reset also clears pending announcements and error state after the form's values reset.

## Verify the interaction

For forms with required fields, Tab through untouched fields and check for premature error presentation or invalid announcements. Submit invalid values and confirm the chosen validation path makes errors understandable and directs focus to the first invalid field or a linked summary; native validation may present errors one at a time, while custom validation must expose the errors it handles. Correct an error and confirm any hint remains associated while the resolved error disappears. If errors appear on blur or change, check for one understandable notification rather than repeated or competing speech. Where the server can reject individual fields, exercise that response; where submission can fail at form level, check its recovery separately. If the form offers reset, check that it clears applicable error state. Use keyboard and the supported screen reader/browser combinations; stop and fix any stale error, lost data, unreachable focus, or unannounced failure.

Sources: [Forms](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/forms/forms.md), [Validate input after interaction](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/forms/validate-input-after-interaction.md), [Required field feedback](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/forms/required-field-feedback.md), and [Accessible error announcement](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/accessibility/accessible-error-announcement.md), upstream commit `4dd9683`.
