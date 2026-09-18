# Retrieval evaluation: agentic-coding-queries vs agentic-coding@0.4.0

- Generated: 2026-09-18T02:53:28+00:00  |  lore 0.1.0-alpha.2  |  mode(s): semantic  |  top-k threshold: 3
- Store: tmp\eval-store-040sem  |  Queries: 155 runnable, 11 skipped
- Install source: official Registry `lorelum/lorelum-packs`, ref `agentic-coding-v0.4.0` — first successful semantic run on this machine (prior 0.4.0/0.3.1 baselines recorded semantic as degraded)
- Skipped (Practice not in this Pack version): 11
- Coverage gap: 2 installed Practice(s) have no positive queries: `planning.admit-only-currently-justified-work`, `planning.define-stop-condition`

## semantic — gate FAILED (positive top-3 79.6% vs fixture minimum 90.0%)

- Positive queries: top-1 57.0% (93 queries), top-3 79.6%
- Neighbor queries: expected selected top-1 43.5% (62 queries), in top-3 72.6%, trap top-1 (query selects the Practice it resembles) 11.3%

Positive queries that missed top-3 (rewrite-priority input):

| query | actual top-3 |
|---|---|
| `requirements.resolve-source-authority.p1` | verification.close-or-declare-evidence-gaps, planning.plan-sufficient-evidence, review.run-subtractive-review-before-commit |
| `requirements.define-acceptance-and-non-goals.p2` | review.run-subtractive-review-before-commit, implementation.inspect-and-reuse-existing-capability, implementation.replan-on-material-drift |
| `requirements.define-acceptance-and-non-goals.p3` | delivery.claim-only-supported-outcome, planning.admit-only-currently-justified-work, planning.define-stop-condition |
| `planning.scale-work-to-risk-and-cost.p2` | testing.classify-failure-before-changing-test, testing.anchor-tests-to-requirements, testing.justify-regression-protection |
| `planning.map-plan-to-user-capability.p2` | delivery.report-material-residuals, recovery.validate-handoff-before-continuation, implementation.confirm-product-surface-expansion |
| `planning.plan-sufficient-evidence.p1` | implementation.make-recovery-behavior-explicit, testing.justify-regression-protection, testing.anchor-tests-to-requirements |
| `implementation.limit-investigation-to-current-decision.p2` | implementation.inspect-and-reuse-existing-capability, testing.classify-failure-before-changing-test, testing.anchor-tests-to-requirements |
| `implementation.surface-unconfirmed-assumptions.p3` | delivery.report-material-residuals, implementation.replan-on-material-drift, planning.scale-work-to-risk-and-cost |
| `implementation.replan-on-material-drift.p1` | delivery.report-material-residuals, review.run-subtractive-review-before-commit, context.write-decision-dense-checkpoint |
| `testing.anchor-tests-to-requirements.p2` | implementation.make-recovery-behavior-explicit, recovery.validate-handoff-before-continuation, recovery.reground-after-context-loss |
| `testing.assert-observable-behavior.p3` | testing.anchor-tests-to-requirements, testing.justify-regression-protection, implementation.make-recovery-behavior-explicit |
| `verification.map-evidence-to-acceptance.p3` | planning.define-stop-condition, planning.admit-only-currently-justified-work, review.run-subtractive-review-before-commit |
| `verification.bind-evidence-to-artifact-state.p1` | testing.justify-regression-protection, verification.close-or-declare-evidence-gaps, delivery.report-material-residuals |
| `delivery.claim-only-supported-outcome.p1` | context.write-decision-dense-checkpoint, review.run-subtractive-review-before-commit, correction.restore-authoritative-baseline |
| `delivery.report-material-residuals.p1` | implementation.inspect-and-reuse-existing-capability, review.run-subtractive-review-before-commit, implementation.choose-smallest-sufficient-design |
| `context.give-delegated-agents-decision-context.p1` | planning.map-plan-to-user-capability, implementation.replan-on-material-drift, review.run-subtractive-review-before-commit |
| `context.give-delegated-agents-decision-context.p2` | requirements.define-acceptance-and-non-goals, implementation.preserve-responsibility-boundaries, context.write-decision-dense-checkpoint |
| `context.give-delegated-agents-decision-context.p3` | delivery.report-material-residuals, delivery.claim-only-supported-outcome, recovery.validate-handoff-before-continuation |
| `recovery.validate-handoff-before-continuation.p3` | verification.close-or-declare-evidence-gaps, recovery.reground-after-context-loss, delivery.claim-only-supported-outcome |

Most confused neighbor selections (queries worded near 'resembles' that selected 'actual top-1' instead of the expected neighbor):

| resembles | actual top-1 selection | count |
|---|---|---|
| `planning.map-plan-to-user-capability` | `testing.assert-observable-behavior` | 2 |
| `testing.assert-observable-behavior` | `testing.assert-observable-behavior` | 2 |
| `requirements.ground-user-goal` | `implementation.make-recovery-behavior-explicit` | 1 |
| `requirements.ground-user-goal` | `context.write-decision-dense-checkpoint` | 1 |
| `requirements.resolve-source-authority` | `implementation.preserve-responsibility-boundaries` | 1 |
| `requirements.define-acceptance-and-non-goals` | `requirements.define-acceptance-and-non-goals` | 1 |
| `planning.scale-work-to-risk-and-cost` | `verification.close-or-declare-evidence-gaps` | 1 |
| `planning.scale-work-to-risk-and-cost` | `review.run-subtractive-review-before-commit` | 1 |

> Evaluation-only evidence: observed retrieval selection for the fixture queries on one machine and one Pack revision. It is not a claim about content quality, other queries, other modes that were unavailable, or downstream Agent behavior.
