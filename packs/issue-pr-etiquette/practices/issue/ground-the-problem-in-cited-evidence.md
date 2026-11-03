---
anti_patterns:
  - description: Asking a repository to act on an uncited claim makes maintainers verify or guess the evidence themselves, so triage stalls on requests for examples that should have led the issue.
    id: issue-pr-etiquette.issue.uncited-claim-as-evidence
    name: Uncited claim standing in for evidence
    severity: warn
applies_when: an issue asserts that something is broken, missing, or worth building, and the author must decide what concrete evidence justifies the claim before asking others to act on it
id: issue-pr-etiquette.issue.ground-the-problem-in-cited-evidence
severity: warn
stage: issue
tech_stack:
  - github-contribution
title: Ground the Problem in Cited Evidence
---

## When to apply

When reporting a bug, describing a recurring problem, or proposing something new, give maintainers
the evidence behind your request. Show what you observed and where they can read it. If that
evidence is confidential, first work out what you can safely cite; do not publish it just to support
the issue.

## Guidance

Lead with the concrete occurrences that motivated the issue: link the incident, failing run, support
thread, or prior issue by number, and quote the smallest fragment that shows the problem. Separate
observed facts from interpretation — write what happened first, then what you conclude it means.
Where earlier issues are related, list each with a one-line role ("evidence this recurs", "prior
attempt, reverted because") instead of a bare number. State the basis explicitly when the claim
rests on your reasoning rather than on observed events, so reviewers can weigh it as a proposal. The
evidence is sufficient when a maintainer can follow the links and understand the problem without
asking you for examples.

## Anti-pattern

A contributor files "retrieval often returns irrelevant Practices" with no links. The maintainer
asks for example queries; the contributor answers three days later with two cases, one of which was
already fixed. The issue spends its first week gathering evidence instead of evaluating it, and the
maintainer cannot judge severity or check for duplicates until the round-trip finishes.

## Why

Reviewers assess issues using evidence they can open, not just the author's confidence. Citations
let them check how widespread the problem is, find duplicates, and decide who should handle it on
first read. Without citations, they must ask for examples before they can assess the issue.

## Exceptions and boundaries

Security reports follow the repository's private advisory channel and must not carry public
reproduction steps — cite the advisory reference instead. Fresh proposals may have no prior
incidents; that absence is itself the stated basis, not a reason to imply evidence that does not
exist. Remove sensitive information from quoted logs before posting them; the Practice about keeping
private material out of public posts explains that check.

## Example

A proposal for a usage-feedback channel opens with two linked issues where real tasks exposed
defects that no fixture caught, quotes one sentence from each, and then lists five related issues
with their roles — two as recurrence evidence, three as prior decisions the proposal must respect.
The maintainer reads the links, sees the pattern is real, and starts the design discussion in the
first comment instead of asking for examples.
