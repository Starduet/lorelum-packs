# 每个 Server Action 内部自证权责

## 适用场景

编写或审查任何标记了 `"use server"` 的函数时应用。判断它的认证（调用者是谁）与授权（这个调用者能否对这个目标做这件事）检查放在哪里。

## 具体指导

把每个 server action 当成公开端点，因为它就是：框架把它变成可寻址的处理器，任何客户端可以用任意实参直接调用，与渲染它的 UI 无关。middleware、layout 守卫和页面级检查保护的是渲染路径——直接投递的 action 调用不会经过它们。因此每个 action 在触碰数据之前自行验证自己的契约：

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

每个 action 三项检查，按序执行：认证调用者；针对这个目标授权这个调用者——看目标自身的归属或成员关系，而不是只看角色；校验输入，因为 action 实参来自不可信的线上数据，客户端传了什么类型都一样。检查放在 action 内部，而不是放在某些 action 可能意外绕过的共享包装器里；只有当所有变更在构造上可证明必然经过时，包装器才可接受。

不要让 UI 暗示 action 并未执行的安全：隐藏或禁用的按钮是便利，不是边界。也不要以为只有破坏性操作才需要——通过 action 泄漏每用户数据的读操作同样要接受这种审视。

## 反模式

管理页在 layout 里检查访客角色，而它的 "use server" `archiveProject` action 自身不做任何检查。用手工构造的请求直接调用 action 时 layout 守卫根本不会运行，于是任何已认证用户都能归档任何项目。

## 原因

action 的处理器独立于渲染它的页面可达；它的安全边界就在自身第一处检查所在的位置，不存在更早的边界。把认证、授权、校验放进每个 action，让执行点与强制点重合——这是攻击者无法绕开的唯一摆放。

## 例外与边界

- 共享 action 包装器或框架 middleware 可以承担认证一步，但前提是所有 action 在构造上保证被覆盖；针对具体目标的授权无法集中化，因为只有 action 自己知道目标是什么。
- 输入校验是输入校验，不是授权：形状合法但调用者不拥有的 ID 仍会倒在归属检查上。
- 框架机制（Next.js「把 action 当公开端点」的指引）固定了通用契约；本篇不替代项目选定的认证库或错误上报约定。
- action 端点的限流、审计、CSRF 姿态是部署层决策，不在本篇范围。

## 示例

邀请 action 在内部完成全部三项：调用者是谁、该调用者是否管理这个具体空间、线上输入是否良构。声明的 helper 代替项目的数据层。

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

渲染这个 action 的对话框可以被隐藏，展示它的管理 layout 可以有守卫——两者都保护不了端点。成员（非所有者）直接调用会倒在归属检查上；格式合法但调用者无权管理的空间的邮箱也会以同样方式失败。
