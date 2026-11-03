# 用一个状态表达互斥的 UI 模式

## 适用场景

一次保存可以是空闲、进行中、已完成或失败，但不能同时处于这些阶段。如果多个布尔值或可选字段允许互相矛盾的组合，就先确认 UI 实际支持哪些情况，把互斥阶段合并成一个状态。

## 具体指导

同一时刻只会有一个模式生效时，用一个状态值表达它。在 TypeScript 中，判别联合（discriminated
union）可以只在特定变体上携带数据，例如把错误消息挂在 failed 变体上。转换时整体替换状态值，让下一个模式与它附带的数据一起变化。

确实可以同时成立、且由不同地方管理或有不同生命周期的值，应继续分开保存。不要只为减少 state 变量就合并无关开关。某个值能否由其他状态计算出来，是另一个问题。

## 反模式

label manager 把 `isCreating` 与 `editingLabelId`
存成两个独立 state。没有任何机制阻止两者同时生效，于是界面可以同时打开新建 label 编辑器和重命名编辑器——而产品只允许存在一个 label 编辑器。

## 原因

独立旗标能编码所有组合，包括产品不允许的组合。一个带标签的模式可以让「关闭」「新建」「正在重命名这个 label」互斥，同时只在 rename 模式上携带 ID。

## 例外与边界

- 可以并存的事实保持独立状态，例如「启用邮件提醒」与「启用短信提醒」：它们是独立选择，不是互斥阶段。
- 这里只决定怎样表达一组互斥状态，不要求使用 `useReducer`、状态机库或特定的状态转换架构。
- 冗余的渲染期推导值、props 同步、请求去重和并发竞态，仍要分别处理。
- 如果流程包含复杂的状态转换或副作用，应另行建模；联合类型能限定合法状态，但不会自动保证所有转换都合法。

## 示例

label
manager 要么新建 label，要么重命名一个既有 label，绝不同时打开两个编辑器。一个带标签的状态保存当前模式与该模式所需的数据。

```tsx
import { useState } from "react";

type Label = { id: string; name: string };
type EditorState =
  | { kind: "closed" }
  | { kind: "create"; name: string }
  | { kind: "rename"; id: string; name: string };

type LabelManagerProps = {
  labels: Label[];
  createLabel: (name: string) => void;
  renameLabel: (id: string, name: string) => void;
};

export function LabelManager({
  labels,
  createLabel,
  renameLabel,
}: LabelManagerProps) {
  const [editor, setEditor] = useState<EditorState>({ kind: "closed" });

  function updateName(name: string) {
    setEditor((current) =>
      current.kind === "closed" ? current : { ...current, name },
    );
  }

  function saveEditor() {
    if (editor.kind === "create") createLabel(editor.name);
    if (editor.kind === "rename") renameLabel(editor.id, editor.name);
    setEditor({ kind: "closed" });
  }

  return (
    <section>
      <button
        type="button"
        onClick={() => setEditor({ kind: "create", name: "" })}
      >
        New label
      </button>
      <ul>
        {labels.map((label) => (
          <li key={label.id}>
            {label.name}{" "}
            <button
              type="button"
              onClick={() =>
                setEditor({ kind: "rename", id: label.id, name: label.name })
              }
            >
              Rename {label.name}
            </button>
          </li>
        ))}
      </ul>
      {editor.kind !== "closed" && (
        <fieldset>
          <legend>{editor.kind === "create" ? "New label" : "Rename label"}</legend>
          <label>
            Name
            <input
              value={editor.name}
              onChange={(event) => updateName(event.currentTarget.value)}
            />
          </label>
          <button type="button" onClick={saveEditor}>
            Save
          </button>
          <button
            type="button"
            onClick={() => setEditor({ kind: "closed" })}
          >
            Cancel
          </button>
        </fieldset>
      )}
    </section>
  );
}
```

`editor.kind` 为 `closed` 时没有 name 或 label ID；`create` 模式有草稿名但没有 ID；`rename`
模式携带将要更新的 ID。如果新建与重命名允许同时进行，它们就是独立模式，不应这样合并。
