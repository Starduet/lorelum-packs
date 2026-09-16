---
anti_patterns:
  - description: Treating a valid resource directory or a successful local script invocation as proof that a released Pack materializes the same bytes, that the link routes the right decision, or that an Agent will use the material correctly conflates separate evidence layers.
    id: pack-creator.evaluation.resource-structure-as-end-to-end-proof
    name: Resource structure reported as end-to-end behavior
    severity: warn
applies_when: a Pack adds or changes references, assets, scripts, or resource links and the author must decide what validation, installation, retrieval, and Agent evidence is needed before describing those materials as ready
id: pack-creator.evaluation.verify-resource-integrity-without-overclaiming
severity: warn
stage: evaluation
tech_stack:
  - lorelum-pack-authoring
title: Verify Resource Integrity as Its Own Evidence Chain
---

## When to apply

Apply when canonical Pack resources or a Practice’s `resource:` link have changed. The decision is
which observations prove file structure, selected-artifact preservation, routing, and downstream
use, without promoting a cheap local check into a broader quality claim.

## Guidance

First run `lore validate` on the Pack and record the Pack revision and structural diagnostics. It
can establish that allowed resource paths and declared links are structurally valid; it does not
execute scripts or assess their logic. For a release candidate, install through the supported
Registry path into an isolated Store, retrieve the linked Practice, and resolve a representative
reference or asset from the returned source root. Record the exact version, ref, source target, and
observed bytes or file identity. Only run a script in a separately authorized task with stated
inputs and expected output.

Then review whether the Practice still carries its immediate decision and whether its link selects
the material at the right moment. Test retrieval and downstream Agent behavior as separate
exercises. Use the [resource review checklist](resource:assets/resource-review-checklist.md) to
record which layers were observed. Stop when every claim says whether it covers structure,
installation, content review, retrieval selection, script execution, or Agent behavior.

## Anti-pattern

An observability Pack adds a binary dashboard template and a log-parser script. `lore validate`
passes locally, and the author runs the parser against one log file. The release note says the Pack
"ships verified observability automation." The test did not install the selected release, did not
show that the Practice routes the correct incident, and did not establish that another Agent can use
the parser safely with production input.

## Why

Resources add two facts beyond ordinary Practice text: the selected artifact must preserve the right
bytes, and the Practice must route a reader to them at the right decision. Structural validation,
remote materialization, retrieval, explicit script execution, and downstream behavior observe
different parts of that chain.

## Exceptions and boundaries

Do not require every helper file to be individually linked or executed. An unreferenced helper can
be structurally valid, and a binary asset may be verified by digest or size rather than being
rendered in a text terminal. A successful install does not prove a script works; a successful script
run does not prove a release artifact contains it. Do not execute scripts merely to make a release
checklist complete.

## Example

A data-migration Pack adds a compatibility reference, a migration-plan template, and a read-only
schema-diff script. The author records a clean `lore validate` result, installs the tagged release
into an isolated Store, gets the migration Practice, reads the reference from its returned root, and
confirms the template exists. A separately authorized test runs the schema-diff script with a
fixture. Retrieval queries and an Agent exercise are reported independently, so the release claim
states exactly which links and bytes were verified.
