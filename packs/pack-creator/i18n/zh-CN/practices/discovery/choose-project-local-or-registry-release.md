# 选择项目目录层还是 Registry 发布版

## 适用场景

团队希望某些 Practice 能被多人使用，但尚不清楚它们是只属于一个代码目录，还是应当独立安装和发布时使用。这里决定分发边界；局部文件如何创建、父子目录怎样覆盖是后续决定。

## 具体指导

当指导的权威、术语、源文件或审查边界属于一个源码树，并应随该树一起变化时，使用项目局部 Pack。把它放在希望开始生效的目录的
`.lorelum/packs/<pack-name>/` 下。它是源码内容：不要为了让它可查询而执行
`lore pack install`、创建 Registry release，或提交 index/cache 文件。

当同一套已经审查的 Pack 必须安装到无关仓库，或必须作为可复现的公共产物保留时，才使用带版本的 Registry
release。这是另一条分发链：要准备版本、不可变 ref、Registry 条目和受支持安装路径的证据。局部 Pack 将来可以被提升，但应把已审查的 canonical 文件复制为新的 release
candidate，不能把持续变化的工作树当作 Registry 产物。

在 Pack
README 或贡献说明中写清选定的受众和生命周期。读者能够判断修改仓库文件是否会改变预期的事实来源，以及 Registry
release 是否明确不在范围内时停止。可执行的局部目录布局和命令见[项目局部 Pack 指南](resource:references/project-local-packs.md)。

## 反模式

一个支付服务需要三条关于自身发布门禁、私有 staging 环境和生成 contract 文件的 Practice，团队希望在编辑该仓库时就能得到它们。作者看到 Pack 已有 name/version，便创建 Registry 条目并要求每个人全局安装。服务指导于是依赖额外安装/更新步骤，可能与仓库脱节，还会出现在无关项目里。正确边界应是局部
`.lorelum/packs/payments-delivery/`；只有当规则后来跨仓库独立维护时，Registry release 才有价值。

## 原因

项目 layer 能让仓库所属的指导立即可用，不污染用户 Store，也不把派生 index 状态变成版本控制内容。Registry
release 解决的是另一件事：分发已经审查且不可变的独立产物。

## 例外与边界

一个仓库可以有意包含公开 Pack 的 release
candidate，但它的局部生效和 Registry 发布仍是两件不同的事。局部 Pack 不要求 Git；普通目录使用相同的
`.lorelum` 合同。当更广泛的发布 Pack 才是预期权威时，不要用局部 layer 静默替换它。

## 示例

基础设施仓库中的 Terraform modules、发布流程和内部 owner map 会一起变化。维护者创建
`.lorelum/packs/infrastructure-delivery/`，并在修改这些文件的同一批 PR 中更新 Practice。之后平台团队抽取两条适用于每个服务的规则，去除仓库私有假设后单独审查并发布 Registry
Pack。局部 Pack 仍归仓库所有；发布版是有独立 provenance 的产物。
