---
anti_patterns:
  - description: A list fan-out awaits every first-level item before starting any second-level follow-up, so the slowest item delays the follow-up of every other item.
    id: react.async.two-stage-list-waterfall
    name: Two-stage batches for nested list data
    severity: warn
applies_when: a fan-out over a list needs a per-item follow-up request that depends on its own item's result
id: react.async.chain-nested-item-fetches
severity: warn
stage: implementation
tech_stack:
  - react
title: Chain Each Item's Follow-Up Fetch Inside Its Own Promise
---

## When to apply

When each list item needs a follow-up request based on its own result, that follow-up can start as
soon as the item is ready. This applies to loading a detail record, enrichment, or sub-resource
without waiting for the rest of the list's first requests to finish.

## Guidance

For each identifier, create one promise that loads the item and then starts its follow-up request.
Await those per-item promises together:

```ts
const board = await Promise.all(
  shipmentIds.map((id) =>
    getShipment(id).then((shipment) =>
      getTrackingSnapshot(shipment.carrier, shipment.trackingNumber),
    ),
  ),
);
```

Each item's follow-up starts when that item's first request resolves. Awaiting all items before
starting any follow-up makes every follow-up wait for the slowest first request, even when its own
input is already available.

Handle failure per item when the page tolerates partial data. Under a bare `Promise.all`, one
rejected item discards the whole board; catching inside the per-item chain and returning a typed
failure entry keeps the other rows. Reserve the uncaught form for callers that genuinely want
all-or-nothing.

When the second stage needs all first-stage results — an aggregate, a cross-item deduplication, a
sort over the complete set — it is a real barrier: sequence the stages. Chaining applies only when
the follow-up depends on its own item alone. For very large lists, combine chaining with a
concurrency cap rather than starting every chain at once.

## Anti-pattern

A logistics board awaits all shipments, then awaits all tracking snapshots. One slow carrier
endpoint holds every row's snapshot even though the other shipments' carriers answered in
milliseconds, because no follow-up may start until the entire first batch has settled.

## Why

Per-item chaining lets each follow-up wait only for its own item's first request, not the slowest
first request in the list. The data dependencies are unchanged; each dependent request can simply
start earlier.

## Exceptions and boundaries

- Aggregate second stages are genuine barriers and stay sequential; this Practice does not split a
  computation that genuinely needs the complete first batch.
- If follow-ups do not depend on item results, there is no nesting; the work is plain parallel
  fetching covered by `react.async.parallel-independent-work`.
- For small lists where both stages are fast, the restructure is not worth the ceremony; this is a
  cost boundary, not a style rule.
- A client-side data layer with per-query caching and deduplication may remove the per-item
  follow-ups entirely; this Practice covers the direct server-side fan-out.

## Example

A shipments board adds each carrier's tracking snapshot to its row. A per-item helper loads the
shipment and then its snapshot, catching snapshot failures so that those rows can still appear. The
board awaits one promise per row. The declared helpers stand in for the data layer.

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

Each snapshot request starts when its own shipment resolves. A slow carrier delays only its own
snapshot request, and a failed snapshot leaves that row with an error; a failed shipment request
still rejects the board's `Promise.all`. Awaiting all shipments before starting snapshots would make
the slowest shipment delay every snapshot request.
