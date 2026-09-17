# 在真实项目语境中验证局部 Pack

## 适用场景

局部 Pack 或嵌套 overlay 已经结构有效，且准备声明它可供仓库使用之前采用。这里验证开发者实际工作的目录是否解析出预期的 current
winner；它不证明 semantic 排名质量或 Registry 可安装性。

## 具体指导

先对 Pack root 运行 `lore format` 与
`lore validate`；这证明 source 结构和严格诊断。再从真实 parent 或 child 工作目录运行
`lore context status`，确认预期 layer 状态和 warning。执行自然语言 keyword query，再执行
`lore get <practice-id>`，这样无需模型，也能证明 current context 返回预期的 canonical Practice。

对于 child overlay，测试一条必须选择 child 的同 ID Practice，以及一条必须继续可用的 parent-only
Practice。若 Store fallback 属于合同，再用 `--no-project`
重复一个聚焦检查，证明它有意选择 Store-only，而不是静默混合来源。完成前检查仓库：`.lorelum/`
应只含作者写的 config 和 Pack
source，不应含派生 cache、vector、model 或 operation 文件。每个结论都应单独命名：Pack 结构已通过、目标目录激活了预期 winner、未实际执行的 retrieval/model 行为仍不作声明时停止。

## 反模式

monorepo 根 Pack 有一条发布 Practice，`services/payments/` 覆盖同一个 ID。作者只在 child
Pack 路径上执行 `lore validate`，又恰好在旧 index ready 时运行一次 semantic
query，就在发布说明中宣称 override 生效。他没有从服务目录检查、没有读取 parent-only
Practice，也没发现复制的 cache 文件在 index 追赶时遮住了新 source。正确检查应从 `services/payments/`
执行 context status、keyword query 和 get，同时验证 child winner 与继承的 parent neighbor。

## 原因

validation 证明 Pack 结构；ProjectContext 是否激活取决于工作目录、layer fold、winner
precedence 和当前 source bytes。把这些观察分开，才能发现单独有效的 Pack 目录不会暴露的问题。

## 例外与边界

自动化 fixture 需要从另一个工作目录目标测试时使用 `--project-root`；它必须指向直接包含 `.lorelum`
的目录。keyword/context 检查之后可再加 semantic smoke，但缺模型和未完成 index 是 lifecycle
state，不是 source loading 失败的证据。Store fallback 不在局部 Pack 合同时，不必强制使用
`--no-project`。

## 示例

仓库 root 提供 `platform.logging`，`services/billing/`
提供更严格的同 ID 日志 Practice 和一条 billing-only Practice。维护者先验证两个 Pack root，再从
`services/billing/` 运行 `lore context status`、keyword query 和
`lore get platform.logging`。返回的是 billing
winner；查询 root-only 发布 Practice 仍能找到继承来源。单独的 `--no-project`
检查只返回选中的 Store 基线。报告记录 context activation 已通过，但不声称跑过 semantic benchmark。
