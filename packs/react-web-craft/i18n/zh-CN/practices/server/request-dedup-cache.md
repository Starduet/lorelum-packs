# 用 React cache 去重请求级查询

## 适用场景

一次服务端渲染中，layout、页面和侧边栏可能各自查询同一个已认证用户。多个组件或辅助函数独立获取同一份请求级用户、租户设置或记录时，可以在这次请求内共享查询，避免重复执行。

## 具体指导

把查询包进 React 的
`cache()`。在同一次服务端请求内，调用同一个缓存函数且实参匹配时，共享一次执行和同一份结果；下次请求不会复用这些缓存结果：

```ts
import { cache } from "react";

export const getCurrentUser = cache(async (token: string | null) => {
  if (!token) return null;
  return loadUserByToken(token);
});
```

`cache()` 用 `Object.is`
逐个比较实参：相同的原始类型值可以命中；每次新建的对象即使内容相同，也无法命中。优先传原始类型的 key；必须传对象时，各调用复用同一个引用。

框架已经去重的地方不必再套 `cache()`。Next.js 会自动记忆化同一请求内相同的 `fetch` 调用，因此
`cache()`
主要用于数据库和 ORM 查询、认证检查、文件读取、开销大的纯计算等非 fetch 工作。它不会跨请求共享结果；跨请求、用户或实例的缓存需要另外设计失效和隔离机制，不是
`cache()` 负责的事。

## 反模式

layout 取一次会话用户，页面为标题再取一次，侧边栏组件为头像又取一次。一次页面渲染发出三条相同的数据库查询；高负载下，后端要为每个组件重复查询。

## 原因

一次服务端渲染中，多个组件可能需要同一个用户或同一条记录。没有请求级记忆化，每个组件都会重复查询。`cache()`
在本次请求内复用实参匹配的查询结果，不会把结果共享给另一个请求或用户。

## 例外与边界

- 如果查询本来就每次请求只执行一次，`cache()` 无法减少重复工作。
- 实参无法用原始类型值或稳定引用表示时，就无法命中缓存；应调整函数签名，而不是每次传新建的对象字面量。
- 实参匹配的调用会在本次请求内复用已缓存的结果。它适合请求期间视为不变的数据，不适合变更后必须立即重新查询的值。
- 模块级或跨请求缓存是另一个决策，需要自己的失效、租户与内存设计；关于把请求级数据挡在模块作用域之外的隔离边界，见
  `react.server.no-module-request-state`。

## 示例

同一账户页上两个独立的服务端组件都需要已认证用户。两者调用同一个 `cache()`
包裹的查询；请求内只加载一次。声明的 helper 代替数据层。

```tsx
import { getCurrentUser } from "./session";

export async function AccountHeader({ token }: { token: string | null }) {
  const user = await getCurrentUser(token);
  return <header>{user?.name}</header>;
}

export async function BillingNotice({ token }: { token: string | null }) {
  const user = await getCurrentUser(token);
  return user?.plan === "trial" ? <p>Trial ends soon.</p> : null;
}
```

组合这两个组件的一次页面渲染只发出一次
`loadUserByToken`，无论多少组件需要该用户。第二个请求——哪怕同一用户刷新——会重新执行查询，因为请求之外什么都不留。
