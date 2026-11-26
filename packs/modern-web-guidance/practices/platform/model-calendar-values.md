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

Determine the business meaning before choosing storage or arithmetic. A birthday is a full calendar date; a card expiry is a year and month; an annual anniversary may be a month and day; an alarm at 09:00 wherever its owner is is a floating wall-clock time. A log entry is an instant. An appointment at a venue is a local date and time in that venue's named IANA zone. Ask whether a future event must remain at local wall time when zone rules change or instead remain at a previously fixed instant; those are different contracts.

Store plain values as validated ISO calendar strings or structured fields with their calendar, not as invented midnight timestamps. Store actual instants with an offset or as epoch time. For an appointment whose future local time must follow a venue's rules, retain the local date-time, named IANA zone and the policy for resolving ambiguous or nonexistent times; if a fixed instant is also stored, document which representation wins if zone rules change. A fixed offset alone does not capture future daylight-saving or legislative changes, though it can represent an instant when those rules are not needed. For example, `new Date("1990-01-01")` represents midnight UTC, which displays as December 31 in New York, not the birthday.

With native Temporal or an explicitly imported compatible polyfill:

```js
const birthday = Temporal.PlainDate.from("1990-01-01");
const storedBirthday = birthday.toString(); // "1990-01-01", no zone
const restoredBirthday = Temporal.PlainDate.from(storedBirthday);
const expiry = Temporal.PlainYearMonth.from("2027-12");
const alarm = Temporal.PlainTime.from("09:00");

// A venue appointment becomes an instant only after choosing zone and policy.
const local = Temporal.PlainDateTime.from("2026-11-01T01:30");
const zone = "America/New_York";
const appointment = local.toZonedDateTime(zone, { disambiguation: "reject" });
const storedInstant = appointment.toInstant().toString();
```

The final conversion intentionally throws `RangeError` for the repeated New York local time in this example. Catch that at the input boundary and ask the user or apply a documented domain policy: `earlier` or `later` selects a resolution; `compatible` is Temporal's default. Spring-forward gaps are nonexistent local times and also need a policy; do not silently assume every local time exists. Invalid date or zone input must likewise be reported rather than stored as an invented instant. For legacy `Date` interoperability, convert an explicitly zoned value through `toInstant().epochMilliseconds`; when reading it back, project the instant into the *intended* zone before extracting a date.

For recurring values, define the recurrence separately from storage. `Temporal.PlainDate.from("2024-01-31").add({ months: 1 })` constrains to February 29; `{ overflow: "reject" }` throws instead. Where relevant, decide whether subsequent occurrences are calculated from the original anchor or the previous constrained date, and define leap-day and missing-day behavior. For an annual `PlainMonthDay`, supply the occurrence year before date arithmetic; for expiry comparisons, compare year-month values without inventing a day. If the business rule needs an expiry instant, it must additionally specify the boundary time and zone.

Temporal support varies: when using it, check the actual target runtimes and load a compatible polyfill before dependent code where needed; importing one does not necessarily install a global. Validated plain fields or strings and a calendar-aware implementation are also viable without Temporal; avoid silently converting through `Date`. Verify the risks relevant to the value and operations: for example, round trips across zones for dates that must not shift, month ends and leap years for recurrence, and daylight-saving gaps and overlaps for zoned appointments. For appointments verify that the selected policy produces the intended instant and local display; do not invent a zone or resolution when the domain requires one and it is unknown.

Source: [Capturing Location-Agnostic Data and Partial Dates with Temporal](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/js/capture-location-agnostic-data.md), v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`.
