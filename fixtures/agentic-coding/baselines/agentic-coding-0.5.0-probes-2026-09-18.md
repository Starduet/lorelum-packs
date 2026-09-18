# Decision-probe run (eval-decisions-run/1)

Pilot run against agentic-coding@0.5.0 @449da50 (PR #30 head, catalog fixture from that branch; store tmp/eval-store-050, fork Registry install). Answering sessions were fresh uncontaminated agent sessions per tmp protocol: blind phase, injected phase, scoring phase. 8/10 blind answers were already correct (strong-agent effect); the two moved-toward probes are the practices whose value is procedural detail; no injected answer triggered a forbidden behavior.

- Generated: 2026-09-18T15:25:31+08:00  |  probes: 10  |  retrieval: keyword
- Directions: moved-toward **2**, no-change **8**, harmful **0**
- Injection-source mismatches (retrieved practice differs from the catalog entry): 0

| probe | injected | direction | already-correct blind | evidence |
|---|---|---|---|---|
| `catalog.requirements.resolve-source-authority` | `resolve-source-authority` | no-change | yes | "The adopted seven-year policy is the controlling source for retention intent; the cleanup job and its green tests only show what exists tod |
| `catalog.planning.decide-scope-and-stop-conditions` | `decide-scope-and-stop-conditions` | moved-toward | no | "I would commit only the failed-job email alert (and the one-filter task) with an observable finish condition — e.g., a failed job produces  |
| `catalog.planning.plan-sufficient-evidence` | `plan-sufficient-evidence` | moved-toward | no | "Unit tests alone cannot distinguish a correct retry from a duplicate charge at the gateway boundary, so I would pair focused retry-state te |
| `catalog.implementation.inspect-and-reuse-existing-capability` | `inspect-and-reuse-existing-capability` | no-change | yes | "Before writing anything, I would open the dependency the other importer already uses and read its closest caller or test to confirm it pres |
| `catalog.implementation.replan-on-material-drift` | `replan-on-material-drift` | no-change | yes | "A fixture exceeding the response limit changes what is delivered (a synchronous response becomes temp files, retries, a queue, cleanup), ho |
| `catalog.testing.classify-failure-before-changing-test` | `classify-failure-before-changing-test` | no-change | yes | "Before touching the snapshot I would reproduce the failure and test the required keyboard navigation directly against the request, since th |
| `catalog.verification.map-evidence-to-acceptance` | `map-evidence-to-acceptance` | no-change | yes | "I would line every result up criterion-by-criterion: the calculation tests, build, static checks, and single submission cover their own cri |
| `catalog.review.run-subtractive-review-before-commit` | `run-subtractive-review-before-commit` | no-change | yes | "I would remove the duplicate parser and wrapper, since nothing in the request justifies them, and reuse or merge into the existing capabili |
| `catalog.delivery.claim-only-supported-outcome` | `claim-only-supported-outcome` | no-change | yes | "I would claim exactly what was demonstrated: one queued edit now replays after reconnect with focused tests green — a repaired path within  |
| `catalog.context.write-decision-dense-checkpoint` | `write-decision-dense-checkpoint` | no-change | yes | "Before compaction I would record the controlling request — diagnosis only, implementation not authorized — the denial path as still unverif |
