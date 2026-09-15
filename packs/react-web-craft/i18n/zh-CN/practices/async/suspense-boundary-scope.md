# 慢子树放进各自的 Suspense 边界

## 适用场景

某个服务端组件的数据需求远慢于页面其余部分时应用。判断这份数据喂养界面的哪一部分，以及隔离它的 Suspense 边界应放在哪里。

## 具体指导

async 组件里的一个 await 会拖延它输出喂养的一切；页面顶部的 await 拖延整个外壳。把慢取数移进需要它的子组件，并在外面套
`<Suspense>`。外壳立即渲染——在 Next.js App
Router 这类流式配置下还会流式传输到客户端——慢子组件在数据落地前显示自己的 fallback。

边界位置就是决策本身。包住整页的边界让快内容也陪着等一个 fallback；每个慢子树一个边界，让各 fallback 按自己的节奏解析，把快而关键的内容留在初始响应里。页面通常要第二种形状：快、布局关键、SEO 相关的内容保持不包裹，只有真正慢的子树坐进边界。

不在父组件 await，也正是兄弟取数得以并发的原因——组件结构本身就是并行机制；父组件若不消费子组件的结果，就不需要在父层对它们做
`Promise.all`。多个消费者需要同一份数据时，启动一次 promise，让每个消费者在同一个边界内用 React
19 的 `use()` 读取：请求只发生一次，它们一起 fallback。

跟着产品选择，而不是只跟着性能分析器。边界换来更快的首绘，代价是内容稍后在 fallback 中到达、可能引起布局移动；这笔取舍要在每个界面上有意识地做，而不是默认。

## 反模式

商品页在返回任何 JSX 之前先 await 评论流。标题、价格、导航都不依赖它，却都要陪最慢的来源等待；评论解析之前浏览器什么都看不到。

## 原因

Suspense 边界把「这个子树的数据」变成「这个子树的时机」：外壳不再被最慢的取数卡住，每个被包裹的子树独立解析。快内容留在边界之外，就保留在初始响应里——这关系到体感速度，也关系到爬虫。

## 例外与边界

- 布局关键的数据——尺寸或位置决定周围结构的内容——属于外壳；藏进 fallback 会引起回流。
- SEO 关键的首屏内容应留在初始响应里，而不是通过 fallback 到达。
- 廉价查询上，fallback 闪动的成本可能超过等待本身；边界是成本边界，不是默认包装。
- 慢子树还需要在页面渲染之前启动（导航期间预取）属于框架导航决策，本篇不覆盖。
- 本篇决定时机在组件树中的隔离位置。单函数内的排序见 `react.async.parallel-independent-work` 与
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
自身从不安置 await，头部数据随初始响应发出，两个面板各自在自己的 fallback 后解析。两个面板的取数也同时启动，因为没有父组件在渲染前 await 它们。
