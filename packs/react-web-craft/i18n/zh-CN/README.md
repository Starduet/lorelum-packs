# `react-web-craft` 简体中文审阅版

这里是 `react-web-craft` 24 篇 canonical Practice 的中文 companion，供中文读者审查每篇的决策边界是否清楚、来源是否可靠、示例是否可用。它不是另一套运行时 Pack，也不参与召回。

[`../../practices`](../../practices/) 中的英文 canonical 文件是运行时权威：Practice ID、anti-pattern ID、触发条件、指导、例外与边界都由英文文件控制。中文文件按相同相对路径与 canonical 一一对应，不复制 runtime frontmatter。每篇译文通过 [`../manifest.yaml`](../manifest.yaml) 中的 `source_digest` 锁定到对应的英文版本；英文内容修订后，应先更新 canonical，再用 `lore i18n sync` 重新核对指纹并同步译文，不能只在中文里另写规则。

## 导航（24 篇）

### state（6）

- [函数式 updater 不会刷新其他捕获值](practices/state/functional-updater-scope.md)
- [协调中的状态放在唯一的共同所有者](practices/state/share-one-owner.md)
- [非渲染用途的每实例记账放在 ref](practices/state/ref-for-nonrendered-values.md)
- [在用户覆盖之前保持响应式默认值](practices/state/fallback-until-overridden.md)
- [用一个状态表达互斥的 UI 模式](practices/state/model-exclusive-modes.md)
- [昂贵的挂载期状态用惰性初始化](practices/state/lazy-initializer.md)

### async（4）

- [独立的异步工作同时启动](practices/async/parallel-independent-work.md)
- [廉价检查先于异步工作启动](practices/async/await-after-cheap-work.md)
- [每一项的后续请求链进各自的 Promise](practices/async/chain-nested-item-fetches.md)
- [慢子树放进各自的 Suspense 边界](practices/async/suspense-boundary-scope.md)

### bundle（2）

- [重型非关键加载延后到需要时](practices/bundle/defer-heavy-loads.md)
- [用户意图出现时预载已延后的代码](practices/bundle/preload-on-intent.md)

### server（3）

- [用 React cache 去重请求级查询](practices/server/request-dedup-cache.md)
- [请求数据不进模块作用域](practices/server/no-module-request-state.md)
- [每个 Server Action 内部自证权责](practices/server/authorize-server-actions.md)

### rendering（5）

- [让渲染条件真正成为布尔值](practices/rendering/boolean-render-guards.md)
- [首次客户端渲染与服务器输出保持一致](practices/rendering/hydration-consistency.md)
- [资源提示与脚本加载按真实需要定级](practices/rendering/resource-hints-scripts.md)
- [紧迫的输入更新与缓慢的后续渲染分流](practices/rendering/update-priority.md)
- [渲染期推导值，不把 props 镜像进 state](practices/rendering/derive-dont-mirror.md)

### composition（4）

- [显式组件变体优于布尔模式旗标](practices/composition/explicit-variants-over-flags.md)
- [用 children 组合；render prop 留给数据绑定的插槽](practices/composition/children-over-render-props.md)
- [React 19 用 ref prop；旧版本线保留 forwardRef](practices/composition/react19-ref-prop.md)
- [用判别联合建模互斥的 React props](practices/composition/model-mutually-exclusive-props.md)
