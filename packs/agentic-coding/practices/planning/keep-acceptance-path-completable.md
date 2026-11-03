---
anti_patterns:
  - description: The agent adds individually plausible protections to the steps the task's own acceptance scenario must travel until that scenario cannot complete without interventions the request never named; each protection cites a risk category, and none names a reachable failure in this deployment.
    id: agentic-coding.planning.acceptance-blocking-protection
    name: Acceptance-blocking protection
    severity: warn
applies_when: proposed validation, authorization, permission, confirmation, readiness, or compatibility checks must work together in a required user workflow, including backend startup, shutdown, repair, or recovery, and the agent must determine whether that workflow can still complete
id: agentic-coding.planning.keep-acceptance-path-completable
severity: warn
stage: planning
tech_stack:
  - agentic-coding
title: Keep the Acceptance Path Completable
---

## When to apply

Use this when several checks will run as part of the same user workflow. Each may look reasonable
alone, yet together they can prevent the user from finishing. Walk through the normal operation,
startup, shutdown, and supported repair or recovery commands, including errors, repeated calls, and
reopening. Do this even if the task never mentions checks or approvals.

If you only need to decide whether one proposed check is necessary, use `justify-added-checks`.
Here, check that the whole workflow has all its required steps and can still finish with the
proposed checks in place.

## Guidance

1. Walk each acceptance condition from the user's first action to the result they should see.
   Include every new check. Make sure a component or person is responsible for each required step
   before deciding how strict the checks should be.
2. For each new check that can reject, delay, or interrupt the operation, choose the least
   restrictive response that handles its specific failure: log it, label the result, ask once for
   confirmation, or refuse the operation. Before doing more than logging, identify who can cause the
   failure and how they can reach that operation in this deployment. Use the actual system facts or
   requirements, not just a risk category or an unspecified attacker. Where possible, apply the
   check only to the cases that need it.
3. Ask what would break, and who would be affected, if you removed that new check. If there is no
   answer, remove it. A confirmation prompt that nobody can answer blocks the operation; use a less
   restrictive response or narrow the check and document how the other cases bypass it.
4. Check what happens when the most likely check fails. Let it fail independently and say which
   other results can still be used. If one failure must invalidate every successful result, explain
   who needs that rule and why labeled or partial results would be misleading.
5. Beside each check's plan item, record what it does on failure and which failure it addresses.

You are done when every acceptance condition can finish without extra intervention beyond the
acceptance requirements or applicable policy, and each new check has a reason for its response. For
a change too small to plan, ask just whether the check blocks or delays a required operation and
which failure or mandatory policy makes that necessary. Keep justified refusals. Otherwise, make the
check less restrictive, limit where it applies, or leave it out.

Recovery commands must work in the conditions they are meant to repair. Rebuilding a damaged index
cannot depend on that index already being healthy. Stopping an identified old process need not
depend on its business API matching the new client. Still check authorization for that operation,
the process's identity, whether it is active, and the consistency requirements. If a required
safeguard conflicts with the promised recovery behavior, report the conflict; do not bypass it just
to make the command succeed.

## Anti-pattern

A task adds a config-set command to a local CLI. The agent ships it with an allowlist of keys, a
path-traversal validator, an ownership permission check, and a confirmation prompt on every write.
The acceptance scenario — developer runs the command, config updates — now requires an interaction
and a grant the request never named, and scripts calling the CLI cannot answer the confirmation.
Only after delivery does the agent adjust the protection by deleting the unnecessary checks.

## Why

A check can look useful on its own while making the complete workflow unusable. Focusing on each
incident a check might prevent makes it easy to miss that accumulated cost. Look separately for
missing steps, new interruptions, and what one failure does to the other results. Passing one of
these reviews does not answer the other two.

## Exceptions and boundaries

An applicable policy or regulation may require a check even when the failure cannot occur locally.
Cite that requirement and keep it. A reachable threat can also justify refusing the operation. This
is not permission to remove justified safeguards.

Treat existing system guards as constraints, not new checks that this rule lets you delete. If they
make the required workflow impossible, report the conflict. Which component should perform a check,
and whether it duplicates another check, are separate questions.

## Example

For config-set, the agent walks through the proposed operation: command, key allowlist, permission
check, confirmation, write, and verification. It asks what removing each new check would change.
Traversal input cannot reach a path; the OS already enforces file ownership; and the prompt only
catches typos outside the acceptance requirements. Those checks can be removed or made less
restrictive. But overwriting the security-token key is known to force re-authentication elsewhere.
The agent keeps one confirmation for those keys. Other keys are written without interruption, and
the change is logged.

A backend's repair command must rebuild a damaged derived index while the service is not ready. The
proposed shared readiness preflight rejects that exact state before repair begins. The agent keeps
readiness enforcement for ordinary queries but gives repair its own authorized path with the
required exclusive mutation protection. Repair can now rebuild the index without first querying it;
an unauthorized caller or a conflicting writer is still refused. No global "skip checks" switch is
introduced.
