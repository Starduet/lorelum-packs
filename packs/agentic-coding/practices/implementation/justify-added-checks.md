---
anti_patterns:
  - description: Adding a precaution before naming a reachable failure or mandatory contract and comparing its extra protection with false rejection, runtime work, availability, and recovery cost.
    id: agentic-coding.implementation.precaution-without-added-protection
    name: A precaution without added protection
    severity: warn
applies_when: the agent is considering new or stronger validation, preflight checks, permission confirmations, integrity scans, or blocking prerequisites while implementing a backend request, local HTTP client, startup, shutdown, or repair command, before deciding whether to add them
id: agentic-coding.implementation.justify-added-checks
severity: warn
stage: implementation
tech_stack:
  - agentic-coding
title: Justify Added Checks Before Implementing Them
---

## When to apply

While planning or coding an ordinary task, you may be tempted to add a preflight, validation,
permission confirmation, integrity scan, or blocking prerequisite "to be safe." Decide whether it
helps before implementing it, not just at final review. The request need not mention gates,
duplication, or cost. Even the first check can be unjustified: it need not duplicate another check
or make the normal workflow impossible to cause problems.

## Guidance

1. Describe exactly what could go wrong without the check: which input, caller, state change, or
   fault can reach this operation, and who would be harmed. Separately identify any mandatory
   contract or policy. A label such as "security risk" does not explain how a failure can happen.
2. Find which component is responsible for preventing that failure and what is already checked. Look
   at ingress validation, producer guarantees, authorization, transactions, installation, and
   publication. Ask what could invalidate those guarantees before use. Localhost, a type cast, or an
   earlier check alone does not prove they still hold.
3. Explain which possible failure the new check would catch that existing protection would miss. Is
   there a new trust boundary, conversion, or concurrent state change, or just another copy of the
   same rule? Investigate unclear security or data-loss risks before treating them as absent.
4. Compare that protection with the check's own effects: false refusal, latency and I/O,
   maintenance, unavailable service, and blocked startup, upgrade, shutdown, or repair. Use a
   bounded observation when actual cost could change the choice; no benchmark or risk-report ritual
   is required.
5. Add or retain necessary protection; otherwise narrow its scope, choose a sufficient nonblocking
   response, move it only if the required guarantee survives, or omit it. Record the reason briefly
   in the existing design or review. Fewer checks is not the goal.

Stop with a justified choice about this proposed check before implementing it. If necessity is
settled and only its location is open, use boundary ownership instead. If several justified checks
must be composed into a usable workflow, walk the acceptance path rather than repeating this
decision.

## Anti-pattern

A routine backend task leads the agent to add a full model-directory hash scan before every launch,
a second business-schema walk after every controlled HTTP response, and a healthy-service probe
before repair. Each is described as safer. Nobody names protection beyond the selected model's
loader, the response producer's established contract, or repair's own identity and permission
checks. Unused files now delay startup, valid results gain another rejection policy, and repair
cannot run when the service is broken. Reviewing each check only after implementation misses the
earlier choice.

## Why

A plausible precaution can add work and new refusal paths without closing a real gap. Making its
necessity a separate decision catches that proposal before the agent commits to it; placing checks
correctly or proving a happy path later does not answer whether to add them in the first place.

## Exceptions and boundaries

Required security, data consistency, and contracts constrain the choice; expense does not authorize
removing them. Retain external-input checks, resource-specific authorization, atomic
concurrent-state protection, required native/model quality and release integrity, and recovery
identity. Independently justified defense in depth remains valid. Change an accepted checking
contract through its owner, not by silently downgrading a failure to a warning.

This is not a production bypass, a new user-approval requirement, or a general ban on startup scans.
A mutable imported model may need verification that an immutable installation does not. A repair
operation may work without business readiness but must still establish its own authorization,
identity, and mutation safety. Types and contract tests do not substitute for real trust boundaries.

## Example

A task connects a desktop client to its bundled local worker. The worker constructs validated
records, the session is authenticated, and responses are serialized without later mutation. Before
adding a second full business-schema traversal, the agent finds no new failure it would catch and
omits it, while retaining decoding, protocol matching, identity, and request correlation. The public
import route still validates arbitrary JSON; it does not inherit the bundled worker's guarantee.

A read-only desktop launch is about to gain its first free-disk-space threshold for a possible
future export feature. It duplicates no check and introduces no dependency cycle. The agent declines
it before coding: launch performs no substantial write, and no accepted contract requires the
threshold, so a supported read-only session would gain a new refusal without added protection.
Required startup input, native/model, and release-integrity checks remain; a mutable model still
needs protection against changes between verification and use.
