# 首次客户端渲染与服务器输出保持一致

## 适用场景

组件渲染的值在服务端渲染与浏览器首次渲染之间可能正当地不同——时钟与相对时间、locale 与时区格式化、随机或每实例标识符、浏览器专属存储——时应用。逐个分歧决定处理方式。

## 具体指导

默认做法是让两端输出相等。渲染期间不读浏览器专属状态；用服务器已知的值初始化，把仅客户端的读取移到显式边界之后：

- 值只是装饰：挂载后再启用。用服务器已知值初始化 state，在 effect 里读浏览器值，接受短暂默认显示——那一下闪动就是分歧的诚实代价。
- 值有意不同但视觉无关紧要——渲染出的时间戳、每实例 id：保留分歧，只对那个元素标记
  `suppressHydrationWarning`。它只对该元素的文本与属性静默告警；React 依旧不做修补，所以只在两侧内容都可接受的地方使用，绝不用于掩盖结构性不匹配（元素树不同、子节点缺失）。
- 值必须在首绘前就正确——主题 class、已认证外壳：修法在 React 渲染之外——用一段在 hydration 之前运行的脚本设置（主题库通用的做法），并给受影响的属性容器标记
  `suppressHydrationWarning`，防止 hydration 把它重置。这是高级且狭窄的技术；服务端与客户端渲染的 React 输出仍必须相同。

对每条 hydration 告警都要查明原因，不要按模式匹配直接压制：React 报告的就是确切分歧，某片叶子上的 mismatch 往往意味着别处有浏览器专属代码在渲染期间运行了。一次压制是针对一个已知分歧、经过审阅的决定，不是构建开关。

## 反模式

一个页面在 SSR 与 hydration 时都渲染
`lastSaved.toLocaleTimeString()`，而套用全代码库的修法是给每个日期附近的元素加
`suppressHydrationWarning`。其中一处落在 `<ul>`
上，而它的子节点在服务端与客户端确实不同——一个真 bug（仅客户端的列表）从此静默地渲染错误，任何地方都没有告警。

## 原因

hydration 假定客户端首渲染复现服务器输出：浏览器沿用服务器的 DOM 并附着其上。分歧迫使 React 要么告警并修复（成本、噪音、闪动），要么被要求别看（`suppressHydrationWarning`）——后者只在两侧内容都真正可接受时才安全。把分歧分成「消除」「标记」「移出渲染」三类，让每种处理都对应它的成因。

## 例外与边界

- 流式 SSR 改变的是 mismatch 出现的位置，不是规则：边界子树渲染的内容在服务端与客户端必须一致。
- `suppressHydrationWarning` 只有 depth 1——不抑制该元素子节点的告警，这正是它只安全用于叶子的原因。
- 本就不该在服务端渲染的纯客户端子树是加载边界决策（见
  `react.async.suspense-boundary-scope`），不是压制决策。
- 本篇不覆盖错误解码式 hydration 修复 API，也不覆盖框架 nonce/CSP 与预 hydration 脚本的交互。

## 示例

草稿编辑器显示草稿的最后保存时间。服务端与客户端渲染出的时间字符串不一致（时区不同），处理方式按界面逐个选择：装饰版挂载后启用、先显示中性文案；必须立即显示真实时间戳的版本只把那片叶子标记为已知分歧。

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

`SavedAt` 在两端渲染一致（"Saved"），hydration 后再升级——闪动是被接受的代价。`SavedAtExact`
保留分歧文本，但把它限制在一片两侧渲染都可接受的叶子上。两者都没有压制任何结构性内容，页面其他地方的真 mismatch 照样告警。
