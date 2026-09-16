---
anti_patterns:
  - description: The author copies every parent Pack into a child directory to change one Practice, or disables inheritance because a child needs one override, causing valid parent guidance and lower-priority fallbacks to disappear.
    id: pack-creator.design.child-layer-copies-or-hides-parent
    name: Child layer copies or hides its parent
    severity: warn
applies_when: a repository has parent and child directories with .lorelum layers, and the author must decide which Practices and configuration fields the child should inherit, override, or isolate
id: pack-creator.design.compose-inherited-project-layers
severity: warn
stage: design
tech_stack:
  - lorelum-pack-authoring
title: Compose Project Layers as Incremental Overlays
---

## When to apply

Apply when a monorepo, nested component, generated subproject, or local experiment needs its own
`.lorelum` directory while an ancestor already supplies guidance. This Practice decides precedence
and scope between layers. It does not decide whether the Pack should be local or released through a
Registry.

## Guidance

Keep broadly applicable repository guidance in the nearest useful parent layer. Add only the
child-specific Pack files or same-ID Practice replacements in the child layer. Lorelum folds layers
from parent to child: a child Practice with the same ID wins, while parent Practices the child does
not replace remain active. A child Pack with the same name is therefore an incremental overlay, not
a whole-Pack replacement.

Let omitted config fields inherit. Use `packs.<name>.enabled` or `priority` only for an explicit
Pack-level decision, and use `base: none` only when the child must exclude the selected user Store.
Set `inherit: false` only for a genuinely isolated subtree; it removes every parent layer rather
than merely choosing one child Practice. Write down the expected winner for every same-ID override
and test it from the child directory. Stop when the child contains only its own decisions, the
parent still supplies unaffected Practices, and an operator can explain why each winner applies.

## Anti-pattern

A repository root has a `platform` Pack with deployment, logging, and database-change Practices. A
service directory needs a stricter same-ID deployment Practice for its regulated release. To avoid
thinking about inheritance, the author copies the whole root Pack into the service and changes one
file. Root corrections now need two edits, the duplicated unrelated Practices can drift, and a
half-written child copy can hide otherwise valid parent guidance. The child should contain only its
replacement Practice; the parent remains the source for the other decisions.

## Why

Incremental overlays preserve the useful baseline while making a local exception visible at the
Practice that actually changes. Whole-Pack shadowing turns a small local decision into a duplicated
maintenance surface and makes ordinary source edits more fragile.

## Exceptions and boundaries

Use `inherit: false` for a vendored, regulated, or intentionally independent subtree whose parent
rules must not affect it. Explicit priority can resolve two valid sources that genuinely need a
stable ordering, but it should not compensate for unclear or duplicate Practice IDs. This Practice
does not change the Store's own installed-Pack conflict rules.

## Example

At the repository root, `.lorelum/packs/platform/` contains `platform.release`, `platform.logging`,
and `platform.database`. The `payments/` directory adds its own
`.lorelum/packs/platform/practices/platform.release.md` with the card-network approval condition.
Querying from `payments/` returns the child release rule plus the root logging and database rules.
Querying from the root returns the original release rule. No Pack was copied, and a future root
logging correction reaches both directories.
