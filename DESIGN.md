---
name: Awesome Startups — GTM 备忘录世界
description: 投资备忘录视觉世界：奶油纸/墨色/牛血红，衬线中文，发丝线层级，红墨稀缺纪律
colors:
  paper: "#F7F5F0"
  paper-night: "#211D18"
  ink: "#1A1815"
  ink-night: "#EAE3D6"
  muted: "#5C564B"
  muted-night: "#A69D8D"
  oxblood: "#8C2F1B"
  oxblood-night: "#D97F60"
typography:
  display:
    fontFamily: "Noto Serif SC, Songti SC, serif"
    fontSize: "clamp(2.6rem, 7.5vw, 5.2rem)"
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: "0.02em"
  headline:
    fontFamily: "Noto Serif SC, Songti SC, serif"
    fontSize: "clamp(1.6rem, 3vw, 2.1rem)"
    fontWeight: 900
    lineHeight: 1.4
  body:
    fontFamily: "Noto Serif SC, Songti SC, serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.9
    letterSpacing: "0.01em"
  label:
    fontFamily: "Noto Serif SC, Songti SC, serif"
    fontSize: "0.78rem"
    fontWeight: 700
    letterSpacing: "0.22em"
rounded:
  stamp: "0.45em"
  toggle: "0"
spacing:
  page-pad: "clamp(1.25rem, 4vw, 3rem)"
  entry-block: "clamp(2.4rem, 5vw, 3.8rem)"
components:
  theme-toggle:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.toggle}"
    padding: "0.45em 1em"
  memo-stamp:
    backgroundColor: "transparent"
    textColor: "{colors.oxblood}"
    rounded: "{rounded.stamp}"
    padding: "0.55em 1.1em 0.6em"
---

# Design System: Awesome Startups — GTM 备忘录世界

## Overview

**Creative North Star: "投资备忘录 (The Investment Memo)"**

整套系统把 Go-To-Market 方法论装订成一份 VC 内部传阅的 IC memo：读者不是被教育框架，而是在读一份正在发生的投资判断。纸面（#F7F5F0）即页面本身，没有卡片、没有阴影装饰——深度全部来自排印层级与发丝线。牛血红（#8C2F1B）是页边批注的墨水，只属于批注、编号与印章三处；它的稀缺就是它的权威。暗色模式不是反色而是同一世界的夜读变体（暖深纸 #211D18、陶土红 #D97F60），由 prefers-color-scheme、`?theme=` 覆盖与页内切换三重驱动。

**Key Characteristics:**
- 连续文档流，禁卡片网格
- 发丝线（1px）做分隔、2.5px 实线做边界的两级线制
- 等宽数字（tabular-nums）承载所有金额与日期
- 点线引导（dotted leaders）的目次是导航的唯一形态
- 全页唯一入场动效：机密章盖章

## Colors

纸面与墨色的双色系统加一种批注红；红色稀缺是刻意的。

