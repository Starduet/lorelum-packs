# Retrieval evaluation: agentic-coding-queries vs agentic-coding@0.5.0

- Generated: 2026-09-17T08:10:55+00:00  |  lore 0.1.0-alpha.2  |  mode(s): keyword  |  top-k threshold: 3
- Store: tmp\eval-store-050  |  Queries: 165 runnable, 0 skipped
- Install source: `Starduet/lorelum-packs` fork Registry (pre-merge evaluation), ref `agentic-coding-v0.5.0` @ `2053c44`, tree identical to the PR branch

## keyword — gate PASSED (positive top-3 100.0% vs fixture minimum 90.0%)

- Positive queries: top-1 96.0% (99 queries), top-3 100.0%
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

> Evaluation-only evidence: observed retrieval selection for the fixture queries on one machine and one Pack revision. It is not a claim about content quality, other queries, other modes that were unavailable, or downstream Agent behavior.
