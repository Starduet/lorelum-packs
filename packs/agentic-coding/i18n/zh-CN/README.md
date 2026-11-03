# `agentic-coding` 简体中文阅读版

这里是未发布工作树 `agentic-coding@0.8.0` 的 39 条 Practice 中文阅读版。本次新增工程结论汇报与具体表达两条；已发布的 `0.7.0` 仍是原有 37 条，不可变发布内容没有改写。中文内容不参与安装、检索或运行时注入。ID、元数据、反模式 ID 和运行时行为仍以 [`../../practices`](../../practices/) 中的英文 canonical 文件为唯一真源；中英文有冲突时，以英文为准。

## Pack 简介

面向 AI Agent 的软件工程决策指导：澄清目标、权威来源、验收与非目标；控制范围与停止条件；让决策集合（计划、验收标准、检查单、规范）不膨胀到超出它要做的决定；在后端和本地服务新增校验、权限、完整性扫描或启动与恢复前置条件之前，权衡额外保护及其自身成本；在不削弱安全、一致性和契约的前提下保持必需路径可完成；提交前做减法评审；以可信证据处理交接、委托代理、交付、恢复与上下文重建。

每个文件与 canonical 保持同一相对路径，仅含中文标题和六个正文章节，不含 runtime frontmatter。同步 digest 由 Lorelum 根据格式化后的英文 Markdown 生成，不应手工修改。

本次修订：全部 Guidance 改写为带停止点的步骤式决策程序；`applies_when` 按检索评测的混淆矩阵改写以区分近邻 Practice；示例补强为冷读者可复述的自包含场景；severity 分为三档（critical=证据与交付诚实，warn=范围与规划，info=惯例）。原"只承诺有理由的工作"与"开工前写停止条件"两条同属开工前范围决策，合并为一条。

`agentic-coding-v0.5.0` 已作为不可变 ref 通过官方 Registry 发布。2026 年 9 月 21 日已用官方安装路径解析该 ref、完成 Pack 解码并读回 34 条 Practice；这只证明安装与物化链路，不证明检索效果或下游 Agent 行为。`agentic-coding-v0.5.1` 为仅元数据发布：目录描述改写以点名 0.5.0 新增的两条规划校准 Practice 的触发时刻，Practice 内容不变；2026 年 9 月 21 日已用官方安装路径解析该 ref（`954324c`）、完成解码并回读 34 条 Practice ID。

## 未发布 0.8.0：向开发者讲清工程结论

- [先把工程结论告诉开发者](practices/delivery/lead-with-engineering-conclusion.md)：先说排查结论、方案建议、实现结果或实际进度，把决定下一步的重要限制放在旁边，再给理由和证据。
- [用具体动作讲清工程工作](practices/delivery/explain-engineering-work-plainly.md)：说出组件做了什么、为什么有用，不用“机制落地”“生命周期闭环”等标签代替解释；保留准确术语、原文和不确定性。

领域仅限软件工程协作，不是生活问答。已有的完成声明与遗留问题规则仍分别决定“可以声称什么”和“哪些问题必须报告”，这两条不替代它们，也不强制每次回复套模板。

先看[中文工程改写对照](../../references/engineering-communication.md)，包括并发刷新、索引取舍、未确认的超时原因和一句话范围答复。示例事实均为构造；[效果记录](../../../../fixtures/agentic-coding/baselines/engineering-communication-2026-11-02.md)另列实际生成的回答及限制。这次不做 #41 的全库改写或简介结构迁移。

当前内容只可按本地路径安装到隔离 Store 后读取，未新增 Registry 或 tag；下文的官方安装命令仍对应已发布 `0.7.0`。

## 0.7.0：把工作经验落到具体判断

本版新增两条，而不是改写已有不可变发布产物：

