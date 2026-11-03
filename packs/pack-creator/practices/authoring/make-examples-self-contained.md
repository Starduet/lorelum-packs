---
anti_patterns:
  - description: Saving space by referring to familiar incidents or internal names, leaving a retrieved example unable to explain the decision outside its original authoring context.
    id: pack-creator.authoring.example-requires-hidden-context
    name: Example that assumes private history
    severity: warn
applies_when: an Example depends on names, incidents, policies, or relationships that a reader cannot infer from the retrieved Practice itself
id: pack-creator.authoring.make-examples-self-contained
severity: warn
stage: authoring
tech_stack:
  - lorelum-pack-authoring
title: Make Each Example Understandable on Its Own
---

## When to apply

A reader should understand the Example without attending the original meetings or opening source
documents and earlier Practices. While writing or rereading it, supply the facts needed to follow
one correct application. Check this scenario on its own; the rest of the Practice must also be
reviewed for hidden dependencies.

## Guidance

State the Pack goal relevant to the scenario, the source or system facts that constrain the choice,
the plausible alternative, and why the selected action is better. Replace unexplained internal names
with what each person or system does and how they relate to the choice. Include only facts that
change the decision. Stop when a reader seeing the Example for the first time can retell the
request, constraint, choice, and result without asking what a local acronym or past incident means.

## Anti-pattern

A security Pack is based on an outage in which a message broker, not the application, owned retry
timing. Reviewers know it as the Omega incident, so the author writes, "As in Omega, keep the owner
in the right layer." The reference feels concise and preserves team history, but a new engineer
cannot tell what was owned, which layer made the wrong choice, or how to apply the lesson to another
broker.

## Why

Lorelum may retrieve one Practice far from its original source context. Missing relationships force
the reader to guess, and that guess can reverse the intended decision even when the example sounds
familiar to its author.

## Exceptions and boundaries

Public standards and universally understood terms may be named directly when their relevant rule is
also stated. Do not reproduce confidential incident details; anonymize names while preserving roles,
constraints, and causality. Extra chronology or decorative data should be removed when it does not
affect the choice.

## Example

A compliance Pack helps importers preserve valid marketing consent. The source policy requires both
the time and source of consent, while the CRM accepts blank values. Rather than defaulting missing
fields to import time, which would create false evidence, the Example shows the importer
quarantining incomplete records for review. The policy fact, tempting shortcut, and correct boundary
are all present.
