---
anti_patterns:
  - description: The author removes repeated context because the README and neighboring Practices already explain it, leaving an individually retrieved entry with references and instructions that only make sense in the full Pack order.
    id: pack-creator.design.hidden-sequence-dependency
    name: Hidden Pack sequence dependency
    severity: warn
applies_when: a complete Practice draft is being reviewed, and its action may depend on Pack order, an earlier Practice, an unexplained local term, or source context that will not accompany retrieval
id: pack-creator.design.keep-each-practice-standalone
severity: warn
stage: design
tech_stack:
  - lorelum-pack-authoring
title: Make Every Practice Usable on Its Own
---

## When to apply

Read a Practice as if it were the only file returned for a request. Would the reader need an earlier
step, an unexplained term, a constraint, or a conclusion from elsewhere before acting? Do this once
the Practice has a clear question to answer and limits on its use. Check the whole entry here, not
just whether its Example supplies enough facts.

## Guidance

Read the Practice without its directory name, README, neighboring entries, or source open. Replace
phrases such as "as established above," "use the previous threshold," and unexplained local
shorthand with the minimum fact needed to decide. Include the trigger, action, direct reason,
stopping point, and material exception in the entry. Link detailed background and evidence rather
than copying a domain manual, but repeat decisive constraints that the action depends on. Stop when
a cold reader can explain when to use the Practice, what to do, and what not to assume.

## Anti-pattern

An incident-response Pack should help on-call engineers decide when and where to escalate an alert.
It follows the exact order of an internal runbook. To avoid duplication, its third Practice says,
"After applying the severity from Practice 2, use the earlier ownership rule and continue to
escalation." The README makes the sequence obvious, and the concise wording looks maintainable. When
the third entry is retrieved alone for an unowned database alert, the reader has neither the
severity definition nor the ownership condition and cannot act safely. The author should include the
decision-critical conditions in that Practice and leave only background detail in the linked
runbook.

## Why

Lorelum may retrieve one Practice without its neighbors. Hidden ordering turns valid content into
incomplete instructions precisely when selective retrieval is working as intended.

## Exceptions and boundaries

A Practice may cite a stable public standard, source document, or another entry for additional
depth. The citation must not carry a fact required for the immediate decision. Do not duplicate an
entire glossary or workflow in every file; explain only uncommon terms and constraints needed to use
this Practice correctly.

## Example

A data-retention Pack should help operators decide what scheduled deletion may safely remove. One
Practice covers backups that may still be under a legal hold. The entry defines a legal hold as a
recorded instruction to preserve specified data, states that the hold overrides the normal retention
deadline, tells the operator where the authoritative hold status comes from, and stops once
protected backups are excluded from the job. It links the full records policy for audit detail, but
a reader does not need another Practice or Pack order to make the deletion decision.
