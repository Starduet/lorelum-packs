---
id: modern-web-guidance.platform.model-calendar-values
title: Model Calendar Values Without Accidental Time Zones
stage: implementation
severity: warn
applies_when: storing or calculating a birthday, wall-clock time, recurring month-day, or year-month that is not an instant
tech_stack:
  - javascript
  - web
anti_patterns:
  - id: modern-web-guidance.platform.calendar-value-as-instant
    name: Treating a calendar value as an instant
    severity: warn
    description: A date without a time zone is stored as a timestamp and later shifts when displayed in another zone.
---

Choose the narrowest Temporal plain type: `PlainDate` for a birthday, `PlainTime` for a floating wall-clock time, `PlainMonthDay` for an annual month/day and `PlainYearMonth` for an expiry month. These have no time-zone offset. Specify the calendar where needed, and define the desired overflow policy for calendar arithmetic: adding a month to January 31 constrains by default; `overflow: 'reject'` throws instead.

```js
const birthday = Temporal.PlainDate.from('1990-01-01');
const expiry = Temporal.PlainYearMonth.from('2027-12');
```

For an actual instant or an appointment tied to a location, use `Temporal.Instant` or `Temporal.ZonedDateTime` instead; converting a plain date to an instant requires an explicit time-zone and time-of-day policy. Store the original semantic value rather than a fabricated midnight timestamp. A named IANA zone captures changing civil-time rules, unlike a fixed offset.

Temporal had limited browser support in the source snapshot, with Safari unsupported. Detect it and load a vetted Temporal polyfill before initializing dependent code, or retain a calendar-aware representation that does not silently turn the value into an instant. The polyfill need not install a global automatically. Verify the project's runtime and polyfill versions rather than assuming support.

Source: [Capturing Location-Agnostic Data and Partial Dates with Temporal](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/js/capture-location-agnostic-data.md), v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`.
