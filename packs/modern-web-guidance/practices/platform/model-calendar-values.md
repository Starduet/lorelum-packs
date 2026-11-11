---
id: modern-web-guidance.platform.model-calendar-values
title: Model Calendar Values Without Accidental Time Zones
stage: implementation
severity: warn
applies_when: designing storage or calculations for dates, times, recurring calendar values, or timestamped events
tech_stack:
  - javascript
  - web
anti_patterns:
  - id: modern-web-guidance.platform.calendar-value-as-instant
    name: Treating a calendar value as an instant
    severity: warn
    description: A date without a time zone is stored as a timestamp and later shifts when displayed in another zone.
---

Decide what the value means before selecting its representation. A birthday is a calendar date, a card expiry is a year and month, and a daily alarm can be a floating wall-clock time; none is inherently an instant. Preserve that meaning in storage rather than inventing a midnight timestamp that may display as the previous day in another time zone.

Use calendar-aware values such as `Temporal.PlainDate`, `PlainYearMonth`, or `PlainTime` for those examples. For a recorded event use an instant; for an appointment tied to a place use a date and time with a named IANA zone and an explicit policy for ambiguous or nonexistent local times. Define month-end behavior for recurrence: adding a month to January 31 constrains by default in Temporal, while `overflow: 'reject'` throws.

When Temporal is unavailable in supported runtimes, load a vetted polyfill before dependent code or use another calendar-aware representation; importing a polyfill does not necessarily install a global. Convert a plain value to an instant only when the application has chosen the time, zone and ambiguity policy. Check round trips across zones and month boundaries.

Source: [Capturing Location-Agnostic Data and Partial Dates with Temporal](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/js/capture-location-agnostic-data.md), v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`.
