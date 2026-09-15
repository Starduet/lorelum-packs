# 用一个状态表达互斥的 UI 模式

## 适用场景

多个布尔值或可选字段共同描述同一个流程阶段时应用——例如一次保存可以处于空闲、进行中、已完成或失败。此时要判断：这些值是否真的可能并存，还是当前状态形状允许出现不可能的组合。

## 具体指导

同一时刻只会有一个模式生效时，用一个状态值表达它。在 TypeScript 中，判别联合（discriminated
union）可以只在特定变体上携带数据，例如把错误消息挂在 failed 变体上。转换时整体替换状态值，让下一个模式与它附带的数据一起变化。

可以同时为真、且所有者或生命周期不同的独立事实保持独立。不要为了减少状态变量个数就合并不相关的开关；也不要用本篇判断「一个值能否从其他状态推导」。

## 反模式

label manager 把 `isCreating` 与 `editingLabelId`
存成两个独立 state。没有任何机制阻止两者同时生效，于是界面可以同时打开新建 label 编辑器和重命名编辑器——而产品只允许存在一个 label 编辑器。

## 原因

独立旗标能编码所有组合，包括产品不允许的组合。一个带标签的模式可以让「关闭」「新建」「正在重命名这个 label」互斥，同时只在 rename 模式上携带 ID。

## 例外与边界

- 可以并存的事实保持独立状态，例如「启用邮件提醒」与「启用短信提醒」：它们是独立选择，不是互斥阶段。
- 本篇只关心一个状态概念的形状；不要求 `useReducer`、状态机库或某种特定的转换架构。
- 不涉及冗余的渲染期推导值、props 同步、请求去重或并发操作竞态。
- 流程包含复杂转换或副作用时单独建模；联合类型让合法状态显式化，但本身并不强制每条转换规则。

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
