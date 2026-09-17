---
anti_patterns:
  - description: The agent promotes an abstraction, fallback, or adjacent feature into committed work because it looks useful later or technically coherent, and records no finish condition, so nearby opportunities keep moving the completion point and the task never reaches a stable end.
    id: agentic-coding.planning.uncapped-scope-promotion
    name: Uncapped scope promotion
    severity: warn
applies_when: a plan is about to become committed work while some candidate items have no current reason, and adjacent improvements could extend execution without a recorded finish, defer, or replan boundary
id: agentic-coding.planning.decide-scope-and-stop-conditions
severity: warn
stage: planning
tech_stack:
  - agentic-coding
title: Decide Scope and Stop Conditions Before Work Begins
---

## When to apply

Apply when candidate work items are about to become the committed plan. This one decision fixes what
is committed, what is deferred, and when execution stops. If implementation has already revealed
facts that change scope or risk, replan from the observed facts instead. This Practice does not
decide how much validation depth a committed item deserves, or which values of an approved public
surface may be exposed.

## Guidance

1. List every candidate work item, including ideas the repository makes look cheap: an unused
   interface, a nearby hook, a nice-to-have refactor, or a generalization the loader already
   accepts.
2. Label each item required, optional, out of scope, or unresolved. Required work must support a
   current acceptance item, an evidenced risk, behavior already promised to callers, or an approved
   expansion. An item supported only by generic practice, possible future use, or visible output
   stays optional or out of scope and cannot block the required path. If the authority to decide is
   missing, mark the item unresolved and ask.
3. Write one observable finish condition for each required item: the behavior another person could
   check. If you cannot state it, return to the requirement instead of writing "until it looks
   good."
4. Record the deferred items by name in a defer list, so a nearby discovery made during execution
   has a recorded place to go instead of becoming new work.
5. Write the replanning signals: which changes in scope, risk, authority, cost, or evidence
   feasibility force revisiting this plan. Ordinary implementation detail is not a signal.

Apply the same admission rule to validation, authorization, retry, and fallback items: name the
reachable failure or explicit policy, the current protection, and the remaining gap. "Another layer
of safety" alone is not a gap, and a brief explanation settles a small change better than a separate
risk document.

Stop when every committed item carries a current reason and a finish condition, the defer list names
the adjacent opportunities you noticed, and another person could decide finish, defer, or replan
from what you recorded.

## Anti-pattern

A task requires installation from one configured repository registry, and failed jobs must send
email alerts. Because the loader already accepts a string, arbitrary file and network locators look
like a cheap future-proof extension; because an unused multi-channel interface exists, SMS and push
look nearly free. The agent commits all of it, never records when the registry install or the email
alert is finished, and each coherent-looking cleanup nearby — a plug-in registry, a discovery
mechanism, compatibility tests — extends the work further. The original task keeps moving and never
reaches a stable end, while the extra channels and locators create validation and security
obligations that no current requirement supports.

## Why

An optional idea is cheapest to defer while it is still a plan item; once code, tests, and consumers
depend on it, removal becomes a compatibility decision. A recorded finish condition and defer list
stop novelty and cleanup opportunities from redefining success, while explicit replanning signals
keep genuine new facts able to change the plan.

## Exceptions and boundaries

Incident response, safety containment, and research may use timeboxed or evidence-based stops, and
immediate containment can precede replanning when delay increases harm. A governing contract or an
evidenced security, privacy, data-integrity, compatibility, or compliance risk can require work the
feature request does not name; explain the actual exposure and consequence, because the category
label alone cannot promote hypothetical work into a requirement. Optional improvements may still be
recorded without becoming commitments.

## Example

A task adds one documented search filter, and the search module also exposes hooks for saved
searches and query suggestions. The candidate list contains the filter field, saved searches, query
suggestions, and a small cleanup of the filter parser. The agent labels the filter field required
(current acceptance), the parser cleanup optional, and saved searches and query suggestions out of
scope, recording both on the defer list. The finish condition reads: the filter produces correct
matching results and correct empty-result behavior for the documented query syntax. The replanning
signal reads: the filter requires a public index migration or invalidates the planned checks. The
deferred hooks now have a recorded place to go when they suggest themselves during implementation,
and the task ends when the finish condition holds.
