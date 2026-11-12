# Modern Web Guidance

Unreleased candidate: decision-focused Lorelum Practices distilled from the web-platform guides in [GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance), pinned to v1.0.0. See [SOURCES.md](./SOURCES.md) for provenance and license.

The candidate contains 14 Practices: four for CSS and layout, four for interface interaction and accessibility, and six for browser performance, security, and date semantics. They target implementation decisions rather than individual features. Check compatibility against the application's browser policy; this selection does not replace the upstream catalog or cover Chrome extensions.

The initial draft organized entries too closely around individual APIs. The current revision keeps 14 decision-focused Practices and expands decision-critical implementation, failure boundaries, examples, and checks based on the pinned sources. See [the evaluation record](../../fixtures/modern-web-guidance/task-evaluation.md) for sampled queries, code smoke, reviewer findings, and a small behavior contrast. Neither length nor count establishes usefulness.

This Pack is an unreleased candidate, not an official Registry release. A targeted security and UI review identified and corrected two risks in this revision. No comprehensive independent domain approval or browser and assistive-technology testing has been completed.
