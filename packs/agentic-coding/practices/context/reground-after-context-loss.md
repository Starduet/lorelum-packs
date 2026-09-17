---
anti_patterns:
  - description: Continuing from a coherent summary because it offers a fast route back into coding can preserve stale assumptions, obsolete scope, and inflated status that the current request, changed files, or test results contradict.
    id: agentic-coding.recovery.summary-as-authority
    name: Summary treated as fact
    severity: warn
applies_when: work is resuming after context reduction, interruption, or a same-agent session pause, and the agent is about to edit or report status using a summary that has not been checked against the current request, files, and results
id: agentic-coding.recovery.reground-after-context-loss
severity: warn
stage: recovery
tech_stack:
  - agentic-coding
title: Reground After Context Loss
---

## When to apply

Apply when the same task or Agent resumes after compaction, interruption, or a long pause and only a
summary or partial memory remains. Do this before editing, expanding the plan, or reporting
progress. Before a known pause, write a checkpoint instead. When the conclusions came from another
Agent or contributor, validate that handoff rather than using this same-session recovery rule.

## Guidance

1. Treat the summary only as an index to find source material; treat none of its conclusions as
   facts.
2. Reopen the current user request, accepted issue or specification, relevant plan and decisions,
   current branch and diff, and recorded test or review results.
3. Check every summary claim the next action depends on against those items.
4. Write down the current goal, what changes are allowed, the first required behavior still missing,
   which results still apply to the current files, and the next justified action; reduce any
   completion statement that lacks proof.

Stop when those facts are clear; do not reread the entire project when a smaller set answers the
next decision.

## Anti-pattern

The user asks for installation from a real remote repository. After compaction, the summary says
"installation is complete; only cleanup remains." The repository has green unit tests, so starting a
refactor feels like useful progress. Reopening the accepted issue and current diff shows that only a
fake transport was tested and the real remote path was never run. The summary has turned partial
implementation into completion.

## Why

Summaries preserve continuity, but they can omit the requirement, file change, or failed check that
matters most. Reopening those concrete sources prevents an omission from becoming the basis for more
work or an inaccurate progress report.

## Exceptions and boundaries

A trivial task with one output may need only a quick comparison with the current file. An earlier
result may remain usable when it tested the same files and conditions. When the user request,
accepted issue, and specification conflict, pause and ask which controls the work instead of
choosing the one that matches the summary. Claims supplied by another Agent require handoff
validation.

## Example

The user asks the parser to reject bad tokens and recover after a truncated declaration. After
resuming the refactor, the agent reopens that requirement, the current diff, and the recorded
results. Valid syntax and bad-token rejection passed on the current commit, but no test truncates a
declaration. The agent reports "core parsing verified; truncated-input recovery not checked" and
runs that missing case next instead of starting cleanup.
