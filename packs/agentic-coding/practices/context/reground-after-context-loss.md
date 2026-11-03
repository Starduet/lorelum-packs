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
title: Recheck Original Sources After Context Loss
---

## When to apply

You return to the same task after compaction, an interruption, or a long pause, with only a summary
or partial memory of the work. Recheck the sources before editing, expanding the plan, or reporting
progress. If the pause is still ahead, write a checkpoint instead. If the conclusions came from
another agent or contributor, validate that handoff rather than treating this as same-session
recovery.

## Guidance

1. Use the summary to find the original material, not as proof that its conclusions are true.
2. Reopen the current user request, accepted issue or specification, relevant plan and decisions,
   current branch and diff, and recorded test or review results.
3. Check each statement in the summary that your next action depends on against those sources.
4. Write down the current goal, allowed changes, first required behavior still missing, which
   results still apply to the current files, and what to do next. Correct any completion statement
   that claims more than the evidence proves.

Stop when those facts are clear. If a few sources answer the next question, do not reread the entire
project.

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
