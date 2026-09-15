---
anti_patterns:
  - description: Keeping detailed evidence, a template, or a helper script beside a Practice without telling a retrieved reader when it matters leaves the material undiscoverable; moving the decision-critical condition into that file makes the Practice incomplete when retrieved alone.
    id: pack-creator.authoring.unrouted-or-decision-hiding-resource
    name: Resource is either unrouted or hides the decision
    severity: warn
applies_when: an author has detailed reference material, a reusable asset, or a helper script to include with a Pack and must decide how a separately retrieved Practice should point to it without depending on directory browsing or hiding its immediate judgment
id: pack-creator.authoring.link-pack-resources-from-the-practice
severity: warn
stage: authoring
tech_stack:
  - lorelum-pack-authoring
title: Route Supplementary Material from the Practice
---

## When to apply

Apply when a Practice is already clear enough to make its immediate decision, but a reader may need
a detailed matrix, evidence record, starter file, or repeatable diagnostic afterwards. The decision
is whether the material belongs in the Pack and how to make its purpose clear when Lorelum returns
only this Practice.

## Guidance

Keep the trigger, action, direct reason, material exception, and stopping point in the Practice.
Place only the supplementary file in `references/`, `assets/`, or `scripts/`, then use a normal
Markdown link with a Pack-root-relative `resource:` target. State the reader's condition for using
the material, not just its filename. For example, write that a public API change requires the
compatibility matrix, that a completed review should begin from a report template, or that a
repeated diagnostic should be run with named inputs and expected output. Use the exact target rather
than a sibling-relative path: `[matrix](resource:references/api-matrix.md)`.

Stop when a cold reader can make the current decision from the Practice, can tell whether the linked
material is needed, and can resolve it from the selected Pack root without guessing a directory.
For the full resource contract and review prompts, see the
[resource authoring guide](resource:references/pack-resources.md).

## Anti-pattern

A database-migration Practice says only "consult the migration material" because the Pack contains a
long compatibility note and a rollback script. The file names make sense to the author, who assumes
an Agent can browse the Pack. When retrieval returns the Practice alone, the Agent does not know
whether the compatibility note is relevant, which file it means, or whether the script is safe to
run. Replacing the sentence with "read `resource:references/migration-compatibility.md`" but moving
the irreversible-migration condition into the note still leaves the immediate decision incomplete.

## Why

Selective retrieval does not carry a directory listing or Pack order with it. An explicit resource
link gives supplemental material a task-level purpose while leaving the judgement that selects it in
the retrievable unit.

## Exceptions and boundaries

Not every Pack file needs a direct link: scripts can use adjacent helpers and an asset set can be
copied together. Do not manufacture links merely to make every file appear in a Practice. Normal web
links and ordinary Markdown relative links remain useful for external sources or document navigation;
use `resource:` only for a same-Pack resource. A resource link is not a file-access allowlist and it
does not authorize executing a script.

## Example

An API-review Pack includes a field matrix and a review-report skeleton. Its Practice states the
breaking-change condition and the checks that decide whether a compatibility review is necessary.
Only after that action it links the matrix with `resource:references/public-api-matrix.md`; after the
review decision, it links `resource:assets/api-review-report.md` and tells the reader to copy it to
the working directory. The Practice remains usable without opening either file, while the reader
knows exactly when both become useful.
