# 昂贵的挂载期状态用惰性初始化

## 适用场景

组件需要一份由稳定输入初始化的可编辑本地副本，而构造该初值需要可感知的解析、规范化、建索引或其他纯计算时应用。此时要判断：这份工作是否真的是挂载期初始化，还是状态应当跟随变化的输入。

## 具体指导

初始计算的成本高到值得关心时，给 `useState` 传初始化函数：

```tsx
const [rules, setRules] = useState(() => buildEditableRules(initialRules));
```

传入计算值（例如
`useState(buildEditableRules(initialRules))`）时，组件函数每次运行都会求值该表达式。React 会忽略已有状态之后的初值，但 JavaScript 已经为计算付出了成本。函数形式让 React 只在初始化该状态时调用初始化器，而不是每次普通渲染都调用。

保持初始化器纯函数：不得修改输入、执行 I/O、调度更新，也不得依赖「只被调用一次」。开发环境下 React
Strict
Mode 可能调用初始化器两次，以暴露不纯实现。廉价值（原始类型或小字面量）不要用函数形式；惰性初始化是成本边界，不是默认风格。

把初始化器的输入视为该组件状态生命周期的快照。新的 prop 值不会重跑初始化器。若编辑状态属于另一份文档或实体，就给编辑器一个稳定的身份边界（例如
`key`），或定义显式的状态转换/重置路径。若值必须始终反映当前 prop，就不要为了用惰性初始化而把它复制进本地状态；应改选受控或响应式覆盖契约。

## 反模式

规则编辑器把数百条表达式解析成 token 数组，作为参数直接传给
`useState`。勾选一个复选框触发重渲染，完整解析随之重复，而算出的数组被丢弃——组件早已持有状态。把表达式换成读存储、写缓存的不纯初始化器并不是安全修法：初始化必须保持纯函数并与渲染行为兼容。

## 原因

Hook 的参数表达式由 JavaScript 在每次组件调用时求值；React 只在首次使用初值，并不会让这个表达式变懒。传入函数把初始化计算与后续渲染分开，而显式的生命周期边界防止这项优化被误当成「跟随 props 变化的同步」。

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
