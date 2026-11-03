# 创建项目局部 Pack

## 适用场景

指导需要随一个仓库维护，就先在仓库里创建 Pack 文件，才能让 Practice 出现在 `lore query` 或
`lore get`
中。本条说明怎样创建一个 Pack 根目录；父子目录的规则怎样合并、预期规则是否实际生效，还需要另外处理。

## 具体指导

在局部层应开始生效的目录中执行一次 `lore init`。它会在缺失时创建可编辑的
`.lorelum/config.yaml`，已有文件保持不变。然后在 `.lorelum/packs/<pack-name>/`
下创建普通 Pack 根目录：`pack.yaml` 声明名称和版本，`practices/` 放带必需 YAML 元数据的权威 Markdown
Practice。Git 不是前提。

让项目配置保持最小。省略字段即可使用通常的继承或默认行为；只有该目录必须不用选中的用户 Store 时才加
`base: none`。不要在 `.lorelum`
下创建索引、向量、模型或 Backend 文件：Lorelum 把查询所需的派生状态放在用户缓存中，需要时从 Pack 源文件重建。

执行 `lore format .lorelum/packs/<pack-name>` 与
`lore validate .lorelum/packs/<pack-name>`，再从预期目录检查 `lore context status`。用关键字查询和
`lore get <practice-id>`
确认源 Practice 可见，无需模型。Pack 校验通过、预期目录能发现它、仓库只含权威源文件和配置而不含派生索引时停止。可复制的目录树、起始 Practice 和命令见[项目局部 Pack 指南](resource:references/project-local-packs.md)。

## 反模式

一个 API 仓库需要临时但应接受审查的兼容性 Pack。作者把它安装到个人 Store，修改已安装的 Pack 文件，还提交 SQLite 索引让同事看到结果。此后同事需要相同 Store 状态，权威来源在仓库外，每次修改还会造成缓存反复更新。正确做法是提交
`.lorelum/packs/api-compatibility/pack.yaml`
及权威 Practice；每个用户的缓存仍是可丢弃、可重建的派生状态。

## 原因

项目层包含归仓库所有、从工作目录发现的指导。把 Pack 根目录和权威 Practice 放在仓库中，就能沿用普通审查、分支、工作树和目录操作，不需要全局安装，也不必清理生成文件。

## 例外与边界

`lore init` 只创建项目层的标记和配置，不会生成 Pack 文件骨架，也不会配置模型。`--project-root`
适合测试另一个目录；正常使用应在开发者正在编辑的层中运行。本条不发布 Pack；只有独立安装才是目标时才走 Registry 发布路径。

## 示例

服务仓库根目录中，作者运行 `lore init`，创建 `.lorelum/packs/service-delivery/pack.yaml` 和
`.lorelum/packs/service-delivery/practices/service-delivery.rollback.md`。该 Practice 说明发布审查何时必须要求回滚计划。格式化和校验后，作者在仓库根运行
`lore query "does this deployment need a rollback plan" --mode keyword`，再用 `lore get`
读取返回 ID。无需全局安装 Pack、下载模型或提交仓库缓存文件。
