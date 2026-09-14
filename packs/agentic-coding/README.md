# Agentic Coding

`agentic-coding@0.3.1` is a tool-neutral Knowledge Pack of 31 decision-focused Practices for AI agents doing software engineering: clarifying goals and authority, controlling scope and investigation, making proportionate implementation and validation choices, and handling reviews, delivery, handoffs, and recovery with trustworthy evidence.

Canonical English · [简体中文](./i18n/zh-CN/README.md)

The Practices cover requirements, planning, implementation, testing, verification, review, delivery, correction, and context recovery. Each entry targets one decision point and is intended to remain useful when retrieved alone; consumers should retrieve only the few entries relevant to the current work and moment.

## Scope

Use this Pack to improve engineering judgment around scope, risk, source authority, investigation boundaries, evidence, implementation drift, review findings, completion claims, corrections, long-session checkpoints, delegation context, and handoffs. Combine it with the domain Practices and project requirements that define what the system itself must do.

## Non-goals

This Pack is not a workflow engine, task manager, test framework, compactor, automatic acceptance system, or replacement for project specifications. It does not prescribe a particular coding agent, repository layout, command, language, or framework. Practice retrieval or citation is not evidence that a task succeeded.

## Release history

- `0.3.1` adds a Practice that limits repository investigation to sources that can change the current decision and clarifies source roles without making broad reading a default.
- `0.3.0` rewrites the Pack for clearer standalone retrieval and adds a Practice for giving delegated Agents the decisions they need to preserve scope and quality.
- `0.2.0` is the immutable first complete 29-Practice release.
- `0.1.0` is an immutable one-entry installation placeholder retained only as release history. Its tag and content are not rewritten.

See [SOURCES.md](./SOURCES.md) for public provenance and the distinction between issue-explicit evidence and author synthesis.

Localized content under [`i18n/`](./i18n/) is provided for human-facing consumption and does not change the canonical runtime Pack, Registry release, retrieval inputs, or Practice IDs.
