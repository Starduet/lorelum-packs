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

Another agent, contributor, delegated task, or workstream reports a conclusion, test result, or
completion status that you need for your next action. Check the statements that action depends on,
not every exploratory detail. If you are recovering your own work after losing context, recheck the
original sources instead. A suggestion that does not affect the next decision can remain clearly
tentative.

## Guidance

1. List the statements in the handoff that would change your plan, edit, approval, or completion
   report.
2. For each, compare it with the current user request, accepted issue, or specification. Confirm
   which branch, file, commit, or environment the sender used, and inspect the cited result as
   closely as the risk requires.
3. Check what changed after the sender finished.
4. Decide whether each statement is usable as written, true only for a narrower scope, unsupported,
   or waiting for a decision from the person responsible for the requirement. Adjust your next
   action to match.

Stop there. Do not repeat the sender's entire task unless the risk requires it.

## Anti-pattern

The user requires a migration that can roll back populated data. A capable specialist reports
"migration verified" with a clean test summary. The receiver trusts the specialist, and the full
fixture is slow, so preparing delivery seems reasonable. The cited run covered only forward
migration on the specialist's earlier commit; the current branch changes rollback handling, and the
handoff omitted both limits.

## Why

Handoffs summarize evidence, assumptions, and unknowns so work can be divided. The receiver still
owns the next decision. Checking only the statements that decision depends on preserves most of the
speed while catching omitted scope, old commits, and unsupported confidence.

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
