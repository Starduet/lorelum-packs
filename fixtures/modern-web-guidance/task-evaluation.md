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
