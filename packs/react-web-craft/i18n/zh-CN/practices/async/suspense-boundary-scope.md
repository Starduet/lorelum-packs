# 慢子树放进各自的 Suspense 边界

## 适用场景

页面上某个服务端组件的数据特别慢时，不要让不依赖它的内容一起等待。先找出哪些子树使用这份数据，再把 Suspense 边界放在那里。

## 具体指导

async 组件必须等 await 完成后才能返回 JSX。如果页面先等慢请求再返回，连不依赖它的页面外壳也要等待。把慢请求移进需要它的子组件，并用
`<Suspense>` 包住该子组件。外壳就能先渲染；在 Next.js App
Router 这类支持流式传输的配置下，还能先发送到客户端。慢子组件在数据返回前显示 fallback。

包住整页的边界会让快内容也一起等待，先显示同一个 fallback。每个慢子树各用一个边界，就能在自己的数据就绪后替换 fallback，把快且关键的内容留在初始响应里。页面通常需要后一种安排：快、影响布局或关系到 SEO 的内容留在这些边界之外，只把真正慢的子树包进去。

父组件不先 await 子组件的结果，兄弟组件就能各自启动取数，不必轮流等待。父组件若不使用这些结果，也就不需要在父层对它们做
`Promise.all`。多个组件需要同一份数据时，只创建一次 promise，再让它们在同一个边界内用 React 19 的
`use()` 读取，这样只发一次请求，等待时也一起显示 fallback。

还要考虑用户看到的页面，而不只是性能分析结果。外壳先显示，部分内容稍后替换 fallback，可能引起布局移动。应针对界面各部分权衡这种取舍，不要默认都加边界。

## 反模式

商品页在返回任何 JSX 之前先 await 评论流。标题、价格、导航都不依赖它，却都要陪最慢的来源等待；评论解析之前浏览器什么都看不到。

## 原因

只把慢子组件放在 Suspense 边界内，它的数据请求就不会再阻止外壳渲染。各自有边界的子树可以在自己的数据到达后替换 fallback。快内容留在边界之外，就能保留在初始响应里，这既关系到体感速度，也关系到爬虫读取内容。

## 例外与边界

- 布局关键的数据——尺寸或位置决定周围结构的内容——属于外壳；藏进 fallback 会引起回流。
- SEO 关键的首屏内容应留在初始响应里，而不是通过 fallback 到达。
- 查询很快时，反复显示和替换 fallback 的成本可能超过直接等待；应比较两者的成本，不要默认给每个组件都加边界。
- 慢子树还需要在页面渲染之前启动（导航期间预取）属于框架导航决策，本篇不覆盖。
- 本篇决定组件树中哪部分需要等待慢数据。单函数内的排序见 `react.async.parallel-independent-work` 与
  `react.async.await-after-cheap-work`。

## 示例

商品页把快的目录读取留在外壳——首屏且 SEO 相关——把两个慢面板各自隔离进边界。声明的 helper 代替数据层。

```tsx
import { Suspense } from "react";

type ProductSummary = { name: string; price: string };

declare function getProductSummary(id: string): Promise<ProductSummary>;
declare function getProductReviews(id: string): Promise<{ items: string[] }>;
declare function getCompatibilityChecks(id: string): Promise<{ rows: string[] }>;

async function ProductHead({ id }: { id: string }) {
  const product = await getProductSummary(id);
  return (
    <header>
      <h1>{product.name}</h1>
      <p>{product.price}</p>
    </header>
  );
}

async function ReviewsPane({ id }: { id: string }) {
  const reviews = await getProductReviews(id);
  return (
    <section>
      {reviews.items.map((item) => (
        <p key={item}>{item}</p>
      ))}
    </section>
  );
}

async function CompatibilityPane({ id }: { id: string }) {
  const checks = await getCompatibilityChecks(id);
  return (
    <aside>
      {checks.rows.map((row) => (
        <p key={row}>{row}</p>
      ))}
    </aside>
  );
}

export function ProductPage({ id }: { id: string }) {
  return (
    <main>
      <ProductHead id={id} />
      <Suspense fallback={<p>Loading reviews…</p>}>
        <ReviewsPane id={id} />
      </Suspense>
      <Suspense fallback={<p>Checking compatibility…</p>}>
        <CompatibilityPane id={id} />
      </Suspense>
    </main>
  );
}
```

`ProductPage`
本身不 await，头部数据随初始响应发出；两个面板先各自显示 fallback，数据到达后再显示内容。两个面板的请求也会并发启动，因为父组件没有在渲染前 await 它们。
