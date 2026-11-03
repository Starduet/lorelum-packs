# 独立的异步工作同时启动

## 适用场景

一个 async 函数要发起多个请求或执行多项 I/O 时，先看每个操作需要什么输入。如果不需要另一个操作的结果，就不必等它完成后才启动。

## 具体指导

用 `Promise.all`
同时启动互不依赖的操作。某个操作需要另一个操作的结果作为输入时，才要等待那个结果。返回的结果仍按调用顺序排列，与完成顺序无关。

`Promise.all`
要么全有要么全无：任一输入 reject 就立即 reject，批内其余结果被丢弃。调用方能利用部分结果时，改用
`Promise.allSettled` 并逐个检查状态。

有依赖关系的请求，也不必拖住其他请求。先启动提供输入的请求，再用它的 promise 衔接后续操作，把衔接后的 promise 与其他独立请求一起放进最终的
`Promise.all`：

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

支付方式请求只需等客户请求完成；税率区和模板请求可以与这两个有依赖关系的请求同时进行。

对长列表逐项发请求时，限制同时运行的请求数，不要一次启动所有请求。`Promise.all`
让多个请求同时等待 I/O，并不会并行执行 CPU 计算。共享同一连接池或单线程资源的请求仍可能串行；独立网络请求通常能受益，但并非所有工作都能获得同样的加速。

## 反模式

某个版本的发票组装器已经有四项请求各自所需的输入，却仍依次 await 客户、税率区、发票模板和支付方式。这个版本中，四个请求互不依赖，串行只会把四次等待相加；一起启动只需等最慢的请求。如果支付方式确实需要客户请求的结果，就应保留前文那样的依赖链，不能把它也当成独立请求。

## 原因

在无关请求之前执行
`await`，会推迟那个请求的启动。同时启动独立请求，就能让它们同时等待 I/O。有依赖关系的请求应在自己的输入就绪后立即启动，不必再等其他无关结果。

## 例外与边界

- 如果每个操作都需要前一个操作的结果，就应按依赖关系串行执行；本篇不要求把真正有依赖的操作改为并行。
- `Promise.all` 的 fail-fast 对组装单一响应通常是正确的；只有调用方对部分结果有明确行为时才选
  `Promise.allSettled`。
- 第三方限流或按次计费会让有意的串行比最大并发更便宜；存在配额时显式限流或串行。
- 本篇停留在单函数层面。重构组件树让慢数据不阻塞页面外壳是 `react.async.suspense-boundary-scope`
  的决策；列表逐项的后续链式请求是 `react.async.chain-nested-item-fetches`。

## 示例

发票组装服务分别需要客户、本次请求的税率区和默认模板；支付方式依赖客户。客户请求完成后立即启动支付方式请求，不必等税率区或模板。示例中声明的辅助函数代表数据层。

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

总耗时现在取决于最长的依赖链，即
`max(customer + paymentMethods, taxRegion, template)`，而不是四次请求时间之和。如果一个请求失败后仍能渲染部分发票，最终的 await 就改为对同样四个 promise 使用
`Promise.allSettled`。
