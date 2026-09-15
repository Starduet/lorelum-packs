# Sources and provenance

This Pack fuses two layers of public Lorelum material into generalized contributor Practices: the written contribution rules of the Lorelum repositories, and two public exemplars that demonstrate expression above those rules. Where the two layers were compared, the rules supplied the skeleton (which gate exists, what must be stated) and the exemplars supplied the demonstrated upper bound of expression (evidence chains, testable criteria, verbatim verification, reviewer notes). Repository-specific mechanisms were deliberately kept out of Practice bodies and collected in the contribution gate map reference.

## Evidence labels

- **Rule-explicit** means a governing document of a Lorelum repository states the requirement: `lorelum/lorelum-benchmark` root AGENTS.md, CONTRIBUTING.md, docs/CHANGE_WORKFLOW.md, docs/PR_REVIEW.md, or `lorelum/lorelum` CONTRIBUTING.md.
- **Exemplar-derived synthesis** means a Practice generalizes structure demonstrated by a public exemplar — issue #150 or PR #162 — that the written rules do not explicitly require.
- **Rule-and-exemplar fusion** means the Practice keeps a rule's mandatory skeleton and takes its demonstrated good expression from an exemplar.

Public sources:

- [`lorelum/lorelum-benchmark` AGENTS.md](https://github.com/lorelum/lorelum-benchmark/blob/main/AGENTS.md) — gate classification, collaboration-language default, Markdown structure, and read-back verification rules
- [`lorelum/lorelum-benchmark` CONTRIBUTING.md](https://github.com/lorelum/lorelum-benchmark/blob/main/CONTRIBUTING.md) — fixture contribution operations and task freeze rule
- [`lorelum/lorelum-benchmark` docs/CHANGE_WORKFLOW.md](https://github.com/lorelum/lorelum-benchmark/blob/main/docs/CHANGE_WORKFLOW.md) — single-problem issue convergence, single declared PR scope, direct-PR root cause/boundary/verification duty
- [`lorelum/lorelum-benchmark` docs/PR_REVIEW.md](https://github.com/lorelum/lorelum-benchmark/blob/main/docs/PR_REVIEW.md) — two-round read-only review gate and code freeze during rounds
- [`lorelum/lorelum` CONTRIBUTING.md](https://github.com/lorelum/lorelum/blob/main/CONTRIBUTING.md) — issue-driven design-first workflow, branch naming, Conventional Commits, squash merge, new-commits-for-feedback, AI-assisted contribution disclosure
- [Issue #150: privacy-safe feedback loop](https://github.com/lorelum/lorelum/issues/150) — exemplar issue: cited evidence chain, direction-not-design statement, non-goals, testable acceptance criteria, related-work map
- [PR #162: Pack-native resource support](https://github.com/lorelum/lorelum/pull/162) — exemplar PR: conventional title, cold-reviewer body with explicit non-behavior and verbatim commands, AI review findings documented in-body
- [`lorelum/lorelum` issue and pull request templates](https://github.com/lorelum/lorelum/tree/main/.github) — `[bug]`/`[feat]` prefixes and the template sections distilled into this Pack's assets

## Practice map

| Practice ID | Provenance | Relationship to source |
| ----------- | ---------- | ---------------------- |
| `issue-pr-etiquette.issue.converge-on-one-problem-with-testable-acceptance-criteria` | Rule-and-exemplar fusion: CHANGE_WORKFLOW.md; #150 | The workflow doc requires single-problem convergence with acceptance and verification wording; #150 demonstrates the checkbox form reviewers can check without the author. |
| `issue-pr-etiquette.issue.ground-the-problem-in-cited-evidence` | Exemplar-derived synthesis: #150 | The written rules require structured issues but not citation; #150's linked incident chain and one-line related-work roles are generalized into the Practice. |
| `issue-pr-etiquette.issue.separate-direction-from-design-and-state-non-goals` | Exemplar-derived synthesis: #150 | #150 states it "establishes the product and governance objective, not the implementation design" and defers named decisions out of scope; no rule requires this separation. |
| `issue-pr-etiquette.communication.write-in-the-repos-collaboration-language-with-clean-markdown` | Rule-explicit: benchmark AGENTS.md | The language default (Chinese for collaborator-facing posts, identifiers untranslated) and Markdown structure rule are generalized from "the declared collaboration language". |
| `issue-pr-etiquette.communication.read-back-your-post-before-requesting-review` | Rule-explicit: benchmark AGENTS.md | The read-back-after-posting verification rule is stated nearly verbatim and generalized beyond the source repository. |
| `issue-pr-etiquette.pull-request.match-the-change-to-the-required-upstream-gate` | Rule-explicit: AGENTS.md, CHANGE_WORKFLOW.md, lorelum/lorelum CONTRIBUTING.md | The contract-class versus direct-PR classification and the root-cause/boundary/verification duty are rules; the OpenSpec mechanism behind them is demoted to the gate-map reference. |
| `issue-pr-etiquette.pull-request.keep-one-pr-to-one-declared-scope` | Rule-explicit: CHANGE_WORKFLOW.md, lorelum/lorelum CONTRIBUTING.md | "Every PR keeps a single declared scope" and one-issue-per-PR are stated rules; the drive-by temptation scenario is author synthesis. |
| `issue-pr-etiquette.pull-request.title-and-commit-conventionally` | Rule-explicit: lorelum/lorelum CONTRIBUTING.md | Conventional Commits, imperative lowercase subjects within 72 characters, and squash-merge title behavior are stated rules. |
| `issue-pr-etiquette.pull-request.write-the-pr-body-for-a-cold-reviewer` | Rule-and-exemplar fusion: CHANGE_WORKFLOW.md, PR template; #162 | The rules require root cause, fix boundary, and verification; #162 demonstrates non-behavior statements, verbatim commands, and reviewer notes that make a body cold-readable. |
| `issue-pr-etiquette.pull-request.keep-secrets-and-private-material-out-of-the-diff` | Rule-explicit: PR template checklist, benchmark sanitization gates | The no-secrets checklist item and benchmark sanitization practice are generalized to a final pre-review diff scan with rotation-first handling. |
| `issue-pr-etiquette.review.address-feedback-with-new-commits-and-freeze-during-review` | Rule-explicit: lorelum/lorelum CONTRIBUTING.md, docs/PR_REVIEW.md | New-commits-not-force-push is a main-repo rule; the round freeze comes from the benchmark two-round gate, generalized without naming the rounds. |
| `issue-pr-etiquette.review.disclose-ai-assistance-and-its-review-findings` | Rule-and-exemplar fusion: lorelum/lorelum CONTRIBUTING.md; #162 | The rules require the AI-assisted checkbox and reject "reviewed every line" as acceptance; #162 demonstrates findings documented in-body as actionable evidence. |

## Synthesis boundary

The written rules and the exemplars were compared rather than stacked: where an exemplar demonstrated practice above the rules (evidence chains, direction/design separation, non-behavior statements, documented AI findings), the Practice adopts the exemplar's expression as the target; where the rules carry repository-specific machinery (OpenSpec artifacts, named review rounds, branch schemes, task freeze), the Practice keeps only the general decision and the machinery lives in the gate-map reference. Provenance explains why guidance was included; it does not prove the Practices retrieve correctly or improve contributor behavior. Fixtures remain evaluation hypotheses until run against a retrieval system and representative tasks.
