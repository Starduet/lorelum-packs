# Modern Web Guidance candidate evaluation

## Scope and provenance

The candidate contains 14 Practices distilled from the pinned GoogleChrome/modern-web-guidance v1.0.0 sources. They are a selection, not a complete conversion. See [the Pack](../../packs/modern-web-guidance/README.md) and [source record](../../packs/modern-web-guidance/SOURCES.md).

## Checks

- `lore validate` returned no diagnostics; an isolated path installation loaded all 14 Practices, and `lore get` read back the container-query Practice.
- Three fenced JavaScript examples passed Node syntax checking. The long-task example produced ordered results and discarded pre-cancelled and invalidated work in Node; this does not establish browser rendering or responsiveness.
- Four previously sampled keyword requests—export freezing, malicious comment markup, a sidebar card, and a dirty editor dialog—returned their intended Practice first. An out-of-scope database rollback request still returned unrelated Practices; lower-ranked results for in-scope requests also included unrelated Practices. These reused, English-only queries are smoke checks, not independent retrieval evaluation.
- In a small before/after contrast, agents reading the prior and current Practices both handled a simple non-cancellable operation without unnecessary cancellation machinery and preserved required HTTPS links in rich comments without inventing unsupported fallback paths. This does not establish an improvement or measure context cost; the generated answers were not executed or independently security-reviewed.
- Targeted security and UI/CSS reviewers found no evidence-backed regression in the final calibration; this is not comprehensive domain approval.

No browser or assistive-technology behavior, sanitizer execution, real WebAuthn flow, semantic retrieval benchmark, or robust controlled agent evaluation was completed. A managed Chromium launch timed out during an earlier smoke attempt. The Pack has not been published to a Registry.
