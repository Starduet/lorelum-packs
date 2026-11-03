---
anti_patterns:
  - description: Providing useful considerations and background without an observable action or stopping point, encouraging the reader to keep exploring after enough evidence exists.
    id: pack-creator.authoring.guidance-without-decision
    name: Guidance that never reaches a decision
    severity: warn
applies_when: a Practice trigger is already clear, but its Guidance does not yet tell the reader what to do, what output to produce, and when the decision is complete
id: pack-creator.authoring.write-concrete-guidance-and-stop-condition
severity: warn
stage: authoring
tech_stack:
  - lorelum-pack-authoring
title: Give Concrete Actions and a Clear Stop
---

## When to apply

Once you know what question a Practice answers and when readers need it, write Guidance that tells
them what to do and how to know they have done enough. Do not use this section to reconsider when
the entry should be found or whether its failure scenario is realistic.

## Guidance

Tell readers what to inspect, compare, choose, record, or change. Explain which facts they need,
what they should have decided or produced at the end, and when they can stop investigating or
expanding the work. Remove advice that would not change that result. Stop when a reader can follow
the Guidance and show an observable result without inventing an extra workflow.

## Anti-pattern

An operations Pack draws from incidents where emergency failover settings differed across regions.
The author gives a thorough list of resilience principles, topology questions, and possible tools
because flexibility seems safer than prescribing an order. A capable operator can study every item
and still not know which configuration to compare or when the failover review is complete, so
investigation expands while the inconsistent setting remains.

## Why

Guidance changes behavior only when it tells the reader what result completes the decision. Without
a stopping point, even relevant advice can delay action, expand the work unnecessarily, or lead
readers to do different things.

## Exceptions and boundaries

An exploratory Practice may end by naming the evidence still missing or asking someone to make a
decision rather than choosing a technical solution. Safety and incident response may require
immediate containment before full analysis. In either case, say what must be handed over or brought
under control before the reader stops following this Practice.

## Example

A frontend Pack helps teams keep product colors consistent. For a proposed one-off color, the
Guidance says to inspect the semantic theme tokens and representative call sites, choose an existing
token when its meaning matches, or record the unmet semantic need for a new token. It stops once one
choice and its affected component are named; it does not require cataloging every color in the
application.
