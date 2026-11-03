---
anti_patterns:
  - description: A "use server" mutation performs no authentication or authorization of its own, relying on middleware, layout, or page guards that a directly invoked endpoint bypasses.
    id: react.server.action-trusts-ui-guards
    name: Server Action trusting page-level guards
    severity: warn
applies_when: a server-side mutation is exposed through a server action, and the placement of its authentication and authorization checks is being decided
id: react.server.authorize-server-actions
severity: warn
stage: implementation
tech_stack:
  - react
  - next
title: Authorize Inside Every Server Action
---

## When to apply

A function marked `"use server"` can be called directly without visiting its page. When writing or
reviewing one, make sure it checks who is calling and whether that caller may act on the target.

## Guidance

Treat every server action as a public endpoint: a client can invoke its handler directly with
untrusted arguments, without using the UI that renders it. Do not assume middleware, layout guards,
or page-level checks cover that call. Each action must check the caller, target permissions, and
input before performing the protected operation:

```ts
"use server";

export async function archiveProject(projectId: string) {
  const session = await verifySession();
  if (!session) {
    throw new Error("Unauthenticated");
  }

  const project = await getProject(projectId);
  if (!project || !canAdminister(session.user, project)) {
    throw new Error("Forbidden");
  }

  await archiveProjectRecord(projectId);
  return { ok: true };
}
```

Check in this order: authenticate the caller, authorize the caller for this specific target, then
validate the input. Authorization must check the target's ownership or membership, not just the
caller's role. Validate arguments because they arrive as untrusted wire data, regardless of the
client's types. Keep these checks inside the action rather than relying on a shared wrapper that
some actions might bypass. Authentication may use the guaranteed-coverage exception below;
target-specific authorization still belongs in the action.

Do not let the UI imply security that the action does not enforce: a hidden or disabled button is a
convenience, not a boundary. And do not treat this as unique to destructive operations — reads that
leak per-user data through actions need the same scrutiny.

## Anti-pattern

An admin page checks the viewer's role in its layout, and its "use server" `archiveProject` action
performs no checks of its own. The layout guard never runs when the action is invoked directly with
a hand-crafted request, so any authenticated user archives any project.

## Why

An attacker can call the action without loading its page. Checks enforced only while rendering that
page therefore cannot protect the mutation. Checking the caller, target permissions, and input on
the action's execution path prevents a direct call from bypassing those checks.

## Exceptions and boundaries

- A shared action wrapper or framework middleware may perform the authenticate step, but only when
  coverage of every action is guaranteed by construction; authorization against the specific target
  cannot be centralized because only the action knows its target.
- Input validation is input validation, not authorization: a valid-shaped ID the caller does not own
  still fails the ownership check.
- Framework-specific mechanisms (Next.js's guidance to treat actions as public endpoints) fix the
  general contract; this Practice does not replace a project's chosen auth library or
  error-reporting conventions.
- Rate limiting, auditing, and CSRF posture for action endpoints are deployment-level decisions
  outside this Practice.

## Example

An invite action checks who is calling, whether that caller administers this specific space, and
whether the submitted email is well-formed before inserting an invite. The declared helpers stand in
for the project's data layer.

```ts
"use server";

declare function verifySession(): Promise<{ userId: string } | null>;
declare function getMembership(
  spaceId: string,
  userId: string,
): Promise<{ role: "owner" | "member" } | null>;
declare function insertInvite(input: {
  spaceId: string;
  email: string;
  invitedBy: string;
}): Promise<void>;

export async function inviteMember(spaceId: string, email: string) {
  const session = await verifySession();
  if (!session) throw new Error("Unauthenticated");

  const membership = await getMembership(spaceId, session.userId);
  if (!membership || membership.role !== "owner") {
    throw new Error("Forbidden");
  }

  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) {
    throw new Error("Invalid email");
  }

  await insertInvite({ spaceId, email, invitedBy: session.userId });
  return { ok: true };
}
```

The dialog that renders this action can be hidden, and the admin layout that shows it can be guarded
— neither protects the endpoint. A member (not owner) calling it directly fails the ownership check;
a well-formed email for a space the caller does not administer fails the same way.
