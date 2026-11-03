# 资源提示与脚本加载按真实需要定级

## 适用场景

给页面或 layout 添加资源提示（`preload`、`preconnect`、DNS 提示），或加载框架 bundle 之外的脚本时，先看页面什么时候会用到它。再决定浏览器应多早准备连接、下载资源或执行脚本。

## 具体指导

根据提示会启动什么工作，以及页面需要该资源的确定程度，选择提示类型：

- 可能访问的域用 `prefetchDNS`，确定很快要访问的域（API origin、字体 CDN）用
  `preconnect`。浏览器能保留的预连接有限，添加太多会让先建好的连接失效。
- 当前页面确定会用到、但解析器很晚才会发现的资源，如关键字体、首屏大图，用 `preload`。React
  DOM 提供可在服务端渲染期间调用的资源函数（`preload`、`preinit`、`preloadModule`），让提示随 HTML 发出，不必等解析器发现资源后才启动。
- 必须尽早加载并执行的样式表或脚本用
  `preinit`。它不只是提前下载，还会应用样式或执行脚本，因此只留给真正关键的资源。

脚本遵循同一套优先级逻辑。经典 `<script src>` 阻塞解析；`defer`
并行下载、解析完成后按序执行；`async`
到达即执行、不保证顺序。按依赖选择，不按习惯：依赖 DOM 或其他脚本的代码用
`defer`；独立的计数器和埋点用 `async`。Next.js 中用框架的脚本组件及其策略（多数第三方埋点用
`afterInteractive`，能等到空闲的用 `lazyOnload`）而不是裸标签，框架会把它们与 hydration 协调起来。

提示可能让资源与页面的关键下载争抢连接和带宽。关键路径变化时应复查提示，删除不再需要提前加载的资源提示。

## 反模式

营销页的 head 对八个第三方 origin 做 preconnect，预加载两张已有 `fetchpriority`
处理的首屏大图，analytics 埋点却仍以裸阻塞脚本加载。浏览器把连接烧在页面可能永远不会调用的 origin 上，而访客真正在等的东西——首绘——却在等一个本该
`async` 的埋点。

## 原因

浏览器得知资源后，才能准备连接或发起获取。提示可以让这些工作早于正常发现时机启动；`defer` 和 `async`
则让适合的脚本不再阻塞解析。不需要的提示会占用关键资源同样需要的连接和带宽，因此只有符合页面实际优先级时，提前加载才有帮助。

## 例外与边界

- 框架路由常会预取自己的路由和字体；框架已发出的不要手工重复——重复提示浪费连接。
- 跨域资源的 `preload` 必须设置匹配的
  `crossorigin`，否则实际使用资源时还会重新请求，白费这次预加载；核对提示与最终使用该资源的元素或请求是否一致。
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
