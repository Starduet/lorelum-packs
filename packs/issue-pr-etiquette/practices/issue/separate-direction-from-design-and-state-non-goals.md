---
anti_patterns:
  - description: Embedding one implementation design in a proposal issue makes acceptance ambiguous and hardens mechanism choices before anyone agreed they are right.
    id: issue-pr-etiquette.issue.design-locked-in-the-proposal
    name: Design locked inside the proposal
    severity: warn
applies_when: a proposal issue could be read as an implementation plan, and the author must decide how much design to commit to inside the issue and what to explicitly exclude
id: issue-pr-etiquette.issue.separate-direction-from-design-and-state-non-goals
severity: warn
stage: issue
tech_stack:
  - github-contribution
title: Separate Direction from Design and State Non-goals
---

## When to apply

Apply when writing a proposal issue whose implementation could reasonably go several ways. The
decision is which parts state the objective and its governing principles, which parts are already
decided, and which decisions are deliberately deferred. Do not apply to defect reports where the
root cause is the content, or to changes whose design was already settled elsewhere.

## Guidance

State the objective and the principles any solution must satisfy; keep implementation choices out of
the acceptance path unless a decision is already made, and then cite where it was made rather than
restating it as new. Add an explicit non-goals section naming the decisions you are deferring and
who or what process will make them. If the repository requires a separate design artifact, point to
it instead of embedding design in the issue. Stop when a reader can agree or disagree with the
objective without first accepting a mechanism, and every deferred decision is named rather than
silently absent.

## Anti-pattern

A feature issue proposing "usage feedback" opens by prescribing the storage schema and the upload
client. The review debate collapses into schema details; two reviewers who agree on the need oppose
the issue because they oppose the storage choice. Months later the prescribed design proves wrong,
and the team must reopen an issue that was marked accepted — nobody can tell what agreement actually
covered.

## Why

Acceptance of an issue is remembered as agreement on a direction. When mechanism is baked in,
reviewers must reject the goal to reject the design, and an accepted issue silently commits work
that was never separately evaluated. Naming non-goals also prevents reviewers from assuming silence
means a deferred decision was considered and taken.

## Exceptions and boundaries

Small, mechanical proposals may legitimately include their one obvious implementation; the boundary
matters when more than one credible design exists. A design already decided upstream should be cited
as settled context, not reopened as a non-goal. Non-goals defer decisions; they do not forbid anyone
from filing the follow-up issue that makes them.

## Example

A proposal for a privacy-safe feedback loop states it "establishes the product and governance
objective, not the implementation design", lists seven hard principles any design must satisfy, and
closes with an out-of-scope section deferring storage, schema, and retention choices to a future
spec. Reviewers argue about principles in the issue and leave mechanism questions to the design
artifact, where they belong.
