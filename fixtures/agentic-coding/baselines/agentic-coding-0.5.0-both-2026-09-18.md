# Retrieval evaluation: agentic-coding-queries vs agentic-coding@0.5.0

- Generated: 2026-09-18T02:49:32+00:00  |  lore 0.1.0-alpha.2  |  mode(s): keyword, semantic  |  top-k threshold: 3
- Store: tmp\eval-store-050  |  Queries: 166 runnable, 0 skipped
- Install source: `Starduet/lorelum-packs` fork Registry (pre-merge evaluation), ref `agentic-coding-v0.5.0` @ `449da50`, tree identical to the PR branch

## keyword — gate PASSED (positive top-3 100.0% vs fixture minimum 90.0%)

- Positive queries: top-1 96.0% (100 queries), top-3 100.0%
- Neighbor queries: expected selected top-1 62.1% (66 queries), in top-3 90.9%, trap top-1 (query selects the Practice it resembles) 19.7%

Most confused neighbor selections (queries worded near 'resembles' that selected 'actual top-1' instead of the expected neighbor):

| resembles | actual top-1 selection | count |
|---|---|---|
| `requirements.ground-user-goal` | `requirements.ground-user-goal` | 1 |
| `requirements.define-acceptance-and-non-goals` | `requirements.define-acceptance-and-non-goals` | 1 |
| `planning.decide-scope-and-stop-conditions` | `planning.decide-scope-and-stop-conditions` | 1 |
| `planning.decide-scope-and-stop-conditions` | `implementation.replan-on-material-drift` | 1 |
| `planning.plan-sufficient-evidence` | `requirements.define-acceptance-and-non-goals` | 1 |
| `implementation.limit-investigation-to-current-decision` | `implementation.limit-investigation-to-current-decision` | 1 |
| `implementation.limit-investigation-to-current-decision` | `implementation.validate-at-the-owning-boundary` | 1 |
| `implementation.surface-unconfirmed-assumptions` | `implementation.surface-unconfirmed-assumptions` | 1 |

Regression vs baseline: 165 common queries, 0 lost hits, 12 gained hits.

## semantic — gate FAILED (positive top-3 78.0% vs fixture minimum 90.0%)

- Positive queries: top-1 59.0% (100 queries), top-3 78.0%
- Neighbor queries: expected selected top-1 43.9% (66 queries), in top-3 71.2%, trap top-1 (query selects the Practice it resembles) 15.2%

Positive queries that missed top-3 (rewrite-priority input):

| query | actual top-3 |
|---|---|
| `requirements.resolve-source-authority.p1` | verification.close-or-declare-evidence-gaps, review.run-subtractive-review-before-commit, planning.decide-scope-and-stop-conditions |
| `requirements.resolve-source-authority.p2` | implementation.replan-on-material-drift, implementation.choose-smallest-sufficient-design, implementation.inspect-and-reuse-existing-capability |
| `requirements.define-acceptance-and-non-goals.p3` | delivery.claim-only-supported-outcome, requirements.ground-user-goal, planning.decide-scope-and-stop-conditions |
| `planning.admit-only-currently-justified-work.p1` | planning.map-plan-to-user-capability, implementation.choose-smallest-sufficient-design, delivery.report-material-residuals |
| `planning.admit-only-currently-justified-work.p2` | review.run-subtractive-review-before-commit, implementation.preserve-responsibility-boundaries, testing.justify-regression-protection |
| `planning.scale-work-to-risk-and-cost.p2` | testing.classify-failure-before-changing-test, testing.anchor-tests-to-requirements, implementation.confirm-product-surface-expansion |
| `planning.map-plan-to-user-capability.p2` | delivery.report-material-residuals, recovery.validate-handoff-before-continuation, implementation.preserve-responsibility-boundaries |
| `planning.plan-sufficient-evidence.p1` | implementation.make-recovery-behavior-explicit, testing.justify-regression-protection, testing.anchor-tests-to-requirements |
| `planning.define-stop-condition.p2` | implementation.preserve-responsibility-boundaries, recovery.reground-after-context-loss, delivery.report-material-residuals |
| `planning.decide-scope-and-stop-conditions.p4` | requirements.ground-user-goal, correction.restore-authoritative-baseline, delivery.claim-only-supported-outcome |
| `implementation.limit-investigation-to-current-decision.p2` | testing.classify-failure-before-changing-test, implementation.inspect-and-reuse-existing-capability, testing.justify-regression-protection |
| `implementation.surface-unconfirmed-assumptions.p3` | planning.scale-work-to-risk-and-cost, delivery.report-material-residuals, implementation.replan-on-material-drift |
| `implementation.replan-on-material-drift.p1` | delivery.report-material-residuals, review.run-subtractive-review-before-commit, context.write-decision-dense-checkpoint |
| `implementation.replan-on-material-drift.p3` | correction.restore-authoritative-baseline, planning.decide-scope-and-stop-conditions, implementation.confirm-product-surface-expansion |
| `testing.anchor-tests-to-requirements.p2` | recovery.validate-handoff-before-continuation, implementation.make-recovery-behavior-explicit, recovery.reground-after-context-loss |
| `testing.assert-observable-behavior.p3` | testing.anchor-tests-to-requirements, testing.justify-regression-protection, implementation.make-recovery-behavior-explicit |
| `verification.bind-evidence-to-artifact-state.p1` | testing.justify-regression-protection, delivery.report-material-residuals, review.run-subtractive-review-before-commit |
| `verification.close-or-declare-evidence-gaps.p2` | testing.classify-failure-before-changing-test, review.run-subtractive-review-before-commit, verification.bind-evidence-to-artifact-state |
| `delivery.claim-only-supported-outcome.p1` | context.write-decision-dense-checkpoint, review.run-subtractive-review-before-commit, correction.restore-authoritative-baseline |
| `delivery.report-material-residuals.p1` | review.run-subtractive-review-before-commit, implementation.inspect-and-reuse-existing-capability, requirements.define-acceptance-and-non-goals |
| `context.give-delegated-agents-decision-context.p2` | requirements.define-acceptance-and-non-goals, context.write-decision-dense-checkpoint, implementation.preserve-responsibility-boundaries |
| `recovery.validate-handoff-before-continuation.p3` | recovery.reground-after-context-loss, delivery.claim-only-supported-outcome, verification.close-or-declare-evidence-gaps |

Most confused neighbor selections (queries worded near 'resembles' that selected 'actual top-1' instead of the expected neighbor):

| resembles | actual top-1 selection | count |
|---|---|---|
| `planning.scale-work-to-risk-and-cost` | `review.run-subtractive-review-before-commit` | 2 |
| `implementation.preserve-responsibility-boundaries` | `implementation.preserve-responsibility-boundaries` | 2 |
| `testing.assert-observable-behavior` | `testing.assert-observable-behavior` | 2 |
| `requirements.ground-user-goal` | `implementation.make-recovery-behavior-explicit` | 1 |
| `requirements.ground-user-goal` | `context.write-decision-dense-checkpoint` | 1 |
| `requirements.resolve-source-authority` | `implementation.preserve-responsibility-boundaries` | 1 |
| `requirements.define-acceptance-and-non-goals` | `requirements.define-acceptance-and-non-goals` | 1 |
| `planning.decide-scope-and-stop-conditions` | `planning.decide-scope-and-stop-conditions` | 1 |

> Evaluation-only evidence: observed retrieval selection for the fixture queries on one machine and one Pack revision. It is not a claim about content quality, other queries, other modes that were unavailable, or downstream Agent behavior.
