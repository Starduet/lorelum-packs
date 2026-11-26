# Project-local Pack guide

Use this reference after deciding that guidance belongs to one repository. It gives a concrete source layout and small verification path; it does not publish anything.

## Choose the layer and base

| Need | Place/configure it this way |
| --- | --- |
| Guidance belongs to one repository or ordinary directory | Put the Pack under that directory's `.lorelum/packs/`. Git is not required. |
| Unrelated repositories must install the reviewed Pack | Prepare a separate versioned Registry release; do not point a Registry release at a mutable project tree. |
| The normal user Store remains a lowest-priority baseline | Omit `base` or set `base: user`. |
| The local layer must be self-contained | Set `base: none` in that layer's `config.yaml`. |
| A child changes one parent Practice | Add only the child Practice with the same ID. Other parent Practices remain active. |
| A child must not inherit any parent layer | Use `inherit: false` deliberately; it removes all parent-layer Pack/config input. |

## Start one local Pack

Run `lore init` from the directory where the local layer should begin. It creates an editable `.lorelum/config.yaml` once and never overwrites an existing file.

```text
repository/
├── .lorelum/
│   ├── config.yaml
│   └── packs/
│       └── service-delivery/
│           ├── pack.yaml
│           └── practices/
│               └── service-delivery.rollback.md
└── service source files
```

```yaml
# .lorelum/packs/service-delivery/pack.yaml
name: service-delivery
version: 0.1.0
description: Repository-owned release and rollback decisions.
applies_to:
  - service-delivery
```

The runtime format requires `id`, `title`, `stage`, `tech_stack`, and `applies_when`; Practice
`severity` is optional. Structured anti-patterns use `id`, `name`, `description`, and `severity`.
The body has no fixed heading set: include only what the decision needs. Localized companions follow
the same relative Practice paths outside runtime input and do not copy the YAML frontmatter.

This concise example uses no body headings:

```markdown
---
id: service-delivery.rollback
title: Require a Rollback Plan for Stateful Releases
stage: implementation
tech_stack:
  - service-delivery
applies_when: a release changes persistent data or an externally visible contract, and the reviewer must decide whether a tested rollback plan is required before approval
severity: warn
anti_patterns:
  - id: service-delivery.unverified-rollback
    name: Rollback assumed from a deployment switch
    description: Treating the ability to redeploy an old binary as proof that changed data and contracts can also be restored.
    severity: warn
---

Before approving a release that changes persistent data or an external contract, review the tested
steps for restoring that data or contract. Redeploying an old binary alone does not establish that
the changed state can be restored.
```

Do not put SQLite indexes, semantic vectors, model files, Backend state, or cache directories under `.lorelum`. They are user-owned derived state and can be recreated from current Pack source.

## Validate where it will be used

From the repository directory:

```sh
lore format .lorelum/packs/service-delivery
lore validate .lorelum/packs/service-delivery
lore context status
lore query "does this release need a rollback plan" --mode keyword
lore get service-delivery.rollback
```

`format` and `validate` check the Pack source. `context status`, keyword query, and `get` confirm that the current directory discovered the intended local winner without requiring a model. For an automated fixture outside the current directory, use `--project-root <directory-containing-.lorelum>`.

## Add a child overlay without copying a Pack

If `repository/` has a root `platform.release` Practice and `repository/services/payments/` needs a stricter rule, place only the replacement under:

```text
services/payments/.lorelum/packs/platform/practices/platform.release.md
```

The child same-ID Practice wins when queried from `services/payments/`; parent-only Practices remain available. Use a child `config.yaml` only for a real config change, such as `base: none`, an explicit Pack priority, or intentional `inherit: false`. Verify both one overridden ID and one parent-only ID from the child directory.

## Keep local source and release distribution separate

Repository-local source is ready after it validates and activates in the intended context. It does not need `lore pack install`, a Registry entry, or an immutable tag. If the Pack later becomes a cross-repository product, create a separate release candidate, update its Registry descriptor, tag the reviewed merge commit, and verify the supported install path before claiming it is installable.
