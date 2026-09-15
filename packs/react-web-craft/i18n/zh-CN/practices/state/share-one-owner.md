# 协调中的状态放在唯一的共同所有者

## 适用场景

两个或更多组件必须依据同一个变化中的 UI 值做决定时应用——例如一个组件编辑筛选条件，另一个组件展示或清除它。此时要判断：该值能否保持局部、是否需要一个共同所有者、消费者经由什么路径访问它。

## 具体指导

没有其他组件需要协调时，状态留在单个组件内部。当多个组件必须读写同一个值时，把它的唯一权威来源移到能够协调这些组件的最近共同 React 所有者上。路径直接且清晰时，通过 props 传值和更新回调。

只有当消费者之间隔着足够多无关层级、逐层透传 props 成为真实成本，或组件契约有意暴露共享 provider 边界时，才使用 Context 或 provider。Context 改变的是值的到达方式；它不会让重复副本变得安全，也不会让 provider 的状态变成全局。不要为了让某个值对一个邻近兄弟可用就把状态挪到应用根节点。

不要把值复制进每个消费者再用 Effect 同步副本，也不要通过 ref 伸进另一个组件。如果该值本属于服务器、URL 或外部 store 而非这个 React 子树，应另行选择那种所有权模型，而不是拉伸这个局部状态决策。

## 反模式

搜索框持有 `query`，旁边的同级结果摘要也持有一份由 props 初始化的
`query`。一个 Effect 把每次按键都复制进摘要的状态。任何一侧变化时两个值都可能分叉，而这段额外同步为一个概念制造了第二个所有者。

## 原因

一个可变的 UI 概念只需要一个权威。把权威放在组件们共享的最低层所有者上，它们就能观察到同一次渲染的值，并通过显式路径发送更新。提升得比必要更远会扩大「谁必须因此重渲染」的范围；复制该值则会制造需要同步的竞争版本。

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

如果选择器和摘要之后在树中相距很远，仍保持同一个唯一所有者，并考虑一个范围收窄的 Context。不要让每个子树自己发明一份评分值。
