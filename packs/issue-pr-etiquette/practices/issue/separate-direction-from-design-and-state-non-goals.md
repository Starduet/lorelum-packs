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

When proposing a change that could be built in several reasonable ways, let reviewers discuss the
goal without having to accept one design at the same time. Distinguish what has already been decided
from what still needs a decision. This is not needed for a defect report focused on its root cause,
or for a change whose design has already been settled elsewhere.

## Guidance

Explain what you want to achieve and the principles any solution must satisfy. Do not make accepting
the proposal depend on a particular implementation unless that choice is already settled; if it is,
cite the earlier decision. In a non-goals section, say which decisions you are leaving for later and
who will make them or which process will be used. If the repository requires a separate design
document, link it rather than putting the design in the issue.

Readers should be able to agree or disagree with the goal without first accepting an implementation.
Name every decision you are postponing so they do not mistake silence for agreement.

## Anti-pattern

A feature issue proposing "usage feedback" opens by prescribing the storage schema and the upload
client. The review debate collapses into schema details; two reviewers who agree on the need oppose
the issue because they oppose the storage choice. Months later the prescribed design proves wrong,
and the team must reopen an issue that was marked accepted — nobody can tell what agreement actually
covered.

## Why

Accepting an issue is usually understood as agreeing to its objective. If the issue also requires
one implementation, reviewers cannot reject that design without rejecting the goal. Acceptance then
commits the team to choices it never evaluated separately. Naming deferred decisions prevents
readers from assuming those choices have already been made.

## Exceptions and boundaries

Small, mechanical proposals may legitimately include their one obvious implementation; the boundary
matters when more than one credible design exists. A design already decided upstream should be cited
as settled context, not reopened as a non-goal. Non-goals defer decisions; they do not forbid anyone
from filing the follow-up issue that makes them.

## Example

A proposal for a privacy-safe feedback loop states it "establishes the product and governance
objective, not the implementation design", lists seven hard principles any design must satisfy, and
closes with an out-of-scope section deferring storage, schema, and retention choices to a future
spec. Reviewers discuss principles in the issue and leave implementation choices to the design
document.
