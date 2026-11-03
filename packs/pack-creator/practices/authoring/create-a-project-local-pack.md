---
anti_patterns:
  - description: The author installs a still-changing repository Pack into a global Store, hand-creates a cache under .lorelum, or writes only a README and expects Lorelum to discover it without a Pack root and canonical Practice files.
    id: pack-creator.authoring.local-pack-without-source-contract
    name: Local Pack bypasses the source contract
    severity: warn
applies_when: an author has decided that guidance belongs to one repository and must create a queryable .lorelum Pack without requiring a global installation or committing derived index state
id: pack-creator.authoring.create-a-project-local-pack
severity: warn
stage: authoring
tech_stack:
  - lorelum-pack-authoring
title: Create a Project-Local Pack
---

## When to apply

If the guidance should live with one repository, create its Pack files there before expecting
Practices to appear in `lore query` or `lore get`. This covers creating one Pack root. How parent
and child directories combine, and whether the intended rules actually take effect, need separate
attention.

## Guidance

From the directory where the local layer should begin, run `lore init` once. It creates an editable
`.lorelum/config.yaml` if missing and leaves an existing file unchanged. Then create a normal Pack
root under `.lorelum/packs/<pack-name>/`: `pack.yaml` declares the Pack name and version, and
`practices/` contains canonical Markdown Practices with the required frontmatter. Git is not
required.

Keep the project config minimal. Omit fields to use the normal inherited/default behavior; add
`base: none` only when this directory must not use the selected user Store. Do not create index,
vector, model, or Backend files under `.lorelum`: Lorelum keeps derived query state in the user
cache and rebuilds it from the Pack source when needed.

Run `lore format .lorelum/packs/<pack-name>` and `lore validate .lorelum/packs/<pack-name>`, then
inspect `lore context status` from the intended directory. Use a keyword query and
`lore get <practice-id>` to confirm the source Practice is visible without needing a model. Stop
when the Pack validates, the intended directory discovers it, and the repository contains only
canonical source/config files rather than generated index state. For a copyable tree, starter
Practice, and command sequence, see
[the project-local Pack guide](resource:references/project-local-packs.md).

## Anti-pattern

An API repository needs a temporary-but-reviewable Pack for its compatibility policy. The author
runs `lore pack install` into a personal Store, writes the policy into an installed Pack view, and
commits a SQLite index so teammates can see results. Teammates now need a matching Store state, the
source of truth is outside the repository, and every edit creates cache churn. The author should
instead commit `.lorelum/packs/api-compatibility/pack.yaml` and its canonical Practice files; each
user's cache remains disposable derived state.

## Why

A project layer contains repository-owned guidance discovered from the working directory. Keeping
the Pack root and canonical Practices in the repository lets ordinary review, branches, worktrees,
and directory use work without a global install or generated files to clean up.

## Exceptions and boundaries

`lore init` creates only the layer marker/config, not a Pack skeleton and not a model setup. An
explicit `--project-root` is useful for testing another directory, but normal use should run from
the directory whose layer the developer is editing. This Practice does not publish the Pack; use the
Registry release path only when independent installation is the actual goal.

## Example

At the root of a service repository, an author runs `lore init` and creates
`.lorelum/packs/service-delivery/pack.yaml` plus
`.lorelum/packs/service-delivery/practices/service-delivery.rollback.md`. The Practice tells a
release reviewer when a rollback plan is required. After format and validation, the author runs
`lore query "does this deployment need a rollback plan" --mode keyword` from the repository root and
reads the returned ID with `lore get`. No global Pack install, model download, or repository cache
file is needed.