- [当历史上下文价值降低时建议换新对话](practices/context/recommend-session-handoff.md)：不必等到错误发生才处理历史干扰；保留会改变接续行为的最小完整条款、决策状态和可用来源。当前折中方法在两个开发样本保住此前追踪的边界，比大附录版缩短约 30%/36%。此前目录提示的两个正例观察到自行检索正文并提供可用交接，两个阴例没有无谓迁移；触发证据属于当时的正文快照，不自动迁移为当前版本的稳定触发证明。
- [围绕能成立的解法组织工作](practices/planning/organize-work-around-the-solution.md)：目标已知后，Agent 应承担选择并推进实际办法的判断，避免用保护机制、任务控制或内部指标替代解题。经验包括 TPM 估算漏掉正常内容、提前限制设计者发挥、用内部分类代替整体效果判断；正文不固定为这些案例的流水线，也不要求额外自查工件。

[内容采用记录](../../../../fixtures/agentic-coding/baselines/agentic-coding-0.7.0-content-2026-10-30.md)区分维护者经验、作者综合和实际验证。有限实现与报告探针可用，但未测出优于对照指导或公开 Skill 的效果。不宣称市场范围的新颖性、模型更新后的频率增长、无损交接、稳定自动触发或普遍领先。

新安装执行 `lore pack install agentic-coding@0.7.0`，已有安装执行 `lore pack update agentic-coding`，Registry 默认选择最新稳定版本。
[0.7.0 正式发布验证](../../../../fixtures/agentic-coding/baselines/agentic-coding-0.7.0-release-2026-10-30.md)记录官方 Registry 精确安装、从 `0.6.0` 的默认更新、37 条 ID 回读和两条新正文一致性；首次下载失败也保留记录。分发成功不证明稳定触发或下游效果改善。

## 校验与恢复决策

**在决定新增或加强检查之前**，先读
[新增检查前先说明理由](practices/implementation/justify-added-checks.md)
（`agentic-coding.implementation.justify-added-checks`）完整正文。
它覆盖规划时刻，也覆盖 Agent 在普通任务中自行提出校验、前置检查、授权或确认、
完整性扫描、启动/恢复阻断条件的时刻。不要等实现完成后才做删减评审。

区分三个问题：

- **为什么值得新增或加强？** `justify-added-checks` 先确定可达失败或强制契约、
  保障负责人、已有覆盖及新增保护，再权衡检查自身的误拒绝、延迟、I/O、可用性、
  维护和恢复成本，决定保留、新增、收窄或不加。
- **应该在哪里检查？**
  [在真正负责该事实的边界校验](practices/implementation/validate-at-the-owning-boundary.md)
  （`agentic-coding.implementation.validate-at-the-owning-boundary`）判断检查归属、
  既有事实何时会失效，以及内部交接是否引入新的失败。
- **组合后的路径还能完成吗？**
  [保持验收路径可完成](practices/planning/keep-acceptance-path-completable.md)
  （`agentic-coding.planning.keep-acceptance-path-completable`）把检查组合起来，
  走过正常使用、启动、维护和恢复路径，选择阻断级别，保留可达的修复/停止路径；
  不能要求先处于恢复本来要重建的健康状态。

[让恢复有明确负责人和可理解的结果](practices/implementation/make-recovery-behavior-explicit.md)
用于准备给失败增加重试、空默认值、备用来源或降级结果的时刻：明确可恢复条件、有限的负责人和
调用方能理解的结果。校验负责建立事实，恢复负责应对失败，两者也可能独立发生。

这些是通用决策，不是要求少检查。外部输入边界、授权、并发状态一致性、native/model 质量、
发布完整性与恢复身份保障仍须保留。必要保护可以支持高成本检查。
不要求新增检查单、强制风险报告或独立审批门禁。

整体工程投入由 `scale-work-to-risk-and-cost` 负责，选择验证观察由 `plan-sufficient-evidence`
负责，都不替代新增检查之前的独立判断。`0.6.0` 新增一个独立 ID，并调整两个近邻的职责；
不改写旧版本内容和不可变发布历史。

