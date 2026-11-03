# 昂贵的挂载期状态用惰性初始化

## 适用场景

编辑器可能要先解析、规范化或索引一份稳定输入，才能生成可编辑的初始状态。如果这项纯计算开销明显，就应避免在普通重渲染时重复执行。先确认需要的确实是挂载时的快照，而不是应该随输入变化的值。

## 具体指导

初始计算的成本高到值得关心时，给 `useState` 传初始化函数：

```tsx
const [rules, setRules] = useState(() => buildEditableRules(initialRules));
```

直接传入计算结果，例如
`useState(buildEditableRules(initialRules))`，会让组件函数每次运行时都先计算这个表达式。已有状态初始化后，React 不再使用这些新算出的初值，但计算仍然发生了。传入函数后，React 可以只在初始化状态时调用它，不必在每次普通渲染中重复计算。

初始化函数必须是纯函数：不能修改输入、执行 I/O、安排状态更新，也不能依赖「只调用一次」。开发环境下，React
Strict
Mode 可能调用两次，以帮助发现不纯的实现。原始类型值或小字面量等开销很小的初值，直接传值即可，不必默认都写成函数。

初始化函数只负责创建这个组件实例的初始状态，不会因 prop 更新而重跑。编辑器切换到另一份文档或实体时，用稳定身份（如
`key`）创建新实例，或明确定义状态转换和重置方式。如果值必须跟随当前 prop，就不要为了惰性初始化而复制到本地 state；按需要使用受控值，或在用户主动覆盖前持续跟随来源值。

## 反模式

规则编辑器把数百条表达式解析成 token 数组，作为参数直接传给
`useState`。勾选一个复选框触发重渲染，完整解析随之重复，而算出的数组被丢弃——组件早已持有状态。把表达式换成读存储、写缓存的不纯初始化器并不是安全修法：初始化必须保持纯函数并与渲染行为兼容。

## 原因

JavaScript 会在每次组件调用时计算 Hook 的参数表达式。React 只在初始化时使用结果，并不代表表达式只计算一次。传入函数，才能把初始化计算与后续渲染分开。还要明确状态何时重建，避免误以为这项优化会让本地状态跟随 props 更新。

## 例外与边界

- 构造成本低时，用更简单的直接初值。
- 派生值应随输入变化而变化时，从当前输入计算或另行做记忆化决策；惰性状态初始化有意不追踪这些变化。
- 用户编辑的是输入的快照时，身份变化如何替换快照要单独决策；不要仅因 props 变了就用 Effect 重置。
- 初始化器必须纯函数。生成随机标识符、读浏览器专属存储、发请求或其他副作用都放在初始化器之外，通过事件、数据加载或组件生命周期路径把结果传入。

## 示例

规则编辑器把所选文档的规则表达式转换为可编辑的 token 列表。文档 key 定义了新编辑器状态生命周期的起点；初始化器在每次挂载时对所选文档规范化一次，后续复选框更新复用这份状态。

```tsx
import { useState } from "react";

type RuleSource = {
  id: string;
  expression: string;
  enabled: boolean;
};

type EditableRule = RuleSource & { tokens: string[] };

type RuleDocument = {
  id: string;
  rules: readonly RuleSource[];
};

function tokenize(expression: string): string[] {
  return expression.match(/\b(?:and|or|not)\b|[A-Za-z_]\w*|\d+(?:\.\d+)?|==|!=|<=|>=|[()<>!]/gi) ?? [];
}

function buildEditableRules(source: readonly RuleSource[]): EditableRule[] {
  return source.map((rule) => ({
    ...rule,
    tokens: tokenize(rule.expression),
  }));
}

export function DocumentRuleEditor({ document }: { document: RuleDocument }) {
  return <RuleEditor key={document.id} initialRules={document.rules} />;
}

function RuleEditor({ initialRules }: { initialRules: readonly RuleSource[] }) {
  const [rules, setRules] = useState(() => buildEditableRules(initialRules));

  function toggleRule(id: string) {
    setRules((current) =>
      current.map((rule) =>
        rule.id === id ? { ...rule, enabled: !rule.enabled } : rule,
      ),
    );
  }

  return (
    <ul>
      {rules.map((rule) => (
        <li key={rule.id}>
          <label>
            <input
              type="checkbox"
              checked={rule.enabled}
              onChange={() => toggleRule(rule.id)}
            />
            {rule.tokens.join(" ")}
          </label>
        </li>
      ))}
    </ul>
  );
}
```

有了
`key`，切换到不同文档会创建新的编辑器实例；普通重渲染或同一文档的 prop 刷新不会重建本地可编辑状态。若同身份的规则更新需要合并进编辑器，就显式定义那条状态转换，而不是期待初始化器重跑。

## 延伸阅读

- [React `useState`](https://react.dev/reference/react/useState) — 初值、初始化函数与 Strict
  Mode 纯度检查。
- [Preserving and Resetting State](https://react.dev/learn/preserving-and-resetting-state)
  — 组件身份与 key 如何界定状态生命周期。
