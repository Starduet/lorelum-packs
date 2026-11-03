# Agentic Coding

The `agentic-coding@0.8.0` working tree contains 39 decision-focused Practices for AI agents doing software engineering. Its two unreleased additions address clear engineering conclusions and concrete explanations to developers. The published `0.7.0` release remains the immutable 37-Practice artifact.

Canonical English · [简体中文](./i18n/zh-CN/README.md)

The published `0.7.0` immutable release ref is `agentic-coding-v0.7.0`. Its two additions are
`agentic-coding.context.recommend-session-handoff` and
`agentic-coding.planning.organize-work-around-the-solution`. The immutable `0.6.0` release
retains its original 35 Practices; no older artifact is replaced.

The [content adoption record](../../fixtures/agentic-coding/baselines/agentic-coding-0.7.0-content-2026-10-30.md)
explains the maintainer observations, concrete decisions, and limited evaluation evidence behind
the additions. The [official release verification](../../fixtures/agentic-coding/baselines/agentic-coding-0.7.0-release-2026-10-30.md)
records exact-version installation, default update from `0.6.0`, all 37 IDs, and matching new bodies.
Distribution success does not establish stable triggering or downstream improvement.

```sh
# New installation:
lore pack install agentic-coding@0.7.0
# Existing installation; the Registry selects the latest stable release:
lore pack update agentic-coding
```

The Practices cover requirements, planning, implementation, testing, verification, review, delivery, correction, and context recovery. Each entry targets one decision point and is intended to remain useful when retrieved alone; consumers should retrieve only the few entries relevant to the current work and moment.

## Unreleased 0.8.0: explain engineering work clearly

- [Give the Developer the Conclusion First](./practices/delivery/lead-with-engineering-conclusion.md)
  puts the diagnosis, recommendation, result, or actual progress before the investigation history,
  with the limitation that changes the developer's next decision beside it.
- [Explain Engineering Work with Concrete Actions](./practices/delivery/explain-engineering-work-plainly.md)
  replaces labels such as "the lifecycle is closed" with what a component does and why it matters.
  Keep useful technical terms, exact literals, and uncertainty.

These are software engineering collaboration Practices, not general everyday advice. They organize
and explain a supported answer; `claim-only-supported-outcome` still decides claim scope and
`report-material-residuals` still selects important remaining issues. Do not replace those
decisions with nicer wording. Short replies need no template; complex judgments retain the
conditions, evidence, and counterevidence that determine the answer.

Start with the [Chinese before-and-after examples](./references/engineering-communication.md):
token-refresh results, an index tradeoff, an unconfirmed timeout cause, and a one-line change-scope
answer. Their facts are constructed. The [effect record](../../fixtures/agentic-coding/baselines/engineering-communication-2026-11-02.md)
shows actual generated engineering replies and keeps usability observations separate from search.

This content has not been released or added to the Registry. For local use, install
`--path ./packs/agentic-coding` into a new isolated `--store-root`, then use `lore get` with either
full ID. The Registry commands above still select published `0.7.0`; they do not fetch `0.8.0`.
No change to the host's instructions, automatic routing, or existing global Store is implied.

## Scope

Use this Pack to improve engineering judgment around scope, risk, source authority, investigation boundaries, evidence, implementation drift, review findings, completion claims, corrections, long-session checkpoints, delegation context, and handoffs. Combine it with the domain Practices and project requirements that define what the system itself must do.

### Experience-derived additions

[Recommend a Fresh Session When History Adds Little Value](./practices/context/recommend-session-handoff.md)
addresses long work where obsolete investigations compete with the next task before an obvious
mistake occurs. It combines a relevance-based migration decision with minimal complete clauses,
decision status, and usable source pointers. The current handoff method retained the tracked
constraints in two development samples while reducing their records by about 30% and 36% from
the larger appendix-based variant. Earlier catalog-cue runs observed autonomous lookup and useful
handoffs in two positive cases, with no unnecessary migration in two negative cases. Those trigger
observations belong to the earlier body snapshot, not a claim of stable triggering for every revision.

[Organize Work Around a Working Solution](./practices/planning/organize-work-around-the-solution.md)
addresses a different choice: the user goal is known, but safeguards, coordination, or internal
standards are replacing the actual solution. Maintainer examples include silently dropping normal
request content during token estimation, predetermining a delegated designer's choices, and
reporting internal classifications instead of the overall result. The guidance keeps the agent
responsible for a concrete, feasible next action without weakening safety or requiring another
checklist. It is not a universal replacement for domain knowledge or specialized Skills.

