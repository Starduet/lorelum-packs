# 在用户覆盖之前保持响应式默认值

## 适用场景

控件可能需要先跟随父级或服务器不断更新的默认值，等用户选定后再保留用户的选择，不被后续默认值覆盖。先分清这是否真是所需行为：完全受控的值始终由父级决定；只在挂载时使用的初值则本来就不会随来源更新。

## 具体指导

先决定谁控制显示值，再决定如何保存状态：

- 如果父级必须在每次渲染时决定显示值，使用受控值和变更回调，不要再存一份可能与父级冲突的本地值。
- 如果只需要组件首次挂载时的来源值，就用它初始化 state；之后来源变化不会自动替换 state，这应是预期行为。
- 如果要在用户编辑前跟随来源，就单独表示「尚无本地覆盖」。有用户选择时显示该值，否则显示当前来源值。这样，来源的后续变化只在用户尚未选择时反映到控件上。

来源切换到另一个实体时，明确本地选择应保留到何时。用稳定的实体 ID 作为编辑器的
`key`，或显式重置本地覆盖，避免把上一条记录的编辑带到下一条。如果 `undefined`
本身也是合法选择，就用带标签的状态分别表示「没有覆盖」和「已选择某个值」，不要同时用 `undefined`
表示这两种含义。

不要用 Effect 持续把来源复制进本地状态。那会抹掉「继承值」与「用户意图」的界线，并引入第二条更新路径。

## 反模式

结果数控件从工作区策略初始化 `pageSize`，然后期待后续策略变化会更新它。`useState`
的初始化器只在首次挂载使用，后续默认值被忽略。若改成用 Effect 把每个新默认值复制进来，又会有覆盖用户明确选择的风险。

## 原因

默认值、受控值和本地覆盖由不同一方控制，更新规则也不同。只用一个普通 state 值表达它们，会看不出该遵循哪条规则。用户未操作时不设置本地覆盖，就能继续显示当前来源的值；用户选定后保留覆盖，就能在来源更新时保住用户的选择。

## 例外与边界

- 完全受控的输入在每次编辑后仍由父级保持权威；本篇不建议再叠一层本地回退。
- 有意只初始化一次的值，忽略后续 prop 变化可能是正确的。给 prop 起相应名字；若身份变化应开启新的状态生命周期，用
  `key` 或显式重置。
- 来源刷新时，本地覆盖可能需要冲突解决或保存/回滚行为。本篇只定义显示优先级，不定义同步、持久化或合并策略。
- 本篇不讨论「能由当前 props/state 算出的纯值该如何存储」，也不一般性地规定 Effect 设计。

## 示例

工作区策略决定每页显示 25、50 或 100 条结果。用户选择本地页大小之前，控件跟随当前策略值；用户做出显式选择后（包括任何合法的数字选项），该选择一直生效，直到用户回到工作区默认。

```tsx
import { useState } from "react";

type PageSize = 25 | 50 | 100;
const pageSizes: PageSize[] = [25, 50, 100];

export function PageSizeSetting({
  workspaceDefault,
}: {
  workspaceDefault: PageSize;
}) {
  const [override, setOverride] = useState<PageSize | undefined>(undefined);
  const pageSize = override ?? workspaceDefault;

  function handleChange(value: string) {
    const nextSize = pageSizes.find((size) => String(size) === value);
    if (nextSize !== undefined) setOverride(nextSize);
  }

  return (
    <fieldset>
      <legend>Result settings</legend>
      <label>
        Results per page
        <select
          value={pageSize}
          onChange={(event) => handleChange(event.currentTarget.value)}
        >
          {pageSizes.map((size) => (
            <option key={size} value={size}>
              {size}
            </option>
          ))}
        </select>
      </label>
      <button type="button" onClick={() => setOverride(undefined)}>
        Use workspace default
      </button>
    </fieldset>
  );
}
```

当 `override` 为 `undefined` 时，`workspaceDefault`
变化后 select 跟随策略。用户选定之后，本地值在后续策略更新中保持优先，直到用户重新选择工作区默认。若生效的设置范围切换到另一个工作区，就在该身份边界处重置或隔离这份覆盖。
