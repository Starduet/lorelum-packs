# Sources and provenance

This Pack generalizes public Lorelum research and sanitized engineering retrospectives into tool-neutral Practices. It does not reproduce repository-local paths, credentials, private identifiers, proprietary evaluation material, or tool-specific operating instructions.

## Evidence labels

- **Issue-explicit** means the linked public issue directly states the failure mode, desired behavior, or candidate Practice.
- **Issue-derived synthesis** means the Practice is an author generalization from a public issue's case or boundary, rather than a direct claim made by the issue.
- **Registry/install synthesis** means the Practice was generalized from a sanitized maintainer retrospective about Registry and installation implementation. The public Practice retains only transferable engineering judgment.
- **Review-workflow synthesis** means the Practice was generalized from a redacted development-review workflow. Private artifacts and tool-specific procedures are intentionally not published.
- **Delegation/Pack-authoring synthesis** means the Practice was generalized from a sanitized Pack-authoring workflow where delegated work repeated a rejected interpretation because the deciding conversation context was absent. Private prompts, identities, and repository-local operating details are not published.
- **Defensive-complexity synthesis** means the Practice was generalized from sanitized maintainer feedback about agents adding repeated validation, normalization, authorization, or fallback behavior through ordinary development.
- **Proportionality synthesis** means the Practice was generalized from sanitized maintainer experience with scheme formation on both sides of agent work — plans and protections proposed by agents, and evaluation standards authored with agent assistance — where locally reasonable additions composed into blocking or brittle wholes. Private evaluation material and tool-specific procedures are not published.
- **Lifecycle-check maintainer synthesis** means the current maintainer explicitly requested an independent decision about whether to add or strengthen checks, including checks an agent proposes during ordinary tasks, after an earlier refinement of the ownership and acceptance-path Practices. The independent entry and its procedure are author synthesis; they are not new rules quoted from public PR #288 or #281.
- **Session-handoff maintainer synthesis** means the Practice was generalized from repeated maintainer observations about low-value history and continuation records, then refined through the current handoff-content work. Public issue #32 is an early motivation for context continuity, not the source of the current fresh-session and clause-preservation procedure.
- **Working-solution maintainer synthesis** means the Practice distills repeated maintainer work observations and the current synthesis about choosing and advancing an approach that actually accomplishes a known goal. The four-part method is author synthesis, not an independent scientific finding or a procedure quoted from an issue or external Skill.

Public issue sources:

