# 显式组件变体优于布尔模式旗标

## 适用场景

组件被要求支持一个新模式——新建、编辑、转发、回复——而提议的改动是再加一个 boolean prop 加上它需要的分支时应用。判断这些模式是否应当是共享部件的独立命名变体。

## 具体指导

每个模式布尔都会让组件的可能状态翻倍，而且各模式本来就需要不同的数据（`dmId` 与 `channelId`）。把模式拆成命名变体，各自只接收自己需要的东西，让真正共用的部分保持共享：

```tsx
export function ThreadComposer({ channelId }: { channelId: string }) {
  return (
    <ComposerFrame>
      <ComposerInput />
      <AlsoSendToChannelField channelId={channelId} />
      <ComposerActions submitLabel="Post" />
    </ComposerFrame>
  );
}

export function EditComposer({ messageId }: { messageId: string }) {
  return (
    <ComposerFrame>
      <ComposerInput />
      <ComposerActions submitLabel="Save" cancel />
    </ComposerFrame>
  );
}
```

共享部分继续共享——框架、输入区、操作行——而每个变体的签名说明了它做什么、需要什么。调用点的读者看到 `<EditComposer messageId=... />`，不用反推真值表。

两条边界防止这变成教条。第一，拆分不是唯一诚实的形状：当各模式确实是同一公开面的变化时，判别联合的 props 契约能在单个组件内实现同样的逐模式数据检查——该契约见 `react.composition.model-mutually-exclusive-props`。拆分决策关乎组合与数据；联合决策关乎保留的单一 API。第二，独立选项不是模式：`disabled`、`compact`、`showAvatar` 是可自由组合的侧面，作为 props 存在；只有互斥的模式才配得上变体。

## 反模式

消息编辑器接收 `isThread`、`isEditing`、`isForwarding` 加上各模式所需的可选 ID。每种模式组合都能通过编译，其中三种是无意义的，渲染体是每个旗标一个分支，而新增「定时发送」模式意味着把所有分支都摸一遍。

## 原因

变体把模式选择推到类型层和调用点——错误的组合要么编译不过，要么根本写不出来；布尔把选择推进运行时分支——所有组合都变得可表达。共享部件防止变体分叉成副本，拆分的代价是组合设计，而不是重复代码。

## 例外与边界

- 单模式组件不要为想象中的未来预先拆分；第二个带不同数据的模式真实到来时，拆分才赚回成本。
- 变体家族需要有意的共享部件设计；没有它，拆分会退化成复制粘贴，比旗标更糟。
- 跨变体存续的状态（草稿、选中项）是状态所有权决策——见 `react.state.share-one-owner`——不是 props 形状问题。
- 本篇不规定共享部件的机制（compound parts、context provider、普通 props）；选最简单又能让变体保持诚实的那种。

## 示例

变体共享 `ComposerFrame`、`ComposerInput` 与 `ComposerActions`。之后新增定时模式就是再加一个变体——不是让新旗标波及每个既有分支：

```tsx
function ScheduledComposer({ channelId, runAt }: { channelId: string; runAt: Date }) {
  return (
    <ComposerFrame>
      <ComposerInput />
      <ScheduleFields runAt={runAt} />
      <ComposerActions submitLabel="Schedule" cancel />
    </ComposerFrame>
  );
}
```

调用点从组件名读出模式——`<ThreadComposer channelId=... />`、`<EditComposer messageId=... />`、`<ScheduledComposer channelId=... runAt=... />`——各拿各的数据。定时帖有 `runAt`；布尔版的这个组件会把它作为可选 prop 携带，在唯一一个模式之外毫无意义，判空还得写进某个分支。
