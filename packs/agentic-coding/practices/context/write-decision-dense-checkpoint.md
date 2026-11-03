---
anti_patterns:
  - description: Preserving recent logs and file activity because they are easy to copy, while omitting the exact request, accepted decisions, required behavior still missing, and limits of completed checks, makes the next session continue from recency rather than facts.
    id: agentic-coding.context.recency-biased-checkpoint
    name: Checkpoint dominated by recent activity
    severity: info
applies_when: a long pause, context reduction, or session boundary is imminent, and the agent must create a durable checkpoint without carrying exploratory noise into the resumed task
id: agentic-coding.context.write-decision-dense-checkpoint
severity: info
stage: context
tech_stack:
  - agentic-coding
title: Write a Checkpoint That Preserves Decisions
---

## When to apply

You know a context reduction, long pause, or session change is coming, and the work will need to
resume afterward. Before that interruption, save a short record where the resumed task can read it,
choosing the facts it will need. If context has already been lost, do not reconstruct a checkpoint
from memory; reopen the request, files, and results instead.

## Guidance

1. Record the current user goal and exactly which request, accepted issue, specification, or plan
   defines the work.
2. Record accepted decisions and what they mean for the next step. For rejected options, keep the
   reason they must not be tried again rather than the whole discussion.
3. Record the first required behavior still unfinished, test or review results that still apply and
   the commit or file they checked, and remaining risks, blockers, and unconfirmed assumptions.
4. Say what to do next and why. Link to changed files and full logs instead of copying them.

Stop when someone who has not read the conversation can tell what to reopen, what is finished, what
is not, what they must not assume, and where to resume.

## Anti-pattern

The user asks only for diagnosis of an authorization failure. Near the context limit, the agent
copies recent command output, edited file names, and a promising cache fix into the checkpoint
because those details are easy to collect and feel concrete. It omits that implementation was not
authorized, the denial path is still unverified, and the cache explanation is only a hypothesis. The
resumed session is likely to start coding the guess.

## Why

The resumed session needs a short record of what controls the work and what remains, not a digest of
recent activity. Keeping the request, accepted decisions, missing behavior, and limits visible
prevents recent logs or an attractive hypothesis from steering the next action. Full evidence can
remain available through links.

## Exceptions and boundaries

When context is about to run out during an active incident or safety containment, write the minimal
recovery record first — current action, owner, containment or rollback state, and the next step —
execute the containment, and complete the full checkpoint once the incident is stable. Retain full
logs separately when incident response, audit, legal, or reproducibility requirements demand them;
the checkpoint should link to that evidence rather than replace it. Very short, stateless tasks may
need only one sentence. A checkpoint does not authorize a new Agent to trust another Agent's
conclusions without validation; that is a handoff boundary.

## Example

The user asks for a storage migration that can roll back without losing existing rows. Before
compaction, the agent records the accepted migration document, the decision to preserve the old
reader until rollback is proved, the files currently changed, and the result that forward migration
passes at the current commit. It states plainly that rollback with populated data has not been run,
links the full output, and records why two abandoned approaches would rewrite rows too early. The
next action is the populated-data rollback check, not implementation cleanup.
