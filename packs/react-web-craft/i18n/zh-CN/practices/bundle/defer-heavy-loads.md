# 重型非关键加载延后到需要时

## 适用场景

某个模块、组件或第三方库相对页面很大、且首绘或首次交互并不需要它——编辑器、图表库、地图组件、导出对话框、analytics 脚本——时应用。此时要决定：什么预先加载，什么等用户真正到达该功能时再加载。

## 具体指导

同时延后两种成本：下载成本和执行成本。静态导入的模块无论其功能是否渲染都会进入初始依赖图；动态导入则成为独立 chunk，在首次渲染或首次调用时才获取：

```tsx
const ReportBuilder = dynamic(() => import("./report-builder"), {
  loading: () => <p>Loading report builder…</p>,
});
```

组件用框架的组件加载器（Next.js 中是 `next/dynamic`），数据与非组件模块用普通 `import()`，第三方脚本用框架的脚本加载策略——analytics 和聊天挂件通常是脚本而非 React 组件，其加载策略与组件代码切分是两回事。诚实地对待取舍：`ssr: false` 让组件退出服务端渲染（在 App Router 中必须从客户端组件使用），因此交付的 HTML 不含它；这对挂件通常正确、对内容通常错误。

保持导入路径可被静态分析。bundler 拆不动它看不见的东西：优先用显式的 loader 函数映射而不是拼接路径字符串；服务端代码里优先用字面量文件路径——过宽的路径还会扩大 Next.js 的输出文件追踪范围：

```ts
const REPORT_LOADERS = {
  sales: () => import("./reports/sales"),
  usage: () => import("./reports/usage"),
} as const;

const loadReport = REPORT_LOADERS[reportKind];
```

延后的同时纠正一个常见误解：`typeof window !== "undefined"` 这类运行时守卫只能阻止模块在服务器上执行，并不能把它移出服务器 bundle。bundle 归属由静态导入和 loader 开关决定，与运行时检查无关。

## 反模式

设置页静态导入了一个完整图表库，而只有管理员可见的用量对话框会渲染它。每个访客——包括那九成九永远不会打开对话框的人——都在页面可交互之前下载并解析了它。

## 原因

初始 bundle 与用户的第一印象竞争；里面的可延后代码是多数人替少数人付的钱。动态导入把这笔成本变成独立 chunk，恰好在功能被触达时获取；显式的 loader 映射让 bundler 的可达集合保持收窄，而不是被迫保守地过度打包。

## 例外与边界

- 不要延后关键渲染路径或首次交互路径上的代码；延后关键组件只是用一种成本换更糟的另一种。
- 小模块不值得拆分：额外的 chunk 请求可能比省下的字节更贵；这是成本边界，不是风格规则。
- `typeof window` 守卫与 `ssr: false` 回答的是两个问题（执行与打包归属）；本篇不替代 rendering 类别中浏览器 API 与 SSR 的边界决策。
- 决定延后 chunk 应在点击前多久预取，是 `react.bundle.preload-on-intent` 的决策；barrel 文件入口的排除在本 Pack 中暂缓，待构建产物证据。

## 示例

设置页渲染一个仅管理员可见的用量区块；图表库藏在动态边界之后，只在管理员展开时获取。大多数访客永远不下载它。

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

图表库随 `usage-charts` chunk 发货，在 `UsageCharts` 首次渲染时获取——对多数访客而言永远不会。若多种报表竞争同一位置，就挂到上面的 loader 映射上，每个条目都是字面量 `() => import(...)`，让 bundler 枚举拆分点而不是过度打包整个目录。