Adoption is based on the observed need, explicit decision method, bounded scope, and limited usable
outputs. Controlled implementation and reporting probes, including state and performance tasks,
did not show an advantage over the compared guidance or public Skill. We do not claim market-wide
novelty, a measured increase in failure frequency after model updates, stable automatic triggering,
lossless handoffs, or demonstrated superiority.

## Validation and recovery decisions

**Before deciding to add or strengthen a check**, read
[Justify Added Checks Before Implementing Them](./practices/implementation/justify-added-checks.md)
(`agentic-coding.implementation.justify-added-checks`). This applies in planning and when an
agent proposes a check on its own during an ordinary task: validation, preflight, authorization
or confirmation, integrity scans, and startup/recovery blockers. Do not wait for a post-implementation
subtractive review.

Keep three decisions distinct:

- **Why add or strengthen it?** `justify-added-checks` identifies a reachable failure or mandatory
  contract, the guarantee's owner and existing coverage, and the added protection. Weigh the
  check's own false rejection, delay, I/O, availability, maintenance, and recovery costs before
  choosing to retain, add, narrow, or omit it.
- **Where does the check belong?**
  [Validate at the Boundary That Owns the Fact](./practices/implementation/validate-at-the-owning-boundary.md)
  (`agentic-coding.implementation.validate-at-the-owning-boundary`) decides ownership, when an
  established fact can become stale, and whether an internal handoff introduces a new failure.
- **Can the combined path still complete?**
  [Keep the Acceptance Path Completable](./practices/planning/keep-acceptance-path-completable.md)
  (`agentic-coding.planning.keep-acceptance-path-completable`) walks normal use, startup,
  maintenance, and recovery with the checks combined. Choose the blocking level and preserve a
  reachable repair/stop path; do not require the healthy state that recovery exists to restore.

Use [Give Recovery One Owner and an Explicit Outcome](./practices/implementation/make-recovery-behavior-explicit.md)
when a failure is about to gain a retry, empty default, alternate source, or degraded result. It
requires a known recoverable condition, a bounded owner, and an outcome the caller can understand.
Validation establishes a fact; recovery responds to a failure. Either decision can arise alone.

These are general-purpose decisions, not a direction to perform fewer checks. Preserve
external-input boundaries, authorization, concurrent state consistency, native/model quality,
release integrity, and recovery identity guarantees. Required protection can justify an expensive
check. No new checklist, mandatory risk report, or independent approval gate is required.

Overall engineering effort belongs to `scale-work-to-risk-and-cost`; choosing verification
observations belongs to `plan-sufficient-evidence`. Neither replaces the pre-addition decision.
Version `0.6.0` adds one independent ID and refines its two neighbors without rewriting older
release content or history.

## Project routing suggestion

Pack descriptions and `applies_when` help selection after discovery; they do not make an agent
query Lorelum automatically. An independent Practice ID does not guarantee that its trigger will
be noticed. A project can adopt the following instruction in its own `AGENTS.md` or in a skill
that its host is configured to require at this decision point:

> Before deciding to add or strengthen a check, including one you propose on your own during
> an ordinary task, read the full body of `agentic-coding.implementation.justify-added-checks`.
> Decide why it is needed before implementing it; a final subtractive review is too late.
> For ownership, stale facts, or internal handoffs, also read
> `agentic-coding.implementation.validate-at-the-owning-boundary`.
> If checks could block normal use, startup, maintenance, repair, or stop, also read
> `agentic-coding.planning.keep-acceptance-path-completable` before choosing the prerequisites.
> Reuse the applicable current body if it is already available in this session. Otherwise, use
> `lore get` with the known full ID; a query or summary hit alone is not the body.
> An empty search is not evidence that no rule applies: get the known ID directly, or consult the
> available catalog to resolve it. Do not repeat retrieval for every helper or tool invocation
> when the same decision and body still apply. If the body cannot be obtained, report that limit
> rather than claiming it was read.

For example, `lore get agentic-coding.implementation.justify-added-checks` retrieves the known
entry point when `0.6.0` is installed or its content is available in the active Pack layer.
The older `0.5.1` release does not contain that ID. Update that installation to `0.6.0`, or read the
linked working-tree body through an available file-reading tool; report any inability to obtain it.
This route targets the check decision, not every tool call, and does not add a global approval gate.

