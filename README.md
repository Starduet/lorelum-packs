# Lorelum Knowledge Packs

This repository is the official public catalog for installable Lorelum Knowledge Packs. Each directory under `packs/` is a self-contained Pack root using the public `pack.yaml + practices/**/*.md + decisions.yaml?` format. A Pack may also include on-demand `references/`, `assets/`, and `scripts/` resources when its Practices route a reader to them with a `resource:` Markdown link.

## Catalog

- `issue-pr-etiquette@0.1.0` — 12 repository-neutral Practices for filing issues, opening pull requests, and taking part in reviews: single-problem convergence with testable acceptance criteria, cited evidence, gate classification, single declared scope, conventional titles, cold-reviewer PR bodies, diff hygiene, review discipline, and honest AI-assistance disclosure. Bundles issue and PR skeleton templates as `assets/` resources.
  - [简体中文本地化](./packs/issue-pr-etiquette/i18n/zh-CN/README.md) is available as non-runtime companion content.
- `pack-creator@0.2.0` — unreleased candidate with 27 domain-neutral Practices for defining, designing, authoring, reviewing, evaluating, localizing, and releasing Packs, including repository-local project layers. The latest published release remains `0.1.0` until `pack-creator-v0.2.0` is created at the reviewed merge commit and the supported install path succeeds.
  - [简体中文本地化](./packs/pack-creator/i18n/zh-CN/README.md) is available as non-runtime companion content.
- `react-web-craft@0.1.0` — 24 Practices for React web application design and performance across component state, async data flow, code loading, rendering, and component composition.
  - [简体中文本地化](./packs/react-web-craft/i18n/zh-CN/README.md) is available as non-runtime companion content.
- `agentic-coding@0.4.0` — unreleased candidate with 33 decision-focused Practices, including validation at responsible boundaries and explicit recovery behavior. The latest published release remains `0.3.1` until a new immutable ref and Registry entry exist.
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

## Evaluation fixtures and scripts

`fixtures/<pack>/` holds `evaluation_only` hypotheses, never runtime input: `practice-catalog.yaml` (per-Practice retrieval and behavior contrasts) and `workflows.yaml` (cross-Practice scenarios). `fixtures/agentic-coding/queries.yaml` additionally holds a retrieval query set — 3 positive and 2 neighbor queries per Practice, worded to avoid restating Practice text — whose expected selections are declared before any run. `fixtures/agentic-coding/baselines/` stores recorded runs. Fixtures state hypotheses, not proof of retrieval or downstream quality.

`scripts/eval-queries` evaluates a query set against an installed Pack by looping the public `lore` CLI (Python 3.9+ with PyYAML; no CLI changes). It supports `--mode keyword|semantic|both`; when the semantic index cannot build on a machine (for example the known `embedding.deadline-exceeded` on some Windows x64 hosts), the run is marked degraded with the failure code instead of failing. It reports per-query hits, positive top-k hit rates, the neighbor confusion matrix, and `--baseline` regression diffs.

```sh
# Isolated-store run against a registry release, writing a JSON artifact and Markdown report.
python scripts/eval-queries --mode both --ensure-install agentic-coding@0.4.0 \
  --store-root tmp/eval-store --out run.json --report run.md

# Compare a later run (for example a rewritten Practice set) against a recorded baseline.
python scripts/eval-queries --mode keyword --baseline fixtures/agentic-coding/baselines/<baseline>.json

# Promotion gate for a future release: every installed Practice must have fixture queries,
# and the positive top-3 hit rate must clear the team's bar. Exits non-zero otherwise.
python scripts/eval-queries --mode keyword --require-coverage --min-top3 0.90 \
  --ensure-install agentic-coding@0.5.0 --store-root tmp/eval-store \
  --baseline fixtures/agentic-coding/baselines/<previous-release>.json
```

### Updating the query set

The query set is a maintained fixture, not a generated one: it grows with the catalog through the promotion flow, and the gates make skipping a step visible.

- **A change that adds a Practice adds its queries in the same change**: 3 positive + 2 neighbor queries in `fixtures/agentic-coding/queries.yaml`. Neighbor expectations follow the practice-catalog `nearest_neighbor` map — update the catalog first if the new Practice changes which neighbor is nearest for an existing one. `--require-coverage` fails any run against a Pack containing a Practice with no positive queries.
- **Queries must be written in situation wording, not the Practice's own words.** Check every change with `python scripts/eval-queries --check-discipline --mode keyword --limit 1` — it fails on any 4+-word run shared with an installed Practice's title or `applies_when`, because such a query matches the keyword index by quotation and proves nothing about retrieval.
- **When Practices merge or are removed, migrate the affected queries' `expect` to the successor Practice ID** and re-run; per issue #17, an old query should hit its successor.
- **The team gate is recorded in the fixture** (`min_top3`); every run enforces it by default. `--min-top3 <rate>` overrides it for a single run, and a degraded semantic mode is reported as not evaluated rather than silently passing.

```sh
# Preflight for a change that touches Practices or queries.
python scripts/eval-queries --mode keyword --require-coverage --check-discipline \
  --ensure-install agentic-coding@0.4.0 --store-root tmp/eval-store \
  --baseline fixtures/agentic-coding/baselines/<previous-release>.json
```

Existing queries double as canaries: re-running them against a new release with `--baseline` reports whether newly added Practices steal hits meant for existing ones.

## Repository layout

```text
.lorelum/registry.yaml
fixtures/
  agentic-coding/
    practice-catalog.yaml
    workflows.yaml
    queries.yaml
    baselines/
scripts/
  eval-queries
packs/
  agentic-coding/
    pack.yaml
    README.md
    SOURCES.md
    practices/
    i18n/
  issue-pr-etiquette/
    pack.yaml
    README.md
    SOURCES.md
    practices/
    assets/
    i18n/
  pack-creator/
    pack.yaml
    README.md
    SOURCES.md
    practices/
    references/
    assets/
    scripts/
    i18n/
  react-web-craft/
    pack.yaml
    README.md
    SOURCES.md
    practices/
    i18n/
```

The `packs/<name>` path is this catalog's organization convention. A project-authored Pack may instead live at `.lorelum/packs/<name>` in its own project; the Pack root format itself is unchanged.
