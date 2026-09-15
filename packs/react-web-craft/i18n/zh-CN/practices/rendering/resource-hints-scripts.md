# 资源提示与脚本加载按真实需要定级

## 适用场景

页面或 layout 声明资源提示（`preload`、`preconnect`、DNS 提示）或加载不属于框架 bundle 的脚本时应用。逐个资源决定：浏览器应当多早开始为它工作。

## 具体指导

提示是一座阶梯，越往上成本越高——高段只花在确定性上：

- `prefetchDNS` 给可能会联系的域；`preconnect` 给确定很快会联系的域（API origin、字体 CDN）。浏览器只保温少数几条连接，满屏 preconnect 会互相挤掉。
- `preload` 给当前页面确定会使用、且解析器要很晚才会发现的资源——关键字体、首屏大图。React DOM 把这些暴露为可在服务端渲染期间调用的函数（`preload`、`preinit`、`preloadModule`），提示于是随 HTML 一起发出，而不是等发现之后。
- `preinit` 给必须尽早就绪并执行的样式表或脚本；它最强，留给真正关键的。

脚本遵循同一套优先级逻辑。经典 `<script src>` 阻塞解析；`defer` 并行下载、解析完成后按序执行；`async` 到达即执行、不保证顺序。按依赖选择，不按习惯：依赖 DOM 或其他脚本的代码用 `defer`；独立的计数器和埋点用 `async`。Next.js 中用框架的脚本组件及其策略（多数第三方埋点用 `afterInteractive`，能等到空闲的用 `lazyOnload`）而不是裸标签，框架会把它们与 hydration 协调起来。

每条提示都是一次插队请求，而队伍是共享的：页面关键路径变化时复查它们，删掉不再关键的资源的提示。

## 反模式

营销页的 head 对八个第三方 origin 做 preconnect，预加载两张已有 `fetchpriority` 处理的首屏大图，analytics 埋点却仍以裸阻塞脚本加载。浏览器把连接烧在页面可能永远不会调用的 origin 上，而访客真正在等的东西——首绘——却在等一个本该 `async` 的埋点。

## 原因

浏览器只有在得知资源存在时才开始为它工作，且按 origin 串行化投机性工作。提示的意义是把确定性提前；脚本的 `defer`/`async` 意义是不让独立代码挡在内容前面。让每个资源坐进它的确定性配得上的那一级，首绘才会快；过度提示正是「为猜测付钱却仍然阻塞」的成因。

## 例外与边界

- 框架路由常会预取自己的路由和字体；框架已发出的不要手工重复——重复提示浪费连接。
- 跨域资源的 `preload` 需要正确的 `crossorigin` 匹配，否则会重新获取、提示作废；核对属性与最终消费者一致。
- 按意图预载已延后的功能代码是另一个决策、另一套信号；见 `react.bundle.preload-on-intent`。
- 本篇不设定缓存或 CDN 策略；提示改变发现时机，不改变可缓存性。

## 示例

文档站只声明它确定的东西：一条搜索域连接、显示字体、关键样式表——analytics 埋点等到空闲。

```tsx
import { preconnect, preload, preinit } from "react-dom";
import Script from "next/script";

export default function DocsLayout({ children }: { children: React.ReactNode }) {
  preconnect("https://search.docs.example.com");
  preload("/fonts/docs.woff2", {
    as: "font",
    type: "font/woff2",
    crossOrigin: "anonymous",
  });
  preinit("/styles/critical.css", { as: "style" });

  return (
    <html>
      <body>
        {children}
        <Script src="https://analytics.example.com/collector.js" strategy="lazyOnload" />
      </body>
    </html>
  );
}
```

资源函数的提示随 HTML 发出，字体和样式表在解析器发现它们之前就开始加载；analytics 埋点——独立且非关键——既不阻塞解析，也不与 hydration 争抢。head 里没有任何投机性内容：没有对页面可能永远不调用的 origin 的 preconnect，没有对浏览器本会及时发现的折叠下方图片的 preload。
