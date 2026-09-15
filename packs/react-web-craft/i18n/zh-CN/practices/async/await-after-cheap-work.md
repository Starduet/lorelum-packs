# 廉价检查先于异步工作启动

## 适用场景

async 函数既能依据廉价的本地数据——props、已加载的记录、请求元数据、配置布尔值——跳过工作，又要为其他条件 await
I/O 时应用。此时要决定守卫与 await 的执行顺序。

## 具体指导

默认顺序：廉价且同步的在前，await 放最后。两种形态覆盖多数情况：

- `remoteFlag && cheapCondition` 这类复合条件：先求值 `cheapCondition`，通过后才 await
  `remoteFlag`；失败一侧永远不发起请求。
- 提前返回：先检查本地状态——工单已关闭、功能被禁用、缺少请求元数据——再去取只有过了这些检查才需要的权限、配置或开关。

把每个 await 推进到消费它的分支里。函数体顶部的 await 对每个调用方都执行，即使唯一消费者是多数调用方永远不会进入的分支；推迟它能把这笔成本从所有提前退出的路径上拿掉。

重排会改变行为时保持原序：「廉价」条件本身昂贵或依赖 I/O；条件要由 await 的值计算；或副作用必须固定先后（例如先写审计记录再做状态变更）。推迟是排序决策，不是改语义的许可。

## 反模式

关闭工单的处理器在检查工单本地状态之前先 await 审计服务的功能开关。大多数调用针对的工单早已关闭，于是开关请求在主导路径上被支付又被丢弃；只有罕见的开启工单路径会读它。

## 原因

在注定丢弃它的路径上启动的 I/O，既是该路径的纯延迟，也是远端服务的纯负载。本地同步守卫只花纳秒；把它们放前面，所有它们失败的路径就都不再产生 I/O——被跳过的分支越常见、被推迟的操作越昂贵，收益越大。

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

在主导的「已关闭」路径上函数零 I/O。普通关闭恰好执行两次必需请求，仅当策略要求审计记录时才有第三次——且审计记录仍先于状态变更，要求的副作用顺序得以保留。
