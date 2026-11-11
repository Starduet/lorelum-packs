# Modern Web Guidance

Unreleased candidate: decision-focused Lorelum Practices distilled from the web-platform guides in [GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance), pinned to v1.0.0. See [SOURCES.md](./SOURCES.md) for provenance and license.

The Practices cover selected CSS and layout, UI and accessibility, and client-side platform decisions. Each addresses a particular implementation choice and its limits. Check current support against the application's actual browser policy; a newer API is not a reason to remove a required fallback. This is a selection, not a replacement for the upstream guide catalog or its Chrome extension guidance.

The candidate has 34 Practices: 18 CSS/layout, 8 UI/accessibility, and 8 platform/security/performance. `lore validate` returned no diagnostics; an isolated path installation listed all 34 and an exact `lore get` read the dialog Practice. No retrieval benchmark, independent domain review, browser/assistive-technology run, or downstream agent evaluation has been performed.

This working-tree Pack has not been published to the Registry. Structural validation and any sampled CLI readback are not evidence of comprehensive retrieval quality, browser behavior, accessibility conformance, or downstream agent improvement.
