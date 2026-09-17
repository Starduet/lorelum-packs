# 把资源完整性作为独立证据链验证

## 适用场景

Pack 新增或修改 reference、asset、script 或 `resource:`
链接时使用。要决定哪些观察分别证明文件结构、所选 artifact 的保存、路由是否恰当和下游使用，避免把廉价的本地检查扩大成质量结论。

## 具体指导

先对 Pack 运行 `lore validate`，记录 Pack
revision 与结构 diagnostics。它可以证明允许的资源路径与链接在结构上有效，但不会运行脚本或评估脚本逻辑。对 release
candidate，通过支持的 Registry 路径安装到隔离 Store，取回链接该资源的 Practice，并从返回的 source
root 解析一个代表性 reference 或 asset。记录版本、ref、target 以及观察到的 bytes 或文件身份。脚本只能在另一个已授权任务中、带明确输入和预期输出时运行。

之后人工审阅 Practice 是否仍保留眼前决定，以及链接是否在正确时机引导材料。检索选择和下游 Agent 行为应作为独立练习。用[资源审阅清单](resource:assets/resource-review-checklist.md)记录实际观察到的层次。每个声明都清楚标记它覆盖结构、安装、内容审阅、检索选择、脚本执行还是 Agent 行为时停止。

## 反模式

可观测性 Pack 新增二进制 dashboard 模板和日志解析脚本。`lore validate`
本地通过后，作者用一个日志文件跑了脚本，发布说明便声称 Pack
“交付了验证过的可观测性自动化”。这既没有证明发布版本实际包含相同文件，也没有证明 Practice 在正确故障时路由它，更没有证明另一个 Agent 可安全使用生产输入。

## 原因

资源比普通 Practice 文本多出两个事实：所选 artifact 必须保存正确 bytes，Practice 也必须在正确决定时把读者带到它。结构验证、远程物化、检索、显式脚本运行和下游行为观察的是不同环节。

## 例外与边界

不要求每个 helper 都直接被链接或执行。未链接 helper 可以结构合法，二进制 asset 可以用 digest 或大小而不是终端渲染来确认。成功安装不证明脚本可用；成功运行脚本不证明 release
artifact 包含它。不要为了补齐 release 清单而执行脚本。

## 示例

数据迁移 Pack 新增兼容性参考、迁移计划模板和只读 schema diff 脚本。作者记录干净的
`lore validate`，安装带 tag 的 release 到隔离 Store，从获取到的 Practice source
root 读取 reference 并确认模板存在。另一个已授权测试再用 fixture 运行 schema
diff。检索查询和 Agent 练习单独报告，因此 release 声明只覆盖实际验证过的链接和 bytes。
