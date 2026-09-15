# 非渲染用途的每实例记账放在 ref

## 适用场景

后续的事件或命令式操作需要一份跨渲染存续的记账数据时应用。此时要判断：该值本身要进入渲染输出，还是只是 UI 无需展示的组件实例私有记忆。

## 具体指导

变化应当更新渲染输出时用 state。私有记账需要跨渲染存续、且将由后续事件或命令式操作读取、渲染并不需要展示它时，用 ref。修改 `ref.current` 不会调度渲染，所以 ref 自身无法让可见输出保持同步。

按值的角色选择，而不只看更新频率。一个频繁变化但驱动用户所见内容的值，仍需要能产出目标 UI 的更新机制。不要只为压掉渲染就把它换成 ref，也不要在事件处理器里直接写 DOM 样式来替代「界面应如何渲染」的决策。不要为了让某个 Effect 运行就把 state 旗标换成 ref：ref 的修改不会调度渲染，Effect 无从观察。由用户事件引发的命令属于那个事件处理器；渲染驱动的外部同步需要渲染可见的输入。

## 反模式

上传进度被存进 ref 以避免渲染，然后 JSX 读取 `progressRef.current`，期待可见的进度标签随之前进。只更新 ref 会让渲染出的标签停留在上一次提交的值。

## 原因

React state 参与渲染；ref 是随组件实例存续的可变存储，变化时不通知 React。混淆这两种职责，要么给私有记账带来无谓渲染，要么让可见 UI 停留在旧值。

## 例外与边界

- 变化的数据必须可见时，使用 state、外部动画系统或其他明确选择的渲染机制。本篇不规定动画架构，也不承诺性能提升。
- ref 也可以持有 DOM 节点、服务命令式 API；本篇只讨论非 DOM 值的 state 与 ref 之择。
- 在长期存续的事件监听器里用 ref 读取变化值，属于另一个闭包/Effect 决策。本篇不推荐 latest-value ref 或 Effect Event。
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

修改 `lastRecordedAtRef.current` 不会重绘按钮。如果用户必须看到冷却状态，就把可见的冷却状态另存进 React state；ref 自身无法更新渲染出的文本或禁用控件。
