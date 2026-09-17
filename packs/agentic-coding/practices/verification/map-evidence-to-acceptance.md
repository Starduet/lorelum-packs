---
anti_patterns:
  - description: Treating a long list of commands, tests, or inspections as proof of acceptance without mapping results to criteria hides unsupported capabilities behind visible activity.
    id: agentic-coding.verification.coverage-by-activity
    name: Coverage by activity
    severity: critical
applies_when: implementation is ready for verification, actual checks or observations are available, and the agent is about to decide which acceptance criteria those results cover
id: agentic-coding.verification.map-evidence-to-acceptance
severity: critical
stage: verification
tech_stack:
  - agentic-coding
title: Map Evidence to Acceptance Criteria
---

## When to apply

Apply after checks or observations exist and before deciding that acceptance has been demonstrated.
The decision is which current criterion each result actually supports. Planning future evidence
happens before implementation; checking whether a result is still fresh is a separate state-binding
decision; resolving a row left uncovered happens after this map exposes it.

## Guidance

1. Copy the current acceptance criteria from the user request, accepted issue, or specification, one
   row per promised behavior.
2. Line up each collected result — test output, inspected file, direct observation, or green command
   — beside the criterion it actually exercised, including the behavior and environment covered.
3. Mark every remaining row "not covered" or "partly covered" when the results stop short. One
   result may support several criteria only when it really observed each outcome.
4. Record mandatory gates separately and label their role, even when they prove no user capability.

A promised behavior is backed only by the result that observed it. Stop with this
criterion-by-criterion table; do not fill empty rows with confidence, test counts, or nearby
successes.

## Anti-pattern

The user asks for booking submission to issue one reservation even when a request is retried. The
repository has green calculation tests, a full build, static checks, and one successful booking
demonstration. Because the log is substantial and every command is green, the agent reports
verification complete. None of those results retries a submission, so the no-duplicate requirement
disappears behind the activity summary.

## Why

Verification results have narrower meaning than their command names suggest. Mapping makes that
meaning explicit, exposes silent gaps, and lets reviewers challenge a particular criterion-to-result
relationship instead of interpreting a dense log as a general proof.

## Exceptions and boundaries

A single end-to-end observation may cover several criteria when it really includes them; do not
duplicate work to force one result per row. If the user request, accepted issue, and specification
do not agree on acceptance, ask which one controls the work before inventing criteria. This Practice
produces the map, not the final delivery wording.

## Example

The user asks for a report with required fields, readable pages, and a file that opens on the target
phone. The repository has a schema test, rendered page images, a successful phone download, and a
green build. The agent lines the results up against the criteria: the schema result covers required
fields, the image inspection covers readability, and the phone observation covers delivery and
opening; the build is recorded only as a required gate. Because no check interrupted and resumed a
download, offline retry remains explicitly uncovered.
