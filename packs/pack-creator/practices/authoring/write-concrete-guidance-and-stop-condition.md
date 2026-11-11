---
anti_patterns:
  - description: Providing considerations and background without an actionable decision, or omitting a stopping point when it is needed to prevent unnecessary investigation.
    id: pack-creator.authoring.guidance-without-decision
    name: Guidance that never reaches a decision
    severity: warn
applies_when: a Practice does not yet make the decision or action clear, or readers need a stopping point to avoid unnecessary investigation
id: pack-creator.authoring.write-concrete-guidance-and-stop-condition
severity: warn
stage: authoring
tech_stack:
  - lorelum-pack-authoring
title: Make Guidance Actionable and Bound Work When Needed
---

## When to apply

Once you know what question a Practice answers, make the relevant action or decision clear. Specify
when to stop if that helps readers avoid unnecessary investigation or expansion.

## Guidance

Tell readers what to inspect, compare, choose, record, or change as the decision requires. Include
the necessary facts and expected result; add a stopping point when it materially bounds the work.
Remove advice that does not help the reader make the decision.

## Anti-pattern

An operations Pack draws from incidents where emergency failover settings differed across regions.
The author gives a thorough list of resilience principles, topology questions, and possible tools
because flexibility seems safer than prescribing an order. A capable operator can study every item
and still not know which configuration to compare or when the failover review is complete, so
investigation expands while the inconsistent setting remains.

## Why

Actionable guidance helps readers make the intended decision. Where investigation might otherwise
expand unnecessarily, a stopping point can help readers know when enough evidence exists.

## Exceptions and boundaries

An exploratory Practice may identify missing evidence or ask someone to make a decision rather
than choosing a technical solution. Safety and incident response may require immediate containment
before full analysis. Specify handoff or containment conditions when they matter to the decision.

## Example

A frontend Pack helps teams keep product colors consistent. For a proposed one-off color, the
Guidance says to inspect the semantic theme tokens and representative call sites, choose an existing
token when its meaning matches, or record the unmet semantic need for a new token. It stops once one
choice and its affected component are named; it does not require cataloging every color in the
application.
