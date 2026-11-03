---
anti_patterns:
  - description: The agent restates the goal, arranges process, or restricts supported behavior without choosing and advancing an approach that actually accomplishes the task.
    id: agentic-coding.planning.process-instead-of-solution
    name: Process instead of a working solution
    severity: warn
applies_when: the outcome is clear but risk lists, process, capability restrictions, over-specified delegation, or internal metrics are replacing a concrete solution; a plan avoids deciding how the work can succeed, normal behavior is disabled to escape a difficulty, or a delegate's design choices are fixed without an accepted reason
id: agentic-coding.planning.organize-work-around-the-solution
severity: warn
stage: planning
tech_stack:
  - agentic-coding
title: Organize Work Around a Working Solution
---

## When to apply

Use this when you know what the user needs but still have to decide how to make it work, where to
solve a difficulty, or what to do after seeing a result. A risk list, a process, or a convenient
partial result must not replace that decision. The same applies to analysis and delegated work, not
just coding.

## Guidance

1. Choose a feasible way to achieve the requested change and act on it. Do the work you are
   responsible for, then use what actually happens to choose the next step. Repeating the goal,
   listing risks, or arranging a process is not a substitute.
2. Use facts that can change the choice: existing behavior, state changes, the materials you are
   working with, domain rules, or accepted decisions. They do not have to fit an input-to-output
   pipeline. Once you know enough, act. If a necessary fact is missing, get that fact rather than
   requiring a complete investigation or a comprehensive set of materials first. Decide technical
   details within your responsibility; bring the user the substantive tradeoffs that only they can
   decide.
3. Fix a difficulty where it arises without dropping other required behavior. Give restrictions,
   checks, delegation, and verification a specific purpose. Do not make a design easier by disabling
   normal capabilities, making someone else's decisions, or substituting an easier task to
   demonstrate. Required safety, authorization, and compatibility still apply. If these really
   cannot coexist with the request, explain what would be lost and offer a feasible alternative,
   rather than silently leaving work out or claiming success.
4. Match the approach to the task. Make an exact small edit directly; deliver a decision when the
   user asked only for analysis; explore when the solution is genuinely unknown. This does not
   replace domain knowledge, debugging, or professional design methods. It does not require an extra
   goal statement, flowchart, self-check list, or complete proposal for every task.

Once the decision has led far enough to determine the next action or deliver the requested result,
continue the task itself. Do not add a separate compliance document or review round for this rule.

## Anti-pattern

A gateway must estimate tokens per minute (TPM) for ordinary request content. The agent adopts a
text-type allowlist because it makes the estimator easy to explain and test. Normal thinking and
tool-call content falls outside the list and contributes nothing. The agent documents the filter,
adds passing tests for the listed types, and reports a completed estimator without resolving the
undercounting that defeats its purpose.

## Why

Knowing the goal is not the same as having a way to achieve it. Work can look orderly and carefully
protected while leaving the decisive problem untouched. A useful approach solves that problem
without removing the behavior the user needed.

## Exceptions and boundaries

Make an exact approved edit without extra planning or asking for approval again. When the way
forward is genuinely unknown, explore the facts that can change the choice, rather than trying to
collect everything. Required safeguards remain requirements; this rule does not let you bypass them.

`ground-user-goal` identifies the needed result. This Practice addresses how to accomplish it once
that result is understood. `choose-smallest-sufficient-design` compares the complexity of already
viable designs; this Practice also applies before any approach has been shown to work.
`justify-added-checks` decides whether a particular check is worth adding; a working solution may
instead require a change in behavior, a domain judgment, or a better division of responsibility.

## Example

A gateway's TPM estimate must cover ordinary request content, including thinking text and tool-call
arguments, while excluding known file payloads. The accepted method is a byte-based estimate, not an
exact tokenizer. A proposed allowlist counts only familiar text blocks, so a normal request with
tool-call arguments is underestimated even though the filter's tests pass.

The agent rejects that filter as insufficient. It applies the agreed estimate to the remaining
request content after excluding the identified file payloads, rather than treating unfamiliar
content types as empty. Within the task's verification scope, it checks that normal thinking and
tool-call content contributes to the estimate and that the known file payload exclusion still holds.
Existing request validation, authorization, and resource limits remain intact. The agent reports
what the estimate covers and its approximation limits; it does not claim exact token counts or
disable supported request content to make the implementation pass.
