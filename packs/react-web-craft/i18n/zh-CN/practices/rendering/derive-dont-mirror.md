# 渲染期推导值，不把 props 镜像进 state

## 适用场景

显示的合计、标签等值如果始终由当前 props 和 state 决定，通常不必另存一份 state 再用 effect 更新。先确认用户或外部系统能否独立修改它；不能的话，就直接用当前输入计算。

## 具体指导

值是当前 props 与 state 的纯函数时，在渲染期间计算它，删掉 state 和 effect：

```tsx
const totalWithTax = subtotal + subtotal * taxRate;
```

在 effect 更新副本之前的那次渲染中，副本可能仍是旧值；effect 如果漏掉某个输入变化，还可能一直不更新。改为渲染时计算，就不必维护第二份值，也不必为它再安排一次状态更新。

下面几种情况要分别处理：

- 值用 prop 初始化，但之后由用户编辑：这是有独立生命周期的草稿，初始化后由本地 state 管理。
- 表单换到另一条记录时必须重置：在记录身份变化处用 `key` 显式重置，不要靠 effect 监听 props 再重置。
- 计算开销大：仍然从输入推导，只在测量证明值得时缓存计算结果。记忆化不能解决重复维护两份值的问题。

对 prop 一变就设置 state 的 effect，也按这个标准判断。effect 可以同步外部系统；要删除的是同一渲染树内只负责复制 props 或根据 props 重算值的 effect。

## 反模式

发票编辑器把 `total`
存进 state，在明细或税率变化后用 effect 重算。修改明细时，先渲染旧合计，再由 effect 触发下一次渲染。如果 effect 的依赖列表遗漏了批量导入会改变的输入，合计还可能一直与导入的明细不一致。

## 原因

把派生值存进 state，相当于另存了一份计算结果。输入变化后，effect 要等使用新输入的那次渲染结束才能更新副本。渲染时直接计算，就能立即使用当前输入，不必同步副本，也无需为该值再更新一次 state。

## 例外与边界

- 有真实用户所有权或独立生命周期的值留在 state；本篇不是要缩减 state，而是要删除重复的 state。
- 渲染期推导必须保持纯：没有副作用、没有写入，哪怕推导再昂贵。
- 用 `useMemo` 缓存计算结果会占用内存，也需要维护正确的依赖列表。应结合测量结果与 React
  Compiler 的使用情况，决定省下的计算是否值得；本篇不替代这项优化决策。
- 在 effect 里为 React 无法表达的布局读取并调整 DOM 属于外部系统同步，不是值镜像。

## 示例

发票摘要的两个数字都在渲染期间从输入推导。没有第二份 state 会失同步，也没有 effect 会被遗忘。

```tsx
function InvoiceSummary({ lines, taxRate }: { lines: InvoiceLine[]; taxRate: number }) {
  const subtotal = lines.reduce((sum, line) => sum + line.amount, 0);
  const totalWithTax = subtotal + subtotal * taxRate;

  return (
    <dl>
      <dt>Subtotal</dt>
      <dd>{subtotal}</dd>
      <dt>Total with tax</dt>
      <dd>{totalWithTax}</dd>
    </dl>
  );
}
```

添加、删除或编辑明细时，两个数字在展示该变化的同一次渲染中更新。若性能分析显示超大发票上的求和确实重要，`useMemo`
包住的就是这条推导——代码的形状不变，只是缓存。
