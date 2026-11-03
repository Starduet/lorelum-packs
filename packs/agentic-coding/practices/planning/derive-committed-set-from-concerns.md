---
anti_patterns:
  - description: The agent grows a decision-bearing set one locally reasonable item at a time without a stated concern set, until the set's own size becomes the failure — diluted judgments, unfair gaps, or all-or-nothing brittleness — and later removals swing it the other way.
    id: agentic-coding.planning.criterion-accretion
    name: Criterion accretion
    severity: warn
applies_when: a decision-bearing set — plan items, acceptance criteria, checklists, definition-of-done lists, standards, checks, rules, or scoring dimensions that will determine what is built, what passes, what scores, or what is allowed — is being formed or revised by adding, merging, or removing items, whether working alone or in discussion
id: agentic-coding.planning.derive-committed-set-from-concerns
severity: warn
stage: planning
tech_stack:
  - agentic-coding
title: Build Plans and Criteria from the Decisions They Must Support
---

## When to apply

Use this when deciding what belongs in a plan, acceptance checklist, review standard, test suite,
validation or permission rules, or scoring rubric. These lists determine what gets built, what
passes, what is allowed, or how candidates score.

Before adding the first item, changing an existing list, or taking over one that has grown over
time, work out what problems and requirements its items must address. Notes, inventories, and
outlines that only record or explore ideas do not need this treatment until they will be used to
make those decisions.

## Guidance

1. Start with what the list needs to settle: which outcomes acceptance must distinguish, which
   failures the evidence shows can occur, and which extensions an authorized person has requested.
   Propose items only to address those needs.
2. For each item, ask what it adds. Does it cover a problem still missing from the list? Would it
   change whether you build or defer work, accept or reject a result, or give two plausible
   candidates different scores? If another item already covers the same thing, merge them.
3. Record the tradeoffs: enough coverage without an unmanageable list, current requirements versus
   requested extensions, and protection without making the work unusable. When someone proposes an
   item, ask which problem it solves before deciding to include it. Leave out items that change no
   decision.
4. For a list inherited from earlier work, first identify why each item was added. Rebuild it from
   those problems and requirements, removing items that have no such basis.

The list is ready when it covers every identified need, each item affects a decision, duplicates
have been merged, and you know what happens if an item fails. Settle the list then; adding more
requires a new problem or requirement. For a change too small to need a plan, the goal and
acceptance conditions are enough to work from. There is no need for an elaborate exercise.

## Anti-pattern

A team's migration reviews start with three checks. Each incident adds another reasonable-sounding
check, until every migration gets blocked and reviewers spend weeks arguing about exceptions. The
team then cuts the list down and loses checks for the failures that started it. Both times, they
change the length of the list without recording which problems it needs to prevent.

## Why

It is easy to justify one more check, and hard to remove a check without seeming to lose protection.
That lets a list grow until people can no longer use it. Work from the problems instead: add a
missing requirement when something important is untested, and combine overlapping criteria when they
split the weight of the same issue. Cutting or adding items by count alone repeats the cycle.

## Exceptions and boundaries

Keep requirements imposed by an applicable contract, policy, or regulation even if you cannot
explain their purpose locally; cite the source. A list of ideas can remain a draft until it will be
used to make decisions.

This rule helps choose the list's contents. You still need to walk through a planned workflow to
check that it can finish, and decide whether each proposed task belongs in the current scope.

## Example

A team is deciding when a schema migration is ready to ship. They need to be able to reverse the
change, preserve existing data, and detect failures. That leads to four checks: a tested rollback
path, an integrity check on migrated rows, an alert on write failures during cutover, and a
condition for aborting. A reviewer suggests checking the migration files' style too. The team sets
it aside: it addresses none of the identified needs and would not change whether they ship or abort.
