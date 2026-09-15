# 独立的异步工作同时启动

## 适用场景

编写或审查一个执行多个请求或其他 I/O 操作的 async 函数时应用。逐个操作判断：它的输入是否依赖另一个操作的结果，只对真正的依赖做排序。

## 具体指导

先分类，再排序。只有消费另一个操作的结果作为输入的操作才是依赖操作；其余都是独立操作，可以立即启动。独立操作用 `Promise.all` 一起启动，结算结果按调用顺序返回，与完成顺序无关。

`Promise.all` 要么全有要么全无：任一输入 reject 就立即 reject，批内其余结果被丢弃。调用方能利用部分结果时，改用 `Promise.allSettled` 并逐个检查状态。

依赖关系不要求把无关工作串行化。输入的 promise 一启动，就立刻从它派生依赖操作的 promise，并把这条链式 promise 放进同一个最终的 `Promise.all`：

```ts
const customerPromise = getCustomer(customerId);
const paymentMethodsPromise = customerPromise.then((customer) =>
  getPaymentMethods(customer.id),
);

const [customer, taxRegion, template, paymentMethods] = await Promise.all([
  customerPromise,
  getTaxRegion(request.countryCode),
  getDefaultInvoiceTemplate(),
  paymentMethodsPromise,
]);
```

依赖泳道只多花自己那一段路；独立泳道与它并行。

控制扇出规模。对长列表逐项执行时，限制并发而不是一次启动所有请求；「同时」指每条泳道内同时，不是无上限。`Promise.all` 重叠的是 I/O 等待；它不并行化 CPU 工作，共享同一连接池或单线程资源的请求最终仍可能串行。把收益预期放在独立网络请求上，不要当成普适倍率。

## 反模式

发票组装器依次 await 客户、税率区、发票模板、支付方式。没有任何结果依赖前一个，总延迟等于四个往返之和，而同样的数据本可以只花最慢单条泳道的时间。

## 原因

放在无关工作之前的每个 `await` 都是一道这些操作必须排队的屏障。独立操作同时启动，把这一组的墙钟时间压缩到最慢成员；依赖操作在输入落定那一刻启动，链条就不会变成整段屏障。

## 例外与边界

- 每个操作都真正喂养下一个时，顺序就是依赖图本身；本篇不要求并行化真正的依赖。
- `Promise.all` 的 fail-fast 对组装单一响应通常是正确的；只有调用方对部分结果有明确行为时才选 `Promise.allSettled`。
- 第三方限流或按次计费会让有意的串行比最大并发更便宜；存在配额时显式限流或串行。
- 本篇停留在单函数层面。重构组件树让慢数据不阻塞页面外壳是 `react.async.suspense-boundary-scope` 的决策；列表逐项的后续链式请求是 `react.async.chain-nested-item-fetches`。

## 示例

发票组装服务独立需要客户、本次请求的税率区、默认模板；支付方式依赖客户。链式 promise 在客户落定瞬间启动，支付方式泳道只多花自己那一段。声明的 helper 代替数据层。

```ts
type Customer = { id: string; name: string };
type TaxRegion = { code: string; rate: number };
type InvoiceTemplate = { id: string; headerHtml: string };
type PaymentMethod = { id: string; label: string };

declare function getCustomer(id: string): Promise<Customer>;
declare function getTaxRegion(countryCode: string): Promise<TaxRegion>;
declare function getDefaultInvoiceTemplate(): Promise<InvoiceTemplate>;
declare function getPaymentMethods(customerId: string): Promise<PaymentMethod[]>;

export async function buildInvoiceSummary(customerId: string, countryCode: string) {
  const customerPromise = getCustomer(customerId);
  const paymentMethodsPromise = customerPromise.then((customer) =>
    getPaymentMethods(customer.id),
  );

  const [customer, taxRegion, template, paymentMethods] = await Promise.all([
    customerPromise,
    getTaxRegion(countryCode),
    getDefaultInvoiceTemplate(),
    paymentMethodsPromise,
  ]);

  return { customer, taxRegion, template, paymentMethods };
}
```

墙钟成本现在是 `max(customer + paymentMethods, taxRegion, template)`——最慢单条泳道，而不是四段之和。若一条泳道失败时发票仍可部分渲染，最终的 await 就换成对同样四个 promise 的 `Promise.allSettled`。
