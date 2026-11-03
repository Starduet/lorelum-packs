# 请求数据不进模块作用域

## 适用场景

一次请求的多个部分需要当前用户、请求 ID 或 locale 时，要让这些值与其他请求隔离。服务端组件、经 SSR 的客户端组件、路由处理器和 server
action 都要遵守这一点，不能靠共享变量传递请求数据。

## 具体指导

服务器上的模块作用域是进程内共享的。并发请求可能使用同一个模块实例，请求 A 写入的变量，请求 B 也能读取或覆盖。如果 A 再读取时值已被 B 替换，A 的响应就可能显示 B 的用户数据。

让请求数据沿渲染树传递——从入口以参数和 props 下传；多个组件需要同一次查询时，用请求级记忆化：

```tsx
export default async function OrderPage({ orderId }: { orderId: string }) {
  const user = await getCurrentUser(token);
  const order = await getOrder(orderId);
  return <OrderSummary user={user} order={order} />;
}
```

明确哪些值可以放在模块作用域：只读一次的不可变配置、常量，以及专为跨请求复用设计、带正确 key 和容量上限的共享缓存。对于请求上下文，要问的是「两个并发请求是否可能需要不同的值？」如果可能，就不能用同一个共享变量保存它。用框架的请求对象或请求级存储传递上下文，不要自行维护全局变量。

## 反模式

仪表盘页把已认证用户赋给模块级
`currentUser`，嵌套组件读取它。两个重叠的请求交错执行：请求 B 在请求 A 赋值之后、渲染嵌套组件之前覆盖了
`currentUser`，A 的页面显示出 B 的账户名。

## 原因

并发请求可能共享同一个模块实例。一个请求替换模块级变量后，另一个请求再去读取，就可能把错误用户的数据渲染进响应。让每次请求分别保存自己的值，才能避免这种交错执行改变响应内容。

## 例外与边界

- 不可变的静态配置和代码常量放在模块作用域是安全的；它们不会因请求而异。
- 有意共享的缓存只有在 key 覆盖数据变化的所有维度（用户、租户、locale）并配备淘汰机制与容量上限时才安全；设计跨请求缓存是另一个决策，请求内共享不需要这套机制。
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
