# Modern Web Guidance

Unreleased candidate: decision-focused Lorelum Practices distilled from the web-platform guides in [GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance), pinned to v1.0.0. See [SOURCES.md](./SOURCES.md) for provenance and license.

The candidate contains 14 Practices: four for CSS and layout, four for interface interaction and accessibility, and six for browser performance, security, and date semantics. They target implementation decisions rather than individual features. Check compatibility against the application's browser policy; this selection does not replace the upstream catalog or cover Chrome extensions.

The first draft contained 34 Practices organized too closely around individual features. This revision removes low-value feature-specific entries and combines guidance where a task needs the choices together; it retains separately triggered decisions such as unsafe HTML insertion and passkey authentication. See [the evaluation record](../../fixtures/modern-web-guidance/task-evaluation.md) for the sampled task queries, known misses, and behavioral comparison. Neither a smaller count nor successful validation proves improvement.

This Pack is an unreleased candidate, not an official Registry release. It has not received independent domain review or browser and assistive-technology testing.
