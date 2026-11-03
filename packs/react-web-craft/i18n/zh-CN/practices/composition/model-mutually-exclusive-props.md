# 用判别联合建模互斥的 React props

## 适用场景

一个组件同时提供单日和日期范围等互斥模式时，不应允许调用者只传一个范围端点，或传入与所选模式不匹配的回调。如果 React
TypeScript 组件的可选 props 或布尔值允许这类组合，可以用判别联合把每种模式与必需的数据绑定起来。

先确认是否仍应保留单个公开组件。各模式可以需要不同的数据和行为；但如果需要分别管理 state、使用独立的 provider、采用无关的组合方式或提供不同的扩展点，就应暴露多个命名组件，不要强行放进一个联合。

## 具体指导

给每个模式一个字面量判别字段，如 `mode: "single"` 或
`mode: "range"`。每种模式对应一个联合成员，列出它必需的输入和回调。已知只属于其他模式的 prop 写成
`?: never`，以拒绝传入的值，包括通过有类型的对象展开传入的值。用穷举 `switch`
根据判别字段收窄 props，只共享两个模式确实共用的渲染。`disabled`
等可独立组合的选项放在模式联合之外。

`?: never` 是编译期约束，不是运行时校验。开启 `strictNullChecks`、未开启
`exactOptionalPropertyTypes` 时，可选的 `never` 属性仍接受显式传入的 `undefined`。它能拒绝非
`undefined` 的冲突值，却不能保证该属性没有被传入。

`exactOptionalPropertyTypes` 要求开启
`strictNullChecks`，并且只在 tsconfig 启用它的项目中收紧赋值规则；可复用组件库不能要求使用者都开启它。运行时应根据判别器决定模式。如果行为要求冲突属性完全不存在，就在输入边界校验或规范化这些属性，不要只依赖类型。

假定使用自动 JSX 运行时（`jsx: "react-jsx"`) 与相应的 React
JSX 类型声明；使用经典转换时按项目要求引入 React。

```tsx
type SingleDateProps = {
  mode: "single";
  selectedDate: Date;
  onSelect: (date: Date) => void;
  startDate?: never;
  endDate?: never;
  onSelectRange?: never;
};

type DateRangeProps = {
  mode: "range";
  startDate: Date;
  endDate: Date;
  onSelectRange: (range: { start: Date; end: Date }) => void;
  selectedDate?: never;
  onSelect?: never;
};

export type DateSelectionProps = SingleDateProps | DateRangeProps;

function assertNever(_value: never): never {
  throw new Error("Unsupported date selection mode");
}

export function DateSelection(props: DateSelectionProps) {
  switch (props.mode) {
    case "single":
      return (
        <section>
          <p>Selected date: {props.selectedDate.toLocaleDateString()}</p>
          <button type="button" onClick={() => props.onSelect(props.selectedDate)}>
            Confirm date
          </button>
        </section>
      );
    case "range":
      return (
        <section>
          <p>
            Selected range: {props.startDate.toLocaleDateString()} – {props.endDate.toLocaleDateString()}
          </p>
          <button
            type="button"
            onClick={() => props.onSelectRange({ start: props.startDate, end: props.endDate })}
          >
            Confirm range
          </button>
        </section>
      );
    default:
      return assertNever(props);
  }
}
```

`mode`
字段让 TypeScript 确定每个分支可用的 props。single 变体不能传入可用的日期范围；range 变体必须有两个端点和范围回调。新增联合成员后，类型检查会要求
`switch` 处理它。固定的 fallback 错误只是防御绕过 TypeScript 约束的值，不能替代外部输入校验。

## 反模式

日历组件接受
`mode?`、`selectedDate?`、`startDate?`、`endDate?`、`onSelect?`、`onSelectRange?`，全部可选。调用者可以只给一个范围端点、省掉所选模式必需的回调、或把单日期与仅范围可用的值组合起来。实现必须处理缺失的模式与不完整的数据、守卫每个可选字段的读取，而不是接收一个必需数据在静态上已知的变体。

## 原因

独立的可选字段描述大量组合，包括 UI 用不上的状态。带标签的联合把每个模式与它的必需输入和回调绑定，TypeScript 按判别器收窄 props，在经过检查的调用点拦下非法组合。穷举
`switch` 还让新增的模式对实现可见。

## 例外与边界

模式需要独立的所有权、单独的 provider、实质不同的组合或不同扩展点时，改用分开的命名组件；联合不应把无关的 UI 硬塞进一个公开组件。TypeScript 不校验 JSON、URL 状态、JavaScript 调用方或其他不可信的运行时输入，构造
`DateSelectionProps`
之前先解析或校验这些值。不要从跨模式属性是否存在来推断模式；以显式判别器分支。当经过检查的赋值也必须拒绝显式传入的
`undefined` 时，注意上文 `exactOptionalPropertyTypes` 的警告。

## 示例

排期界面通过同一个日历组件提供单日选择和日期范围选择。两个变体共用一个公开组件，但需要不同的选择数据与回调。上面的代码只演示 props 约束；生产级日历仍需实现日期导航、选择与校验。
