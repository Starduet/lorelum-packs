---
anti_patterns:
  - description: The author validates a Pack directory in isolation and assumes it wins in the intended child directory, or uses one semantic result as proof while never checking the current context, same-ID winner, Store escape hatch, or generated-file boundary.
    id: pack-creator.evaluation.isolated-pack-pass-as-context-proof
    name: Isolated Pack pass reported as context activation
    severity: warn
applies_when: a repository-local Pack or child overlay has been authored, and the maintainer must verify that the intended working directory resolves the current Practices, inheritance, and fallback behavior without treating index state as source evidence
id: pack-creator.evaluation.verify-project-local-pack-activation
severity: warn
stage: evaluation
tech_stack:
  - lorelum-pack-authoring
title: Verify a Project-Local Pack in Its Real Context
---

## When to apply

Apply after a local Pack or nested overlay is structurally valid and before saying it is ready for
repository use. The question is whether the directory where developers work resolves the expected
current winners. It is not a claim about semantic ranking quality or Registry installability.

## Guidance

Run `lore format` and `lore validate` on the Pack root first; that establishes source structure and
strict diagnostics. From the real parent or child working directory, run `lore context status` and
confirm the expected layer state and warnings. Run a natural keyword query followed by
`lore get <practice-id>` so the test does not require a model and proves that the current context
returns the intended canonical Practice.

For a child overlay, test one same-ID Practice that must select the child and one parent-only
Practice that must remain available. If Store fallback matters, repeat a focused check with
`--no-project` to prove that it deliberately selects Store-only behavior rather than silently mixing
sources. Inspect the repository before completion: `.lorelum/` should contain the authored config
and Pack source, not derived cache, vector, model, or operation files. Stop when each claim is named
precisely: Pack structure passed, the target directory activated the expected winner, and any
retrieval or model behavior not exercised remains unclaimed.

## Anti-pattern

A monorepo root Pack contains a deployment Practice, and `services/payments/` overrides that same
ID. The author runs `lore validate` on the child Pack path and one semantic query after an old index
happens to be ready. The release note says the override works. No check was made from the service
directory, no parent-only Practice was read, and no one noticed that a copied cache file masked the
new source while the index caught up. The correct check uses context status, keyword query, and get
from `services/payments/`, then verifies both the child winner and the inherited parent neighbor.

## Why

Validation proves Pack structure, while ProjectContext activation depends on the working directory,
layer fold, winner precedence, and current source bytes. Keeping those observations separate catches
the mistakes that a valid standalone Pack directory cannot reveal.

## Exceptions and boundaries

Use `--project-root` when an automated test must target a fixture from another working directory; it
should name a directory that directly contains `.lorelum`. A semantic smoke test may be useful after
keyword/context checks, but missing models and incomplete indexes are lifecycle states rather than
proof that source loading failed. Do not require `--no-project` when Store fallback is not part of
the local Pack's contract.

## Example

A repository root supplies `platform.logging`, while `services/billing/` supplies a stricter same-ID
logging Practice and one billing-only Practice. The maintainer validates both Pack roots, then runs
`lore context status`, a keyword query, and `lore get platform.logging` from `services/billing/`.
The returned Practice is the billing winner; a query for the root-only deployment Practice still
finds the inherited source. A separate `--no-project` check returns only the selected Store
baseline. The report records context activation as passed and does not claim a semantic benchmark
was run.
