# Task-shaped evaluation of the unreleased candidate

## Design and limits

The initial 34-Practice draft was organized too closely around APIs and component-specific guides. The revised 12-Practice candidate groups guidance only where decisions arise together, removes narrow feature entries, and keeps distinct high-consequence decisions separate. The count itself is not a quality metric. The candidate is a selected synthesis of the pinned upstream corpus, not exhaustive coverage.

## Structural and usage checks

On 2026-11-11, `lore validate packs/modern-web-guidance` reported valid and zero diagnostics. A path installation into an isolated Store listed all 12 Practices. These checks establish decoding and installation, not correctness or retrieval quality.

## Keyword task queries

The same eight natural-language queries were run with `lore query --mode keyword --top-k 3 --no-project` against isolated stores containing the initial 34-Practice draft and the 12-Practice revision. The expected decision was identified from the task (not necessarily a single exact ID). Results below report the first result and whether a relevant decision appeared in the top three; top-three relevance was judged manually. IDs from the two versions are not identical after merging.

| Query | Initial top result | Initial relevant in top 3 | Revision top result | Revision relevant in top 3 |
|---|---|---|---|---|
| A product card breaks when placed in a narrow sidebar | component container size | yes | component container size | yes |
| A mobile page overflows horizontally with long text | mobile viewport chrome | yes | long main-thread work | yes |
| Build an accessible confirmation before deleting a record | dialog modality | yes | overlay interaction | yes |
| Choose between a menu and a modal for account actions | list reordering | yes | overlay interaction | yes |
| Display rich text submitted by users safely | searchable hidden content | yes | sanitize untrusted HTML | yes |
| The interface freezes while processing a large list | local language model | no | long main-thread work | yes |
| A product page loads slowly on mobile connections | mobile viewport chrome | no | sanitize untrusted HTML | no |
| Implement recurring birthday dates without shifting days | calendar values | yes | calendar values | yes |

In this small, non-independent sample, the judged relevant decision appeared in the first three results for 6/8 initial queries and 7/8 revised queries. The slow-page query missed in that revision. Results often included unrelated second or third items, so a smaller Pack did not eliminate context noise. No semantic retrieval test or confidence interval was performed.

After that run, the image-priority Practice was revised into a broader slow-loading diagnosis Practice. Reinstalling the changed Pack and repeating the slow-page query placed `modern-web-guidance.platform.diagnose-slow-page-loading` first, followed by unrelated HTML sanitization and external-asset security results. This is a targeted, post-observation check, not an independently selected test; the other seven queries were not rerun against this final revision.

## Small behavior contrast

Two separate agents answered the same three design questions: a product card in a main column and narrow sidebar; safe rendering of plain and limited rich-text comments; and a destructive confirmation that blocks background interaction. One was instructed not to consult the Pack; the other manually selected and read relevant candidate Practices (not Lorelum query results). Both were asked for choices, failure boundaries and checks. This is an exploratory comparison, not a blind controlled benchmark or proof of general improvement.

Both answers independently selected container-aware layout, text rendering versus sanitization, and a modal dialog. The Pack-assisted answer additionally called out container self-query/containment constraints, alignment between native and fallback sanitization policies, and clearing a dialog's `returnValue` before reopening. The unaided answer included deletion failure and duplicate-submission handling, which the Pack-assisted answer omitted. The assisted agent read five Practices for the three tasks, including three CSS Practices for the card. Therefore this run shows concrete additions and omissions, not that the Pack reliably improves an agent or reduces loaded context.

No application was implemented or browser/assistive-technology behavior exercised. Independent domain review and broader task-based evaluation remain open.

## Accessibility revision: targeted keyword checks

After content review, the candidate gained form-error and reduced-motion Practices; the main-thread trigger was broadened to include save and export work. It also clarifies guarded dialog closing and `hidden="until-found"` layout constraints. The isolated path install loaded 14 Practices and `lore validate` returned zero diagnostics; `lore get` returned the complete form Practice.

In keyword mode with `--top-k 3`, the previously missed signup-validation, responsive-export, and reduced-motion queries each returned their intended Practice first. Previously checked product-grid, account-menu, and XSS queries also returned their relevant Practice first. Two new paraphrases about server-returned form errors and static content when animations are disabled likewise returned the intended Practice first. The out-of-scope query “A database transaction must roll back on failure” returned form validation, content controls, and passkey Practices instead of no results. Many second and third results were unrelated.

