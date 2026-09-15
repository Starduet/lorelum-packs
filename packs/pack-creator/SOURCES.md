# Sources and provenance

This Pack combines Lorelum's public format and retrieval boundaries with sanitized lessons from authoring and reviewing a multi-stage Knowledge Pack. It generalizes the authoring decisions rather than reproducing one Pack's subject matter, private prompts, contributor identities, or repository-local operating details.

## Evidence labels

- **Format-explicit** means the public Lorelum format or Registry contract directly establishes the structural or release requirement.
- **Issue-derived synthesis** means a Practice generalizes a content, retrieval, evidence, or scope boundary discussed in a public Lorelum issue.
- **Pack-authoring synthesis** means a Practice was generalized from a sanitized authoring and review retrospective, including rejected abstract wording, unrealistic examples, missing delegation context, trigger collisions, localization review, and remote installation checks.
- **Protocol-aligned synthesis** means a Practice records the reviewed resource-directory, locator, and non-execution boundary of the current Lorelum Pack protocol; it does not by itself claim that a future released version is installable.

Public sources:

- [ADR 0003: Practice and Pack format](https://github.com/lorelum/lorelum/blob/main/docs/adr/0003-practice-pack-format.md)
- [ADR 0008: Pack Registry and user-scope installation](https://github.com/lorelum/lorelum/blob/main/docs/adr/0008-pack-registry-and-user-scope-install.md)
- [ADR 0009: Pack localization authoring assets](https://github.com/lorelum/lorelum/blob/main/docs/adr/0009-pack-localization-authoring.md)
- [Issue #28: Practice retrieval and injection at critical moments](https://github.com/lorelum/lorelum/issues/28)
- [Issue #32: Practice guidance before context compaction](https://github.com/lorelum/lorelum/issues/32)
- [Issue #35: Reward hacking and over-engineering in agent coding](https://github.com/lorelum/lorelum/issues/35)
- [`agentic-coding` clarity revision PR #6](https://github.com/lorelum/lorelum-packs/pull/6), used as public evidence of concrete wording, scenario, and authoring-review changes, not as a required template. The final [`agentic-coding@0.3.0`](https://github.com/lorelum/lorelum-packs/tree/agentic-coding-v0.3.0/packs/agentic-coding) tag shows the resulting Pack content, not the full review process.

## Practice map

| Practice ID                                                                      | Provenance                                                    | Relationship to source                                                                                                                                |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pack-creator.discovery.define-pack-decision-outcome`                            | Issue-derived synthesis: #28, #35; Pack-authoring synthesis   | Generalizes the difference between improving a real decision and producing an impressive collection of topics or artifacts.                           |
| `pack-creator.discovery.ground-content-in-sources-and-observed-needs`            | Issue-derived synthesis: #28, #32; Pack-authoring synthesis   | Adapts the fact, assumption, and evidence boundary to Pack sources so author synthesis remains visible rather than acquiring false authority.         |
| `pack-creator.discovery.identify-retrieval-moments`                              | Issue-derived synthesis: #28, #32; Pack-authoring synthesis   | The issues motivate guidance at consequential moments; this Practice turns that boundary into a collection-level authoring decision.                  |
| `pack-creator.design.decompose-one-decision-per-practice`                        | Format-explicit: ADR 0003; Issue-derived synthesis: #28       | ADR 0003 defines discrete retrievable Practices; the one-decision boundary is author synthesis for making that unit useful when retrieved alone.      |
| `pack-creator.design.separate-neighboring-triggers`                              | Issue-derived synthesis: #28; Pack-authoring synthesis        | Generalizes review findings where individually plausible entries still competed for the same query and needed a meaningful routing distinction.       |
| `pack-creator.design.keep-each-practice-standalone`                              | Format-explicit: ADR 0003; Issue-derived synthesis: #28, #32  | Selective retrieval and context loss require a Practice to carry the decisive facts rather than depend on hidden Pack order or omitted context.       |
| `pack-creator.authoring.write-discriminating-applies-when`                       | Format-explicit: ADR 0003; Pack-authoring synthesis           | ADR 0003 requires `applies_when`; the discriminating decision-moment test generalizes trigger tuning and nearest-neighbor review.                     |
| `pack-creator.authoring.write-concrete-guidance-and-stop-condition`              | Issue-derived synthesis: #35; Pack-authoring synthesis        | Generalizes the need for an executable intervention with a stopping point so advice does not become ceremony or unbounded work.                       |
| `pack-creator.authoring.use-realistic-failure-mechanisms`                        | Issue-derived synthesis: #28, #35; Pack-authoring synthesis   | Generalizes rejected examples that proved a rule only by making the actor implausibly careless instead of exposing a credible local incentive.        |
| `pack-creator.authoring.make-examples-self-contained`                            | Issue-derived synthesis: #32; Pack-authoring synthesis        | Applies context-hygiene lessons to examples so a reviewer does not need an omitted incident, repository, or earlier Practice to reconstruct meaning.  |
| `pack-creator.authoring.give-anti-pattern-and-example-distinct-jobs`             | Format-explicit: ADR 0003; Pack-authoring synthesis           | ADR 0003 defines structured anti-patterns; the section-role distinction comes from removing repeated scenarios that added no new review evidence.     |
| `pack-creator.authoring.prefer-plain-language-and-concrete-referents`            | Pack-authoring synthesis                                      | Generalizes human review where dense abstract nouns and coined terms obscured the actor, object, action, and state in both English and Chinese.       |
| `pack-creator.authoring.explain-the-direct-causal-reason`                        | Pack-authoring synthesis                                      | Generalizes review that replaced philosophical downstream claims with the first important consequence of following or ignoring the instruction.       |
| `pack-creator.authoring.write-specific-exceptions-and-boundaries`                | Issue-derived synthesis: #28, #35; Pack-authoring synthesis   | Generalizes the need to state recognizable override conditions without weakening a default rule into a list of broad domain labels.                   |
| `pack-creator.review.run-subtractive-content-review`                             | Issue-derived synthesis: #35; Pack-authoring synthesis        | Extends subtractive engineering review to Pack content: remove duplication and ceremony while retaining distinctions needed for correct retrieval.    |
| `pack-creator.evaluation.test-retrieval-with-contrasting-queries`                | Issue-derived synthesis: #28; Pack-authoring synthesis        | Turns critical-moment retrieval into testable positive, paraphrase, near-miss, and nearest-neighbor hypotheses rather than title-matching fixtures.   |
| `pack-creator.evaluation.separate-structural-and-semantic-evidence`              | Issue-derived synthesis: #28, #35; Pack-authoring synthesis   | Generalizes evidence-scoped completion: schema, human review, retrieval behavior, and downstream Agent behavior support different claims.             |
| `pack-creator.localization.localize-for-human-review-without-forking-runtime`    | Format-explicit: ADR 0009; Pack-authoring synthesis           | ADR 0009 defines canonical runtime content and mirrored localization assets; authoring review supplies the natural-language and fidelity gates.       |
| `pack-creator.release.preserve-versioned-content-and-provenance`                 | Format-explicit: ADR 0008, ADR 0009; Pack-authoring synthesis | Registry refs and localization digests require reproducible canonical content, while the authoring retrospective motivates explicit synthesis labels. |
| `pack-creator.release.verify-the-supported-install-path-before-claiming-release` | Format-explicit: ADR 0008; Pack-authoring synthesis           | ADR 0008 defines the Registry-to-LocalStore path; a sanitized release retrospective showed local validation cannot prove that remote path works.      |

## Resource-practice provenance

| Practice ID | Provenance | Relationship to source |
| --- | --- | --- |
| `pack-creator.authoring.link-pack-resources-from-the-practice` | Protocol-aligned synthesis; Pack-authoring synthesis | Keeps the trigger, action, reason, exception, and stop condition in one retrievable Practice, with `resource:` links used only for supplemental same-Pack files. |
| `pack-creator.authoring.choose-reference-asset-or-script` | Protocol-aligned synthesis; Pack-authoring synthesis | Distinguishes read-on-demand references, copy-before-edit assets, and explicitly authorized scripts without inventing descriptors or execution authority. |
| `pack-creator.evaluation.verify-resource-integrity-without-overclaiming` | Protocol-aligned synthesis; Pack-authoring synthesis | Separates resource structure, selected-artifact preservation, explicit script behavior, retrieval selection, and downstream Agent evidence. |

The release Practices also apply to resource-only updates: changed bytes require a new immutable Pack
artifact and release evidence even when an unchanged Practice retains its canonical digest.

## Synthesis boundary

Provenance explains why guidance was included; it does not prove that the resulting Pack improves retrieval or downstream behavior. Fixtures remain evaluation hypotheses until run against a retrieval system and representative Agent tasks.
