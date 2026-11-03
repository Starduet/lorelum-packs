---
anti_patterns:
  - description: Recounting searches, edits, internal classifications, or successful checks before stating the engineering conclusion and the limitation that changes the developer's next decision.
    id: agentic-coding.delivery.conclusion-after-work-log
    name: Conclusion hidden behind the work log
    severity: warn
applies_when: an agent is reporting a diagnosis, design recommendation, implementation result, or current progress to a developer, and the conclusion or important limitation is buried behind investigation history or implementation detail
id: agentic-coding.delivery.lead-with-engineering-conclusion
severity: warn
stage: delivery
tech_stack:
  - agentic-coding
title: Give the Developer the Conclusion First
---

## When to apply

Use this when deciding how to report engineering work to a developer. Say what the investigation
found, which approach you recommend, what changed, or what is still blocking the work before
recounting the details. Keep a limitation that changes that conclusion beside it. The reader should
not have to reconstruct the answer from your work log.

## Guidance

1. Answer the developer's actual question in a short opening paragraph. Report a cause only when
   established; otherwise state what is known and what remains unknown. For a design discussion,
   give the recommendation and decisive tradeoff. For unfinished work, give the current result or
   blocker rather than a premature completion claim.
2. Keep the scope or unresolved condition that changes the next decision in that opening. A local
   check, an untested browser flow, and a production result are not interchangeable. Use the
   supported claim and material remaining issues already established for this task; do not add a
   generic list of everything that was not tested.
3. Follow with the reasons, changes, and evidence the developer needs to judge that answer. Connect
   each important change to its effect. Name the relevant file, command, environment, observation,
   or source when it makes the result checkable. Preserve conditions, comparison bases, units,
   counterevidence, and uncertainty that affect the conclusion.
4. Stop after the necessary explanation and actionable remaining work. Explain each limitation once
   unless a different claim needs it repeated. Drop process chronology, internal labels, generic
   disclaimers, and repeated conclusions. A one-line engineering answer needs no report headings; a
   complex recommendation needs its reasons, not an unsolicited rollout plan.

Stop when the first paragraph lets the developer understand the result and whether they can act, and
the rest makes its basis and important limits easy to find.

## Anti-pattern

Asked whether a reconnect fix is ready, the agent lists searches, files, and passing unit tests,
then says "sync is fixed," with the untested browser path at the bottom. Moving the work log under
headings does not repair the buried answer. The useful opening is that local queued-edit replay
works in the observed case, but browser reconnect has not been checked, so that evidence does not
yet establish readiness for the developer's intended use.

## Why

Developers use the conclusion to decide whether to review, merge, release, investigate, or choose
another approach. Putting the answer and its controlling limit first makes the engineering judgment
visible without asking the reader to replay the investigation.

## Exceptions and boundaries

Respect a requested format or an interactive debugging sequence. Put an urgent safety action before
explanation when delay would cause harm. This is engineering collaboration, not a rule for unrelated
everyday advice or a mandatory report template.

`agentic-coding.delivery.claim-only-supported-outcome` decides what the evidence supports;
`agentic-coding.delivery.report-material-residuals` decides which remaining issues matter. This
Practice arranges that justified content rather than establishing facts or adding disclosure
requirements. Use `agentic-coding.delivery.explain-engineering-work-plainly` when the order is clear
but the wording still hides the mechanism.

## Example

A draft says "first I traced acknowledgments, then updated the state handler, then checked saves."
The observed result is that edits made after revision 12 remain pending when revision 12 is
acknowledged; the browser refresh path has not been checked. Lead with "Newer edits now remain
pending when an older save finishes. The focused revision-12 case passes; browser refresh is still
unverified." Then explain the revision comparison and give the relevant evidence, without calling
all autosave behavior verified.

Read the
[Chinese engineering before-and-after examples](resource:references/engineering-communication.md)
when comparing a report draft with its source facts. The examples are supplementary, not a template.
