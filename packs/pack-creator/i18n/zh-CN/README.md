# `pack-creator` 简体中文审阅版

这里是 `pack-creator@0.2.0` 27 条 canonical Practice 的中文 companion，供中文读者审查这套 Pack 的写作判断是否清楚、具体且适用于不同领域。`0.2.0` 仍是未发布候选；当前已发布版本仍为 `0.1.0`。它不是另一套运行时 Pack，也不会参与召回。

[`../../practices`](../../practices/) 中的英文 canonical 文件是运行时权威：Practice ID、anti-pattern ID、trigger、动作、例外和发布含义都由英文文件控制。中文文件通过相同相对路径与 canonical 对应，不复制 runtime frontmatter。若中英文意义冲突，应先修正 canonical，再重新同步译文，不能只在中文中另写规则。

## 导航（27 条）

### 发现（4）

- [先定义这套 Pack 要改善哪些判断](practices/discovery/define-pack-decision-outcome.md)
- [选择项目目录层还是 Registry 发布版](practices/discovery/choose-project-local-or-registry-release.md)
- [每条重要规则都要有可追溯的依据](practices/discovery/ground-content-in-sources-and-observed-needs.md)
- [找出整套 Pack 应该在什么时候提供帮助](practices/discovery/identify-retrieval-moments.md)

### 设计（4）

- [一条 Practice 只处理一个可独立出现的决定](practices/design/decompose-one-decision-per-practice.md)
- [把父子项目层组成增量覆盖](practices/design/compose-inherited-project-layers.md)
- [让每条 Practice 脱离相邻文件也能直接使用](practices/design/keep-each-practice-standalone.md)
- [把会竞争同一查询的相邻 Practice 区分开](practices/design/separate-neighboring-triggers.md)

### 写作（11）

- [原因要写动作直接造成的结果](practices/authoring/explain-the-direct-causal-reason.md)
- [按读者下一步动作选择 reference、asset 或 script](practices/authoring/choose-reference-asset-or-script.md)
- [创建项目局部 Pack](practices/authoring/create-a-project-local-pack.md)
- [让反模式和示例各自提供不同信息](practices/authoring/give-anti-pattern-and-example-distinct-jobs.md)
- [单个示例本身要交代清楚决定所需事实](practices/authoring/make-examples-self-contained.md)
- [从 Practice 中明确引导补充资源](practices/authoring/link-pack-resources-from-the-practice.md)
- [用普通词直接说清人、东西和动作](practices/authoring/prefer-plain-language-and-concrete-referents.md)
- [反模式要写能力正常的人也可能犯的错](practices/authoring/use-realistic-failure-mechanisms.md)
- [指导要给出具体动作和明确停止点](practices/authoring/write-concrete-guidance-and-stop-condition.md)
- [`applies_when` 要能选中这一条，而不是整个主题](practices/authoring/write-discriminating-applies-when.md)
- [例外要写成读者能识别的具体条件](practices/authoring/write-specific-exceptions-and-boundaries.md)

### 评估（4）

- [不同检查结果只能证明各自观察到的事情](practices/evaluation/separate-structural-and-semantic-evidence.md)
- [在真实项目语境中验证局部 Pack](practices/evaluation/verify-project-local-pack-activation.md)
- [用应该匹配和不该匹配的查询一起测试召回](practices/evaluation/test-retrieval-with-contrasting-queries.md)
- [把资源完整性作为独立证据链验证](practices/evaluation/verify-resource-integrity-without-overclaiming.md)

### 本地化（1）

- [本地化要便于人工审阅，但不能产生第二套运行时含义](practices/localization/localize-for-human-review-without-forking-runtime.md)

### 发布（2）

- [内容变化要发布为可追溯的新版本](practices/release/preserve-versioned-content-and-provenance.md)
- [声称发布前先走通用户真正使用的安装路径](practices/release/verify-the-supported-install-path-before-claiming-release.md)

### 审查（1）

- [删除不能改变决定的内容](practices/review/run-subtractive-content-review.md)
