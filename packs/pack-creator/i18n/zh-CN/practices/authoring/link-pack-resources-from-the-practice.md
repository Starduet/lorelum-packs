# 从 Practice 中明确引导补充资源

## 适用场景

读者只靠 Practice 已经能作出眼前的决定，但之后还可能需要详细矩阵、证据记录、模板或可重复运行的诊断脚本，就考虑是否把材料放进 Pack，并说明什么时候用。即使 Lorelum 只返回当前这一条，读者也应能看懂这些材料的用途。

## 具体指导

把当前决定所需的信息保留在 Practice 本文中；只有决定需要时才加入原因、例外或停止点。只把补充文件放进
`references/`、`assets/` 或 `scripts/`，再用普通 Markdown 链接引用，目标地址使用相对于 Pack 根目录的
`resource:`
路径。说明读者在什么条件下需要该材料，而不只是给出文件名：例如确认有公开 API 变更后阅读兼容矩阵、完成审查决定后复制报告模板，或在任务已授权且输入、预期输出明确时运行重复诊断。

使用精确地址，例如
`[矩阵](resource:references/api-matrix.md)`，不要使用同级相对路径。读者能只靠这条 Practice 做出当前决定、判断链接材料是否需要，并能从已选 Pack 根目录找到它时停止。需要完整规则和审阅提示时阅读[资源编写指南](resource:references/pack-resources.md)。

## 反模式

数据库迁移 Practice 只说“查阅迁移材料”，因为 Pack 中有兼容性说明和回滚脚本。作者假定 Agent 会自行浏览目录；实际只取回这一条时，Agent 不知道何时需要说明、是哪一个文件，也不知道运行脚本是否安全。即使把文字改成
`resource:references/migration-compatibility.md`，只要不可逆迁移的判断条件被藏在说明文件里，Practice 仍不完整。

## 原因

选择性检索不会附带目录清单或 Pack 顺序。明确的资源链接告诉读者何时需要补充材料，同时把判断是否需要它的条件保留在 Practice 本文中。

## 例外与边界

不是每个 Pack 文件都要直接链接：脚本可以有相邻 helper，成组 asset 也可以一起复制。不要为了让每个文件看似被使用而制造链接。普通网页链接和普通相对 Markdown 链接仍可用于外部来源或文档导航；只有同 Pack 资源才用
`resource:`。资源链接不是文件访问白名单，也不授权执行脚本。

## 示例

API 审查 Pack 包含字段矩阵和审查报告骨架。Practice 先写明破坏性变更条件及是否需要兼容审查的判断；之后链接
`resource:references/public-api-matrix.md`，并在审查决定完成后链接
`resource:assets/api-review-report.md`，要求先复制到工作区再编辑。即使不打开任一文件，Practice 也仍然可用。
