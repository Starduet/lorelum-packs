# 显式组件变体优于布尔模式旗标

## 适用场景

组件要新增新建、编辑、转发或回复模式时，先别急着加一个 boolean
prop 和相应分支。看看各模式需要哪些数据、怎样组合界面，再考虑是否拆成共享公共部件的命名组件。

## 具体指导

每增加一个表示模式的布尔值，组件允许的状态组合就会翻倍，而各模式通常还需要不同的数据（如 `dmId` 与
`channelId`）。把模式拆成命名组件，各自只接收所需的数据，再复用真正相同的部分：

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

共享部分继续共享——框架、输入区、操作行——而每个变体的签名说明了它做什么、需要什么。调用点的读者看到
`<EditComposer messageId=... />`，不用反推真值表。

不一定要拆成多个组件。如果各模式仍适合放在同一个公开组件 API 中，可以用判别联合要求每种模式所需的数据，见
`react.composition.model-mutually-exclusive-props`。各模式需要不同的组合方式和数据时，选择命名变体；保留单个组件时，用联合约束各模式的 props。

独立选项不等于模式：`disabled`、`compact` 和 `showAvatar`
可以自由组合，可以继续作为独立 props。只有互斥模式才需要变体。

## 反模式

消息编辑器接收
`isThread`、`isEditing`、`isForwarding`，再加上各模式所需的可选 ID。每种模式组合都能通过编译，但其中有些毫无意义。每个标志都增加渲染分支，新增「定时发送」模式时又要修改已有分支。

## 原因

命名变体要求调用者明确选择模式，每个变体的 props 再要求该模式的数据。多个独立布尔值则允许调用者传入各种组合，组件必须在运行时解释或拒绝它们。复用公共部件，可以避免把相同实现复制到每个变体。

## 例外与边界

- 只有一种模式时，不要为了将来可能出现的需求预先拆分。等第二种确实需要不同数据的模式出现后，再考虑拆分。
- 拆分时要设计好公共部件的复用；如果只是复制粘贴多个组件，反而比布尔标志更糟。
- 跨变体存续的状态（草稿、选中项）是状态所有权决策——见
  `react.state.share-one-owner`——不是 props 形状问题。
- 本篇不规定共享部件的机制（compound parts、context
  provider 或普通 props）；选择能避免重复、又能满足各模式需求的最简单机制。

## 示例

变体共享 `ComposerFrame`、`ComposerInput` 与
`ComposerActions`。之后新增定时模式就是再加一个变体——不是让新旗标波及每个既有分支：

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

调用点从组件名读出模式——`<ThreadComposer channelId=... />`、`<EditComposer messageId=... />`、`<ScheduledComposer channelId=... runAt=... />`——各拿各的数据。定时帖有
`runAt`；布尔版的这个组件会把它作为可选 prop 携带，在唯一一个模式之外毫无意义，判空还得写进某个分支。
