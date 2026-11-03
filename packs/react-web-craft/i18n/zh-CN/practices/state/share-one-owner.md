# 协调中的状态放在唯一的共同所有者

## 适用场景

一个组件编辑筛选条件，另一个组件显示或清除它时，两者需要读写同一个值。应选一个组件统一保存状态，让其他组件通过明确的方式使用它，不要分别存副本再同步。只有一个组件需要的值，则继续留在本地。

## 具体指导

没有其他组件需要共同读写时，状态留在当前组件。多个组件需要同一个值时，把它放到能协调它们的最近共同 React 父级，只保存一份。路径直接清楚时，用 props 传值和更新回调。

如果隔着许多无关层级，逐层传 props 已经造成明显负担，或者组件 API 本来就设计成通过共享 provider 使用，再考虑 Context 或 provider。Context 只是换了读取值的方式，不会让多个副本变得安全，也不会让 provider 的 state 自动变成全局状态。不要只为让邻近的兄弟组件使用一个值，就把状态提到应用根节点。

不要把值复制进每个使用它的组件，再用 Effect 同步副本，也不要通过 ref 访问另一个组件的内部状态。如果值由服务器、URL 或外部 store 管理，而不是这个 React 子树，就应另行选择对应的所有权模型；本篇只决定局部 UI 状态放在哪里。

## 反模式

搜索框持有 `query`，旁边的同级结果摘要也持有一份由 props 初始化的
`query`。一个 Effect 把每次按键都复制进摘要的状态。任何一侧变化时两个值都可能分叉，而这段额外同步为一个概念制造了第二个所有者。

## 原因

多个组件需要共享变化中的 UI 值时，在最近共同所有者中只保存一份，就能让它们读取同一个值，并通过同一条回调路径更新。状态提升得更高，变化时可能使更大范围的组件树参与渲染；在各组件中分别保存可编辑副本，则可能出现不一致，还需要额外同步。

## 例外与边界

- 只有一个组件读取并修改该值时，保持局部；「将来可能复用」不是加 provider 的理由。
- 父组件已经通过 `value` 与 `onChange`
  控制子组件时，父组件就是所有者；除非有意建立另一种本地覆盖契约，子组件不应再造第二份可编辑副本。
- 许多遥远的后代需要同一个值时，Context 可以减少 props 传递，但要慎重选择 provider 的作用范围。本篇不规定 compound-component
  API、状态管理库或服务器数据缓存。
- 两个值只是当前内容恰好相同、但代表不同所有权或生命周期时，它们并不必然是重复状态。

## 示例

评论撰写器持有选中的评分：子组件选择器修改它，同级摘要与提交控件读取它。子组件只接收同一个值和一条更新路径，谁都不再自留第二份评分状态。

```tsx
import { type FormEvent, useState } from "react";

type Rating = 1 | 2 | 3 | 4 | 5;
const ratings: Rating[] = [1, 2, 3, 4, 5];

type RatingPickerProps = {
  name: string;
  value: Rating | null;
  onChange: (rating: Rating) => void;
};

function RatingPicker({ name, value, onChange }: RatingPickerProps) {
  return (
    <fieldset>
      <legend>Your rating</legend>
      {ratings.map((rating) => (
        <label key={rating}>
          <input
            type="radio"
            name={name}
            value={rating}
            checked={value === rating}
            onChange={() => onChange(rating)}
          />
          {rating} star{rating === 1 ? "" : "s"}
        </label>
      ))}
    </fieldset>
  );
}

function RatingSummary({ rating }: { rating: Rating | null }) {
  return <p>{rating === null ? "Choose a rating" : `Selected: ${rating} stars`}</p>;
}

export function ReviewComposer({
  submitReview,
}: {
  submitReview: (rating: Rating) => void;
}) {
  const [rating, setRating] = useState<Rating | null>(null);

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (rating !== null) submitReview(rating);
  }

  return (
    <form onSubmit={handleSubmit}>
      <RatingPicker name="review-rating" value={rating} onChange={setRating} />
      <RatingSummary rating={rating} />
      <button type="submit" disabled={rating === null}>
        Send review
      </button>
    </form>
  );
}
```

如果选择器和摘要之后在树中相距很远，仍保持同一个状态所有者，并考虑限定作用范围的 Context。不要让每个子树分别保存自己的评分值。
