# 在每个 Server Action 内检查授权

## 适用场景

标记了 `"use server"`
的函数可以被直接调用，调用者不必先访问页面。编写或审查这类函数时，要确认它会检查调用者身份，以及该调用者能否对这个具体目标执行操作。

## 具体指导

把每个 server
action 当作公开端点：客户端可以绕过 UI，直接调用它的处理器并提交不可信参数。不要假定 middleware、layout 守卫或页面级检查也覆盖这次调用。每个 action 都必须在执行受保护的操作之前，检查调用者身份、对目标的权限以及输入：

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

检查顺序是：先认证调用者，再确认其是否有权操作这个具体目标，最后校验输入。授权要看目标的归属或成员关系，不能只看调用者的角色。网络传来的实参不可信，客户端的类型声明不能代替输入校验。检查应放在 action 内部，不要依赖某些 action 可能绕过的共享包装器。认证这一步可采用下文保证覆盖所有 action 的例外；针对具体目标的授权仍在 action 内执行。

隐藏或禁用按钮只能影响 UI，不能阻止别人直接调用 action，真正的权限限制必须由 action 执行。也不只是删除、归档这类操作需要检查：通过 action 读取用户私有数据，同样要检查身份和权限。

## 反模式

管理页在 layout 里检查访客角色，而它的 "use server" `archiveProject`
action 自身不做任何检查。用手工构造的请求直接调用 action 时 layout 守卫根本不会运行，于是任何已认证用户都能归档任何项目。

## 原因

攻击者不必加载页面就能调用 action。因此，只在页面渲染时执行的检查保护不了变更操作。在 action 的执行路径上检查身份、目标权限和输入，才能避免直接调用绕过这些检查。

## 例外与边界

- 共享 action 包装器或框架 middleware 可以承担认证一步，但前提是所有 action 在构造上保证被覆盖；针对具体目标的授权无法集中化，因为只有 action 自己知道目标是什么。
- 输入校验不等于授权：ID 格式合法但调用者无权访问它，仍必须拒绝。
- 框架机制（如 Next.js 要求把 action 当作公开端点）明确了这项通用要求；本篇不替代项目选定的认证库或错误上报约定。
- action 端点的限流、审计和 CSRF 防护属于部署层决策，不在本篇范围。

## 示例

邀请 action 在插入邀请前，检查调用者身份、是否有权管理这个具体空间，以及提交的邮箱格式是否正确。示例中声明的辅助函数代表项目的数据层。

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

隐藏调用 action 的对话框，或给管理页的 layout 加守卫，都不能保护这个端点。普通成员而非所有者直接调用时，会因没有管理权限而被拒绝；即使邮箱格式合法，只要调用者无权管理该空间，同样会被拒绝。
