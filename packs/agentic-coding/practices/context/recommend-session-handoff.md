---
anti_patterns:
  - description: Carrying low-value history into later work, then replacing it with a repetitive handoff that revives obsolete decisions or invents project locations from the current environment.
    id: agentic-coding.context.history-obscures-current-task
    name: Historical context obscures the current task
    severity: warn
applies_when: most accumulated history has little value for the intended continuation or is distorting current decisions, and the agent must decide whether to suggest a fresh conversation for ongoing work or the next phase
id: agentic-coding.context.recommend-session-handoff
severity: info
stage: context
tech_stack:
  - agentic-coding
title: Recommend a Fresh Session When History Adds Little Value
---

## When to apply

The conversation has moved on, but most of its history is about finished investigations, logs, or
plans that no longer apply. Suggest a fresh session when a concise handoff could preserve what the
ongoing work or agreed next phase needs. You need not wait for a mistake; old directions may already
be competing with accepted decisions. If the move is already decided and you only need to choose
what to record, write a checkpoint.

## Guidance

1. Establish what will continue: remaining work and agreed next phases. Select the facts and exact
   requirements that determine its inputs, promised behavior, data handling, conditional outcomes,
   and evidence to be collected or reused. Keep their qualifications and whether they were accepted,
   proposed, or still uncertain. Do not summarize every topic. Leave unrelated and superseded
   history behind, and correct known departures from the agreed direction. If the next focus has not
   been chosen, say that; do not choose it through the handoff.
2. Recommend moving when a short record can replace substantial irrelevant history or stop old
   directions interfering. Do not wait for errors or count turns. Keep working if the history is
   still useful and causes no interference, or if the work is ending with nothing to continue.
3. Before writing the overview, make a drafting list showing where each selected source clause will
   go: directly in the handoff, or at an exact source location to read before a specified action. Do
   not include this drafting list in the handoff itself.

   Account for each independent obligation and each conditional branch, not just the topics.
   Data-handling rules and credential-storage limits cannot both disappear into the word "privacy."
   Keep the smallest complete clause, including its conditions, exceptions, outcome, and decision
   status. Quote it if paraphrasing could change what it requires or permits; do not quote whole
   groups of rules. Distinguish accepted requirements, proposals, and hypotheses: agreeing to
   "continue discussing" something does not approve it.

   For experimental evidence, include the controls on how the experiment was run as well as its
   results and caveats in the drafting list. A procedure needed later can remain at a precise,
   accessible source location, provided that location preserves its rules and status. A document
   name or a link to the whole history is not enough. If no usable reference exists, include the
   necessary clauses without the surrounding discussion. Redact sensitive values.

4. Write one compact record of the goal, current state, decisions, limits of the evidence, next
   actions, and necessary source references. Keep short constraints in the main text. Add detail to
   consult on demand only when it is essential and cannot be referenced elsewhere; do not create
   another summary for every topic. State each fact once and have the opener refer to this record.

   Say when current facts are unknown rather than repeating outdated snapshots. For adjacent tasks,
   retain dependencies, not plans or an inventory of what you left out. Keep a rejected option's
   reason only if it still limits a choice. Omit historical numbers, directory inventories, and
   debugging chronology that would not change the next decision.

5. Keep historical paths exactly as supplied. Use an absolute project root only if the source or an
   explicit check established it for that project; your current working directory is not evidence.
   If the root is unknown, keep the relative path and say the root is unknown instead of guessing.
   The actual location of a handoff you just created is valid new information. Distinguish that
   location from historical artifact locations, and leave out unrelated environment or test-harness
   details.
6. Compare every source clause in your drafting list with the written handoff or its exact required
   reading location. Check included and excluded inputs, independent obligations, conditions,
   exceptions, outcomes, and experimental method controls, with their original decision status. A
   topic label, "preserve the contract," or an optional general source index does not preserve a
   missing rule.

   Remove material that changes no continuation decision, required behavior, or usable first action.
   Do not cut a fact that controls the work just to shorten the file. At a stable point in the work,
   explain why moving helps and provide the handoff and a ready-to-paste opener.

Stop when the user can resume from the record. If the user stays in the current session, continue
working; suggest a move again only after a material change.

## Anti-pattern

After a long gateway design discussion, implementation needs only the accepted behavior,
constraints, and relevant files. The agent waits for a mistake before suggesting a restart. Its
eventual handoff repeats the same design under background, status, and a full opening prompt, lists
rejected designs as open choices, and prefixes historical relative paths with its current directory.
The new session inherits extra reading and an unsupported project location.

## Why

History can add reading cost and compete with current instructions before visible drift occurs. A
handoff helps only when it preserves the controlling information without recreating that history or
filling gaps with the writer's environment.

## Exceptions and boundaries

Relevance, not length or coherence alone, guides the move. Keep working if preparing and loading a
handoff adds more effort than it removes; a completed phase can still be a useful boundary for the
next one. Independently pasted prompts need enough context or a usable shared reference. Remove
repetition before cutting a necessary constraint; no fixed word limit proves sufficiency. Shorter
text alone does not prove lower total cost or better downstream execution.

## Example

The user finishes a gateway design and asks to implement it. Most history concerns tokenizer trials
and a rejected text-type allowlist; no mistake has occurred. The agent records the accepted byte
estimate, reservation/reconciliation behavior, and known-file-payload exclusion while retaining
other content. It states once that implementation is unverified and retains the allowlist's
undercounting reason. A historical path such as src/estimate.ts stays relative when its project root
is unknown. The agent saves the handoff, gives its actual location, and supplies a short
implementation opener that reads it rather than repeating the discussion.
