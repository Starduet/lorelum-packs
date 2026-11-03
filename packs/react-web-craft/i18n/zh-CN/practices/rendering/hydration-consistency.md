# 首次客户端渲染与服务器输出保持一致

## 适用场景

时间、locale 和时区格式、随机或每个实例的标识符、浏览器存储，都可能让服务器和浏览器生成不同内容。服务端渲染的组件用到这些值时，要决定怎样让首次客户端渲染保持一致，或怎样处理范围明确的已知差异。

## 具体指导

默认应让服务端输出与首次客户端渲染一致。用服务器已知的值初始化，不要在渲染期间读取浏览器专属状态。仅客户端可用的值，按下面的情况安排读取和显示时机：

- 值只是装饰：用服务器已知值初始化 state，挂载后在 effect 中读取浏览器值。首次渲染保持一致，并接受 hydration 后显示的值会改变。
- 如果值已知会不同，但差异不影响展示要求，例如时间戳或每个实例的 id，可以保留差异，只在该元素上加
  `suppressHydrationWarning`。它只关闭这个元素文本和属性的告警，React 不会因此修补内容。必须确认两端内容都可接受，不能用它掩盖元素树不同或子节点缺失。
- 如果主题 class 这类显示设置必须在首绘前正确，应使用框架或主题库提供的 hydration 前设置方式。脚本可以提前设置 class，并仅在受影响的属性容器上使用
  `suppressHydrationWarning`。压制告警不是修复机制：服务端与客户端的 React 输出仍必须相同。这种显示设置不能建立认证状态，也不能授权访问受保护内容。

每条 hydration 告警都应先查明原因，再决定是否关闭。React 会指出具体差异；某个叶子元素不一致，可能是别处在渲染期间运行了浏览器专属代码。只有审阅并确认某个已知差异可以保留后，才对它使用 suppression，不要把它当成通用开关。

## 反模式

页面在 SSR 与 hydration 时都渲染
`lastSaved.toLocaleTimeString()`。开发者没有逐项查明差异，就给每个日期附近的元素都加上
`suppressHydrationWarning`。其中一处加在 `<ul>`
上，但两端实际不同的是它的子节点。压制告警既修不好结构性错误，也不覆盖子节点的不匹配，原本仅客户端生成列表的问题仍未解决。

## 原因

hydration 会复用服务端生成的 DOM，并要求客户端首次渲染与它一致。不一致可能引发告警、恢复工作和可见变化。压制告警并不会让两端输出相等，也不会修好已知的不匹配。只有某个独立元素在两端的内容都可接受时，才使用压制；否则应消除差异，或采用适当的 hydration 前设置方式。

## 例外与边界

- 流式 SSR 改变的是 mismatch 出现的位置，不是规则：边界子树渲染的内容在服务端与客户端必须一致。
- `suppressHydrationWarning` 只作用于当前这一层，不会关闭子节点的告警，因此只能安全地用于叶子元素。
- 本就不该在服务端渲染的纯客户端子树是加载边界决策（见
  `react.async.suspense-boundary-scope`），不是压制决策。
- 本篇不覆盖错误解码式 hydration 修复 API，也不覆盖框架 nonce/CSP 与预 hydration 脚本的交互。

## 示例

草稿编辑器显示最后保存时间，但服务器与浏览器的时区会产生不同字符串。`SavedAt`
先在两端显示相同的中性文案，挂载后再格式化时间。`SavedAtExact`
则允许单个文本元素存在已知差异，但前提是两个时区下显示的时间都可接受。

```tsx
function SavedAt({ isoTimestamp }: { isoTimestamp: string }) {
  const [mounted, setMounted] = useState(false);
  useEffect(() => setMounted(true), []);

  return (
    <span>
      {mounted
        ? `Saved at ${new Date(isoTimestamp).toLocaleTimeString()}`
        : "Saved"}
    </span>
  );
}

function SavedAtExact({ isoTimestamp }: { isoTimestamp: string }) {
  return (
    <span suppressHydrationWarning>
      {new Date(isoTimestamp).toLocaleTimeString()}
    </span>
  );
}
```

`SavedAt` 首先在两端显示 "Saved"，hydration 后再显示浏览器格式化的时间。`SavedAtExact`
保留单个元素上的已知文本差异，不要求 React 修补它。两者都不用压制告警来掩盖不同的元素树或缺失的子节点；其他 hydration 不匹配仍须查明原因。
