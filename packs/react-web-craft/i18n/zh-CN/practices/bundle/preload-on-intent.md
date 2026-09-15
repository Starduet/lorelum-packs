# 用户意图出现时预载已延后的代码

## 适用场景

功能的代码藏在动态导入之后、用户经由一个可见且可预期的步骤到达它——按钮、标签页、向导的下一阶段——时应用。此时要决定：chunk 是否应在点击之前的某个信号出现时就开始加载，以及哪个信号配得上这个提前量。

## 具体指导

按信号强度与成本排序。朝该功能迈出的显式一步（按键、完成向导上一阶段、已知的启用开关）最强；指针与焦点意图（`onMouseEnter`、`onFocus`）用很小的代价换一点提前量；挂载即无条件预载最弱且通常是错的。预载当前界面真正通向的少数 chunk，而不是一份目录：

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

预载调用无需记账：模块的 `import()` promise 自带缓存，点击时的调用与更早的预载共享同一次进行中或已完成的获取。给点击处理器写它自己的 `import()` 调用，而不是保存共享状态。

了解框架已经做了什么。Next.js 会预取链接路由（生产环境 `<Link>` 在进入视口时预取），所以基于意图的预载主要在动态导入 chunk 和非链接目标上才有价值——恰好是延后决策拆出去的那部分代码。预载是提前花掉的带宽：猜错就与当前页面自己的字节争抢，因此把预载清单当成一个小的、经过度量的决策，而不是默认配置。

## 反模式

仪表盘挂载后立即预载每个面板的 chunk——十二个重型模块——因为「说不定有人会打开」。在计量资费和移动网络下，预载扼杀了仪表盘自己的数据获取；用户最常打开的面板并没有因此更快。

## 原因

延后把成本从所有人转移到功能的使用者；按意图预载则在这些使用者还在犹豫时把下载还给他们，点击到达时 chunk 已经就位。区分「提前量」与「税」的是信号，而不是挂载事件。

## 例外与边界

- 被延后的功能离每次会话只有一次点击、且小到本就即时，就不必预载；这是成本边界。
- 不要用预载补偿关键路径代码被错误延后；先修延后决策。
- 预载代码不等于预取数据：缓存的模块代码在使用时仍要取自己的数据，数据预取自有一套过期与隐私考量，不在本篇范围。
- 在服务器上预载没有意义——那里的守卫问题是执行而非打包归属；见 `react.bundle.defer-heavy-loads`。

## 示例

结算向导的每个阶段由各自的延后 chunk 渲染，并在用户落到当前阶段时立即预载下一阶段的 chunk——显式的一步，最强的信号。两个重型阶段被延后；`AddressForm` 是留在主包里的小型本地组件，拆它省的比花的多。

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

用户填写地址表单时，review chunk 已经在路上；跨入下一阶段时面对的是热 chunk 而不是转圈。预载保持有界——每步一个 chunk，由用户真正所在的步骤触发。