### Primary
- **奶油纸 Cream Paper** (#F7F5F0): 页面即纸张，body 直接使用；暗色下变暖深纸 (#211D18)。
- **墨色 Ink** (#1A1815): 正文与标题；暗色下为暖米白 (#EAE3D6)。

### Secondary
- **牛血红 Oxblood** (#8C2F1B): 批注边栏、章节编号、机密章、交叉引用（§03）——全部「页边声音」；暗色下提亮为陶土红 (#D97F60) 以保对比度 ≥4.5:1。

### Neutral
- **弱化墨 Muted Ink** (#5C564B): 抬头小字、目次案例名、页脚；暗色 (#A69D8D)。
- **发丝线 Hairline** (ink 16% 透明度): 全部分隔线；暗色为米白 18%。

### Named Rules
**The Red Ink Rule.** 牛血红只出现在批注、编号、印章三处，任意视口占比 <10%。红一旦出现在正文或装饰上，备忘录就变成了海报。

## Typography

**Display Font:** Noto Serif SC（Google Fonts，Songti SC 回退）
**Body Font:** 同上——全页单一衬线家族，靠字重与尺度分层

**Character:** 中文宋体衬线的「公文感」是世界的骨架；绝不引入无衬线做标题。

### Hierarchy
- **Display** (900, clamp(2.6rem, 7.5vw, 5.2rem), 1.15): 仅页面主标题。
- **Headline** (900, clamp(1.6rem, 3vw, 2.1rem), 1.4): 章节标题，编号在前的牛血红小号数字（.55em）。
- **Body** (400, 1.0625rem, 1.9): 中文行高 1.9 起，栏宽 ≤38em。
- **Label** (700, .72–.78rem, letter-spacing .2em+, uppercase): 抬头 MEMO NO.、目次 CONTENTS、字段标签 致/自/日期/事由。
- **数字**: 一律 `font-variant-numeric: tabular-nums`，金额列对齐。

### Named Rules
**The One Voice Rule.** 全页只用一个衬线家族；层级靠 900/700/400 三档字重与尺度跳变，不靠换字体。

## Layout

单栏纸面，容器 max-width 1200px、页边距 clamp(1.25rem, 4vw, 3rem)。章节为双栏网格：正文 minmax(0,1fr) + 300px 批注边栏，批注与正文同段落起始对齐、互不竞读；≤900px 批注并入正文下方并出现「批注 Margin Notes」标签。抬头字段栏为 4 列（≤900px 折 2×2），列间 1px 竖发丝线。目次 2 列（≤720px 1 列，案例名隐藏）。

## Elevation & Depth

无阴影。纸面深度由线制与留白承担：1px 发丝线分隔，2.5px 实线只出现在抬头底边一处，作为「信笺折线」。

### Named Rules
**The Two-Weight Rule.** 结构线只有两种：1px（发丝分隔）与 2.5px（抬头边界）。第三种粗细出现即装饰，删除。

## Shapes

无圆角体系。唯一的圆角是机密章的 0.45em 橡皮章外缘与其内嵌双圈（inset 双重 box-shadow 模拟章圈）；按钮与字段全部直角。

## Components

### 主题切换按钮 (theme-toggle)
- **Shape:** 直角，1px 实线边框
- **Color:** 透明底、墨色字与框；hover 转 牛血红字与框
- **Typography:** Label 规格，内容为「切换暗色/切换亮色」（控件自称其动作）

### 机密章 (memo-stamp)
- **Shape:** 0.45em 圆角矩形，2.5px 红框 + inset 双圈，rotate(-7deg)
- **Color:** 透明底、牛血红字与框，opacity .92
- **Motion:** 盖章入场（内层 scale 1.7→0.94→1.03→1 + 外层 opacity），全页唯一动效；prefers-reduced-motion 下静止
- **注意:** 缩放动画不得作用在定位元素本身（会锁定横向滚动溢出），见 components 实现

### 批注边栏 (margin-note)
- **Style:** 牛血红正文（.92rem/1.85），条目间以 45% 透明度红发丝线分隔；公司名 700 加粗，来源「§ 主录」为点状下划线链接

### 目次行 (toc-row)
- **Style:** flex + 点线引导（1px dotted 填充），编号牛血红 tabular 数字，尾部灰色案例名；hover 整行转红、点线变实红

### 备忘录表格 (memo-table)
- **Style:** th 小号 Label 规格 + 1.5px 墨色底线；td 1px 发丝底线；金额列牛血红 tabular 数字，不换行

## Do's and Don'ts

### Do:
- **Do** 让红墨只服务「页边声音」：批注、编号、印章（The Red Ink Rule）。
- **Do** 用点线引导与发丝线做全部结构与导航。
- **Do** 保持全页单一衬线家族与 900/700/400 三档字重。
- **Do** 所有数字用 tabular-nums 并标注时点（如 ARR $2B（2026.03））。

### Don't:
- **Don't** 使用卡片网格、阴影、渐变或圆角容器——备忘录是连续文档。
- **Don't** 让牛血红进入正文、装饰或大面积色块。
- **Don't** 引入无衬线或等宽字体做视觉声音（等宽只用于数据语义）。
- **Don't** 在盖章之外添加入场动效；页面其余部分静默。
