# 廉价检查先于异步工作启动

## 适用场景

async 函数有时只看 props、已加载的记录、请求元数据或配置布尔值，就能提前返回。遇到这种情况，先检查这些本地值，再启动只有继续执行才需要的 I/O。

## 具体指导

默认先做开销小的同步检查，再等待异步结果。常见的写法有两种：

- `remoteFlag && cheapCondition` 这类复合条件：先求值 `cheapCondition`，通过后才 await
  `remoteFlag`；失败一侧永远不发起请求。
- 提前返回：先检查本地状态——工单已关闭、功能被禁用、缺少请求元数据——再去取只有过了这些检查才需要的权限、配置或开关。

把请求的启动和 await 都放进需要该结果的分支。函数顶部发起的请求，即使调用方在使用结果前就返回了，也仍会执行。只移动
`await` 而不移动请求的启动位置，省不掉这次 I/O。

如果调整顺序会改变行为，就保留原顺序。例如，条件本身开销很大或需要 I/O，条件要根据 await 的结果计算，或者副作用必须按固定顺序执行（如先写审计记录，再变更状态）。不能为了推迟请求而改变这些行为。

## 反模式

关闭工单的处理器先 await 审计服务的功能开关，再检查工单的本地状态。大多数调用针对已关闭的工单，却仍发出一次用不到结果的开关请求；只有工单尚未关闭时才会读这个结果。

## 原因

在用不到结果的路径上启动 I/O，会增加该路径的延迟和远端服务的负载。本地同步检查不需要网络往返；先做这些检查，就能省掉提前返回路径上的 I/O。这类路径越常见、被推迟的操作越昂贵，收益越大。

## 例外与边界

- 「廉价」指本地且同步：内存字段、请求元数据、已加载配置中的字面量。碰网络或数据库的条件再短也不廉价。
- 提前退出本身需要只有 I/O 才能提供的数据时，await 就是门槛；不要越过它重排。
- 推迟不得改变外部可观察的副作用顺序，也不得让并发启动的操作失去它已经依赖的值。
- 本篇是单函数内的排序。独立操作同时启动是
  `react.async.parallel-independent-work`；组件树中隔离慢子树的时机是
  `react.async.suspense-boundary-scope`。

## 示例

关闭支持工单时先查工单本地状态和本地功能开关，再碰网络；权限查询只在关闭路径上执行；审计记录模板只在需要它的分支内获取。

```ts
type Ticket = { id: string; status: "open" | "closed"; channel: string };
type Session = { userId: string };

declare function getPermissions(userId: string): Promise<{ canClose: boolean }>;
declare function getAuditNoteTemplate(channel: string): Promise<string>;
declare function appendAuditNote(ticketId: string, note: string): Promise<void>;
declare function transitionToClosed(ticketId: string, userId: string): Promise<void>;

export async function closeTicket(
  ticket: Ticket,
  session: Session,
  options: { closingEnabled: boolean; requireAuditNote: boolean },
) {
  if (ticket.status === "closed") {
    return { closed: false as const, reason: "already-closed" as const };
  }
  if (!options.closingEnabled) {
    return { closed: false as const, reason: "disabled" as const };
  }

  const permissions = await getPermissions(session.userId);
  if (!permissions.canClose) {
    return { closed: false as const, reason: "forbidden" as const };
  }

  if (options.requireAuditNote) {
    const template = await getAuditNoteTemplate(ticket.channel);
    await appendAuditNote(ticket.id, template);
  }

  await transitionToClosed(ticket.id, session.userId);
  return { closed: true as const };
}
```

在最常见的「已关闭」路径上，函数不执行任何 I/O。普通关闭恰好执行两次必需请求，仅当策略要求审计记录时才多一次模板请求。审计记录仍先于状态变更，要求的副作用顺序不变。
