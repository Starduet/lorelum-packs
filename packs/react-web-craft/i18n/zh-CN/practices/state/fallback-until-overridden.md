# 在用户覆盖之前保持响应式默认值

## 适用场景

可编辑控件的初值来自父级或服务器提供的、可能变化的值，而用户做出本地修改后该修改应当优先时应用。此时要判断：父级拥有每一个值、组件只需要挂载时初值，还是组件需要一份「用户行动之前不存在」的本地覆盖。

## 具体指导

先选所有权契约，再选状态形状：

- 若父级必须在每次渲染决定显示值，使用受控值加变更回调；不要再造一份竞争的本地副本。
- 若来源只在组件实例首次挂载时有意义，就把它作为 state 初始化器使用，并接受「之后的来源变化不会自动替换该状态」。
- 若控件应当在用户编辑前跟随变化中的来源，就把「尚无本地覆盖」与实际值分开存储：有本地值时显示本地值，否则显示当前来源。这样来源更新只在尚无覆盖时保持可见。

来源切换到另一个实体时，要让覆盖的生命周期显式化。用稳定的实体身份作为编辑器的
`key`，或有意重置本地覆盖；否则对一条记录的编辑可能泄漏进下一条。若该领域中包括 `undefined`
在内的每个值都是合法的用户选择，就用显式的 tagged state，不要拿 `undefined` 兼作哨兵。

不要用 Effect 持续把来源复制进本地状态。那会抹掉「继承值」与「用户意图」的界线，并引入第二条更新路径。

## 反模式

结果数控件从工作区策略初始化 `pageSize`，然后期待后续策略变化会更新它。`useState`
的初始化器只在首次挂载使用，后续默认值被忽略。若改成用 Effect 把每个新默认值复制进来，又会有覆盖用户明确选择的风险。

## 原因

默认值、受控值、本地覆盖分属不同的所有者、遵循不同的更新规则。把它们塞进同一个普通 state 值会掩盖这些规则。在用户行动之前让覆盖「不存在」，当前来源就能保持权威；此后的显式覆盖则保住用户的选择。

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
