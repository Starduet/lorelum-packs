---
anti_patterns:
  - description: The author treats broad subject coverage as success because it mirrors the available sources, producing a useful-looking reference collection that does not help a reader make a better choice at a real decision point.
    id: pack-creator.discovery.topic-list-as-pack-outcome
    name: Topic list used as the Pack outcome
    severity: warn
applies_when: a new Pack is described by a domain, document collection, or list of topics, but the author has not stated whose recurring decisions the collection should improve
id: pack-creator.discovery.define-pack-decision-outcome
severity: warn
stage: discovery
tech_stack:
  - lorelum-pack-authoring
title: Define the Decisions the Pack Should Improve
---

## When to apply

If you can describe the proposed Pack only as "PostgreSQL operations" or "frontend accessibility,"
decide who will use it and which recurring choices it should help them make before choosing
Practices. First establish what the collection should help readers do better; then work out when
they will need that help.

## Guidance

Write one sentence saying who the Pack is for, which decisions they repeatedly face, and how it
should help them choose. Test each candidate topic against that sentence: if knowing the topic would
not change one of those decisions, it does not belong merely for completeness. Narrow the scope or
separate unrelated groups of decisions instead of hiding them under a broad domain name. Stop when
the outcome sentence lets you include useful guidance and reject topics that look impressive but do
not help the intended reader choose.

## Anti-pattern

A team wants a database-operations Pack that reduces avoidable production incidents. The source
repository is organized into backup, replication, indexing, and configuration chapters, so copying
that table of contents looks comprehensive and easy to review. The author makes one Practice for
every chapter and calls the Pack complete. A database operator asking whether a risky schema change
can be rolled back receives definitions from several chapters but no guidance for that decision. The
better outcome would name the operational choices the Pack should improve, then include source
topics only when they support those choices.

## Why

Knowing which decisions the Pack should improve gives you a reason to include or exclude content. A
topic list can grow indefinitely and still offer no help when a reader has to choose.

## Exceptions and boundaries

Early research may begin with a provisional outcome and refine it as real needs appear. A Pack may
serve several related decision families when the relationship is explicit; it should not force
unrelated audiences into one collection. This Practice does not choose individual `applies_when`
text or require a fixed number of Practices.

## Example

An accessibility Pack is intended for frontend reviewers. The author states: "Help reviewers decide
whether a proposed interface change preserves keyboard use, focus visibility, and understandable
control names before approval." Color theory and general visual branding may be useful subjects, but
they do not enter this Pack unless they change one of those review decisions. The outcome is
specific enough to guide discovery without dictating the final Practice list.