- [Issue #28: Practice retrieval and injection at critical moments](https://github.com/lorelum/lorelum/issues/28)
- [Issue #32: Practice guidance before context compaction](https://github.com/lorelum/lorelum/issues/32)
- [Issue #35: Reward hacking and over-engineering in agent coding](https://github.com/lorelum/lorelum/issues/35)
- [Issue #9: Hierarchical repository instructions and progressive context loading](https://github.com/lorelum/lorelum-packs/issues/9)

## Practice map

| Practice ID                                                           | Provenance                                                   | Relationship to source                                                                                                                                                          |
| --------------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agentic-coding.requirements.ground-user-goal`                        | Issue-explicit: #28, #35                                     | Both issues make the intended user capability, rather than the implementation artifact, the baseline for later work.                                                            |
| `agentic-coding.requirements.resolve-source-authority`                | Issue-explicit: #28, #32; Issue-derived synthesis: packs #9  | The issues distinguish current requirements from summaries, legacy code, external material, and agent assumptions; #9 informs the clarified roles of repository sources without requiring broad source discovery. |
| `agentic-coding.requirements.define-acceptance-and-non-goals`         | Issue-explicit: #28, #35                                     | Observable acceptance and explicit scope boundaries are stated as defenses against partial completion and plan expansion.                                                       |
| `agentic-coding.planning.decide-scope-and-stop-conditions`            | Issue-explicit: #35; Issue-derived synthesis: #35; Registry/install synthesis | The issue explicitly separates required, optional, and out-of-scope work and rejects future value as sufficient current justification; the finish, defer, and replan boundary generalizes preventing implementation opportunities from extending accepted work. Merges the former `admit-only-currently-justified-work` and `define-stop-condition` rows (0.5.0). |
| `agentic-coding.planning.scale-work-to-risk-and-cost`                 | Issue-explicit: #35                                          | The issue compares simple, ordinary, and high-risk work and requires engineering effort to follow actual complexity and risk.                                                   |
| `agentic-coding.planning.map-plan-to-user-capability`                 | Issue-explicit: #28                                          | The issue directly contrasts a list of technical tasks with coverage of the complete user capability.                                                                           |
| `agentic-coding.planning.organize-work-around-the-solution`           | Working-solution maintainer synthesis; Issue-derived background: #28, #35 | Repeated maintainer observations motivate the distinction between actual problem solving and goal/process substitution. The current four-part method is the October 30 generalization; the sanitized TPM allowlist example illustrates the reported failure, not a recovered execution trace or controlled incident test. See the dated source boundary and public content record below. |
| `agentic-coding.planning.plan-sufficient-evidence`                    | Issue-derived synthesis: #28, #35; review-workflow synthesis | The issues require verification of real outcomes; the minimum-sufficient and escalation framing generalizes the redacted workflow's risk-sensitive evidence planning.           |
| `agentic-coding.planning.derive-committed-set-from-concerns`         | Proportionality synthesis                                    | Generalized from sanitized maintainer experience with decision-bearing sets — evaluation gates, review standards, plan task lists — that grew one locally reasonable entry at a time until size itself failed; see synthesis boundary. |
| `agentic-coding.planning.keep-acceptance-path-completable`            | Issue-derived synthesis: #35; Proportionality synthesis; Lifecycle-check maintainer synthesis | The issue's over-engineering cases inform the original subject matter; the acceptance-path walk and failure-composition procedure are synthesis. The current maintainer request distinguishes combined-path blocking levels and reachable recovery from the independent decision about whether to add a check. |
| `agentic-coding.implementation.inspect-and-reuse-existing-capability` | Registry/install synthesis                                   | A sanitized retrospective showed that runtime, dependency, or local capabilities should be checked before duplicating behavior.                                                 |
| `agentic-coding.implementation.limit-investigation-to-current-decision` | Issue-derived synthesis: packs #9; Delegation/Pack-authoring synthesis | #9 identifies context waste from indiscriminate loading; this Practice generalizes the boundary across code, tests, configuration, documents, and logs without prescribing a host or retrieval mechanism. |
| `agentic-coding.implementation.surface-unconfirmed-assumptions`       | Issue-explicit: #28, #32                                     | Both issues explicitly require distinguishing unconfirmed assumptions from facts before those assumptions steer implementation or recovery.                                     |
| `agentic-coding.implementation.confirm-product-surface-expansion`     | Issue-derived synthesis: #35; Registry/install synthesis     | The issue rejects unsupported features and extension points; the narrow public-surface check generalizes the Registry case.                                                     |
| `agentic-coding.implementation.choose-smallest-sufficient-design`     | Registry/install synthesis                                   | A sanitized retrospective supports choosing the smallest design that satisfies current requirements and invariants without duplicate layers or I/O.                             |
| `agentic-coding.implementation.preserve-responsibility-boundaries`    | Issue-derived synthesis: #28                                 | The issue's domain-model failure demonstrates that technically valid code can violate the component or domain that owns the invariant.                                          |
| `agentic-coding.implementation.replan-on-material-drift`              | Registry/install synthesis; review-workflow synthesis        | The replanning loop generalizes cases where new surfaces, I/O, files, risk, or evidence cost made the accepted plan stale during implementation.                                |
| `agentic-coding.implementation.validate-at-the-owning-boundary`       | Defensive-complexity synthesis; Lifecycle-check maintainer synthesis | Generalized from sanitized maintainer feedback about repeated validation, normalization, and authorization. The current request keeps this Practice focused on check ownership, invalidation of established facts, and internal handoffs; the add/strengthen decision now has its own entry. See synthesis boundary and dated notes. |
| `agentic-coding.implementation.justify-added-checks`                 | Lifecycle-check maintainer synthesis; author-constructed decision procedure | Explicitly requested in the current maintainer round as an independent pre-addition decision, including agent-initiated proposals. Reachable failure or mandatory contract, guarantee owner, existing coverage, marginal protection, and the check's own costs inform retain/add/narrow/omit. This is not a new rule stated in #288 or #281, nor evidence of improved retrieval or behavior. |
| `agentic-coding.implementation.make-recovery-behavior-explicit`       | Defensive-complexity synthesis                               | Generalized from sanitized maintainer feedback about unqualified retries and fallbacks turning failure into false success; see synthesis boundary.                               |
| `agentic-coding.testing.anchor-tests-to-requirements`                 | Issue-explicit: #28, #35                                     | Both issues explicitly reject tests that protect the current implementation or agent-invented behavior instead of requirements.                                                 |
| `agentic-coding.testing.assert-observable-behavior`                   | Issue-explicit: #28                                          | The issue calls for tests around observable scenarios and user capability rather than internal implementation structure.                                                        |
| `agentic-coding.testing.classify-failure-before-changing-test`        | Issue-explicit: #28                                          | The issue explicitly identifies the moment when a failing test is about to be changed and requires first deciding what the failure means.                                       |
| `agentic-coding.testing.justify-regression-protection`                | Issue-explicit: #35                                          | The issue distinguishes durable negative contracts and real regressions from tests that memorialize rejected agent behavior.                                                    |
| `agentic-coding.verification.map-evidence-to-acceptance`              | Issue-explicit: #28                                          | The issue directly contrasts what focused checks prove with the acceptance conditions they leave uncovered.                                                                     |
| `agentic-coding.verification.bind-evidence-to-artifact-state`         | Issue-derived synthesis: #28; review-workflow synthesis      | Evidence freshness appears in the issue; explicit binding to artifact state and scoped invalidation generalize the redacted workflow.                                           |
| `agentic-coding.verification.close-or-declare-evidence-gaps`          | Issue-explicit: #28; review-workflow synthesis               | The issue requires unmet evidence boundaries to remain visible; the close, narrow, or declare decision is a generalized review discipline.                                      |
| `agentic-coding.review.validate-findings-before-action`               | Review-workflow synthesis                                    | The Practice generalizes a redacted workflow in which findings are checked against current requirements, artifact state, and contracts before action.                           |
| `agentic-coding.review.run-subtractive-review-before-commit`          | Registry/install synthesis                                   | A sanitized subtractive review removed unsupported duplication while preserving required capabilities and protections.                                                          |
| `agentic-coding.delivery.claim-only-supported-outcome`                | Issue-explicit: #28                                          | The issue directly documents a technical slice being misreported as a completed user capability and requires claim scope to match evidence.                                     |
| `agentic-coding.delivery.report-material-residuals`                   | Issue-explicit: #28                                          | The issue explicitly requires delivery to preserve remaining work, risk, evidence limits, and handoff information.                                                              |
| `agentic-coding.delivery.lead-with-engineering-conclusion` | Engineering-communication maintainer synthesis; [packs #40](https://github.com/lorelum/lorelum-packs/issues/40); ste-zh and humanizer | The maintainer clarified software engineering collaboration as the target domain. The Practice orders an already supportable diagnosis, recommendation, result, or progress report; it does not decide truth scope or mandatory residual disclosure. See the dated source and license record below. |
| `agentic-coding.delivery.explain-engineering-work-plainly` | Engineering-communication maintainer synthesis; [packs #40](https://github.com/lorelum/lorelum-packs/issues/40); ste-zh and humanizer | The Practice replaces engineering labels with component actions and effects while retaining specialist terms, exact literals, and uncertainty. Examples are constructed, not actual project measurements. |
| `agentic-coding.correction.restore-authoritative-baseline`            | Issue-explicit: #28, #35                                     | Both issues require a correction to return to authoritative requirements without converting a rejected agent choice into a new rule.                                            |
| `agentic-coding.context.write-decision-dense-checkpoint`              | Issue-explicit: #32                                          | The issue directly identifies what compaction should preserve, summarize, mark uncertain, or stop carrying forward.                                                             |
| `agentic-coding.context.recommend-session-handoff`                    | Session-handoff maintainer synthesis; Issue-derived early motivation: #32 | #32 motivates preserving useful context across boundaries. Maintainer observations and the accepted fifteenth revision supply the fresh-session recommendation, compact action record, clause mapping, and path/status preservation guidance. Early trigger observations concern earlier bodies; current content observations are recorded separately below. |
| `agentic-coding.context.give-delegated-agents-decision-context`       | Delegation/Pack-authoring synthesis                          | A sanitized authoring retrospective showed that a file path and generic quality rule were insufficient when accepted and rejected interpretations existed only in conversation. |
| `agentic-coding.recovery.reground-after-context-loss`                 | Issue-explicit: #28, #32                                     | Both issues require post-compaction work to treat the summary as an index and re-establish facts, scope, and evidence from durable sources.                                     |
| `agentic-coding.recovery.validate-handoff-before-continuation`        | Issue-explicit: #28, #32                                     | Multi-agent handoffs are explicitly identified as a boundary where conclusions must be checked against current authoritative state.                                             |

## Synthesis boundary

For the rewritten entries, the `0.5.0` revision (lorelum-packs #19) is editorial: their knowledge
sources are unchanged. The revision additionally adds two knowledge-bearing Practices
(`derive-committed-set-from-concerns`, `keep-acceptance-path-completable`) under a new
Proportionality synthesis label, described below. Every
Guidance was rewritten as an ordered decision procedure with an explicit stop, `applies_when` was
reworded to discriminate neighbors using the #17 keyword baseline's confusion matrix, and examples
were made self-contained for a cold reader. The former `admit-only-currently-justified-work` and
`define-stop-condition` Practices were merged into `decide-scope-and-stop-conditions` because
admission labeling and finish/defer/replan boundaries occur at the same pre-work scope decision;
the merged provenance row above preserves both original labels. Severity was tiered for the first
time — critical for evidence-and-delivery honesty, warn for scope and planning, info for
conventions — which is author synthesis with no external source.

The 0.5.0 additions `agentic-coding.planning.derive-committed-set-from-concerns` and
`agentic-coding.planning.keep-acceptance-path-completable` are **Proportionality synthesis**:
generalized from sanitized maintainer experience on both sides of agent work — schemes the agents
proposed (plans, validation, permission checks) and evaluation standards the maintainers authored
with agent assistance (hard-gate criteria, judge rubrics) — where locally reasonable additions
composed into failure: sets grew until their size became the failure, and protections accumulated
until the task's own acceptance path could not complete. The concern set, admission questions, rung
ladder, deletion test, and failure-composition walk are author-constructed decision procedures, not
quotations from the linked issues; issue #35's over-engineering cases inform the closure Practice's
subject matter only. The single-tenant/multi-tenant fixture pair and the config-set CLI example are
author-constructed composite scenarios, not claims of incidents in those systems.

The `0.4.0` additions `agentic-coding.implementation.validate-at-the-owning-boundary` and
`agentic-coding.implementation.make-recovery-behavior-explicit` are **Defensive-complexity synthesis**:
sanitized maintainer feedback about agents repeating validation, normalization, authorization, and
fallbacks throughout ordinary development. The two decisions concern the owner of an established
fact and the semantics of recovery after failure. Security is one application, not their scope.
HTTP/import/domain/database and cache/retry examples are author-constructed composite scenarios,
not claims of incidents or measurements in those systems.

The same synthesis refines `define-acceptance-and-non-goals`, `admit-only-currently-justified-work`,
`scale-work-to-risk-and-cost`, `choose-smallest-sufficient-design`,
`preserve-responsibility-boundaries`, `run-subtractive-review-before-commit`, and
`assert-observable-behavior`. Their original provenance above still applies; the new distinctions
about repeated internal checks, bounded uncertainty, false success, and safeguard costs are author
synthesis rather than quotations from those issues. The generic local-stop example illustrates
recovery prerequisites and makes no claim that all process identity or compatibility checks are
unnecessary.

The defensive-complexity fixtures state contrasting selection and behavior hypotheses for typed
internal handoffs, independent ingress, concurrent writes, enforced and bypassable gateways,
stale cache, nested retries, and local stop. Structural validation and semantic author review
alone do not establish retrieval quality or measured downstream Agent improvement; recorded
evaluation results must be read within their own content and environment boundaries.

The mapping records provenance, not empirical proof that retrieval improves task outcomes. The public fixtures provide testable hypotheses for retrieval and behavior evaluation. Benchmark or scoring methods, private artifacts, and unpublished review procedures are outside this repository.

`fixtures/agentic-coding/queries.yaml` turns those hypotheses into a runnable retrieval query set (three positive and two neighbor queries per Practice, expected selections declared before the run, wording held away from Practice text). Recorded runs under `fixtures/agentic-coding/baselines/` report observed selection only — keyword mode plus, where the semantic index builds on that machine, semantic mode; a degraded semantic run is annotated with its failure code rather than reported as a result.


## October 20, 2026: validation ownership and integration scope

- https://github.com/lorelum/lorelum/pull/288 — the root `AGENTS.md` addition
  “验证所有权与简化原则” grounds the refinements to
  `implementation.validate-at-the-owning-boundary` (controlled internal postconditions,
  representation-specific checks, reachable test failures, duplicate work, and retained protections)
  and `planning.plan-sufficient-evidence` (reuse applicable evidence and test added risks).
- https://github.com/lorelum/lorelum/pull/281 — the root `AGENTS.md` diff removes only
  the sentence identifying `packages/mcp` as a non-product scaffold. It retains the CLI-first
  integration restriction and separately approved remote boundary. The refinement to
  `implementation.confirm-product-surface-expansion` is author synthesis of that narrow change
  and retained context: scaffold presence or removal does not authorize a new product surface.

These are refinements of existing decisions, not new Practice IDs. The examples generalize the
source repository's policies; they do not impose its MCP restriction on other products. These
sources provide rationale and provenance, not evidence of improved retrieval or Agent outcomes.

## October 22, 2026: an independent decision before adding checks

The current maintainer request supplies the **Lifecycle-check maintainer synthesis** above.
An earlier working-tree approach refined only the ownership and acceptance-path Practices.
The maintainer then explicitly requested a separate entry because those refinements did not
establish reliable triggering of the pre-addition decision. The new
`agentic-coding.implementation.justify-added-checks` is author synthesis of that request,
not a new rule quoted from #288 or #281.

Read it **before deciding to add or strengthen** validation, preflight, authorization/confirmation,
integrity scans, or startup/recovery blockers, including an agent's own proposal during an ordinary
task. It asks why the check is justified: reachable failure or mandatory contract, guarantee owner,
existing coverage, added protection, and its own false rejection, delay, I/O, availability,
maintenance, and recovery costs. The outcome can retain, add, narrow, or omit a check.
This does not wait for a post-implementation subtractive review.

The neighboring decisions remain distinct: `validate-at-the-owning-boundary` asks where the check
belongs, when a fact can become stale, and whether an internal handoff introduces a new failure;
`keep-acceptance-path-completable` asks whether combined checks leave required paths completable,
with suitable blocking levels and reachable recovery. Overall effort (`scale-work-to-risk-and-cost`),
verification observations (`plan-sufficient-evidence`), and retry/fallback outcomes
(`make-recovery-behavior-explicit`) are not substitutes for this decision.
Startup scans and repair/stop prerequisites that could require the healthy state being restored
are composite examples from the request, not reported incidents or measurements in #288 or #281.

The source boundaries remain narrow:

- [PR #288](https://github.com/lorelum/lorelum/pull/288) supports ownership and reuse of
  established facts. Its D1–D6 were explicitly **not implemented**, with their error, safety,
  path, or durability guarantees left for maintainer decisions. Neither those deferred questions
  nor this synthesis authorize deleting existing schemas or bypassing checks. External input,
  authorization, concurrency, native/model quality, final release integrity, and recovery identity
  protections remain in scope.
- [PR #281](https://github.com/lorelum/lorelum/pull/281) concerns removal of unused scaffolds
  while preserving the product's CLI-first and separately approved remote boundary. The
  product-surface Practice does not turn every backend guard into a product expansion or impose
  general guard approval. The routing suggestion does not add a global tool-approval gate.

Version `0.6.0` contains **35 Practice IDs**, including the new independent entry; the immutable
`0.5.1` release retains its original 34. Versioning does not establish automatic lookup or behavior
improvement. The project `AGENTS.md` /
required-skill routing examples in the English and Chinese Pack READMEs are adoption suggestions
only; this repository has not deployed them to the Lorelum product repository or its plugin/skill.
The official [Lorelum `0.1.0-alpha.6` prerelease](https://github.com/lorelum/lorelum/releases/tag/v0.1.0-alpha.6)
includes an omp plugin and a skill. Availability of those integration surfaces, an independent
Practice ID, Pack descriptions, or `applies_when` metadata does not establish automatic rule
lookup. The real Windows host flow for this suggestion has not been tested.

Evidence must distinguish query selection (**retrieval**), successful delivery of the relevant
full body to the agent via `get` or reuse of applicable current session text (**body provision**),
and observed use in a decision (**decision impact**). A query/summary hit does not prove body
provision; body provision does not prove changed behavior. An empty query does not establish
the absence of an applicable rule when a known ID can be fetched directly or resolved through
the catalog. The new ID requires `0.6.0` installed content or a Pack layer containing it; it is not
in the older `0.5.1` release. Read the working-tree body with an available file-reading tool if needed,
or state that the text could not be obtained. Repeated lookup per helper or tool call is not required.

The existing `scripts/eval-decisions` runner performs query/get and inserts the retrieved body
into the answering prompt. Its paired answers can assess body-assisted decisions, and its
retrieval records can separately describe query selection, but forced injection does not test
whether an agent autonomously recognizes a trigger and retrieves the rule. Fixture additions
declare hypotheses; they do not establish retrieval success, downstream improvement, or stable
host routing. The [October 22 alpha.6 two-Practice evaluation](../../fixtures/agentic-coding/baselines/agentic-coding-backend-checks-alpha6-2026-10-22.md)
is retained as a **historical comparison of the earlier two-neighbor approach**, not a result for
the new independent entry. It records keyword gains and regressions, successful body provision,
failed semantic model preparation, and all six decisions already correct blind in each arm.
No causal decision improvement or deployed automatic routing was established by that run.
Those observations do not carry over as success evidence for the 35-Practice candidate.

The [independent-entry alpha.6 evaluation](../../fixtures/agentic-coding/baselines/agentic-coding-independent-check-alpha6-2026-10-22.md)
separates unchanged query contracts from two migrated expectations and nine new queries. It records
successful query/get and pre-decision body reading in one catalog-only and one explicitly routed
session, with required protections retained in their stated designs. It provides no no-knowledge
control, repeated trigger trials, semantic ranking results, or real host deployment, and therefore
does not establish stable automatic triggering or causal decision improvement.

## October 22, 2026: official 0.6.0 release

PR #38 was merged at `547a13f`; release metadata promotion produced immutable artifact
`agentic-coding-v0.6.0` at `68a4be166a488166931330f9dfd5afd01d807421`, without changing canonical
Practice Markdown. The official Registry entry was added only after that tag existed. Unmerged
PR #36 is not part of this artifact, and old release refs remain unchanged.

The [official release verification](../../fixtures/agentic-coding/baselines/agentic-coding-0.6.0-release-2026-10-22.md)
records an isolated exact-version installation, default update from `0.5.1`, retention of all 34
existing IDs plus the new entry, full-body readback, and the installed keyword gate. Installation
returned success while semantic index sync reported `embedding.not-configured` in the intentionally
model-free environment. Availability and finite keyword observations do not establish semantic
quality, repeated automatic triggering, or causal decision improvement.

## October 30, 2026: session continuity and working solutions

The two additions are experience-derived Practices. The maintainer's adopted release objective is
to distill recurring work observations into actionable guidance with reasonable boundaries and
finite usability evidence. It does not require superiority to an external Skill. Neither the
observations nor the publication establish that recent models make these errors more frequently.

### Session handoff: current content versus early triggering

`agentic-coding.context.recommend-session-handoff` retains the accepted **fifteenth revision**.
Its source is the maintainer's repeated experience with histories that add little continuation
value, followed by the current handoff-content synthesis. [Issue #32](https://github.com/lorelum/lorelum/issues/32)
provides early context-continuity motivation; it does not state the current procedure for suggesting
a fresh conversation or preserving the smallest complete controlling clauses.

The [October 30 public content record](../../fixtures/agentic-coding/baselines/agentic-coding-0.7.0-content-2026-10-30.md)
separates early retrieval/trigger observations from current-body evidence. Earlier routing work
used earlier guidance and is not evidence that the fifteenth revision triggers autonomously or
stably. The fifteenth-revision observations concern two reused sources, one generation per source,
with reading and focused source-clause comparisons. They support a bounded content-usability
judgment, not zero omissions, zero irrelevant history, independent full-source completeness,
lower token cost, or better downstream execution. Private source conversations are not published;
the public record preserves sanitized methods, observations, and limitations.

### Working solution: observation, synthesis, and limited transfer checks

`agentic-coding.planning.organize-work-around-the-solution` takes its current method from the
October 30 four-paragraph generalization, not from the earlier use-path or consumer-pipeline
drafts. Its experiential source is the maintainer's repeated observation that agents can restate
the goal, arrange process, or restrict normal capabilities without making the judgment that lets
the task work. [Issue #28](https://github.com/lorelum/lorelum/issues/28) and
[issue #35](https://github.com/lorelum/lorelum/issues/35) supply related goal-substitution and
over-engineering background, not the four-part method or proof of its effectiveness.

The TPM example is a sanitized, self-contained rendering of the maintainer-reported text-allowlist
undercounting of normal thinking and tool-call content. The original full execution chain was not
recovered; this is an experience source, not a replayed or independently measured incident.
The final method generalizes beyond input/output pipelines: facts that change a choice may be
behavior, state, materials, domain rules, or accepted decisions. Exact small edits remain direct;
analysis and exploration retain their appropriate scope. Required safety, authorization,
compatibility, and normal capabilities remain constraints.

The same [public content record](../../fixtures/agentic-coding/baselines/agentic-coding-0.7.0-content-2026-10-30.md)
documents finite constructed state, performance, and exact-edit checks of the Chinese candidate.
One session per condition handled those tasks in a fixed sequence under a shared host; later
tasks within a condition were not independent samples. The previous draft, generalized candidate,
and full external `karpathy-guidelines` body all completed the observed tasks, with identical core
code in the two coding tasks. The external body was a comparison condition, not the source or a
demonstrated inferior alternative. These observations support limited usability, not additional
benefit, stable generalization, autonomous retrieval, or superiority over an external Skill.
The canonical English and Chinese Practices organize that method into the Pack's six-section
format with applicability, stop, neighbor boundaries, and an illustrative example; they are not
byte-identical to the evaluated candidate, and its results are not a fresh test of the final bodies.

## October 30, 2026: official 0.7.0 release

PR #39 merged at `4efd8b82d20ed6d873216056bc7fb74060715d5e`. Documentation promotion
created the artifact commit `6715efa7cc152a4e222cca508ee6789a843854b0`, tagged immutably as
`agentic-coding-v0.7.0`; canonical Practice content was not changed. Registry promotion followed
in `0d74cbe41b74c19b8a5cd85b2537b9426cd218b5`, after the tag existed remotely.

The [official release verification](../../fixtures/agentic-coding/baselines/agentic-coding-0.7.0-release-2026-10-30.md)
records 37-ID installation, matching new bodies, and default update from `0.6.0` preserving all
35 original IDs with exactly two additions and no changed or invalidated IDs. Initial download
failure and GitHub API transport failures remain disclosed. Runtime artifact identity binds the
existing keyword results without duplicating the full evaluation. Index readiness and finite
keyword selection do not establish semantic quality, stable host triggering, or causal benefit.

## November 2, 2026: clear reports in software engineering collaboration

The maintainer requested clearer language and conclusion-first reports in [packs #40](https://github.com/lorelum/lorelum-packs/issues/40),
then explicitly selected **software engineering collaboration** as the domain. The earlier
generic-communication interpretation and everyday examples were rejected and removed. The two
new entries belong in `agentic-coding`; they do not establish a separate communication Pack,
extend to unrelated everyday advice, or implement #41's repository-wide summaries.

The source screenshots motivate expression and ordering only. Their financial figures and causal
claims were not verified or adopted. The concrete engineering mechanisms, stop conditions,
neighbor boundaries, and Chinese examples in this revision are author synthesis, not quotations
or recovered execution traces. The [worked examples](./references/engineering-communication.md)
and evaluation fixtures label their facts as constructed. The
[engineering effect record](../../fixtures/agentic-coding/baselines/engineering-communication-2026-11-02.md)
separates actual generated replies from illustrative rewrites and search observations.

### Reviewed external material

- [dualface/ste-zh `SKILL.md`](https://github.com/dualface/ste-zh/blob/22f868ec3ab77e902571379ad1eaccee4c38fdac/SKILL.md),
  revision `22f868ec3ab77e902571379ad1eaccee4c38fdac`: necessary term explanations and concrete
  actions (R2–R4, R6, R12), key information first (R18), distinct work and verification scope,
  locatable evidence, and uncertainty (R20–R22, R24–R25). Its
  [MIT license](https://github.com/dualface/ste-zh/blob/22f868ec3ab77e902571379ad1eaccee4c38fdac/LICENSE)
  was checked. This Pack does not adopt explicit activation, fixed status vocabulary, sentence
  limits, or mandatory output templates, and does not claim ASD-STE100 compliance.
- [blader/humanizer `SKILL.md`](https://github.com/blader/humanizer/blob/0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0/SKILL.md),
  revision `0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0`: preserve source claims when rewriting
  (How to work, steps 2–3), remove staged openings and inflated language, name concrete actors,
  and match the reader rather than repeat their background. Its
  [MIT license](https://github.com/blader/humanizer/blob/0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0/LICENSE)
  was checked. It was discovered through [skills.sh](https://skills.sh/blader/humanizer/humanizer)
  and reviewed at the upstream source. No punctuation blacklist, forced personality,
  draft/critique/final protocol, upstream quality claim, or AI-detector goal is adopted.

The split is by decision, not by source: `lead-with-engineering-conclusion` decides what the
developer reads first; `explain-engineering-work-plainly` decides how the mechanism is expressed.
They arrange and explain justified content. The existing `claim-only-supported-outcome` still
decides what evidence supports, and `report-material-residuals` still selects important unresolved
facts. Editing a reusable Practice remains the Pack-authoring neighbor's responsibility.

Version `0.8.0` names unreleased working-tree content with 39 IDs. Registry and immutable
`agentic-coding-v0.7.0` content remain unchanged. Content examples, actual body-assisted replies,
retrieval selection, and autonomous host triggering are separate evidence layers; none proves
general superiority or stable behavior.

### MIT notices for the reviewed material and adaptations

MIT License

Copyright (c) 2026 dualface

Copyright (c) 2025 Siqi Chen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
