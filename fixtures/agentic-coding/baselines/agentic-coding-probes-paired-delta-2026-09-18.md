# Decision-probe paired comparison: agentic-coding 0.4.0 vs 0.5.0 (2026-09-18)

A lightweight behavior check of the issue #19 rewrite: same probes, same answering
agent, old and new pack content — the delta between the two runs is attributable to
the pack, not to the responder.

## Method

- 10 probes emitted from the 0.5.0 practice-catalog fixture (`tmp/catalog-050.yaml`,
  PR #30 head @449da50) into `tmp/probes-v2-040` (store `tmp/eval-store-040`) and
  `tmp/probes-v2-050` (store `tmp/eval-store-050`). Blind prompts are byte-identical
  across the two dirs (verified), so one blind answer set serves both runs.
- One fresh, uncontaminated answering agent answered **blind once**, then all 0.4.0
  injected prompts, then all 0.5.0 injected prompts, then scored both dirs against the
  same manifest rubrics (`tmp/probe-run-v2-040.{json,md}`, `tmp/probe-run-v2-050.{json,md}`).
- Injection content is each store's real top-1 keyword hit, so retrieval differences
  between versions flow into the run exactly as a `lore` consumer would see them.

Injection sources differed on 2 of 10 probes:

- `requirements.resolve-source-authority`: 0.4.0 retrieved `run-subtractive-review-before-commit`
  (a known 0.4.0 confusion pair); 0.5.0 retrieved the correct practice.
- `planning.decide-scope-and-stop-conditions`: 0.4.0 retrieved one old parent
  (`admit-only-currently-justified-work`); 0.5.0 retrieved the merged practice.

## Result (advisory protocol)

| run | moved-toward | no-change | harmful |
|---|---|---|---|
| 0.4.0 (`agentic-coding-0.4.0-probes-2026-09-18.json`) | 1 | 9 | 0 |
| 0.5.0 (`agentic-coding-0.5.0-probes-paired-2026-09-18.json`) | 2 | 8 | 0 |

The runs diverge on exactly one probe: `decide-scope-and-stop-conditions` went
`no-change` (old parent formalized admission labels but supplied no defer list or
replanning signals) → `moved-toward` (merged practice supplied exactly those). No
probe scored better under 0.4.0 than under 0.5.0. `plan-sufficient-evidence` moved
toward under both versions.

## Negative controls (instrument validation)

A corrupted body was produced by inverting the merged practice's guidance
(future-value admission rule, polish-until-done finish condition) while keeping it
plausible; the rubric's `forbidden_behavior` names exactly those inversions.

1. **Advisory mode** ("use it if it helps, ignore it if it does not"): a fresh
   responder **detected and rejected** the corrupted practice — verdict `no-change`,
   no forbidden behavior. Finding: advisory-mode `0 harmful` is *weak* evidence about
   content quality; a responder with a correct blind answer masks bad injections.
   Advisory sensitivity exists only where the blind answer has headroom (both
   moved-toward probes were blind-incomplete).
2. **Compliance mode** ("a team practice you have decided to follow"): the same
   corrupted body, followed, produced **both** forbidden behaviors and 0/4 expected
   elements — verdict `harmful`. The instrument detects bad content once the
   responder actually applies what was injected.

## Compliance coverage (direct content-quality readout)

Same situation, same responder, instruction to apply the injected practice;
scored against the rubric's four expected elements (admission labels with current
reason / observable finish condition per required item / recorded defer list /
named replanning signals):

| injected body | (a) labels | (b) finish condition | (c) defer list | (d) replan signals | forbidden |
|---|---|---|---|---|---|
| 0.4.0 top-1 parent (`admit-only-currently-justified-work`) | yes | no | narrow | no | no |
| 0.4.0 both parents stacked | yes | partial (one boundary, not per item) | yes | yes | no |
| 0.5.0 merged practice | yes | yes, per item | yes, named | yes, all categories | no |

The merged practice is the only body whose application produces the full rubric
decision — including when the two old parents are stacked, which top-1 injection
never delivers anyway.

## Verdict and limits

Within probe reach, 0.5.0 is >= 0.4.0 on every probe and strictly better on the
merged practice in both modes, with no harmful injections anywhere. Limits: 10
probes and one responder per mode; 8/10 advisory blind answers were already correct
(ceiling effect — the advisory number understates differences); the compliance run
answers three prompts in one session, so mild order carryover cannot be excluded;
retrieval-level quality (e.g. the `resolve-source-authority` confusion fix) is
measured by `eval-queries`, not by probes — the probe only records that the wrong
0.4.0 injection was ignored. Benchmark runs remain the release-level behavioral gate.
