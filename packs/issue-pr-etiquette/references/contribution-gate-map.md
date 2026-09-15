# Lorelum contribution gate map

Use this reference after a Practice's immediate decision says the change needs a repository's gate
rules. It records the repository-specific mechanisms of the Lorelum repositories that the Practices
deliberately keep out of their own bodies: what counts as contract-class, which artifacts each gate
requires, branch naming, review rounds, and freeze rules. Where this map and a repository's own
governing documents disagree, the repository wins.

## Source documents

- [`lorelum/lorelum-benchmark` AGENTS.md](https://github.com/lorelum/lorelum-benchmark/blob/main/AGENTS.md) — repo-level process gates, language policy, read-back rule
- [`lorelum/lorelum-benchmark` CONTRIBUTING.md](https://github.com/lorelum/lorelum-benchmark/blob/main/CONTRIBUTING.md) — fixture contribution operations and task freeze rule
- [`lorelum/lorelum-benchmark` docs/CHANGE_WORKFLOW.md](https://github.com/lorelum/lorelum-benchmark/blob/main/docs/CHANGE_WORKFLOW.md) — issue + change + PR workflow detail
- [`lorelum/lorelum-benchmark` docs/PR_REVIEW.md](https://github.com/lorelum/lorelum-benchmark/blob/main/docs/PR_REVIEW.md) — two-round review gate
- [`lorelum/lorelum` CONTRIBUTING.md](https://github.com/lorelum/lorelum/blob/main/CONTRIBUTING.md) — issue-driven workflow, branch naming, Conventional Commits, AI-assisted contribution rules
- [`lorelum/lorelum` issue templates](https://github.com/lorelum/lorelum/tree/main/.github/ISSUE_TEMPLATE) and [pull request template](https://github.com/lorelum/lorelum/blob/main/.github/PULL_REQUEST_TEMPLATE.md) — `[bug]` / `[feat]` title prefixes and the PR body sections

## Gate classification

`lorelum/lorelum-benchmark` treats changes to **suite, task, schema, evaluator, runner, treatment,
environment, experiment protocol, or record** as contract-class: before implementation they require
a linked issue plus a change artifact under `openspec/changes/<change-name>/` that passes
`openspec validate --strict`. Non-contract process or documentation fixes follow the direct-PR
exception: no issue, but the PR body must state root cause, fix boundary, and verification.

`lorelum/lorelum` is issue-driven and design-first: every change starts with an issue, and changes
to the product surface — Practice/Pack format, retrieval model, CLI commands, MCP interface — need
design alignment before code. One issue per PR.

## Branch naming

- `lorelum/lorelum-benchmark`: `codex/<change-name>` from the latest mainline.
- `lorelum/lorelum`: `feat/<scope>-<short>`, `fix/<scope>-<short>`, `spec/<topic>`, `docs/<topic>`.

## Commits and merge

Both repositories use Conventional Commits (types `feat`, `fix`, `perf`, `refactor`, `docs`,
`test`, `build`, `ci`, `chore`; imperative, lowercase subject within 72 characters). `lorelum/lorelum`
squash-merges, so the PR title becomes the commit and follows the same format. Address review
feedback with new commits; do not force-push mid-review unless asked.

## Review rounds (benchmark contract PRs)

PRs touching the contract-class list above must pass two independent read-only review rounds before
merge. Round 1 (`ai-code-review`) covers evaluation validity, reproducibility, public/private
isolation, lifecycle, and gates. Round 2 (`thermo-nuclear-code-quality-review`) covers structural
quality, dead logic, and the 1k-line file limit. Code changes are frozen during each round; record
findings and batch fixes between rounds.

## Language and posting rules

Issue and PR titles, bodies, reviews, and significant status comments default to Chinese in both
repositories unless the user requests otherwise; paths, commands, code identifiers, and untranslatable
proper nouns stay in their original language. Posts must use clear Markdown headings, paragraphs,
and lists, and the author must read back the saved post on GitHub — verifying nothing was flattened
or broken — before requesting review or merge.

## Freeze and templates

A benchmark task with existing run records is immutable: its statement, starter, evaluator, oracle
mapping, environment, and pinned evaluator version cannot change; correctness changes require a new
`v<version + 1>` directory. Issues in `lorelum/lorelum` open with the `[bug]` or `[feat]` title
prefix and require the duplicate-search confirmation from the issue templates.
