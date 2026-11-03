# 每一项的后续请求链进各自的 Promise

## 适用场景

加载列表时，如果每一项都要根据自身结果再请求详情、补充数据或子资源，就要决定后续请求是逐项启动，还是等第一批请求全部完成后再启动。

## 具体指导

为每个标识符创建一个 promise：先加载该项，再用它的结果发起后续请求。最后一起 await 这些逐项 promise：

```ts
const board = await Promise.all(
  shipmentIds.map((id) =>
    getShipment(id).then((shipment) =>
      getTrackingSnapshot(shipment.carrier, shipment.trackingNumber),
    ),
  ),
);
```

每项的第一个请求完成后，就启动该项的后续请求。如果先 await 全部项，再启动全部后续请求，那么即使某项的输入早已就绪，也必须等最慢的第一个请求完成。

页面容忍部分数据时按项处理失败。裸 `Promise.all`
下一个项 reject 就丢弃整个面板；在逐项链内捕获并返回带类型的失败条目，能保住其余行。不做捕获的形态留给真正要求全有全无的调用方。

如果第二阶段要聚合全部结果、跨项去重或对完整集合排序，就确实需要等第一阶段全部完成，应保持两阶段的先后顺序。只有后续请求仅依赖自身那一项时，才能逐项衔接。列表很大时还要限制并发数，不要一次启动所有请求链。

## 反模式

物流面板先 await 全部运单，再 await 全部轨迹快照。一个慢承运商端点拖住了每一行的快照，尽管其他运单的承运商几毫秒就应答了——因为整个第一批落定之前任何后续请求都不能启动。

## 原因

逐项衔接让每个后续请求只等自身那一项的第一个请求，不必等列表中最慢的第一个请求。数据依赖没有变，只是依赖请求可以更早启动。

## 例外与边界

- 第二阶段要聚合全部结果时，必须等第一批全部完成；不要拆开真正需要完整数据的计算。
- 后续请求不依赖项结果时就没有嵌套，属于 `react.async.parallel-independent-work`
  覆盖的普通并行取数。
- 如果列表很小、两阶段请求都很快，就不必为这点收益重构；这是成本边界，不是风格规则。
- 带逐查询缓存与去重的客户端数据层可能让逐项后续请求整体消失；本篇覆盖的是直接的服务端扇出。

## 示例

运单面板给每行补上承运商的轨迹快照。逐项辅助函数先加载运单，再加载快照；捕获快照请求的失败，让对应行仍能显示。面板等待每行各自的 promise。示例中声明的辅助函数代表数据层。

```ts
type Shipment = { id: string; carrier: string; trackingNumber: string };
type TrackingSnapshot = { status: string; updatedAt: string };

type BoardRow =
  | { shipment: Shipment; snapshot: TrackingSnapshot }
  | { shipment: Shipment; snapshot: null; error: string };

declare function getShipment(id: string): Promise<Shipment>;
declare function getTrackingSnapshot(
  carrier: string,
  trackingNumber: string,
): Promise<TrackingSnapshot>;

async function loadRow(id: string): Promise<BoardRow> {
  const shipment = await getShipment(id);
  try {
    return {
      shipment,
      snapshot: await getTrackingSnapshot(
        shipment.carrier,
        shipment.trackingNumber,
      ),
    };
  } catch (error) {
    return { shipment, snapshot: null, error: String(error) };
  }
}

export function loadShipmentBoard(shipmentIds: string[]): Promise<BoardRow[]> {
  return Promise.all(shipmentIds.map(loadRow));
}
```

每项运单请求完成后，立即启动该项的快照请求。承运商响应慢只会拖延自己的快照；快照请求失败时，该行保留错误信息。运单请求本身失败仍会使面板的
`Promise.all` reject。如果先等全部运单再请求快照，最慢的运单就会拖住所有快照请求。