## 项目路由建议

Pack description 与 `applies_when` 能帮助发现后的选择，不能让 Agent 自动查询 Lorelum；
独立 Practice ID 也不保证 Agent 会识别触发时机。项目可把下面的指令采纳进自己的 `AGENTS.md`，
或放进宿主配置为在这个决策点强制读取的 skill：

> 在决定新增或加强检查之前，包括在普通任务中自行提案时，读取
> `agentic-coding.implementation.justify-added-checks` 完整正文。
> 实现之前先决定为什么需要它，完工后的删减评审不能替代这个判断。
> 涉及检查归属、事实失效或内部交接时，再读取
> `agentic-coding.implementation.validate-at-the-owning-boundary`。
> 如果检查可能阻断正常使用、启动、维护、修复或停止，再读取
> `agentic-coding.planning.keep-acceptance-path-completable`，然后才选择前置条件。
> 当前会话已有适用的当前正文时可以复用；否则用已知完整 ID 执行 `lore get`。
> query 或 summary 命中不等于拿到正文。检索为空不代表没有规则：直接 get 已知 ID，
> 或查可用 catalog 确认 ID。同一决策和正文仍适用时，不必每写一个 helper 或每次调用工具都重查。
> 取不到正文就如实说明限制，不要声称已经读过。

例如，安装 `0.6.0` 或当前活动 Pack 层提供该版本内容时，
`lore get agentic-coding.implementation.justify-added-checks` 可以直接读取已知入口，不依赖检索命中。
旧 `0.5.1` 不含这个 ID，应更新到 `0.6.0`，或用文件读取工具读取上方链接的工作树正文；无法取得时如实说明。
这个路由面向检查决策，不要求每次工具调用都查询，也不引入新的全局审批门禁。

