# 重型非关键加载延后到需要时

## 适用场景

编辑器、图表库、地图组件、导出对话框或 analytics 脚本可能占了很大体积，但首绘和首次交互并不需要它们。这时可以等用户用到对应功能时再加载，不必放进首次加载中。

## 具体指导

同时延后两种成本：下载成本和执行成本。静态导入的模块无论其功能是否渲染都会进入初始依赖图；动态导入则成为独立 chunk，在首次渲染或首次调用时才获取：

```tsx
const ReportBuilder = dynamic(() => import("./report-builder"), {
  loading: () => <p>Loading report builder…</p>,
});
```

组件用框架的组件加载器（Next.js 中是 `next/dynamic`），数据与非组件模块用普通
`import()`，第三方脚本用框架的脚本加载策略。analytics 和聊天挂件通常是脚本，不是 React 组件，不能把脚本加载策略与组件代码切分混为一谈。还要注意
`ssr: false` 会让组件不参与服务端渲染，交付的 HTML 因而不含它。在 App
Router 中，这个选项必须从客户端组件使用。不在 HTML 中输出挂件通常合适，不输出内容通常不合适。

导入路径要能被 bundler 静态分析，否则它无法确定该拆分哪些模块。优先用明确列出 loader 函数的映射，不要拼接路径字符串。服务端代码也优先用字面量文件路径，过宽的路径还会扩大 Next.js 输出文件追踪的范围：

```ts
const REPORT_LOADERS = {
  sales: () => import("./reports/sales"),
  usage: () => import("./reports/usage"),
} as const;

const loadReport = REPORT_LOADERS[reportKind];
```

延后的同时纠正一个常见误解：`typeof window !== "undefined"`
这类运行时守卫只能阻止模块在服务器上执行，并不能把它移出服务器 bundle。bundle 归属由静态导入和 loader 开关决定，与运行时检查无关。

## 反模式

设置页静态导入了一个完整图表库，而只有管理员可见的用量对话框会渲染它。每个访客——包括那九成九永远不会打开对话框的人——都在页面可交互之前下载并解析了它。

## 原因

初始 bundle 中的代码，即使访客从不使用对应功能，也要下载和解析。动态导入把代码放进独立 chunk，让条件功能在渲染或调用时才加载它。显式的 loader 映射告诉 bundler 具体可能加载哪些模块，避免因为路径不确定而打包更大的范围。

## 例外与边界

- 不要延后关键渲染路径或首次交互路径上的代码；延后关键组件只是用一种成本换更糟的另一种。
- 小模块不值得拆分：额外的 chunk 请求可能比省下的字节更贵；这是成本边界，不是风格规则。
- `typeof window` 守卫与 `ssr: false`
  回答的是两个问题（执行与打包归属）；本篇不替代 rendering 类别中浏览器 API 与 SSR 的边界决策。
- 决定延后 chunk 应在点击前多久预取，是 `react.bundle.preload-on-intent`
  的决策；barrel 文件入口的排除在本 Pack 中暂缓，待构建产物证据。

## 示例

设置页只为管理员渲染用量区块。图表库放在独立 chunk 中，非管理员访客不需要加载它。本例中，管理员即使尚未展开
`<details>`，也已经渲染了 `UsageCharts`；加载不是由展开动作触发的。

```tsx
"use client";

import dynamic from "next/dynamic";

const UsageCharts = dynamic(() => import("./usage-charts"), {
  loading: () => <p>Loading charts…</p>,
});

export function SettingsPage({ isAdmin }: { isAdmin: boolean }) {
  return (
    <main>
      <h1>Settings</h1>
      <ProfileForm />
      {isAdmin && (
        <details>
          <summary>Usage</summary>
          <UsageCharts />
        </details>
      )}
    </main>
  );
}
```

图表库位于 `usage-charts` chunk 中，在 `UsageCharts`
首次渲染时加载；多数访客不会渲染它，也就不需要这次加载。若同一位置可能显示多种报表，就使用上面的 loader 映射，每个条目写成字面量
`() => import(...)`，让 bundler 确定具体拆分点，避免把整个目录都包含进去。
