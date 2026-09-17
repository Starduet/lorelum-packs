# Agentic Coding

`agentic-coding@0.5.0` is an unreleased, tool-neutral Knowledge Pack of 32 decision-focused Practices for AI agents doing software engineering: clarifying goals and authority, controlling scope and investigation, making proportionate implementation and validation choices, and handling reviews, delivery, handoffs, and recovery with trustworthy evidence.

Canonical English · [简体中文](./i18n/zh-CN/README.md)

The Practices cover requirements, planning, implementation, testing, verification, review, delivery, correction, and context recovery. Each entry targets one decision point and is intended to remain useful when retrieved alone; consumers should retrieve only the few entries relevant to the current work and moment.

## Scope

Use this Pack to improve engineering judgment around scope, risk, source authority, investigation boundaries, evidence, implementation drift, review findings, completion claims, corrections, long-session checkpoints, delegation context, and handoffs. Combine it with the domain Practices and project requirements that define what the system itself must do.

## Validation and recovery decisions

Use [Validate at the Boundary That Owns the Fact](./practices/implementation/validate-at-the-owning-boundary.md)
when the same data is parsed, normalized, authorized, or checked again across layers. It asks what
new invalid state is possible at each location and keeps external input, business-state, concurrency,
and independently justified trust checks distinct. An extra layer does not automatically need an
extra copy of the same rule.

Use [Give Recovery One Owner and an Explicit Outcome](./practices/implementation/make-recovery-behavior-explicit.md)
when a failure is about to gain a retry, empty default, alternate source, or degraded result. It
requires a known recoverable condition, a bounded owner, and an outcome the caller can understand.
Validation establishes a fact; recovery responds to a failure. Either decision can arise alone.

The surrounding requirements, planning, implementation, testing, and final-review Practices reinforce
these choices without requiring a new checklist or risk document for every change. Examples span
HTTP and CLI ingress, imports, typed domain calls, database constraints, caches, authorization, and
local lifecycle recovery. These rules preserve required protections and accepted degraded behavior;
they do not authorize deleting existing guards or changing project contracts without evidence.

## Non-goals

This Pack is not a workflow engine, task manager, test framework, compactor, automatic acceptance system, or replacement for project specifications. It does not prescribe a particular coding agent, repository layout, command, language, or framework. Practice retrieval or citation is not evidence that a task succeeded.

## Release history

- `0.5.0` is an unreleased candidate rewriting every Practice as a step-style decision procedure with an explicit stop, merging the two pre-work scope Practices into `decide-scope-and-stop-conditions` (33 to 32 entries), tiering severity into critical/warn/info, and retuning `applies_when` against the #17 keyword retrieval baseline. Publishing still requires an immutable release ref and Registry entry; this source version is not an installability claim.
- `0.4.0` is an unreleased candidate adding two independent validation and recovery Practices and refining seven existing entries against unnecessary defensive complexity.
- `0.3.1` adds a Practice that limits repository investigation to sources that can change the current decision and clarifies source roles without making broad reading a default.
- `0.3.0` rewrites the Pack for clearer standalone retrieval and adds a Practice for giving delegated Agents the decisions they need to preserve scope and quality.
- `0.2.0` is the immutable first complete 29-Practice release.
- `0.1.0` is an immutable one-entry installation placeholder retained only as release history. Its tag and content are not rewritten.

See [SOURCES.md](./SOURCES.md) for public provenance and the distinction between issue-explicit evidence and author synthesis.

Localized content under [`i18n/`](./i18n/) is provided for human-facing consumption and does not change the canonical runtime Pack, Registry release, retrieval inputs, or Practice IDs.
