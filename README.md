# Lorelum Knowledge Packs

This repository is the official public catalog for installable Lorelum Knowledge Packs. Each directory under `packs/` is a self-contained Pack root using the public `pack.yaml + practices/**/*.md + decisions.yaml?` format.

## Catalog

- `pack-creator@0.1.0` — 20 domain-neutral Practices for defining, designing, authoring, reviewing, evaluating, localizing, and releasing Lorelum Packs.
  - [简体中文本地化](./packs/pack-creator/i18n/zh-CN/README.md) is available as non-runtime companion content.
- `react-web-craft@0.1.0` — 24 Practices for React web application design and performance across component state, async data flow, code loading, rendering, and component composition.
  - [简体中文本地化](./packs/react-web-craft/i18n/zh-CN/README.md) is available as non-runtime companion content.
- `agentic-coding@0.3.1` — 31 decision-focused Practices for AI agents doing software engineering: goals and authority, scope and investigation, implementation and validation, reviews, delivery, handoffs, and recovery.
  - [简体中文本地化](./packs/agentic-coding/i18n/zh-CN/README.md) is available as non-runtime companion content.

## Use Packs

Pack commands use the user-level LocalStore by default. Use `--store-root <path>` only when a
worktree, test, or other isolated environment needs its own Pack and derived-index data; it does not
select a model, Backend address, or runtime directory.

### Browse installed Packs and Practices

```sh
# List installed Packs, or include their descriptions and applicability metadata.
lore pack list
lore pack list --details

# List one Pack's Practice catalog, then read one exact Practice in full.
lore pack list agentic-coding
lore get agentic-coding.testing.classify-failure-before-changing-test
```

`lore pack list <pack>` returns compact Practice summaries (`id`, `title`, and `applies_when`).
`lore get <practice-id>` reads the selected Practice's complete guidance, anti-patterns, and source
metadata.

### Install or update

```sh
# Install the latest stable release into a Store where the Pack is not yet installed.
lore pack install agentic-coding

# Use `@version` to select an exact release.
lore pack install <pack>
lore pack install <pack>@<version>
lore pack install agentic-coding@0.3.1
lore pack update <pack>
lore pack update <pack>@<version>
lore pack update agentic-coding@0.3.1
```

Omit `@version` to resolve the Registry's latest stable release. `install` is for a new Pack; use
`update` when replacing a Pack that is already installed. The Lorelum CLI contains the official
Registry repository name, not the Pack content: it reads the Registry descriptor, resolves the
release, validates the Pack, and writes it to the selected LocalStore.

### Remove a Pack

```sh
lore pack remove agentic-coding
```

### Use a different public Registry or an isolated Store

Another public GitHub repository can expose the same layout and be selected explicitly:

```sh
lore pack install agentic-coding@0.3.1 --registry owner/repository
lore pack update agentic-coding --registry owner/repository

# The global --store-root option can appear before or after the Pack command.
lore --store-root ./tmp/lore-store pack install agentic-coding
lore pack list --store-root ./tmp/lore-store
```

Custom registries must expose `.lorelum/registry.yaml` from a supported public GitHub repository.

## Repository layout

```text
.lorelum/registry.yaml
packs/
  agentic-coding/
    pack.yaml
    README.md
    SOURCES.md
    practices/
    i18n/
  pack-creator/
    pack.yaml
    README.md
    SOURCES.md
    practices/
    i18n/
  react-web-craft/
    pack.yaml
    README.md
    SOURCES.md
    practices/
    i18n/
```

The `packs/<name>` path is this catalog's organization convention. A project-authored Pack may instead live at `.lorelum/packs/<name>` in its own project; the Pack root format itself is unchanged.
