# React 19 用 ref prop；旧版本线保留 forwardRef

## 适用场景

调用者可能需要通过 ref 聚焦输入框，或访问对话框的 DOM 节点、命令式句柄来定位。组件确实需要提供这类访问时，应根据项目支持的所有 React 版本选择如何传递
`ref`。

## 具体指导

在 React 19 上，`ref` 是普通 prop：声明它、透传它，不需要包装器：

```tsx
function TextField({ ref, label, ...props }: InputProps & { ref?: React.Ref<HTMLInputElement> }) {
  return (
    <label>
      <span>{label}</span>
      <input ref={ref} {...props} />
    </label>
  );
}
```

`forwardRef` 在 React 19 上仍然可用。但只支持 React 19 的新组件可以直接接收和传递
`ref`，无需包装器及其单独的类型参数。按兼容性选择：

- React 19 项目：新组件写 ref-as-prop；碰到本就要改的文件时顺手迁移 `forwardRef` 包装。
- 同一份源码要支持 React 18 和 19，或组件库的 peer 依赖范围包含 18：保留
  `forwardRef`，它在两个版本上都可用；不要在仍支持 18 的版本中使用仅适用于 19 的 ref prop。
- 如果内建机制能覆盖所有支持的版本，就不要另造一套传法，例如在已有 `ref` 需求之外再增加 `domNodeRef`
  之类的自定义 prop。

使用 `useImperativeHandle` 暴露命令式句柄时，也要通过所选机制接收
`ref`；版本选择与传递 DOM 节点 ref 时相同。

## 反模式

组件库声明兼容 React 18，一位贡献者却把文本输入框改成 React 19 的 ref-as-prop，删除了
`forwardRef`。在 React 18 上，调用者的 `ref`
不再传到输入框。调用点可能没有类型错误，运行时也不崩溃，但聚焦输入框的功能失效了。

## 原因

React 18 不会把 `ref` 当作普通 prop 传给函数组件；`forwardRef` 则同时支持 React
18 和 19。选择所有目标版本都支持的机制，调用者的 ref 才能正常工作。组件库还应在 peer 依赖中写明支持的版本范围。

## 例外与边界

- 不需要暴露节点或句柄的组件就不应接收 ref；这里讨论的是需要 ref 时怎样传递，而不是要求所有组件都支持 ref。
- 高阶组件或组合工具如果不能预先确定被包裹组件使用的版本，迁移期间可能需要兼容两种机制。应限制这层兼容代码的范围，最低支持版本升到 React
  19 时将其删除。
- 通过抓来的 ref 读别的组件的 DOM 节点——与接收传下来的 ref 相对——是组件边界决策，本篇不覆盖。

## 示例

搜索面板在打开的瞬间聚焦它的组合框。组件在 React
19 线上暴露自己的输入框；调用点既不知道也不关心 ref 是怎么传的。

```tsx
import { useEffect, useRef } from "react";

function Combobox({ ref, label, ...rest }: InputProps & { ref?: React.Ref<HTMLInputElement> }) {
  return (
    <label>
      <span>{label}</span>
      <input ref={ref} role="combobox" {...rest} />
    </label>
  );
}

function SearchPanel() {
  const queryRef = useRef<HTMLInputElement>(null);
  useEffect(() => queryRef.current?.focus(), []);

  return <Combobox ref={queryRef} label="Search" />;
}
```

在仍支持 React 18 的库版本线上，同一个组件用 `forwardRef`
编写，调用点逐字节相同——这正是机制选择留在组件内部与版本线内、绝不泄漏给调用者的原因。
