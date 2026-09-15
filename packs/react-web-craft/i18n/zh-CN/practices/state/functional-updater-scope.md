# 函数式 updater 不会刷新其他捕获值

## 适用场景

在重构 `useCallback`、改为传入 updater 函数以使回调不再直接读取它所更新的 state 时应用。此时要判断：回调读取的其他 props、state 或 render 局部值是否仍必须保留为依赖。本篇只收窄这一个依赖决策，不是所有 stale-closure 问题的通用指南。

## 具体指导

当下一个值必须由同一个 state 变量的待处理值（pending value）计算得出时，才使用 updater。updater 收到的是该 state 的值；它不会让外层回调重新执行，也不会刷新回调创建时捕获的其他值。保持 updater 纯函数：只返回下一个状态，不修改现有值、不产生副作用。

当 `useCallback` 还读取其他响应式值时，把这些值保留在依赖列表里。只移除回调不再直接读取的那一项 state 依赖——因为 updater 已经通过参数拿到待处理值。如果回调身份并不需要稳定，不要为了管理依赖而专门加 `useCallback`。

判断每个被捕获的值本应代表哪个时刻。用户发起操作时传入或捕获的 workspace ID 可能就是有意标识那一次操作的。如果回调必须跟随「当前渲染的 workspace」，就让该值在回调中保持响应式，或显式传入目标 ID；消息列表的 updater 替你做不了这个决定。

## 反模式

一个记忆化的「标记当前工作区已读」回调通过 `setMessages(current => ...)` 更新 `messages`，却使用了空依赖列表，尽管 updater 内部还要将每条消息与 `activeWorkspaceId` 比较。updater 拿到的是最新的待处理 `messages`，但 `activeWorkspaceId` 仍是回调创建那次渲染捕获的值。切换工作区后，回调可能继续把消息标记到旧工作区上。

## 原因

state updater 只为一个 state 变量提供待处理值。记忆化的回调仍是某次渲染创建的那个函数，它的其他响应式读取不会因为其中一次 state 读取被搬进 updater 就变成「活」的。省略这些依赖后，回调在这些值变化之后被调用时，仍会沿用旧行为。

## 例外与边界

- 若回调除被更新的 state 外不读取任何其他会变化的响应式值，updater 可以移除该 state 的依赖。稳定的 setter 和模块级 helper 无需加入依赖。
- 若下一个状态是事件或其他来源已经给出的替换值，直接传值即可；updater 可用并不意味着必须使用。
- 若操作应当使用发起那一刻的值，就显式捕获或传入该值；若应当使用更晚的值，就通过恰当的数据流让回调拿到那个更晚的值。不要把「取最新」当成天然正确。
- 使用 `useCallback` 时，其依赖列表必须覆盖回调读取的其他响应式值；函数身份稳定不会让这些值变成活的。需要通过 ref 或其他机制读取变化值的稳定事件处理器属于另一个决策；本篇不推荐任何「latest value」变通。

## 示例

下面的回调更新消息列表时既依赖待处理状态，又按当前工作区过滤，因此依赖列表包含 `activeWorkspaceId`；updater 只是替代了从渲染快照读取 `messages` 的需要。该 TSX 示例假定使用自动 JSX 运行时；请遵循项目实际配置的 JSX 运行时。

```tsx
import { useCallback, useState } from "react";

type Message = {
  id: string;
  workspaceId: string;
  read: boolean;
};

const initialMessages: Message[] = [
  { id: "m-1", workspaceId: "north", read: false },
  { id: "m-2", workspaceId: "south", read: false },
];

export function WorkspaceInbox({
  activeWorkspaceId,
}: {
  activeWorkspaceId: string;
}) {
  const [messages, setMessages] = useState(initialMessages);

  const markActiveWorkspaceRead = useCallback(() => {
    setMessages((currentMessages) =>
      currentMessages.map((message) =>
        message.workspaceId === activeWorkspaceId
          ? { ...message, read: true }
          : message,
      ),
    );
  }, [activeWorkspaceId]);

  return (
    <section>
      <button type="button" onClick={markActiveWorkspaceRead}>
        Mark this workspace read
      </button>
      <ul>
        {messages.map((message) => (
          <li key={message.id}>
            {message.workspaceId}: {message.read ? "read" : "unread"}
          </li>
        ))}
      </ul>
    </section>
  );
}
```

如果这个回调只按固定的操作参数与待处理 `messages` 过滤，它也可以改为接收 workspace ID 作为参数，从而不必捕获该 prop。这里回调的契约明确是「标记本次渲染的活动工作区」，所以 workspace ID 保留为依赖。
