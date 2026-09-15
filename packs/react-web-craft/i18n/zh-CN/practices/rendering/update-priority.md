# 紧迫的输入更新与缓慢的后续渲染分流

## 适用场景

一次交互既更新用户紧盯的控件——文本输入、滑块、选中的标签页——又驱动一帧内完不成的昂贵工作时应用。判断更新中哪部分是紧迫的、哪部分可以滞后。

## 具体指导

两种机制表达分流，按滞后的形态选择：

- 滞后在于渲染输入值的派生视图（过滤大列表、重绘昂贵图表）：推迟值本身。控件保持自己的即时状态，被推迟的值拖在后面，React 保持输入可响应：

  ```tsx
  const [query, setQuery] = useState("");
  const deferredQuery = useDeferredValue(query);
  const results = useMemo(
    () => filterEntries(corpus, deferredQuery),
    [corpus, deferredQuery],
  );
  const isStale = query !== deferredQuery;
  ```

- 滞后在于用户不需要同步完成的状态更新（切换内容很重的标签页、导航）：把更新包进 `startTransition`；UI 需要显示后续工作在途时用 `useTransition`。

用诚实的方式标注滞后——把过时的结果调暗、标签页上加一个细微的 pending 指示——让分流可见，而不是看起来像卡死。不要在分流之外使用这些工具：transition 不会让高频更新变便宜，也不是滚动节流；被推迟的值不是网络防抖，不会取消请求；transition 的 `isPending` 描述的是被推迟更新自身的生命周期，异步后续工作的错误处理与竞态仍是独立决策。

## 反模式

定价页的区间滑块把值写入 state，每次变化都同步地重新过滤并重渲染两百张卡片组成的网格。拖动滑块时掉帧的偏偏是滑块手柄本身——那个必须跟随指针的元素——尽管网格完全可以从容地滞后几帧。

## 原因

并发渲染让 React 能中断低优先级工作，但前提是代码说明了哪些更新可以等。声明输入更新紧迫、派生工作可推迟，被盯着的控件就能保持满帧率，昂贵部分随后落定；过时标记则告诉用户滞后是有意为之。

## 例外与边界

- 派生渲染足够便宜、能在一帧预算内完成时，加推迟只是仪式；先用测量说话。
- 昂贵的是网络请求而非渲染成本时，要分流的是请求生命周期与缓存，不是渲染优先级。
- 后续工作改变用户正看着的内容（不是滞后的镜像，而是导航）时，在导航边界用 transition 决策；隐藏内容的时机是 `react.async.suspense-boundary-scope` 的决策。

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

手柄以满帧率跟随指针，因为它的更新从不等待网格。网格晚一两帧落定，调暗状态告诉用户：滞后是有意的过滤，不是冻结。
