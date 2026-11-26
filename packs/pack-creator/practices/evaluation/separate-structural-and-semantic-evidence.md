---
anti_patterns:
  - description: Using valid files, complete catalogs, or passing fixture checks to claim useful guidance or improved Agent behavior turns evidence about structure into a broader claim it never tested.
    id: pack-creator.evaluation.structural-pass-as-semantic-proof
    name: Structural pass reported as semantic quality
    severity: warn
applies_when: the author is reviewing Pack readiness or reporting evaluation results and must decide what schema checks, human content review, retrieval runs, and downstream Agent tasks each actually prove
id: pack-creator.evaluation.separate-structural-and-semantic-evidence
severity: warn
stage: evaluation
tech_stack:
  - lorelum-pack-authoring
title: Keep Different Kinds of Pack Evidence Separate
---

## When to apply

Before saying a Pack is ready because several checks passed, ask what each check actually showed. A
valid file, a domain reviewer's approval, the right Practice appearing in a query, and an Agent
using it well are different results. Keep those differences visible when reporting them together.

## Guidance

Keep the results in separate groups. Structural checks can show that frontmatter is valid, paths are
safe, IDs are unique, and the catalog is covered. Human content review checks whether the guidance
and any decision-relevant context are correct for the domain, not whether every entry contains a
fixed list of elements. Retrieval runs show which Practices a particular system selected for stated
queries; selection alone does not establish that the guidance improves decisions.

To assess added value, compare representative tasks using the same strong model without the Pack
and with the relevant Practices, keeping other conditions comparable. Record the tasks, model, Pack
revision, conditions, and observed decision outcomes, including regressions. For each conclusion,
say which result supports it and exactly what was observed. If a stronger claim was not tested,
keep the wording narrow. Do not average these groups into a quality score unless a separate
evaluation contract defines that score.

## Anti-pattern

A team creates an accessibility Pack. The repository’s schema validator passes, all catalog IDs have
fixture rows, and the fixture files parse. Because the release checklist needs a simple answer and
the structural results are objective, the author reports that the Pack “has complete accessibility
guidance and retrieves correctly.” No accessibility reviewer has checked the advice, no retrieval
system has run the queries, and no Agent task has used the guidance. The neat structural dashboard
encourages a claim three layers broader than the evidence.

## Why

Each evidence type answers a different question. Mixing them hides what remains unknown and makes
later reviewers unable to tell whether a failure comes from file structure, content, selection, or
downstream use. Separate claims allow progress at one layer without pretending the others have
passed.

## Exceptions and boundaries

One experiment may produce evidence for more than one layer when it directly observes each one, but
record the observations separately. Expert review is still judgment, not retrieval behavior. A
successful downstream task may include retrieval evidence, yet one task does not prove broad content
coverage. This Practice classifies evidence; it does not prescribe a particular evaluation tool or
fixed benchmark size.

## Example

A privacy Pack revision passes schema and unique-ID checks. Two privacy engineers then review the
data-deletion Practices and find one exception too broad. After correction, a retrieval run shows
that deletion queries select the intended Practice while retention queries select its neighbor. A
small Agent exercise later follows the retrieved deletion guidance but misses a repository-specific
approval step. The author reports four separate findings—structure passed, reviewed content was
corrected, sampled retrieval distinguished the neighbors, and downstream behavior still has one
gap—instead of calling the Pack simply “validated.”