This is an adoption suggestion in this Pack's documentation only. It has not been deployed to the
Lorelum product repository, its `AGENTS.md`, plugin, or skill. The official
[Lorelum `0.1.0-alpha.6` prerelease](https://github.com/lorelum/lorelum/releases/tag/v0.1.0-alpha.6)
includes an omp plugin and a skill; their availability does not establish that this route fires.
The real Windows host flow for this suggestion has not been tested.

Keep three kinds of evidence separate: **retrieval** records which IDs a query selects;
**body provision** records that `get` successfully supplies the relevant full text to the agent
(or that the current text is already in its session); **decision impact** needs evidence of what
the agent actually decided with it. None proves the next. The existing `scripts/eval-decisions`
runner queries and gets text, then forces it into an injected prompt. That can test body-assisted
decisions, not whether an agent independently notices the trigger and looks up the rule. Fixture
expectations are hypotheses, not successful retrieval, behavior, or deployed routing.

The [October 22 alpha.6 two-Practice evaluation](../../fixtures/agentic-coding/baselines/agentic-coding-backend-checks-alpha6-2026-10-22.md)
is a **historical comparison of the earlier two-neighbor refinement**, not a result for the new
independent entry. It records limited keyword gains alongside existing-query regressions,
failed semantic preparation, successful body provision, and no observed decision improvement.
Those observations do not establish stable lookup or carry over as evidence that the new
35-Practice candidate succeeds.

The [independent-entry alpha.6 evaluation](../../fixtures/agentic-coding/baselines/agentic-coding-independent-check-alpha6-2026-10-22.md)
records its own query rankings and controlled catalog-only versus explicit-route sessions. Both
sessions read the new body before their design decisions and retained required safeguards. One
session per arm, no blind control, and no real host deployment do not establish stable triggering
or causal decision improvement.

## Non-goals

This Pack is not a workflow engine, task manager, test framework, compactor, automatic acceptance system, or replacement for project specifications. It does not prescribe a particular coding agent, repository layout, command, language, or framework. Practice retrieval or citation is not evidence that a task succeeded.

## Release history

- `0.7.0` adds `context.recommend-session-handoff` and `planning.organize-work-around-the-solution`, with Chinese companions, source attribution, and retrieval fixtures. It preserves the 35-Practice `0.6.0` artifact and separates experience-derived content value from unproven causal gains.
- `0.6.0` adds `implementation.justify-added-checks` before deciding to add or strengthen safeguards, separates necessity from ownership and combined-path decisions, and carries the validation/evidence/product-surface refinements from PR #38. It contains 35 Practices at `agentic-coding-v0.6.0`. Limited keyword and controlled-session evidence is linked above; semantic quality, stable automatic triggering, and causal decision improvement are not established. Unmerged PR #36 is not included.
- `0.5.1` is the immutable release at `agentic-coding-v0.5.1`, available through the official Registry. It is a metadata-only retune: the `pack.yaml` description — the routing surface agents see in the session-start pack catalog — now names the two planning-calibration moments added in `0.5.0` (decision-bearing sets growing past what they must decide; validation, permission, or confirmation checks blocking the acceptance path) and tracks the `decide-scope-and-stop-conditions` merge. No Practice content changes. A representative official Registry install on September 21, 2026 resolved this ref (`954324c`), decoded the Pack, and read back all 34 Practice IDs including both planning-calibration entries; that verifies the supported materialization path, not retrieval quality or downstream Agent behavior. It rewrites every Practice as a step-style decision procedure with an explicit stop, merges the two pre-work scope Practices into `decide-scope-and-stop-conditions`, adds two planning-calibration Practices (`derive-committed-set-from-concerns`, `keep-acceptance-path-completable`; 33 to 34 entries), tiers severity into critical/warn/info, and retunes `applies_when` against the #17 keyword retrieval baseline. A representative official Registry install on September 21, 2026 resolved this ref, decoded the Pack, and read back all 34 Practice IDs; that verifies the supported materialization path, not retrieval quality or downstream Agent behavior.
- `0.4.0` adds two independent validation and recovery Practices and refines seven existing entries against unnecessary defensive complexity (tag `agentic-coding-v0.4.0` + Registry entry).
- `0.3.1` adds a Practice that limits repository investigation to sources that can change the current decision and clarifies source roles without making broad reading a default.
- `0.3.0` rewrites the Pack for clearer standalone retrieval and adds a Practice for giving delegated Agents the decisions they need to preserve scope and quality.
- `0.2.0` is the immutable first complete 29-Practice release.
- `0.1.0` is an immutable one-entry installation placeholder retained only as release history. Its tag and content are not rewritten.

See [SOURCES.md](./SOURCES.md) for public provenance and the distinction between issue-explicit evidence and author synthesis.

Localized content under [`i18n/`](./i18n/) is provided for human-facing consumption and does not change the canonical runtime Pack, Registry release, retrieval inputs, or Practice IDs.
