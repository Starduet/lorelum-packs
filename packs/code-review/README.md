# Code Review

An unreleased, lightweight Knowledge Pack for reviewing changes in repository context. Eight independently retrievable Practices target concrete backend and frontend change signals; findings require reachable scenarios, relevant contracts and user-visible consequences, not merely suspicious syntax.

## Required review entry point

Before each review, the calling harness or user must explicitly load [the review execution contract and workflow](resource:references/review-workflow.md) into the actual reviewer's context. It contains the model and reasoning-level requirements, permitted assistance, and the complete diff-to-finding workflow. Neither a Pack README nor an on-demand resource is automatically resident; Pack installation and Practice retrieval alone do not enforce this contract or select a model. If the harness cannot establish a requested model or reasoning level, substantive review is blocked rather than silently routed elsewhere.

The requested reviewer performs all substantive review decisions. Other agents may assist with factual lookup, not candidate findings or module-by-module judgments. Posting comments, modifying code and transmitting repository content remain subject to the user's authorization.

## Use

For local authoring, install this directory into an isolated Lorelum Store using `lore pack install --path ./packs/code-review --store-root <isolated-store>`. Explicitly load the execution contract. Before retrieval, the reviewer writes a short, neutral sentence describing the change's intent and includes it with the diff; do not rely on raw diff alone, which performed poorly in the recorded sample. Even intent-assisted retrieval missed cases; inspect relevant neighboring Practices and do not claim comprehensive coverage. Repository-specific requirements and actual code determine whether a side effect must block, be durable, or can fail independently; accounting is not assumed disposable.

This candidate is not registered or released. Installation, retrieval, and actual review behavior are distinct evidence; see the evaluation fixtures for hypotheses, not claims of success. [Sources](./SOURCES.md) record what external examples support and their limits.

## Local evidence

Lorelum 0.1.0-alpha.7 validated the Pack and updated all eight Practices in an isolated Store.
On 16 positive fixture diffs, raw keyword queries returned the intended Practice first in 4 cases
and in the top three in 9; raw semantic queries scored 2 and 6 respectively. Adding a prewritten
neutral change-intent sentence improved keyword to 12 and 15, and semantic to 10 and 14. Neither
shape satisfies complete coverage; raw diff retrieval in particular remains poor. Both query
shapes, expectations, and per-case rankings are recorded in
`fixtures/code-review/diff-retrieval-rerun.json`. The earlier observation remains separately
recorded; one fixture changed, so its aggregate is not a controlled before/after comparison.

After adding a delivery synonym, an independent `openai/gpt-6.1-terra` agent saw only numbered
diffs and wrote neutral change descriptions without expected Practice IDs. With those descriptions,
keyword retrieval returned the intended Practice first in 14/16 and in the top three in 15/16;
semantic returned it first in 9/16 and in the top three in 16/16. The keyword miss was the terminal
state case. See `fixtures/code-review/blind-intent-retrieval.json` for the descriptions and results.
This small, synthetic sample is not proof of generalization or review behavior, and the Pack revision
differs from the earlier run.

After the plain-language rewrite, the same 16 recorded intent-plus-diff inputs were queried using
`versions/0.1.0-alpha.7/lore.exe` directly against the isolated Store. Keyword returned the intended
Practice first in 12/16 and in the top three in 16/16; semantic returned it first in 10/16 and in
the top three in 16/16. See `fixtures/code-review/plain-language-retrieval.json`. The earlier runs
used `lore.cmd`; a later user report found that wrapper can mishandle multiline arguments, so they
are not a reliable controlled baseline for measuring the rewrite's effect.

The user reported an Opus 5.5 run over all 32 synthetic cases, with 16/16 positive matches and
no false positives among 16 negatives. The reported run used low reasoning and the reviewer had
previously seen the answers, so it is a process exercise, not independent blind or high-effort
acceptance evidence. This report has not been independently reproduced here.

Two real AACR-Bench PRs are pinned in `fixtures/code-review/aacr-candidates.yaml` without
copying their reference comments. The LocalAI candidate was checked out at its recorded head,
and its benchmark base-to-head merge-base diff was accessible. An intent plus the first hunk
of `core/http/endpoints/openai/chat.go` returned the LLM Practice first in keyword mode and
third in semantic mode. Sending the whole 6,323-character patch as one query failed with
`usage.invalid`. These are input and retrieval smoke observations, not a complete diff review,
an independent label judgment, or benchmark acceptance.

This exercise does not establish real-PR review quality. Issue #45's specified-model, high-effort
blind review acceptance remains unmet.
