---
anti_patterns:
  - description: Treating a concise handoff as proven because the sender is trusted or rerunning work is costly lets omitted limits, references to old files or commits, and unsupported conclusions control the receiver's next decision.
    id: agentic-coding.recovery.handoff-as-proof
    name: Handoff treated as proof
    severity: warn
applies_when: another agent, contributor, or delegated task has returned conclusions or completion status, and the receiver is about to rely on them without checking the current request, files, commit, and cited results
id: agentic-coding.recovery.validate-handoff-before-continuation
severity: warn
stage: recovery
tech_stack:
  - agentic-coding
title: Validate Handoffs Before Continuing
---

## When to apply

Apply when receiving conclusions, test results, or completion status from another Agent,
contributor, delegated task, or workstream and the next action depends on them. Check only the
statements needed for that action, not every exploratory detail. Same-Agent recovery after context
loss requires re-grounding instead; a suggestion that will not affect the next decision may remain
clearly tentative.

## Guidance

1. List the handoff statements that would change your plan, code edit, approval, or completion
   report.
2. For each one, check the current user request, accepted issue, or specification; confirm the
   branch, file, commit, or environment the sender used; and inspect the cited result closely enough
   for the risk.
3. Check for changes made after the sender finished.
4. Decide for each statement: usable as written, usable only for a smaller scope, unsupported, or
   blocked on a decision from the person who owns the requirement. Update the next action
   accordingly.

Stop there; do not repeat the sender's entire task unless the risk requires it.

## Anti-pattern

The user requires a migration that can roll back populated data. A capable specialist reports
"migration verified" with a clean test summary. The receiver trusts the specialist, and the full
fixture is slow, so preparing delivery seems reasonable. The cited run covered only forward
migration on the specialist's earlier commit; the current branch changes rollback handling, and the
handoff omitted both limits.

## Why

Handoffs shorten evidence, assumptions, and unknowns so work can be divided. The receiver still owns
the next decision. Checking only the statements that decision depends on preserves most of the speed
while catching omitted scope, old commits, and unsupported confidence.

## Exceptions and boundaries

Low-impact suggestions can remain clearly tentative until they affect a decision. Trusted automated
results need less inspection when the exact commit and tested behavior are clear. Security,
migration, release, and destructive claims need stronger checks. If a handoff says the scope
changed, trace that change to the user, maintainer, or accepted specification that actually controls
the work; the sender cannot change scope merely by reporting it.

## Example

The user asks for rate limits that remain correct when one service instance loses the shared store.
A delegated task reports the fix verified. The receiver checks the cited commit and test output,
confirming burst limiting in one process but finding no shared-store failover run. It records the
single-process result as valid, rejects the broader "production fix verified" wording, and makes
failover the next required check.
