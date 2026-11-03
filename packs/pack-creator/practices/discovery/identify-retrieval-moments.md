---
anti_patterns:
  - description: The author uses policy chapters or repository folders as retrieval moments because they preserve source organization, leaving real decision queries scattered across several topics or unmatched by any Practice.
    id: pack-creator.discovery.source-outline-as-retrieval-map
    name: Source outline used as the retrieval map
    severity: warn
applies_when: the Pack outcome is known and the author is about to select Practices without first identifying the recurring moments when a reader would benefit from the collection
id: pack-creator.discovery.identify-retrieval-moments
severity: warn
stage: discovery
tech_stack:
  - lorelum-pack-authoring
title: Identify When the Pack Should Be Retrieved
---

## When to apply

Once you know which decisions the Pack should improve, look for the points in the reader's work
where help could change a choice, approval, diagnosis, or report. Do this before turning sources
into individual Practices. You are finding when readers need help, not yet writing each Practice's
exact trigger.

## Guidance

Follow the work where those decisions arise. List the points where a reader is about to decide or
act, including the conditions that make help useful. Questions, review comments, incidents, and near
misses often reveal needs that a source's table of contents misses. Merge entries that describe the
same situation, remove ones that do not serve the Pack's purpose, and flag important decisions where
guidance is missing and mistakes would have serious consequences. Do not force the work into a fixed
lifecycle. Stop when the important decisions are covered, without deciding the exact files yet.

## Anti-pattern

A privacy-compliance Pack should help product teams make correct data-handling choices. The accepted
policy is divided into retention, consent, access, and vendor chapters, so using those headings as
the retrieval map preserves authority and makes provenance easy. Real questions arrive instead while
adding a database field, designing account deletion, or approving an analytics vendor. Each question
crosses several chapters, and queries for those moments retrieve broad policy summaries rather than
a usable decision. The better map starts from those recurring product choices and links the relevant
policy facts afterward.

## Why

Retrieval happens from the reader's current situation, not from the author's source navigation.
Mapping those situations exposes missing help before content is divided into files.

## Exceptions and boundaries

Some Packs support event-driven work, ongoing review, or rare high-risk decisions rather than a
linear workflow. Their moment map should reflect that reality. A source chapter may also be a
genuine retrieval moment, but only when readers actually frame their decision that way. This
Practice does not define one Practice's final trigger wording.

## Example

An on-call operations Pack aims to improve decisions that prevent noisy alerts from becoming missed
incidents. The author identifies three useful moments: before changing an alert threshold, when
repeated alerts have no clear owner, and before closing an incident with muted notifications still
active. These moments guide later Practice discovery. The author does not add a Practice for every
monitoring-tool menu or assume that alert creation, response, and closure must form a universal
workflow.
