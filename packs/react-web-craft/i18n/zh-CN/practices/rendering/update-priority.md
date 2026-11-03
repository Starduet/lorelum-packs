# 紧迫的输入更新与缓慢的后续渲染分流

## 适用场景

输入文字、拖动滑块或切换标签页时，后续工作可能太重，一帧内做不完。这时要让控件本身及时响应，再判断哪些后续内容可以稍晚更新。

## 具体指导

根据要推迟的是派生值，还是一次状态更新，选择机制：

- 如果慢的是根据输入值渲染结果，例如筛选大列表或重绘复杂图表，用 `useDeferredValue`
  提供一个可稍后更新的值。控件仍使用立即更新的 state，结果视图读取 deferred 值，让 React 可以优先处理输入：

  ```tsx
  const [query, setQuery] = useState("");
  const deferredQuery = useDeferredValue(query);
  const results = useMemo(
    () => filterEntries(corpus, deferredQuery),
    [corpus, deferredQuery],
  );
  const isStale = query !== deferredQuery;
  ```

- 用户不需要同步完成的状态更新（切换内容很重的标签页、导航）：把更新包进
  `startTransition`；需要显示更新尚未完成时，使用 `useTransition`。

把旧结果调暗，或给标签页添加 pending 指示，说明控件已更新、内容尚未跟上。transition 不会降低高频更新本身的成本，也不是滚动节流。`useDeferredValue`
不会给网络请求防抖，也不会取消请求。transition 的 `isPending`
跟踪该 transition 的生命周期；异步后续工作仍需单独处理错误和竞态。

## 反模式

定价页的区间滑块把值写入 state，每次变化都同步地重新过滤并重渲染两百张卡片组成的网格。拖动滑块时掉帧的偏偏是滑块手柄本身——那个必须跟随指针的元素——尽管网格完全可以从容地滞后几帧。

## 原因

并发渲染允许 React 中断低优先级渲染，但代码要先区分哪些更新可以等待。控件的更新保留高优先级，React 就能优先处理它，再更新结果视图。旧结果或 pending 指示则解释了视图为何仍在显示先前的内容。

## 例外与边界

- 如果派生渲染能在一帧预算内完成，就不必增加推迟机制；应先测量。
- 如果慢的是网络请求，而不是渲染，就应处理请求生命周期与缓存，而不是靠渲染优先级解决。
- 如果后续工作是导航到新内容，而非更新当前输入对应的结果，就在导航处考虑使用 transition；哪些内容需要等待慢数据，见
  `react.async.suspense-boundary-scope`。

## 示例

定价页的区间滑块过滤两百张卡片组成的网格。滑块写自己的紧迫状态；网格读取被推迟的值，滞后期间调暗。

```tsx
function PriceExplorer({ products }: { products: Product[] }) {
  const [maxPrice, setMaxPrice] = useState(500);
  const deferredMaxPrice = useDeferredValue(maxPrice);

  const visible = useMemo(
    () => products.filter((product) => product.price <= deferredMaxPrice),
    [products, deferredMaxPrice],
  );
  const isStale = maxPrice !== deferredMaxPrice;

  return (
    <>
      <input
        type="range"
        min={50}
        max={500}
        value={maxPrice}
        onChange={(event) => setMaxPrice(Number(event.currentTarget.value))}
      />
      <div style={{ opacity: isStale ? 0.6 : 1 }}>
        <ProductGrid products={visible} />
      </div>
    </>
  );
}
```

滑块的值立即更新，网格则使用被推迟的值。React 可以优先处理控件，再处理低优先级渲染。调暗旧结果表明网格尚未更新，用户不必猜测操作是否被忽略。
