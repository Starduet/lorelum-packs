# 用 React cache 去重请求级查询

## 适用场景

一次服务端渲染需要同一个请求级值——已认证用户、租户设置、多个组件都要展示的记录——而多个组件或 helper 各自独立获取它时应用。此时要决定：这次「每请求一次」的查询放在哪里。

## 具体指导

把查询包进 React 的
`cache()`。在同一次服务端请求内，对缓存函数的每次调用共享一次执行、一份结果；缓存恰好存活一个请求，此外不留任何东西：

```ts
import { cache } from "react";

export const getCurrentUser = cache(async (token: string | null) => {
  if (!token) return null;
  return loadUserByToken(token);
});
```

让实参匹配缓存的相等判定。`cache()` 用 `Object.is`
比较实参：原始类型命中，新建的对象字面量永远未命中。传原始类型的 key；对象实参不可避免时，传一份稳定引用到处使用。

框架已经去重的地方不要再用 `cache()`：Next.js 中同一请求内的相同 `fetch` 调用会自动记忆化，`cache()`
的价值在非 fetch 工作——数据库与 ORM 查询、认证检查、文件读取、昂贵的纯计算。也不要指望它跨请求共享任何东西：跨请求、跨用户、跨实例的去重是另一个决策，涉及
`cache()` 有意不承担的失效与隔离后果。

## 反模式

layout 取一次会话用户，页面为标题再取一次，侧边栏组件为头像又取一次。一次页面渲染发出三条相同的数据库查询；高负载下后端工作量按组件数翻倍。

## 原因

一次服务端渲染是一个逻辑工作单元，但它的组件树由许多独立编写的部件组成；没有请求级记忆化，每个部件都要重新推导共享输入。`cache()`
恰好把记忆化限定在请求内：共享发生在请求内部，请求之间、用户之间保持隔离。

## 例外与边界

- 查询本来每次请求只跑一次时，`cache()` 只添仪式没有收益；这是成本边界。
- 无法表达为原始类型或稳定引用的实参会让缓存失效；重塑函数签名，而不是传新鲜的对象字面量。
- 缓存值在请求生命周期内是冻结的：用于请求视为常量的数据，不用于后续变更必须立即重读的值。
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
