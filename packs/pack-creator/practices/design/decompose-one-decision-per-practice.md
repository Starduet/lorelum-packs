---
anti_patterns:
  - description: The author keeps several decisions together because one guide or repository module discusses them together, producing a polished Practice that is too broad for focused retrieval and too costly for readers who need only one choice.
    id: pack-creator.design.source-section-as-practice-boundary
    name: Source section used as the Practice boundary
    severity: warn
applies_when: a candidate Practice contains several actions or rules that could be needed by different queries, and the author must decide whether to split the content
id: pack-creator.design.decompose-one-decision-per-practice
severity: warn
stage: design
tech_stack:
  - lorelum-pack-authoring
title: Decompose Guidance into One Decision per Practice
---

## When to apply

If one draft tells readers to make several choices, ask whether they will always need those actions
together. Split choices that can arise separately so readers can find each on its own. Once the
files are separate, check whether their triggers still compete for the same request.

## Guidance

Look at what the draft asks the reader to decide or do. If they could reasonably need one action
without the others, give each decision its own trigger, guidance, explanation of what can go wrong,
and limits. Keep shared evidence in provenance or links; a source chapter need not become one file.
Put pieces back together if they offer no independent choice and merely repeat setup. Stop when each
Practice helps with one decision without bringing along unrelated guidance.

## Anti-pattern

A frontend-performance Pack should help teams prevent slow page loads. One internal guide covers
image sizing, cache policy, bundle splitting, and performance measurement in a single chapter, so
keeping them together preserves context and avoids repeated citations. The author creates "Optimize
Page Performance" with all four actions. A reviewer deciding whether an image variant is needed
receives cache and bundler guidance, while a query about cache policy may not retrieve the broad
title at all. The better design splits the independently triggered decisions and keeps the shared
guide as provenance.

## Why

Practices that each answer one question give retrieval a clear target and let readers act without
unrelated instructions. Source structure describes how knowledge was documented, not necessarily how
decisions arise.

## Exceptions and boundaries

Steps that always occur as one decision and would be misleading alone can remain together. Do not
split a Practice merely to shorten it or create one file per paragraph. A multi-step check may still
be atomic when every step is required to answer the same question.

## Example

A database-change Pack should help engineers make schema changes that can recover without losing
existing data. One draft says to choose an online migration method, define rollback behavior, and
verify populated-data rollback before release. The author finds three distinct moments: selecting
the migration approach, deciding what rollback must preserve, and assessing whether evidence
supports release. Each can arise independently and has a different failure, so the author creates
separate Practices. The vendor migration guide remains a shared source rather than forcing the three
decisions back into one file.
