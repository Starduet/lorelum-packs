# Code Review

An unreleased, lightweight Knowledge Pack for reviewing changes in repository context. Ten independently retrievable Practices cover backend and frontend behavior, tests, and logging; findings require reachable scenarios, relevant contracts and user-visible consequences, not merely suspicious syntax.

## Required review entry point

Before each review, the calling harness or user must explicitly load [the review execution contract and workflow](resource:references/review-workflow.md) into the actual reviewer's context. It contains the model and reasoning-level requirements, permitted assistance, and the complete diff-to-finding workflow. Neither a Pack README nor an on-demand resource is automatically resident; Pack installation and Practice retrieval alone do not enforce this contract or select a model. If the harness cannot establish a requested model or reasoning level, substantive review is blocked rather than silently routed elsewhere.

The requested reviewer performs all substantive review decisions. Other agents may assist with factual lookup, not candidate findings or module-by-module judgments. Posting comments, modifying code and transmitting repository content remain subject to the user's authorization.

## Use

For local authoring, install this directory into an isolated Lorelum Store using `lore pack install --path ./packs/code-review --store-root <isolated-store>`. Explicitly load the execution contract. Before retrieval, the reviewer writes a short, neutral sentence describing the change's intent and includes it with the diff; do not rely on raw diff alone, which performed poorly in the recorded sample. Even intent-assisted retrieval missed cases; inspect relevant neighboring Practices and do not claim comprehensive coverage. Repository-specific requirements and actual code determine whether a side effect must block, be durable, or can fail independently; accounting is not assumed disposable.

This candidate is not registered or released. Installation and retrieval do not prove that a
reviewer will find real defects. [Sources](./SOURCES.md) records the references used to write the
Practices.

## Validation limits

Lorelum 0.1.0-alpha.7 validated and installed the ten-Practice Pack in an isolated Store. Local
retrieval checks included both synthetic changes and selected real PR diffs; they are not proof
of real-world review quality. A reported review of 32 synthetic cases used low reasoning and a
reviewer who had previously seen the answers, so it does not satisfy issue #45's independent
Opus 5.5 high review requirement. That acceptance remains unmet.