这只是本 Pack 文档中的采纳建议，尚未部署到 Lorelum 产品仓库、其 `AGENTS.md`、插件或 skill。
官方 [Lorelum `0.1.0-alpha.6` 预发布](https://github.com/lorelum/lorelum/releases/tag/v0.1.0-alpha.6)
包含 omp 插件和 skill；它们的存在不证明这个路由会触发。此建议的 Windows 真实 host 流尚未测试。

须分别记录三类证据：**召回**记录 query 选中了哪些 ID；**正文提供**记录 get 成功把相关完整正文交给 Agent
（或当前正文已在会话中）；**决策影响**需要 Agent 实际如何据此决策的证据。前一项不证明后一项。
现有 `scripts/eval-decisions` 先 query、get，再强制把正文放进 injected prompt，只能测正文辅助后的决策，
不能测 Agent 是否自主识别触发时机并查规则。Fixture 预期是假设，不是召回成功、行为有效或路由已部署的证据。

[10 月 22 日 alpha.6 两条 Practice 方案评估](../../../../fixtures/agentic-coding/baselines/agentic-coding-backend-checks-alpha6-2026-10-22.md)
保留为**此前仅补强两个近邻的历史比较**，不是新增独立入口的评估结果。它记录了有限的
keyword 改善及旧查询退化、语义准备失败、正文成功提供，但未观察到决策改善。
这些观察既不证明稳定自动查询，也不能继承为新 35 条候选方案成功的证据。

[独立入口 alpha.6 评估](../../../../fixtures/agentic-coding/baselines/agentic-coding-independent-check-alpha6-2026-10-22.md)
另行记录了新方案的排名，以及仅提供目录与明确路由的受控会话。两个会话均在设计决定前读取新正文，
并保留必要保障；但每组只有一个会话、没有无知识盲测对照、也未部署真实宿主，不证明稳定触发或因果性决策改善。

## 导航（39 条）

### 需求（3）

- [先说清用户真正要得到什么](practices/requirements/ground-user-goal.md)
- [同时写清完成条件和不做什么](practices/requirements/define-acceptance-and-non-goals.md)
- [多份要求冲突时先确认听谁的](practices/requirements/resolve-source-authority.md)

### 规划（7）

- [开工前定下范围和停止条件](practices/planning/decide-scope-and-stop-conditions.md)
- [从关切推导承诺集，不从条目堆叠](practices/planning/derive-committed-set-from-concerns.md)
- [保持验收路径可完成](practices/planning/keep-acceptance-path-completable.md)
- [按用户完成的整条能力来检查计划](practices/planning/map-plan-to-user-capability.md)
- [为每项验收要求安排够用的最小证明](practices/planning/plan-sufficient-evidence.md)
- [按失败代价决定投入多少工程工作](practices/planning/scale-work-to-risk-and-cost.md)
- [围绕能成立的解法组织工作](practices/planning/organize-work-around-the-solution.md)

### 实现（10）

- [在能完整工作的方案里选最不复杂的](practices/implementation/choose-smallest-sufficient-design.md)
- [暴露新能力前确认用户能依赖什么](practices/implementation/confirm-product-surface-expansion.md)
- [新写代码前先查仓库里有没有](practices/implementation/inspect-and-reuse-existing-capability.md)
- [新增检查前先说明理由](practices/implementation/justify-added-checks.md)
- [没有未决判断，就不要扩大调查范围](practices/implementation/limit-investigation-to-current-decision.md)
- [让负责数据或规则的组件统一作决定](practices/implementation/preserve-responsibility-boundaries.md)
- [在真正负责该事实的边界校验](practices/implementation/validate-at-the-owning-boundary.md)
- [让恢复有明确负责人和可理解的结果](practices/implementation/make-recovery-behavior-explicit.md)
- [新事实改变任务时暂停并重做计划](practices/implementation/replan-on-material-drift.md)
- [把安全且临时的假设明确写出来](practices/implementation/surface-unconfirmed-assumptions.md)

### 测试（4）

- [每个测试都要说明自己保护哪项契约](practices/testing/anchor-tests-to-requirements.md)
- [断言用户或调用方真正能依赖的结果](practices/testing/assert-observable-behavior.md)
- [检查失败后先判断谁错了，再改代码或测试](practices/testing/classify-failure-before-changing-test.md)
- [永久回归保护必须有长期理由](practices/testing/justify-regression-protection.md)

### 验证（3）

- [旧的验证结果只用于它仍覆盖的文件和环境](practices/verification/bind-evidence-to-artifact-state.md)
- [发现缺少验证后：补测、缩小目标或明确未完成](practices/verification/close-or-declare-evidence-gaps.md)
- [把每项验收要求对应到实际检查结果](practices/verification/map-evidence-to-acceptance.md)

### 审查（2）

- [提交前删掉没有必要的改动](practices/review/run-subtractive-review-before-commit.md)
- [按审查意见改代码前先确认它成立](practices/review/validate-findings-before-action.md)

### 交付与工程汇报（4）

- [完成声明只说证据证明的部分](practices/delivery/claim-only-supported-outcome.md)
- [只报告会改变接收方决策的剩余问题](practices/delivery/report-material-residuals.md)
- [先把工程结论告诉开发者](practices/delivery/lead-with-engineering-conclusion.md)
- [用具体动作讲清工程工作](practices/delivery/explain-engineering-work-plainly.md)

### 纠正（1）

- [确认纠正后把工作复位到权威基线](practices/correction/restore-authoritative-baseline.md)

### 上下文与委派（5）

- [委派前给被委派的 Agent 足够的决策上下文](practices/context/give-delegated-agents-decision-context.md)
- [当历史上下文价值降低时建议换新对话](practices/context/recommend-session-handoff.md)
- [上下文丢失后先重新落地](practices/context/reground-after-context-loss.md)
- [继续之前先验证交接内容](practices/context/validate-handoff-before-continuation.md)
- [写下能保住决策的检查点](practices/context/write-decision-dense-checkpoint.md)
