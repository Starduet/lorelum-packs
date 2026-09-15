# 每一项的后续请求链进各自的 Promise

## 适用场景

加载一个列表、且每项都需要一个由该项结果派生的第二次请求——详情记录、数据充实、子资源——时应用。此时要决定：后续请求按项启动，还是等整个第一批完成后再启动。

## 具体指导

在项内链式衔接。把每个标识符映射成一个「解析该项并继续其后续请求」的 promise，然后一起 await 这些映射结果：

```ts
const board = await Promise.all(
  shipmentIds.map((id) =>
    getShipment(id).then((shipment) =>
      getTrackingSnapshot(shipment.trackingNumber),
    ),
  ),
);
```

每项的第二段在该项落地时启动。常见的两段式——先 await 全部项，再 await 全部后续——会把最慢的第一段项变成所有后续请求的屏障，哪怕其他项早已落定。

页面容忍部分数据时按项处理失败。裸 `Promise.all`
下一个项 reject 就丢弃整个面板；在逐项链内捕获并返回带类型的失败条目，能保住其余行。不做捕获的形态留给真正要求全有全无的调用方。

第二段需要全部第一段结果时——聚合、跨项去重、对完整集合排序——那是真屏障：保持分段顺序。只有后续请求仅依赖自己那一项时才适用链式。超大列表把链式与并发上限结合，而不是一次启动所有链。

## 反模式

物流面板先 await 全部运单，再 await 全部轨迹快照。一个慢承运商端点拖住了每一行的快照，尽管其他运单的承运商几毫秒就应答了——因为整个第一批落定之前任何后续请求都不能启动。

## 原因

逐项链式移除了跨项屏障：每行的延迟变成它自己的两段路，而不是「最慢同伴的第一段 + 自己的第二段」。数据依赖没有变——只是每个依赖请求允许启动的时点提前了。

## 例外与边界

- 聚合型第二段是真屏障，保持串行；本篇不拆分真正需要完整第一批的计算。
- 后续请求不依赖项结果时就没有嵌套，属于 `react.async.parallel-independent-work`
  覆盖的普通并行取数。
- 两段都很快的小列表不值得重构的仪式感；这是成本边界，不是风格规则。
- 带逐查询缓存与去重的客户端数据层可能让逐项后续请求整体消失；本篇覆盖的是直接的服务端扇出。

## 示例

运单面板给每行充实其承运商的轨迹快照。逐项 helper 链起两段路并容忍单行失败，面板对每项 await 一个行 promise。声明的 helper 代替数据层。

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

每行的快照在自己的运单落定时启动，一个慢的或失败的承运商只损失它那一行。若面板改为先 await 全部运单再 await 全部快照，最慢的运单就会拖住每一行的充实。
