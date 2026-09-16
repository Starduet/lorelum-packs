---
anti_patterns:
  - description: Calling every supplementary file a reference obscures whether a reader should read it, copy it, or explicitly execute it; treating a script as an installation hook silently turns a Pack file into authority it does not have.
    id: pack-creator.authoring.resource-kind-hides-consumption-boundary
    name: Resource kind hides how it is consumed
    severity: warn
applies_when: an author has decided to include Pack-native supplementary material and must choose whether it is a reference, an asset, or a script while preserving predictable Agent behavior and no automatic execution
id: pack-creator.authoring.choose-reference-asset-or-script
severity: warn
stage: authoring
tech_stack:
  - lorelum-pack-authoring
title: Choose a Resource Kind by the Reader's Next Action
---

## When to apply

Apply after deciding that a file belongs beside a Practice, before choosing its Pack directory. The
decision is what the next reader should do with the file: read it for conditional detail, copy it
into a deliverable, or explicitly run it as a bounded operation.

## Guidance

Put material whose next action is reading in `references/`: examples include a long policy, field
table, evidence note, compatibility matrix, or runbook. Put material whose next action is making a
task artifact in `assets/`: examples include a report outline, checklist, config skeleton, or
starter file; instruct the reader to copy it to the intended workspace before editing. Put a
repeated, deterministic diagnostic, check, or conversion in `scripts/`; the linking Practice must
name when it is useful, its inputs, expected output, and the condition that ends the work.

Use the smallest resource that supports the next action. Keep scripts explicit and self-contained
enough to inspect: do not make installation install dependencies, read credentials, connect to a
service, or execute a script. Stop when a reader can infer one intended action from the directory
and the Practice's link text, without treating every resource as an executable instruction.

When an author needs a bounded review inventory, they may explicitly run the
[resource inventory helper](resource:scripts/inspect-resources.py) with the Pack root as its only
input. It prints JSON file paths and does not replace `lore validate`; run it only when the current
task authorizes that inspection.

## Anti-pattern

An incident-response Pack stores its report template, a long severity table, and a Python checker in
one `references/` folder. The Practice says "use the incident resources." A reader opens the wrong
file, edits the installed template in place, and assumes the Python file ran during installation.
Renaming the folder without stating the script inputs does not fix the missing consumption boundary.

## Why

The three directories communicate different safe defaults without requiring a descriptor for every
file: reference means read on demand, asset means copy before editing, and script means explicitly
run only when the task authorizes it. That distinction prevents both unnecessary context loading and
accidental execution assumptions.

## Exceptions and boundaries

An asset may be a binary file and a script can legitimately include unlinked helper files. A static
JSON fixture may be a reference when it is read as evidence, or an asset when it is copied into the
caller’s output; choose based on the next action, not its extension. This classification does not
make a script trusted, sandboxed, or portable across host environments. `lore validate` checks file
structure but does not run scripts or prove their behavior.

## Example

A deployment-review Practice links a cloud-provider compatibility table from `references/`, tells
the release manager to copy a change-summary skeleton from `assets/`, and links a deterministic diff
checker under `scripts/` for repositories with a public API change. The Practice names the diff
range and expected report, while install and retrieval merely preserve the script bytes. Each file’s
location matches the reader’s next action.
