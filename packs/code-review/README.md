# Code Review

An unreleased, lightweight Knowledge Pack for reviewing changes in repository context. Eight independently retrievable Practices target concrete backend and frontend change signals; findings require reachable scenarios, relevant contracts and user-visible consequences, not merely suspicious syntax.

## Required review entry point

Before each review, the calling harness or user must explicitly load [the review execution contract and workflow](resource:references/review-workflow.md) into the actual reviewer's context. It contains the model and reasoning-level requirements, permitted assistance, and the complete diff-to-finding workflow. Neither a Pack README nor an on-demand resource is automatically resident; Pack installation and Practice retrieval alone do not enforce this contract or select a model. If the harness cannot establish a requested model or reasoning level, substantive review is blocked rather than silently routed elsewhere.

The requested reviewer performs all substantive review decisions. Other agents may assist with factual lookup, not candidate findings or module-by-module judgments. Posting comments, modifying code and transmitting repository content remain subject to the user's authorization.

## Use

For local authoring, install this directory into an isolated Lorelum Store using `lore pack install --path ./packs/code-review --store-root <isolated-store>`. Load the execution contract explicitly, then retrieve relevant Practices for the changed behavior. Repository-specific requirements and actual code determine whether a side effect must block, be durable, or can fail independently; accounting is not assumed disposable.

This candidate is not registered or released. Installation, retrieval, and actual review behavior are distinct evidence; see the evaluation fixtures for hypotheses, not claims of success. [Sources](./SOURCES.md) record what external examples support and their limits.

## Local evidence

Lorelum 0.1.0-alpha.7 validated the Pack and updated all eight Practices in an isolated Store.
Sixteen positive fixture diffs were submitted directly as queries, with expected Practice IDs
fixed before execution. Keyword retrieval ranked 5 first and 9 in the top three; semantic retrieval
ranked 3 first and 9 in the top three. Both modes missed seven targets in the top three, although
not always the same cases. See `fixtures/code-review/diff-retrieval-observation.json` in the
repository for per-case rankings. These are retrieval failures, not a pass.

The 32 synthetic positive and negative cases have not been run as independent review sessions.
Specified-model routing and real review quality remain unverified. Do not treat this Pack as
satisfying issue #45's review behavior acceptance until the requested model and reasoning level are
verified and the cases run.
