# 函数式 updater 不会刷新其他捕获值

## 适用场景

把 `useCallback`
改成函数式 updater 后，回调可能不再需要直接读取它所更新的 state。但它读取的其他 props、state 或渲染局部值，仍然可能需要放在依赖列表里。缩短依赖列表时要分清这一点，不要把 updater 当成解决所有闭包旧值问题的办法。

## 具体指导

当下一个值必须由同一个 state 变量的待处理值（pending
value）计算得出时，才使用 updater。updater 收到的是该 state 的值；它不会让外层回调重新执行，也不会刷新回调创建时捕获的其他值。保持 updater 纯函数：只返回下一个状态，不修改现有值、不产生副作用。

`useCallback`
如果还读取其他响应式值，就把它们留在依赖列表中。只删除回调已不再直接读取的那个 state 依赖，因为 updater 会通过参数收到其待处理值。如果不需要保持函数引用稳定，就不要只为管理依赖而添加
`useCallback`。

先确认操作应使用哪个时刻的值。发起操作时传入或捕获的 workspace
ID，可能正是这次操作应该使用的 ID。如果回调要操作当前渲染的工作区，就保留相应依赖，或在调用时明确传入目标 ID。更新消息列表的 updater 不会替你决定该用哪个工作区。

## 反模式

一个记忆化的「标记当前工作区已读」回调通过 `setMessages(current => ...)` 更新
`messages`，却使用了空依赖列表，尽管 updater 内部还要将每条消息与 `activeWorkspaceId`
比较。updater 拿到的是最新的待处理 `messages`，但 `activeWorkspaceId`
仍是回调创建那次渲染捕获的值。切换工作区后，回调可能继续把消息标记到旧工作区上。

## 原因

state
updater 只提供一个 state 变量的待处理值。记忆化的回调仍是某次渲染创建的函数；把一项 state 读取移进 updater，不会更新它捕获的其他值。省略这些依赖后，即使值已变化，再次调用回调仍可能使用旧值。

## 例外与边界

- 若回调除被更新的 state 外不读取任何其他会变化的响应式值，updater 可以移除该 state 的依赖。稳定的 setter 和模块级 helper 无需加入依赖。
- 若下一个状态是事件或其他来源已经给出的替换值，直接传值即可；updater 可用并不意味着必须使用。
- 若操作应当使用发起那一刻的值，就显式捕获或传入该值；若应当使用更晚的值，就通过恰当的数据流让回调拿到那个更晚的值。不要把「取最新」当成天然正确。
- 使用 `useCallback`
  时，依赖列表必须包含回调读取的其他响应式值；函数引用稳定不代表捕获值会更新。稳定事件处理器若要通过 ref 或其他机制读取变化值，属于另一个决策；本篇不建议用「始终取最新值」的变通办法。

## 示例

下面的回调更新消息列表时既依赖待处理状态，又按当前工作区过滤，因此依赖列表包含
`activeWorkspaceId`；updater 只是替代了从渲染快照读取 `messages`
的需要。该 TSX 示例假定使用自动 JSX 运行时；请遵循项目实际配置的 JSX 运行时。

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

如果这个回调只按固定的操作参数与待处理 `messages` 过滤，它也可以改为接收 workspace
ID 作为参数，从而不必捕获该 prop。这里回调的契约明确是「标记本次渲染的活动工作区」，所以 workspace
ID 保留为依赖。
