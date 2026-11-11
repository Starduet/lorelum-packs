# Task-shaped Pack design examples

These hypothetical examples illustrate ways to derive content from a task; they are not Pack types, a complete taxonomy, or a required set of questions. Replace the assumptions with evidence from the actual users, tasks, and sources. A capable model may already understand general review, implementation, or privacy concepts: include domain-specific knowledge and reasoning that changes the task outcome rather than restating those capabilities. Do not invent requirements, thresholds, version behavior, or other parameters when evidence is missing.

## Reviewing a change

A team wants reviewers to notice whether a change violates an established compatibility promise. Examine representative changes, the actual promise, and past failures or review decisions. If the promise and its scope are documented, a Practice can explain how to recognize the relevant change and apply that promise, with an example that demonstrates the decision. Independent review questions may merit separate triggers; checks that only make sense together can remain together. Avoid a generic review checklist that duplicates what a strong model already knows. Evaluate with changes that do and do not affect the promise, and compare findings with and without the guidance. Do not claim a compatibility rule that the evidence does not establish.

## Implementing a domain workflow

A team implements a workflow governed by domain-specific rules. Inspect real requests, authoritative rules, and examples of correct and incorrect outcomes. A Practice might need the meaning of domain terms, the decision logic, and an example showing the consequences of a choice, rather than a list of general coding steps. Separate independently needed decisions only if each remains understandable at its point of use; keep coupled constraints together. Evaluate whether implementations for representative cases follow the sourced rules, including a case where the guidance should not apply. Where a rule or parameter is unresolved, identify the missing authority instead of choosing one.

## Working with version-sensitive technology

A task depends on behavior that may differ across releases of a tool. Use the relevant version's authoritative documentation and the project's actual version evidence; record the scope and route readers to the source for details likely to change. The Practice should retain what is necessary to choose an action at the decision point, while a linked reference can carry supplementary version details. Do not infer exact version boundaries or configuration values without support. Evaluate representative tasks within and outside the documented scope and check that an unknown version leads to obtaining evidence, not assuming behavior.

## Privacy and backend implementation together

A service change handles personal data, and the choice of storage or logging may affect a privacy obligation. Inspect the actual data flow, applicable policy or other authoritative requirements, and implementation context. A useful Practice can connect a specific handling decision to its supported constraint and consequence; keep coupled privacy and implementation reasoning together when either alone would mislead. Other independently triggered decisions can be separate. Do not invent a retention period, legal requirement, or technical setting; surface missing evidence and the need to resolve it. Evaluate a representative change against the supported constraint and a neighboring change where it does not apply, comparing behavior without the Pack.

Across examples, format validation only establishes the checks it performs. Retrieval evaluation asks whether the intended guidance is selected; task evaluation asks whether it leads to a better supported action. Record each result and its limits separately.
