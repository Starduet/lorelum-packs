# 用 children 组合；render prop 留给数据绑定的插槽

## 适用场景

设计一个将由他人填充内容的组件——框架、卡片、工具栏、对话框——时应用。判断 API 的哪些部分是调用者已经持有的结构，哪些是组件必须用自己的数据填充的插槽。

## 具体指导

结构用 children 传递。调用者在调用点能写成元素的内容——头部、操作区、分区——应以 `children` 或包含元素的名义插槽 prop 传递，而不是组件回过头来调用的函数：

```tsx
<Card>
  <Card.Header title="Billing" />
  <PlanSummary plan={plan} />
  <Card.Footer>
    <Button onClick={openPortal}>Manage subscription</Button>
  </Card.Footer>
</Card>
```

只有插槽是数据绑定时，render 函数的间接层才值回票价：组件持有调用者渲染所需的信息——表格的每一行、虚拟列表的每一项、测量出的尺寸——回调是投递机制：

```tsx
<DataTable rows={invoices} renderRow={(invoice) => <InvoiceRow key={invoice.id} invoice={invoice} />} />
```

对每个 prop 可审查的问题是：渲染这个槽，调用者需要组件内部的任何东西吗？不需要，就收元素。结果从不触及内部状态的 `renderHeader?: () => ReactNode` 是冒充 prop 的回调，白白付出可读性与内联的代价。命名跟随这条例：插槽 prop 是元素 prop；数据绑定的才叫 `render*`、以数据为参数，而不是零参 thunk。

## 反模式

工具栏组件声明了 `renderLeft`、`renderRight`、`renderOverflow`——全是零参。调用者为了拼几个普通按钮还得研究组件签名，每处使用都把静态元素包进箭头函数，而三个插槽谁也收不到工具栏状态——因为组件从不传。

## 原因

children 是声明式的、树形的、人尽皆知；render 函数增加一层调用，只有组件在每次调用时提供数据才值回成本。元素 prop 与 render prop 分开，组件契约也就自描述了：元素 prop 说「把结构带来」，render prop 说「我会带着我的数据调用你」。

## 例外与边界

- 零参 render prop 偶尔可用于延迟挂载（把重型子树推迟到插槽渲染时）；延迟动机应当写明，而 Suspense 边界通常表达得更好。
- compound-component API（`<Toolbar.Left />`）是插槽元素的共享上下文进化版；它带来的机关是一次性插槽用不上的。
- 数据绑定插槽与任何列表渲染一样需要 key 纪律和稳定回调；本篇只管 API 形状，不管列表渲染语义。
- 包裹 children 注入 context 属于 provider 设计，不是 render prop；其底层的所有权决策见 `react.state.share-one-owner`。

## 示例

页头以元素接收结构，只留一个数据绑定插槽给只有表格才知道的东西。声明的 `Button` 与 `FilterInput` 代替真实组件。

```tsx
function PageHeader({ title, actions, children }: {
  title: string;
  actions?: React.ReactNode;
  children?: React.ReactNode;
}) {
  return (
    <header className="page-header">
      <h1>{title}</h1>
      {children}
      <div className="page-header-actions">{actions}</div>
    </header>
  );
}

<PageHeader
  title="Invoices"
  actions={<Button onClick={newInvoice}>New invoice</Button>}
>
  <FilterInput value={filter} onChange={setFilter} />
</PageHeader>
```

`actions` 与 `children` 是元素：调用者直接组合真实的按钮和输入，没有回调层。render prop 在这里只有在页头必须把内部信息交给调用者时才有立足之地——比如说哪些操作溢出进了菜单——那时签名会说明：`renderOverflow?: (items: Action[]) => ReactNode`，数据是参数，不是零参 thunk。
