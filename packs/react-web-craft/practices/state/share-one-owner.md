---
anti_patterns:
  - description: Two components keep separate copies of a value that must stay in sync, and an Effect or ref is used to forward changes between them instead of choosing one owner.
    id: react.state.duplicate-coordinated-state
    name: Duplicated state synchronized across components
    severity: warn
applies_when: multiple React components must read or update the same changing UI value, and the current owner boundary would require duplicate state or cross-component synchronization
id: react.state.share-one-owner
severity: warn
stage: design
tech_stack:
  - react
title: Keep Coordinated State at One Shared Owner
---

## When to apply

If one component edits a filter while another displays or clears it, they need to read and update
the same value. Choose one component to own that state and a clear way for the others to use it,
rather than keeping copies synchronized. Leave the value local when only one component needs it.

## Guidance

Keep state inside one component when no other component needs to coordinate with it. When several
components must read or update the same value, move its single source of truth to the nearest common
React owner that can coordinate them. Pass the value and update callback through props when the path
is direct and understandable.

Use Context or a provider when passing props through many unrelated layers becomes a real cost, or
when the component API deliberately offers a shared provider. Context changes how components reach
the value; it does not make duplicate copies safe or turn provider state into global state. Do not
move state to the application root just so one nearby sibling can use it.

Do not copy the value into each consumer and synchronize those copies with Effects, and do not reach
into another component through a ref. If the value belongs to a server, URL, or external store
rather than this React subtree, select that ownership model separately instead of stretching this
local-state decision.

## Anti-pattern

A search box owns `query`, while a sibling result summary owns another `query` initialized from
props. An Effect copies every keystroke into the summary's state. The two values can diverge when
either side changes, and the extra synchronization creates a second owner for one concept.

## Why

When several components must share a changing UI value, storing it once in their nearest common
owner lets them read the same value and update it through one callback path. Moving it farther up
can cause more of the tree to render when it changes. Keeping editable copies in each consumer
instead creates values that can disagree and must be synchronized.

## Exceptions and boundaries

- If one component alone reads and changes the value, keep it local; anticipated future reuse is not
  a reason to add a provider.
- If a parent already controls a child through `value` and `onChange`, the parent is the owner; the
  child should not create a second editable copy unless a distinct local-override contract is
  intentional.
- If many distant descendants need one value, Context may reduce prop plumbing, but choose the
  provider's scope deliberately. This Practice does not prescribe compound-component APIs, a
  state-management library, or server-data caching.
- If two values merely happen to have the same current contents but represent different ownership or
  lifetimes, they are not necessarily duplicate state.

## Example

The review composer owns the selected rating because a child picker changes it while a sibling
summary and the submit control read it. The children receive one value and an update path; neither
keeps a second rating state.

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

If the picker and summary later move far apart in the tree, keep the same single owner and consider
a narrowly scoped Context. Do not let each subtree invent its own rating value.
