# 创建项目局部 Pack

## 适用场景

局部分发边界已确定，且第一条仓库所属 Practice 需要出现在 `lore query` 或 `lore get`
中之前使用。本条创建一个 Pack root；父子 layer 的设计和是否真实生效的验证是其他决定。

## 具体指导

在局部 layer 应开始生效的目录中执行一次 `lore init`。它会在缺失时创建可编辑的
`.lorelum/config.yaml`，已有文件保持不变。然后在 `.lorelum/packs/<pack-name>/` 下创建普通 Pack
root：`pack.yaml` 声明 Pack name/version，`practices/` 放带必需 frontmatter 的 canonical Markdown
Practice。Git 不是前提。

让项目 config 保持最小。省略字段即可使用通常的继承/默认行为；只有该目录必须不用选中的用户 Store 时才加
`base: none`。不要在 `.lorelum`
下创建 index、vector、模型或 Backend 文件：Lorelum 把派生 query 状态放在用户 cache 中，需要时会从 Pack
source 重建。

执行 `lore format .lorelum/packs/<pack-name>` 与
`lore validate .lorelum/packs/<pack-name>`，再从预期目录检查 `lore context status`。用 keyword
query 和 `lore get <practice-id>` 确认 source
Practice 可见，无需模型。Pack 校验通过、预期目录能发现它、仓库只含 canonical
source/config 而不含派生 index 时停止。可复制的目录树、starter
Practice 和命令见[项目局部 Pack 指南](resource:references/project-local-packs.md)。

## 反模式

一个 API 仓库需要临时但应审查的兼容性 Pack。作者把它安装到个人 Store，在已安装 Pack
view 中写策略，还提交 SQLite
index 让同事看到结果。此后同事需要相同 Store 状态，事实来源在仓库外，每次修改还会制造 cache
churn。正确做法是提交 `.lorelum/packs/api-compatibility/pack.yaml` 及 canonical
Practice；每个用户的 cache 保持可丢弃的派生状态。

## 原因

项目 layer 是从工作目录发现的 source-owned 内容。把 Pack root 和 canonical
Practice 放在仓库中，能让审查、分支、worktree 和普通目录行为可预测，同时避免全局安装和生成文件清理。

## 例外与边界

`lore init` 只创建 layer marker/config，不会生成 Pack skeleton，也不会配置模型。`--project-root`
适合测试另一个目录；正常使用应在开发者正在编辑的 layer 中运行。本条不发布 Pack；只有独立安装才是目标时才走 Registry
release。

## 示例

服务仓库根目录中，作者运行 `lore init`，创建 `.lorelum/packs/service-delivery/pack.yaml` 和
`.lorelum/packs/service-delivery/practices/service-delivery.rollback.md`。该 Practice 说明何时发布审查必须要求 rollback
plan。format/validate 后，作者在仓库根运行
`lore query "does this deployment need a rollback plan" --mode keyword`，再用 `lore get`
读取返回 ID。无需全局安装 Pack、下载模型或提交仓库 cache 文件。
