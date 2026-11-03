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

Use this when a developer asks what you found, what you recommend, what changed, or where the work
stands. Answer that question before recounting the investigation. Put any limitation that changes
the answer beside it, so the reader does not have to assemble the conclusion from your work log.

## Guidance

1. Start with the answer the developer needs. Give a cause only if it is established; otherwise say
   what is known and what is not. For a design choice, recommend an approach and explain the
   decisive tradeoff. For progress, say what is done and what is blocked. If several tasks are at
   different stages, report them separately rather than calling the whole batch "mostly complete."
2. Keep a limitation beside the claim it changes. A passing local check does not establish an
   untested browser flow or production behavior. Use the supported result and important remaining
   issues already established for the task; do not invent a list of everything that was not tested.
3. Add the explanation and evidence needed to judge the answer. Say how the important change affects
   behavior, and give the relevant file, command, environment, observation, or source when it helps
   someone check it. If the opening already states the mechanism, later details should add evidence
   or explain a necessary distinction, not describe the same mechanism again. Preserve conditions,
   comparison bases, units, counterevidence, and uncertainty that affect the conclusion.
4. Finish when the question is answered, its basis is clear, and any necessary action is stated. Do
   not repeat the answer as a closing summary or add a rollout plan or next-step list that the
   question does not need. Explain a limitation once unless another claim would otherwise mislead.
   Leave out investigation chronology, internal labels, and generic disclaimers. Use headings only
   when they help the reader find different parts of a longer answer; a one-line answer needs none.

The report is ready when the reader can find the answer, the reason to believe it, and the limits
that matter without piecing together or rereading the same information.

## Anti-pattern

Asked whether a reconnect fix is ready, the agent lists searches, files, and passing unit tests,
then says "sync is fixed," with the untested browser path at the bottom. Moving the work log under
headings does not repair the buried answer. The useful opening is that local queued-edit replay
works in the observed case, but browser reconnect has not been checked, so that evidence does not
yet establish readiness for the developer's intended use.

## Why

Developers use the conclusion to decide whether to review, merge, release, investigate, or choose
another approach. Putting the answer and its important limitation first lets the reader judge the
result without having to retrace the investigation.

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
