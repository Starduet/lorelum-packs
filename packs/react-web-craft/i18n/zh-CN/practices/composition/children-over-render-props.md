# 用 children 组合；render prop 留给数据绑定的插槽

## 适用场景

卡片、工具栏、对话框等容器需要调用者填入内容时，通常可以直接接收元素。设计插槽前先看：调用者是否已有渲染所需的信息，还是必须由组件先提供数据？

## 具体指导

调用者能直接写成元素的内容，如头部、操作区和分区，应通过 `children`
或具名的插槽 prop 传入，不必包成函数再让组件调用：

```tsx
<Card>
  <Card.Header title="Billing" />
  <PlanSummary plan={plan} />
  <Card.Footer>
    <Button onClick={openPortal}>Manage subscription</Button>
  </Card.Footer>
</Card>
```

组件必须提供数据，调用者才能渲染插槽时，再用 render 函数。例如表格的每一行、虚拟列表的每一项或测量出的尺寸，都可以通过回调参数传给调用者：

```tsx
<DataTable rows={invoices} renderRow={(invoice) => <InvoiceRow key={invoice.id} invoice={invoice} />} />
```

逐个 prop 判断：渲染这个插槽，是否需要组件内部的数据？不需要就接收元素。`renderHeader?: () => ReactNode`
如果不接收内部数据，只会让调用者多写一层函数，得不到额外能力。需要组件提供数据的回调命名为
`render*`，把数据写进参数；其他插槽则接收元素。

## 反模式

工具栏组件声明了
`renderLeft`、`renderRight`、`renderOverflow`——全是零参。调用者为了拼几个普通按钮还得研究组件签名，每处使用都把静态元素包进箭头函数，而三个插槽谁也收不到工具栏状态——因为组件从不传。

## 原因

children 直接表达组件树，调用者已经熟悉这种写法。render 函数会多一层调用，只有需要组件提供数据时才有用。区分元素 prop 与 render
prop，也让 API 更清楚：前者接收调用者写好的结构，后者把组件的数据交给调用者渲染。

## 例外与边界

- 零参 render
  prop 偶尔可用于延迟挂载（把重型子树推迟到插槽渲染时）；延迟动机应当写明，而 Suspense 边界通常表达得更好。
- compound-component API（如
  `<Toolbar.Left />`）可以在插槽元素之间共享上下文；只有一次使用、无需共享上下文的插槽不需要增加这套机制。
- 数据绑定插槽和其他列表渲染一样，需要正确的 key 和稳定回调；本篇只决定 API 形式，不改变列表渲染语义。
- 包裹 children 注入 context 属于 provider 设计，不是 render prop；其底层的所有权决策见
  `react.state.share-one-owner`。

## 示例

页头以元素接收操作区和筛选输入框，两者都不需要页头内部的数据。`Button` 与 `FilterInput`
代表实际组件。

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

`actions` 与 `children`
接收元素，调用者可以直接组合按钮和输入框，无需增加回调。只有页头必须提供内部信息时，例如哪些操作被移进了溢出菜单，才需要 render
prop。此时应在签名中写明数据参数，如
`renderOverflow?: (items: Action[]) => ReactNode`，而不是使用无参函数。
