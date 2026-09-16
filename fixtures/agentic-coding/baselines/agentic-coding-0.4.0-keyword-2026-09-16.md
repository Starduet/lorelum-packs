# Retrieval evaluation: agentic-coding-queries vs agentic-coding@0.4.0

- Generated: 2026-09-16T03:10:18+00:00  |  lore 0.1.0-alpha.1  |  mode(s): keyword, semantic  |  top-k threshold: 3
- Store: tmp\eval-store-040  |  Queries: 165 runnable, 0 skipped

## keyword

- Positive queries: top-1 86.9% (99 queries), top-3 92.9%
- Neighbor queries: expected selected top-1 54.5% (66 queries), in top-3 83.3%, trap top-1 (query selects the Practice it resembles) 19.7%

Positive queries that missed top-3 (rewrite-priority input):

| query | actual top-3 |
|---|---|
| `requirements.ground-user-goal.p3` | implementation.choose-smallest-sufficient-design, implementation.inspect-and-reuse-existing-capability, implementation.replan-on-material-drift |
| `requirements.resolve-source-authority.p1` | implementation.replan-on-material-drift, review.run-subtractive-review-before-commit, implementation.choose-smallest-sufficient-design |
| `requirements.define-acceptance-and-non-goals.p2` | implementation.inspect-and-reuse-existing-capability, planning.admit-only-currently-justified-work, review.run-subtractive-review-before-commit |
| `requirements.define-acceptance-and-non-goals.p3` | planning.define-stop-condition, recovery.validate-handoff-before-continuation, implementation.confirm-product-surface-expansion |
| `planning.admit-only-currently-justified-work.p2` | review.run-subtractive-review-before-commit, requirements.define-acceptance-and-non-goals, implementation.replan-on-material-drift |
| `implementation.limit-investigation-to-current-decision.p2` | verification.map-evidence-to-acceptance, testing.justify-regression-protection, implementation.replan-on-material-drift |
| `verification.map-evidence-to-acceptance.p3` | implementation.choose-smallest-sufficient-design, review.run-subtractive-review-before-commit, implementation.replan-on-material-drift |

Most confused neighbor selections (queries worded near 'resembles' that selected 'actual top-1' instead of the expected neighbor):

| resembles | actual top-1 selection | count |
|---|---|---|
| `planning.map-plan-to-user-capability` | `implementation.make-recovery-behavior-explicit` | 2 |
| `testing.justify-regression-protection` | `testing.justify-regression-protection` | 2 |
| `requirements.ground-user-goal` | `requirements.ground-user-goal` | 1 |
| `requirements.define-acceptance-and-non-goals` | `requirements.define-acceptance-and-non-goals` | 1 |
| `planning.plan-sufficient-evidence` | `requirements.define-acceptance-and-non-goals` | 1 |
| `planning.define-stop-condition` | `planning.define-stop-condition` | 1 |
| `implementation.limit-investigation-to-current-decision` | `implementation.limit-investigation-to-current-decision` | 1 |
| `implementation.limit-investigation-to-current-decision` | `implementation.validate-at-the-owning-boundary` | 1 |

## semantic: DEGRADED — not evaluated on this machine

Index preparation failed with `embedding.deadline-exceeded` (The embedding operation exceeded its deadline.). No semantic numbers below; run on a machine where the semantic index builds to collect them.

> Evaluation-only evidence: observed retrieval selection for the fixture queries on one machine and one Pack revision. It is not a claim about content quality, other queries, other modes that were unavailable, or downstream Agent behavior.
