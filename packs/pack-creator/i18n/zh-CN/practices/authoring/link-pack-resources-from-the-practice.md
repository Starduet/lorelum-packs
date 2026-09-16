# 从 Practice 中明确引导补充资源

## 适用场景

一条 Practice 已足以做出眼前决定，但读者随后可能需要字段矩阵、证据记录、模板或可重复执行的诊断脚本时使用。这里要决定这些材料是否应放入 Pack，以及在 Lorelum 只返回当前 Practice 时，怎样说明它们的用途。

## 具体指导

把触发条件、动作、直接原因、重要例外和停止点保留在 Practice 本文中。只把补充文件放进
`references/`、`assets/` 或 `scripts/`，再用指向 Pack root 的普通 Markdown `resource:`
链接引用它。说明读者在什么条件下需要该材料，而不只是给出文件名：例如发生公开 API 变更时阅读兼容矩阵、决定完成后从报告模板开始，或在输入和预期输出明确时运行重复诊断。

使用精确 target，例如
`[矩阵](resource:references/api-matrix.md)`，不要使用同级相对路径。读者能只靠这条 Practice 做出当前决定、判断链接是否需要、并能从已选 Pack
root 解析它时停止。需要完整规则和审阅提示时阅读[资源编写指南](resource:references/pack-resources.md)。

## 反模式

数据库迁移 Practice 只说“查阅迁移材料”，因为 Pack 中有兼容性说明和回滚脚本。作者假定 Agent 会自行浏览目录；实际只取回这一条时，Agent 不知道何时需要说明、是哪一个文件，也可能以为脚本会在安装时自动执行。即使把文字改成
`resource:references/migration-compatibility.md`，只要不可逆迁移的判断条件被藏在说明文件里，Practice 仍不完整。

## 原因

选择性检索不会附带目录清单或 Pack 顺序。显式资源链接把补充材料放到任务语境中，同时把决定本身留在可检索的最小单元里。

## 例外与边界

不是每个 Pack 文件都要直接链接：脚本可以有相邻 helper，成组 asset 也可以一起复制。不要为了让每个文件看似被使用而制造链接。普通网页链接和普通相对 Markdown 链接仍可用于外部来源或文档导航；只有同 Pack 资源才用
`resource:`。资源链接不是文件访问白名单，也不授权执行脚本。

## 示例

API 审查 Pack 包含字段矩阵和审查报告骨架。Practice 先写明破坏性变更条件及是否需要兼容审查的判断；之后链接
`resource:references/public-api-matrix.md`，并在审查决定完成后链接
`resource:assets/api-review-report.md`，要求先复制到工作区再编辑。即使不打开任一文件，Practice 也仍然可用。
