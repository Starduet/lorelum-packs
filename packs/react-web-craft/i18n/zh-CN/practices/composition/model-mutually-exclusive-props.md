# 用判别联合建模互斥的 React props

## 适用场景

一个公开的 React
TypeScript 组件 API 必须表达需要不同 props 或回调的互斥模式，而布尔或可选字段让调用者得以描述 UI 无法支持的组合时应用。先确认保留单一公开组件面仍然合适：各模式可以需要不同的数据与行为，但不应需要独立所有的 state、单独的 provider、无关的组合方式或不同的扩展点；若需要，应改为暴露命名组件，而不是把两个变体硬塞进一个联合。

## 具体指导

给每个模式一个字面量判别器，如 `mode: "single"` 或
`mode: "range"`。每个模式定义一个联合成员，并要求该模式的输入与回调。对已知的跨模式 prop 用
`?: never` 拒绝传入的值，包括经类型化对象展开进来的值。用穷举 `switch`
按判别器收窄；只共享真正属于两个模式的渲染。`disabled` 之类的独立选项放在模式联合之外。

`?: never` 是编译期约束，不是运行时校验。开启 `strictNullChecks` 且未开启
`exactOptionalPropertyTypes` 时，可选的 `never` 属性仍接受显式传入的 `undefined`；非 `undefined`
的冲突值会被拒绝，但属性缺席并不被保证。`exactOptionalPropertyTypes` 要求
`strictNullChecks`，且只在 tsconfig 开启它的项目里收紧赋值；可复用组件库无法要求消费者使用该选项。运行时的模式信号以判别器为准。若运行时行为依赖冲突属性缺席，就在边界校验或规范化输入，不要信任类型。

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
字段为每个分支收窄 props。single 变体给不出可用的范围；range 变体要求两个端点和它的范围回调。`switch`
让新增联合成员成为类型检查问题；固定的 fallback 错误只是对绕过 TypeScript 契约的值的防御性失败，不能替代对外部输入的校验。

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

排期界面通过同一张日历面提供单日选择与日期范围选择。两个变体共享日历的公开组件边界，但各自需要不同的选择数据与回调。上面的代码是紧凑的 prop 契约示例；生产级日历仍需实现日期导航、选择与校验。
