# 用户意图出现时预载已延后的代码

## 适用场景

用户通过按钮、标签页或向导下一步打开动态导入的功能时，点击前的操作可能已经表明他们会用到它。这时可以考虑提前加载代码，但要先判断哪些操作足以支持这次提前下载。

## 具体指导

选择预载时机，要看信号有多明确，以及猜错会花多少带宽。按键、完成向导上一阶段、已知会启用功能的开关，都是更明确的信号；悬停和聚焦（`onMouseEnter`、`onFocus`）也能以较小成本提前一点加载。挂载后就无条件预载最缺乏依据，通常不应这样做。只预载当前界面确实可能用到的少数 chunk，不要把所有功能都预载一遍：

```tsx
const preloadCheckout = () => {
  void import("./checkout-flow");
};

export function CheckoutEntry() {
  return (
    <button
      onMouseEnter={preloadCheckout}
      onFocus={preloadCheckout}
      onClick={() => void import("./checkout-flow").then((m) => m.openCheckout())}
    >
      Go to checkout
    </button>
  );
}
```

对同一模块重复调用 `import()`，会复用正在进行的加载或已缓存的模块。点击处理器可以再调用一次
`import()` 来使用它，不必用共享状态变量记录预载进度。

先了解框架已经做了哪些预取。Next.js 会预取链接路由（生产环境 `<Link>`
进入视口时会预取），所以这里的意图预载主要用于动态导入的 chunk 和非链接目标，也就是此前拆出去延后加载的代码。猜错会浪费带宽，还会和当前页面的加载竞争；因此只选少量 chunk，并根据度量结果决定，不要默认全部预载。

## 反模式

仪表盘挂载后立即预载每个面板的 chunk——十二个重型模块——因为「说不定有人会打开」。在计量资费和移动网络下，预载扼杀了仪表盘自己的数据获取；用户最常打开的面板并没有因此更快。

## 原因

延后加载能让不使用该功能的访客免于下载它。出现意图信号后再预载，会在点击前启动下载；用户继续操作时，需要等待的时间就可能缩短。每次挂载都预载，则会在用户尚无使用意图时也消耗带宽。

## 例外与边界

- 被延后的功能离每次会话只有一次点击、且小到本就即时，就不必预载；这是成本边界。
- 不要用预载补偿关键路径代码被错误延后；先修延后决策。
- 预载代码不等于预取数据：缓存的模块代码在使用时仍要取自己的数据，数据预取自有一套过期与隐私考量，不在本篇范围。
- 在服务器上预载没有意义——那里的守卫问题是执行而非打包归属；见 `react.bundle.defer-heavy-loads`。

## 示例

结算向导的重型阶段分别放在延后加载的 chunk 中。用户进入当前阶段后，就预载下一阶段的 chunk，这是明确的操作信号。`AddressForm`
是留在主包里的小型本地组件，因为拆分它的成本高于节省的成本。

```tsx
"use client";

import { useEffect } from "react";
import dynamic from "next/dynamic";

const ReviewStage = dynamic(() => import("./review-stage"));
const PaymentStage = dynamic(() => import("./payment-stage"));

export function CheckoutWizard({ stage }: { stage: "address" | "review" | "payment" }) {
  useEffect(() => {
    if (stage === "address") void import("./review-stage");
    if (stage === "review") void import("./payment-stage");
  }, [stage]);

  if (stage === "address") return <AddressForm />;
  if (stage === "review") return <ReviewStage />;
  return <PaymentStage />;
}
```

用户填写地址表单时，review
chunk 已在加载。如果进入下一阶段前下载完成，该阶段就不必再等待下载。每一步只预载一个下一阶段的 chunk，由用户当前所在的步骤决定。
