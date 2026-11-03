---
anti_patterns:
  - description: The agent promotes an abstraction, fallback, or adjacent feature into committed work because it looks useful later or technically coherent, and records no finish condition, so nearby opportunities keep moving the completion point and the task never reaches a stable end.
    id: agentic-coding.planning.uncapped-scope-promotion
    name: Uncapped scope promotion
    severity: warn
applies_when: committed work is about to begin and adjacent improvements could extend execution without a recorded finish, defer, or replan boundary, whether candidate items still lack admission reasons or the scope is already fixed
id: agentic-coding.planning.decide-scope-and-stop-conditions
severity: warn
stage: planning
tech_stack:
  - agentic-coding
title: Decide Scope and Stop Conditions Before Work Begins
---

## When to apply

Before starting work, agree what must be done, what can wait, and how you will know the task is
finished. This helps both when choosing tasks for a plan and when the requester has already fixed
the scope. If the scope is fixed, treat those tasks as required and start with their finish
conditions; do not reopen the decision about whether to include them.

If implementation has uncovered facts that change the scope or risk, revisit the plan from those
facts. Deciding how much verification a task needs, or which values an approved public interface
should accept, are separate decisions.

## Guidance

1. List the proposed work, including tempting additions that look cheap: an unused interface, a
   nearby hook, a small refactor, or extra inputs the loader could already accept.
2. Mark each item required, optional, out of scope, or unresolved. Required work must serve a
   current acceptance requirement, a risk backed by evidence, a promise already made to callers, or
   an approved extension. General advice, possible future use, or the chance to show more output is
   not enough to make an item required. Keep such ideas optional or out of scope, and do not let
   them block required work. If you lack authority to decide, mark the question unresolved and ask.
3. For each required item, say what another person could check to confirm it is finished. If you
   cannot say, clarify the requirement rather than writing "until it looks good."
4. Record postponed ideas by name so that rediscovering one while coding does not silently add it to
   this task.
5. Say which new facts would require a new plan: changes to scope, risk, authority, cost, or whether
   the planned verification is possible. Ordinary implementation details do not require replanning.

Use the same test before adding validation, authorization, retries, or fallbacks. Explain which
failure can occur or which policy requires them, what protection already exists, and what remains
unprotected. "Another layer of safety" does not identify a missing protection. For a small change, a
brief explanation is enough; do not create a separate risk document just for this.

Stop planning when every required item has a current reason and a checkable finish condition, the
postponed ideas are recorded, and another person could tell when to finish, defer work, or replan.

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

It is easier to postpone an idea before code, tests, and callers depend on it. After that, removing
it may break compatibility. Recording the finish conditions and postponed ideas keeps discoveries
and cleanup from moving the goalposts, while the stated reasons to replan leave room for genuine new
facts.

## Exceptions and boundaries

Incidents, safety containment, and research may stop at a time limit or after collecting specified
evidence. If waiting increases harm, contain it before revising the plan.

An applicable contract or an evidenced security, privacy, data-integrity, compatibility, or
compliance risk may require work the feature request did not mention. Explain the actual exposure
and consequence; naming a risk category is not enough to make hypothetical work required. You can
still record optional improvements without promising to implement them.

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
