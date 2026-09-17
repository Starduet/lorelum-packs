---
anti_patterns:
  - description: Treating an untested required behavior as proved because it shares code, UI, or a happy path with a passing check hides what is still unknown and leads to an overbroad completion report.
    id: agentic-coding.verification.gap-by-implication
    name: Untested behavior inferred from a nearby pass
    severity: critical
applies_when: comparison with the acceptance criteria shows that a required behavior has no adequate result, and the agent must decide whether to run another check, ask to reduce the promised scope, or report the work incomplete
id: agentic-coding.verification.close-or-declare-evidence-gaps
severity: critical
stage: verification
tech_stack:
  - agentic-coding
title: Resolve Missing Verification Results
---

## When to apply

Apply only after a criterion-by-criterion review has identified one specific behavior with no result
or only a partial result. Decide what to do about that missing proof before delivery. Choosing the
first set of checks belongs to planning; writing the final completion statement belongs to delivery.

## Guidance

1. Name the exact uncovered behavior that remains unproved, and explain why the existing results
   stop short.
2. Choose one action: run the missing check, narrow the promise with the person who owns the
   requirement, or mark the item explicitly unfinished and name what remains.
3. Base the choice on the harm of being wrong, whether the requirement is mandatory, and whether the
   check can be performed. A must-have requirement cannot be silently reduced because its check is
   slow or inconvenient.

Stop when every important missing result has one visible action; a nearby success never counts as a
pass by implication.

## Anti-pattern

The user requires an upgrade from version 1 to retain every installed Pack. Fresh installation and
the migration function's unit tests are green, and the upgrade writes through the same store code.
Building a real version-1 store is slower, so the agent treats retention as implied. No result opens
an existing store, runs the upgrade, and reads the installed Packs afterward, so the required
upgrade behavior disappears behind nearby passes.

## Why

A missing result becomes a hidden assumption when no one decides what to do with it. An explicit
action produces a new observation, a smaller goal accepted by the right person, or a clear statement
of what is still unfinished before anyone relies on more than was tested.

## Exceptions and boundaries

The user or maintainer who owns a low-impact requirement may accept a smaller goal when the missing
check is infeasible. Safety, authorization, data integrity, migration, compatibility, and
irreversible-release requirements may forbid that choice. Do not let the Agent grant itself
permission to drop an explicit must-have requirement.

## Example

The user asks for a backup that can restore a service after data loss. The repository's backup job
completes and the archive checksum passes, but no test restores it into a clean database. The
checksum makes the archive look trustworthy, yet it cannot reveal missing tables or an unusable
restore command. The agent performs the restore with representative data or reports recovery
verification incomplete; it does not replace the required recovery goal with "backup file created."
