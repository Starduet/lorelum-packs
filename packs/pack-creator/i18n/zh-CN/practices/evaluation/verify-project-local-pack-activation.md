# 在真实项目语境中验证局部 Pack

## 适用场景

局部 Pack 或子目录的覆盖内容通过结构检查后，先确认开发者在实际工作的目录中能拿到预期的当前 Practice，再说可以使用。这不能证明语义搜索排名好，也不能证明 Registry 发布版可以安装。

## 具体指导

先对 Pack 根目录运行 `lore format` 与
`lore validate`，确认源文件结构并查看严格校验的诊断。再从实际使用的父目录或子目录运行
`lore context status`，确认预期项目层状态和警告。执行自然语言关键字查询，再执行
`lore get <practice-id>`，无需模型即可确认当前目录返回预期的权威 Practice。

对于子层覆盖，测试一条必须选择子层的同 ID
Practice，以及一条必须继续可用、仅父层拥有的 Practice。若需要验证用户 Store 的回退行为，再用
`--no-project` 做一次针对性检查，确认它只选 Store，而非静默混合来源。完成前检查仓库：`.lorelum/`
应只含作者编写的配置和 Pack 源文件，不应含派生缓存、向量、模型或操作状态文件。能够分别报告 Pack 结构通过、目标目录启用了预期 Practice，且不对未执行的召回或模型行为作声明时停止。

## 反模式

多项目共用的仓库中，根 Pack 有一条发布 Practice，`services/payments/`
覆盖同一个 ID。作者只对服务中的 Pack 路径执行
`lore validate`，又恰好在旧索引可用时运行一次语义查询，就在发布说明中宣称覆盖生效。他没有从服务目录检查、没有读取仅父层拥有的 Practice，也没发现复制的缓存文件在索引更新期间遮住了新源文件。正确检查应从
`services/payments/` 执行 `lore context status`、关键字查询和
`lore get`，同时验证子层版本及继承的父层条目。

## 原因

校验证明 Pack 结构；哪些 Practice 生效还取决于工作目录、父子层怎样合并、哪个来源优先，以及当前源文件内容。把这些事实分开检查，才能发现单独有效的 Pack 目录无法暴露的问题。

## 例外与边界

自动化测试需要从另一个工作目录检查测试项目时，使用 `--project-root`，指向直接包含 `.lorelum`
的目录。关键字查询和目录状态检查之后，可以再做语义查询冒烟测试；但缺少模型和索引尚未完成只是运行准备状态，不是源文件加载失败的证据。若局部 Pack 不涉及 Store 回退行为，不必强制使用
`--no-project`。

## 示例

仓库根目录提供 `platform.logging` 和一条发布 Practice，`services/billing/`
提供更严格的同 ID 日志 Practice 及一条计费专用 Practice。维护者先验证两个 Pack 根目录，再从
`services/billing/` 运行 `lore context status`、关键字查询和
`lore get platform.logging`。返回的是子层日志版本；查询仅根目录拥有的发布 Practice，仍能找到继承来源。单独的
`--no-project` 检查只返回选中的 Store 基线。报告记录预期 Practice 已生效，不声称跑过语义基准测试。
