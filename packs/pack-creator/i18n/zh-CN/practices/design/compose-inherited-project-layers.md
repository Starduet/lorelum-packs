# 把父子项目层组成增量覆盖

## 适用场景

monorepo、嵌套组件、生成的子项目或局部实验需要自己的 `.lorelum`
目录，而祖先目录已提供指导时使用。这里决定 layer 之间的优先级和范围，不再判断 Pack 应局部存在还是通过 Registry 发布。

## 具体指导

把适用于整个仓库的指导放在最近且合适的父 layer。child
layer 只增加它特有的 Pack 文件，或增加同 ID 的 Practice 替换。Lorelum 从父到子 fold
layer：child 的同 ID Practice 获胜，child 未替换的 parent Practice 仍保持 active。因此同名 child
Pack 是增量 overlay，不是整包替换。

未声明的 config 字段继续继承。只有在确有 Pack 级决定时才使用 `packs.<name>.enabled` 或
`priority`；只有 child 必须排除选中的用户 Store 时才设置 `base: none`。`inherit: false`
只适用于真正需要隔离的子树，它会移除所有 parent layer，而不是只选择一个 child Practice。为每个同 ID
override 写明预期 winner，并在 child 目录中验证。child 只保留自己的决定、parent 仍提供未受影响的 Practice、维护者能解释每个 winner 为什么生效时停止。

## 反模式

仓库根目录的 `platform`
Pack 包含发布、日志和数据库变更 Practice。某个服务需要更严格的同 ID 发布 Practice。作者为了避免处理继承关系，把整个根 Pack 复制到服务目录并只改一个文件。之后根目录的修正需要改两次，复制的无关 Practice 会漂移，半写 child
copy 还可能遮住原本有效的 parent 指导。child 应只保存替换的那条 Practice，其他决定继续由 parent 提供。

## 原因

增量 overlay 保留可复用的基线，同时把局部例外明确放在真正变化的 Practice 上。整包遮蔽会把一个小决定变成重复维护面，也让普通源码编辑更脆弱。

## 例外与边界

对 vendored、受监管或有意独立的子树，可以使用
`inherit: false`，因为 parent 规则本就不应影响它。显式 priority 可以解决两个有效来源确实需要稳定排序的情况，但不能弥补不清晰或重复的 Practice
ID。本条不改变 Store 内已安装 Pack 的冲突规则。

## 示例

仓库根目录的 `.lorelum/packs/platform/` 包含 `platform.release`、`platform.logging` 和
`platform.database`。`payments/` 目录新增同 ID 的
`.lorelum/packs/platform/practices/platform.release.md`，其中包含卡组织审批条件。从 `payments/`
查询时，得到 child 的发布规则以及 root 的日志、数据库规则；从 root 查询时，仍得到原发布规则。没有复制整包，未来 root 的日志修正仍会到达两个目录。