These are small, English keyword-only examples; the three formerly missed queries were used to guide the revision and are not a held-out benchmark. Relevant top results do not prove that a downstream Agent will select only useful guidance, follow it correctly, or improve over no Pack. A managed Chromium smoke attempt timed out at browser launch; no dialog, find-in-page, browser, or assistive-technology behavior was tested.

## Decision-depth revision

The 14 Practices were rewritten using the pinned upstream material to make task-specific choices, implementation constraints, examples and verification observable. A targeted security review found that a username-free passkey request with preferred user verification could resolve to an account requiring verification; the text now requires the stricter current server policy and describes the rejection case. A UI review found missing modal scroll containment; the text now gives the upstream progressive enhancement and its unsupported-browser boundary. Neither finding was reproduced in an application; this is a content correction, not runtime proof.

The revised Pack passed `lore validate` with no diagnostics, installed 14 Practices into an isolated Store, and `lore get` read the long-task Practice. Three fenced JavaScript examples passed Node syntax checks. The actual long-task example was executed in Node with a synchronous `processItem`: correct ordered results, cancellation before processing and invalidation during processing passed. This does not demonstrate browser rendering, sanitizer safety, Temporal behavior, real WebAuthn verification or assistive-technology behavior.

Ten English keyword queries and their expected IDs were declared before the run. Nine returned their expected ID first in the first revised snapshot: export freeze, late hero image, unsafe comment preview, CDN changes, responsive sidebar card, dirty dialog, form errors, reduced motion, and daylight-saving appointment. “My long text is clipped in a small panel” missed its expected overflow Practice in the top three. After the trigger was clarified, a targeted rerun against a new isolated install returned it first; the other nine queries were not rerun on that final snapshot. The out-of-scope database-rollback query still returned unrelated Practices. Second and third results often remained unrelated. These small keyword-only observations do not establish semantic retrieval quality or a reliable relevance threshold.

Two separate agents each answered an export task and a rich-comment task, once without Pack access and once after reading the relevant rewritten Practice. For export, both covered immutable snapshots, cancellation, stale results and performance measurement; the unassisted answer selected a worker-first design while the assisted answer supplied a main-thread chunking example and discussed worker tradeoffs. For comments, the unassisted answer proposed a structured-data renderer that avoids HTML parsing; the assisted answer gave a native/DOMPurify design with an explicit HTTPS link policy and parity checks. Neither answer was executed or independently security-reviewed, and these different designs do not establish that the Pack caused a better result. These two cases, one answer per condition and manually supplied Practices, cannot measure retrieval, overall improvement or context cost.

## Calibrating defaults and edge cases

All 14 Practices were reviewed for ordinary paths, observable conditions for safeguards, and examples whose assumptions might be mistaken for product policy. The revision makes media-query fallbacks depend on actual placements and target browsers, scopes cancellation and generation tracking to operations where those conditions can arise, and makes the restrictive HTML example one policy rather than a universal allowlist. Security verification, protection of untrusted insertion boundaries, and applicable keyboard and focus behavior remain required.

Before and after the revision, separate agents each read the relevant Practice and answered two identical tasks. In both versions, the simple immutable, non-cancellable, non-overlapping computation was implemented without a cancellation signal or generation counter; the rich-comment task preserved required HTTPS links using a native sanitizer and URL checks, without adding a fallback or server-rendering path absent from the task. These are two manual, non-blind observations: the previous version already produced these outcomes, so they do not establish an improvement. The generated answers were not executed or security-reviewed.

The calibrated Pack passed `lore validate` without diagnostics, installed all 14 Practices in an isolated Store, and `lore get` returned the container-query Practice. Three fenced JavaScript examples passed Node syntax checking; the long-task example produced correct ordered results and discarded pre-cancelled and invalidated work in Node. No browser, sanitizer, real WebAuthn, screen-reader or semantic-retrieval behavior was exercised in this revision.

Four previously sampled keyword requests—export freezing, malicious comment markup, a sidebar card, and a dirty editor dialog—returned their intended Practice first in the calibrated Store. The out-of-scope database-rollback request still returned unrelated Practices; second and third results on the four in-scope queries also included unrelated Practices. These reused queries are smoke checks, not new independent retrieval evidence.
