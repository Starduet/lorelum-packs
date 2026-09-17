---
anti_patterns:
  - description: Reusing a previous pass because a later edit looks small, without checking the exact commit, built file, configuration, and environment that were tested, lets changed work inherit proof it never received.
    id: agentic-coding.verification.stale-proof-carryover
    name: Old result reused for changed work
    severity: critical
applies_when: the agent is about to cite or reuse a verification result obtained before relevant code, configuration, dependencies, generated files, environment, or external conditions may have changed
id: agentic-coding.verification.bind-evidence-to-artifact-state
severity: critical
stage: verification
tech_stack:
  - agentic-coding
title: Reuse Evidence Only When It Still Applies
---

## When to apply

Apply whenever the agent wants to cite an earlier pass after the code, configuration, dependencies,
built package, runtime environment, or relevant outside service may have changed. Decide whether the
old result still describes what will be delivered now. Mapping evidence to acceptance asks which
requirement a result covers; closing a gap asks what to do when there is no adequate result.

## Guidance

1. For each earlier result you plan to cite, write down exactly what it tested: the commit or diff,
   the built or generated file, relevant configuration and dependency versions, the machine or
   service when it matters, the observation time for changing outside facts, and the behavior
   exercised.
2. Compare those details with the current deliverable, change by change.
3. Mark each result usable now, outdated, or unaffected by the later change, and say why.
4. Re-run only the checks whose conclusion could change; rebuild and recheck when the file being
   delivered changed.

Stop when every earlier result you plan to cite has this decision.

## Anti-pattern

The user asks for an archive that another application can open. The repository passes its
compatibility check, then the agent performs a "small cleanup" in serialization. The edit looks
mechanical and the external check is slow, so the agent reuses the earlier pass. The delivered bytes
now come from code that the compatibility result never exercised.

## Why

A pass describes specific files under specific conditions; it is not a permanent badge on the task.
Recording those specifics prevents an old result from proving changed work, while avoiding wasteful
reruns when a later edit cannot affect what was observed.

## Exceptions and boundaries

An unchanged fact can remain usable after an unrelated edit. A documentation-only change does not
normally invalidate a parser unit test; changing parser code does invalidate an earlier binary test.
Security, destructive operations, releases, and results that depend on a live environment may
require a new check more often. Follow mandatory project rerun rules even when the edit appears
unrelated.

## Example

The user asks for a compiled CLI that installs a Pack. A binary built from commit A passes a real
installation test. A later comment-only edit leaves that result usable. When argument parsing
changes at commit B, the agent rebuilds the binary and repeats the installation check; source-level
unit tests at B cannot prove that the old binary from A represents the current code.
