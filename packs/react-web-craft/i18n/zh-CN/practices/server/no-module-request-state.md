# 请求数据不进模块作用域

## 适用场景

编写或审查需要把当前用户、请求 ID、locale 之类的值在一次请求的多个部分之间共享的服务端代码——服务端组件、经 SSR 的客户端组件、路由处理器、server
action——时应用。此时要决定：这个值放在哪里。

## 具体指导

把服务器上的模块作用域当作进程级共享内存。并发渲染运行在同一个进程里：请求 A 写入的模块级变量会被请求 B 读到，最后写入者获胜——竞态、跨请求污染、把一个用户的数据渲染进另一个用户的响应，都由此而来。

让请求数据沿渲染树传递——从入口以参数和 props 下传；多个组件需要同一次查询时，用请求级记忆化：

```tsx
export default async function OrderPage({ orderId }: { orderId: string }) {
  const user = await getCurrentUser(token);
  const order = await getOrder(orderId);
  return <OrderSummary user={user} order={order} />;
}
```

为「可以放在模块作用域的东西」维护一份显式允许清单：只读一次的不可变配置、常量、以及为跨请求复用而设计、带正确 key 和容量上限的共享缓存。判别问题不是「它是不是全局？」，而是「这个值在两个并发请求之间是否可能不同？」——可能，就不属于模块作用域。框架的请求对象与请求级存储正是为携带每请求上下文而生；用框架的设施，不要手搓全局变量。

## 反模式

仪表盘页把已认证用户赋给模块级
`currentUser`，嵌套组件读取它。两个重叠的请求交错执行：请求 B 在请求 A 赋值之后、渲染嵌套组件之前覆盖了
`currentUser`，A 的页面显示出 B 的账户名。

## 原因

请求隔离是服务器最基本的正确性边界。模块状态悄悄溶解了它——每个请求共享同一个模块实例；这类缺陷只在并发下、在生产环境、以「别人的数据」的形式出现：是最难复现、也最不该上线的缺陷类型。

## 例外与边界

- 不可变的静态配置和代码常量放在模块作用域是安全的；它们不会因请求而异。
- 有意共享的缓存只有在 key 覆盖数据变化的所有维度（用户、租户、locale）并配备淘汰与容量上限时才安全；设计它本身就是一个决策，而请求内共享不需要这些机关。
- 本篇针对可变的请求级数据；不携带每请求状态的模块级单例（如数据库客户端）是另一种模式、另一套约束。
- 请求内重复查询的性能问题由 `react.server.request-dedup-cache` 处理；本篇管辖的是结果可以放在哪里。

## 示例

订单页在入口处解析它的请求级值并向下传递。每个并发请求都针对自己的值渲染。

```tsx
import { getCurrentUser } from "./session";

export default async function OrderPage({
  orderId,
  token,
}: {
  orderId: string;
  token: string | null;
}) {
  const user = await getCurrentUser(token);
  const order = await getOrder(orderId, user);
  return (
    <section>
      <OrderTitle order={order} />
      <OrderItems order={order} />
      <SupportContact user={user} />
    </section>
  );
}
```

`user` 与 `order`
只存在于本次请求的渲染树里；涉及的模块级对象只有导入的函数和只读配置。两个针对不同订单的重叠请求无法观察到彼此的数据——因为根本没有可供观察的共享变量。
