# 不用于渲染的组件实例数据放在 ref

## 适用场景

事件处理器有时要记住上次接受点击的时间等数据，供后续事件或命令式操作使用，而且重渲染后不能丢失。先看这份组件实例内的数据是否需要显示：需要更新界面的值，不能只放进 ref。

## 具体指导

值变化后需要更新界面时，用 state。数据只供组件内部使用、需要跨渲染保存，并由后续事件或命令式操作读取时，用 ref。修改
`ref.current` 不会触发渲染，所以仅靠 ref 无法让界面跟随它更新。

按值的用途选择，不要只看更新频率。频繁变化但决定显示内容的值，仍需要能更新 UI 的机制。不要仅为避免渲染就把它改为 ref，也不要靠事件处理器直接写 DOM 样式，回避该如何渲染界面的问题。

也不要为了触发 Effect 就把 state 标志换成 ref。修改 ref 不会触发渲染，Effect 不会因此运行。用户事件触发的命令放在对应处理器中；随渲染同步外部系统时，则需要 props 或 state 等能让 React 观察到变化的输入。

## 反模式

上传进度被存进 ref 以避免渲染，然后 JSX 读取
`progressRef.current`，期待可见的进度标签随之前进。只更新 ref 会让渲染出的标签停留在上一次提交的值。

## 原因

React
state 的变化会参与渲染；ref 则是随组件实例保留的可变存储，修改时不会通知 React。混淆两者的职责，要么为无需显示的数据触发多余渲染，要么让界面停留在旧值。

## 例外与边界

- 变化的数据必须可见时，使用 state、外部动画系统或其他明确选择的渲染机制。本篇不规定动画架构，也不承诺性能提升。
- ref 也可以保存 DOM 节点、支持命令式 API；本篇只讨论非 DOM 值应选择 state 还是 ref。
- 在长期存续的事件监听器里用 ref 读取变化值，属于另一个闭包/Effect 决策。本篇不推荐 latest-value
  ref 或 Effect Event。
- 当前不展示、但之后会影响一次用户可见动作的值，若其生命周期与预期读取时机都明确，放在 ref 里仍是合适的。

## 示例

遥测按钮会抑制一秒内重复到达的本地打点。最近一次接受的时刻影响后续的事件判断，但从不在界面显示，因此可以放在 ref 里。这只是组件实例内的采样防护，不是服务器端限流。

```tsx
import { useRef } from "react";

export function CheckpointButton({
  recordCheckpoint,
}: {
  recordCheckpoint: () => void;
}) {
  const lastRecordedAtRef = useRef<number | null>(null);

  function handleClick() {
    const now = performance.now();
    const previous = lastRecordedAtRef.current;
    if (previous !== null && now - previous < 1000) return;

    lastRecordedAtRef.current = now;
    recordCheckpoint();
  }

  return (
    <button type="button" onClick={handleClick}>
      Record checkpoint
    </button>
  );
}
```

修改 `lastRecordedAtRef.current`
不会重绘按钮。如果用户必须看到冷却状态，就把可见的冷却状态另存进 React
state；ref 自身无法更新渲染出的文本或禁用控件。
