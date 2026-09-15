# 渲染期推导值，不把 props 镜像进 state

## 适用场景

发现组件把一个完全由当前 props 或 state 决定的值存进 state——并且通常由 effect 回写——时应用。判断这个值有自己独立的生命，还是只是一件披着 state 外衣的计算。

## 具体指导

值是当前 props 与 state 的纯函数时，在渲染期间计算它，删掉 state 和 effect：

```tsx
const totalWithTax = subtotal + subtotal * taxRate;
```

存储版在每个方向上都更糟：它晚一拍渲染（effect 在绘制后才运行）；某条代码路径更新了输入却没有触发镜像时它会漂移；为了保持同步还把状态翻倍。

三种情况形似镜像但不是，各自有各自的决策：

- 值从 prop 出发、但用户可以编辑：那是拥有独立生命周期的可编辑草稿；用 prop 初始化，之后由本地持有。
- 值必须在身份变化时重置（表单换绑另一条记录）：在身份边界用 `key`
  显式重置，而不是在 effect 里盯着 props。
- 计算昂贵：照样推导，测量证明值得再记忆化——记忆化是对正确形状的优化，从来不是对错误形状的修法。

同样的判据适用于「响应」prop 变化而设置 state 的 effect：effect 可以与外部系统同步，但同一渲染树内 props 到 state 的方向正是本篇要移除的。

## 反模式

发票编辑器把 `total`
存进 state，由 effect 在每次变化时从明细和税率重算。切换一条明细的那一帧，旧合计先被画出来；另一位开发者新增了一条批量导入路径，只设置明细不触发 effect，显示的合计从此悄悄偏离它所汇总的明细。

## 原因

存储的派生值为一个事实制造了第二个权威，而维护它的 effect 运行在用户所见的渲染之后。渲染期推导保持唯一权威，让值不可能偏离其输入，并省掉额外一次渲染——剩下的 state 恰好就是用户或外部系统真正拥有的那部分。

## 例外与边界

- 有真实用户所有权或独立生命周期的值留在 state；本篇不是要缩减 state，而是要删除重复的 state。
- 渲染期推导必须保持纯：没有副作用、没有写入，哪怕推导再昂贵。
- 用 `useMemo` 记忆化推导，是用内存与依赖卫生换计算；这笔交换是否划算属于测量驱动、考虑 React
  Compiler 的决策，不在本篇范围。
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
