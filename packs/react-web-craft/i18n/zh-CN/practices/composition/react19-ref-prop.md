# React 19 用 ref prop；旧版本线保留 forwardRef

## 适用场景

编写或审查需要向调用方暴露 DOM 节点或命令式句柄的组件——值得获得焦点的输入框、需要定位的对话框——时应用。按项目运行的 React 版本线，决定
`ref` 如何传递。

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

`forwardRef` 在 React
19 上没有错——它仍然可用——但新组件从它那里得不到任何东西，它的间接层（第二层函数边界、独立的类型参数）如今是纯仪式。把它当作迁移决策，而不是风格战争：

- React 19 项目：新组件写 ref-as-prop；碰到本就要改的文件时顺手迁移 `forwardRef` 包装。
- 一条源码线要同时支持 React 18 与 19，或发布的库声明兼容 18 的 peer 范围：保留
  `forwardRef`——它在两个版本上都可用；不要从这条线上发出 19-only 的 ref prop。
- 两种内建机制之一能覆盖版本线时，绝不手搓替代品——在 `ref` 之外再传一个 `domNodeRef`
  风格的自定义 prop。

同样的版本线思维管着 ref 的其余部分：`useImperativeHandle`
的命令式句柄与其附着机制完全一致，上述决策把它们一并覆盖。

## 反模式

组件库锁定 React 18 兼容，一位贡献者把文本输入框「现代化」成 React 19 的 ref-as-prop 并删掉了
`forwardRef`。在 React 18 上，所有调用点的 `ref`
悄悄失效——焦点管理坏了，调用点没有类型错误，运行时也不崩溃，只有死掉的行为。

## 原因

两种机制与版本锁死：ref-as-prop 对 React 18 不可见，`forwardRef` 在 React
19 上是噪音。按项目支持的 React 版本线选择——并在库的 peer 依赖里把这条线写明白——才能在生态完成 19 迁移的过程中保持 ref 支持可用且一致。

## 例外与边界

- 从不暴露节点或句柄的组件根本不该接收 ref；本篇决定的是机制，不是能力存废。
- 高阶组件与组合工具必须对被包裹组件的版本保持不可知，迁移窗口内可能需要同时支持两种机制；把这个垫片收窄，版本下限升到 19 时删除。
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
