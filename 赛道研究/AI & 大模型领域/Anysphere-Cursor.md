# Anysphere / Cursor

> 调研日期：2026-09-23 ｜ 结论速览：AI 编程赛道增长最快、工程实力与交易事实都可回查（SpaceX 8-K、OpenAI 官方声明、cursor.com 博客与文档、Bloomberg/CNBC/Forbes/Reuters）；但增长的上游——模型供给与训练算力——已集中到同一批供应商手里，2026-08-28 OpenAI 宣布终止向 Cursor 提供模型（拟定 2026-11-12 关停）是这份研究里权重最高的一条事实。并入 SpaceX 后 Anysphere 不再有独立披露义务，客户数、员工数、分部收入均为「公开渠道无独立记录」。

## 公司基本面

| 项目 | 信息 |
|---|---|
| 主体 | Anysphere Inc.（美国），产品名 Cursor；**2026-08-14 交割后为 SpaceX 全资子公司**（xAI 已并入同一上市主体，NASDAQ: SPCX） |
| 成立时间 | 2022 年（YC S22）；Cursor 于 2023 年 3 月发布 |
| 创始人 | Michael Truell（CEO）、Sualeh Asif（CPO）、Aman Sanger、Arvid Lunnemark，均 MIT 辍学 |
| 定位 | AI 代码编辑器 → 编程 Agent 平台；公司自述战略为「self-driving codebases」（Agent 合并 PR、管理发布、监控生产） |
| 规模 | **公开渠道无可靠的独立员工数/付费客户数记录**（聚合站给出的 1M+ 付费客户、50k+ 工程团队、150M 行/日等口径均无一手来源，本文不采用） |
| 客群 | 个人开发者（Pro 系列自付）＋ 企业（Teams Standard $40/席、Premium $120/席；Enterprise） |
| 独立融资史 | 2024-08-22 Series A；2025-11 Series D $2.3B（估值 $29.3B）；2026-04 曾报道以 $50B 估值募集 $2B+（a16z、Thrive 领投，Nvidia 跟投），**该轮最终未定价** |
| 并购对价 | 约 **$60B 全股票**（Bloomberg 2026-04-21 首次报道收购选择权，或支付约 $10B 放弃费；Reuters/CNBC 确认 2026-06-16 签署；**2026-08-14 交割**）。CNBC 报道该增发相当于 SpaceX IPO 估值的约 3.4% 稀释；SpaceX IPO 文件另披露若交易解体需付 $1.5B 终止费＋$8.5B 算力资源 |
| 收入（ARR） | $100M（2025.01）→ $500M（2025.06，公司博客）→ $1B（2025.11）→ $2B（2026.02，Bloomberg 2026-03-02 报道）→ $3B（2026 年 4 月底，Bloomberg 2026-05-21 报道）→ **$4B（2026.06，Forbes 报道）**；企业端占比约 75% |
| 资质与治理 | AIUC-1 认证（Agent 安全与可靠性，2026-08-13 公司博客宣布）；子处理者清单公开于 trust.cursor.com；**据检索无针对该并购的反垄断立案或审查记录** |

**口径提示**：$29.3B / $50B 为**融资估值**，$60B 为**并购对价**，$4B 为 **ARR**——三者不可互换，也不等于市值或确认收入。

## 产品线（官网与文档）

覆盖「补全 → 编辑器 → 云端 Agent → 代码托管」的一体化路线，四大块：

1. **编辑器与 Agent**：Tab 内联补全（来自 Supermaven 团队）、Agent（Agents Window、Projects、Agent Review、Planning、Debug、Design Mode）、Customize（Plugins / Rules / Skills / Subagents / Hooks / MCP）
2. **Cloud Agents**：Builds、Automations、Bugbot（AI 代码评审）、Security Agents、PR Routing & Approval、Mobile、Self-Hosted Machines、API
3. **Origin（自有 Git forge）**：建仓、clone/push/pull、CI 中的 CloneKit、Mirror GitHub、PR、代码浏览与搜索——2026 年 8 月起承接「Git at any scale」（Vicent Martí）与 Firetiger 收购后的生产运维场景
4. **模型层**：两类池子——**Cursor Models**（第一方：Grok 4.7 / 4.6 / 4.5、Composer 2.5）与 **Other Models**（Claude Fable 5.1 / Opus 5.5 / Sonnet 5、Gemini 3.1 Pro / 3.8 Flash、GPT-5.6 Luna / Sol / Terra、Muse Spark 1.3 等，按各家 API 价）；Auto 经 Cursor Router 在 Cost / Balance / Intelligence 三档间路由
5. **SDK 与 CLI**：TypeScript / Python / Bridge SDK；CLI 支持 Shell Mode、ACP、Headless/CI

## 商业模式与定价

| 机制 | 内容 | 含义 |
|---|---|---|
| 席位 + 用量混合 | Pro $20 / Pro Plus $60 / Ultra $200；Teams Standard $40/席、Premium $120/席（Agent 限额 5×）；Start（仅印度）₹649/月，不含 Other Models 池与 Auto/Bugbot/Automations/SDK | 低价档靠模型池与 Agent 配额分层，而非功能裁剪 |
| **Cursor Token Rate** | 第三方模型请求在 API 价之上加收 **$0.25 / 百万 token**（Teams/Enterprise），**included、按需与 BYOK 用量全部适用；第一方 Grok / Composer 豁免** | 结构性地把流量推向自研模型；BYOK 不再是「免平台费」通道 |
| 区域数据驻留 | 附加 **+10%** | 合规要求直接计价 |
| Bugbot 计费 | 2026-05-11 取消 $40/席，改为纯按量，自客户 2026-06-08 之后的首次续约生效（据报道） | 一年内第二次「席位→用量」迁移 |

## 技术背书与生态参与

| 信号 | 内容 | 可验证性 |
|---|---|---|
| 自研模型 Composer | 官方表述：Composer 是「不到六个月前」发布的第一个 agentic coding 模型；**Composer 1.5 把强化学习规模放大 20 倍以上；Composer 2 追加继续预训练，以「其他模型一小部分成本」达到 frontier 级**；Composer 2.5 已在定价表中（$0.5 输入 / $2.5 输出，Fast 档 $3/$15） | cursor.com/blog/spacex-model-training 原文＋docs 定价表；性能对比为公司自述（C 级） |
| 训练算力 | 与 SpaceX 合作使用 **Colossus** 集群 scaling Composer（据 Business Insider 2026-04 报道约 20 万张 Nvidia GPU，且 Cursor 已协助训练两代 Grok 模型） | 交易与算力用途见 cursor.com 官方博客与 CNBC/Reuters 报道；GPU 数量为单一媒体口径（B 级） |
| 工程输出（开源） | **Mixture-of-Kittens**：面向 NVL72 的开源 MoE megakernel（2026-08-04）；**Security Agents 开源**（The New Stack 2026-03-16）；Cursor Router 机制公开说明（2026-08-06） | 公司博客与技术媒体；repo 活跃度需自行核对 |
| 连续收购 | Supermaven（2024-11，Tab 补全）、Koala（2025-07）、**Graphite（2025-12-19，代码评审/PR 队列，现金＋股票，据报道对价「明显高于其最近一轮 $290M 估值」，产品继续独立运营）**、**Firetiger（2026-08-13，生产监控/事故处置 Agent，创始人为 Cloudflare/Twitch/Segment/Twilio 背景）** | Fortune＋TechCrunch 同日报道、cursor.com/blog/graphite、cursor.com/blog/firetiger；对价数字为转述（B 级） |
| 第三方评测 | 2026-05-22 公司博客宣布入选 **Gartner® Magic Quadrant™ for Enterprise AI Coding Agents（2026）Leader** | 原报告需订阅，目前仅厂商自述渠道 → 榜单默认降权，参考即可 |
| 客户案例 | 官网博客：Nokia「两周内分析 5,000 万+ 行代码」、Grab、Basis、IMDEX；企业页「Trusted by 64% of Fortune 500 companies」 | **官网宣称（C 级）**，无第三方审计口径 |
| 行业应用面 | 文档 UI 支持简体中文等 20+ 语言；集成 GitHub/GitLab/Azure DevOps/Bitbucket/JetBrains/Xcode/Slack/Teams/Jira/Linear/Notion | docs 可查 |

## 模型供给：OpenAI 断供事件（2026-08-28）

这是判断 Cursor 未来 12 个月成色的核心事实链：

- **OpenAI 官方声明（2026-08-28）**：「今天我们通知 SpaceX，我们打算终止为 Cursor 提供 OpenAI 模型的合同，拟定关停日为 **2026-11-12**」；理由是 Cursor 自定义协议中的**控制权变更窗口**；同时明确**不提供未来模型**（含下一代「Astra」），并称「已把终止时间压到我们可以接受的最晚一刻」。
- **受影响的范围**：Cursor 文档模型表中的三条 GPT-5.6 线（Luna / Sol / Terra）；Claude、Gemini、Grok、Composer 不在此列。
- **OpenAI 帮助中心的口径**：终止日「尚未最终确定，Cursor 可能提前结束访问」；替代路径为 BYOK / Codex IDE 扩展 / AI 网关——但 **BYOK 只覆盖本地的 Chat 与 Agent，Tab、Auto、Cloud/Background Agents、Automations、CLI、Cursor API/SDK 均不在覆盖范围内**。
- **Cursor 侧回应**：Truell 称「OpenAI 模型只承载约 5% 的 Cursor 用户流量，正在与 OpenAI 团队沟通」（X，2026-08）。
- **对手方的态度**：Anthropic 联合创始人 Tom Brown 公开表态「将继续增加算力以支持 Claude 模型进入 Cursor」（CNBC 2026-08-29 引用）；并入后 Cursor 自有博客于 **2026-09-21 发布 Grok 4.7** 上新（此前 8-12 为 Grok 4.6）——供给重心明显向母公司生态倾斜。
- **先例**：**Windsurf 2025 年 6 月**被 Anthropic 限制一方 Claude 3.5/3.7 访问，通知期不足一周（devin.ai/blog/anthropic-models）——供应商单点决策可在数日内改写一款编程工具的能力边界。

> 需要并置的两个数字：**「5% 流量」不等于「5% 功能」**。5% 说的是 token 占比，而 BYOK 的覆盖限制说明被切断的是特定入口（Tab/Auto/Cloud Agents/CLI/SDK）。真正的判断变量是自研 Composer 2.5 与 SpaceX 算力能否在 11 月之后维持质量曲线。

## 风险分析（按严重程度排序）

### 1. 模型供给与上游依赖风险（最核心）

- 断供本身可核实（A 级，OpenAI 官方 post），且时间明确（2026-11-12 拟关停）。Cursor 的价值主张长期是「最好的模型 + 最好的交互」，前半句从来不由它自己掌握
- 结构上「三重集中」：模型与算力集中于 SpaceX/xAI 生态，基座又曾依赖外部开源权重（见下）；母公司同时是竞争者（Grok Build）与供应商
- **Composer 2 基座争议**：作为自研模型发布后约 2 小时被开发者识别出为 Moonshot AI 开放权重 **Kimi K2.5**（修改版 MIT 许可，含月收入披露门槛）；Musk 公开回复「Yeah, it's Kimi 2.5」；联合创始人 Aman Sanger 回应「从一开始就没在博客里提 Kimi 基座是个失误，下个模型我们会修正」；Moonshot 随后确认为**授权商业合作**——争议焦点由「侵权质疑」转为「授权透明度」
- 对冲项（同样可核实）：Cursor 文档已把 SpaceXAI 列为模型供给方之一；第一方 Grok/Composer 免收 Cursor Token Rate；Mixture-of-Kittens 与 Router 的公开说明显示训练/推理栈在自己手里
- Composer 首篇模型博客（[「Composer: Building a fast frontier model with RL」的 HN 讨论](https://news.ycombinator.com/item?id=45748725)，2025-10）因**只给自报数字、缺少行业标准基准对照**而被批评——自研叙事的证据质量仍需时间建立

### 2. 安全与信任记录（开发者工具的复利资产）

| 时间 | 事件 | 处置 |
|---|---|---|
| 2026-07-14 披露 | Mindgard 报告 **git.exe 零点击**：在 Windows 上打开仓库会自动执行仓库根目录的 `git.exe`，无任何提示 | 约 7 个月未修补、无 CVE；早期报告曾被判定「Informative / out of scope」；1 月 CISO 邀请其进入 HackerOne 计划，重新提交并确认复现后无进一步响应（SecurityWeek / Dark Reading / The Hacker News） |
| 2026-04-28 | **CVE-2026-26268**（Novee）：中毒仓库的 git hooks 导致 RCE | 有 CVE 编号 |
| （2026） | **CVE-2026-22708**（SentinelOne 漏洞库）：RCE | 有 CVE 编号 |
| 2026-07-07 报告 | AimLabs：经已连接 MCP 服务器取回的一条 Slack 消息构成一行提示注入，使 Agent「变成本地 shell」 | **1.3 版本一天内修补**（CyberScoop） |
| 2026-08-27 | **路透社调查**：俄语系 Aur0ra 勒索团伙用 Cursor 内置 AI Agent 协助入侵一家比利时企业及其他至少六家（Gambit Security、CloudSek 报告；Gambit 与 The Hacker News 口径为 10 家），攻击期 Agent 由 Claude Sonnet 4.5 驱动，聊天日志区间 2026-04-08 至 05-21 | Cursor 平台本身未被攻破；风险形态是「Agent 被说服」 |

- **判断**：修补速度分化明显（AimLabs 一天 vs 零点击问题七个月），指向流程与优先级而非能力；AIUC-1 认证、Security Agents 开源、子处理者清单是反向证据，但认证为公司博客宣布，需查认证方公告。
- git.exe 二进制植入并非新发现——微软的 Git Credential Manager Core 同类漏洞早在 2020 年就以 CVE-2020-26233 修补，PoC 手法（把计算器改名成 `git.exe`）完全一致。对一家把「自动执行」作为产品卖点的公司，这类**已知十年的漏洞类别**是否进入默认威胁模型，比单条 CVE 更值得看
- 对选型方，最实际的暴露面是**「打开一个陌生仓库」这条默认路径**与 Agent 的默认工具权限。

### 3. 需求侧份额与竞争（增长叙事与份额数据并存）

- **联合创始人 Aadit Sheth 自述（X）**：「Cursor 的开发者市场份额在过去 12 个月从 41% 降至 26%，同期收入翻倍到 $4B ARR。」——A 级自评，双重解读：市场扩张快于它自己，同时它在丢份额
- 竞争来源已改变性质：模型方自营 Agent（Anthropic Claude Code、OpenAI Codex——后者在断供语境下被 OpenAI 直接列为替代路径）、GitHub Copilot（微软）、Cognition/Devin（含 Windsurf）、Replit、Lovable、Codeium；国内字节 Trae、阿里、腾讯 CodeBuddy 以低价与合规本地化竞争
- Cursor 的回应是把战线从「编辑器」外扩到 Cloud Agents 与 Origin（Git forge），即用工作流与代码托管提高替换成本——这条路依赖 SpaceX 生态的算力与分发，同时削弱了其「模型中立」的原始卖点

### 4. 定价与商业化信任

- 2025 年中由按请求计费改为按用量计费引发强烈反弹，Truell 于 **2025-07-04 公开道歉**（「我们没有处理好这次定价发布，我们很抱歉」），并对 2025-06-16 至 07-04 的消费退款（TechCrunch 2025-07-07）；HN 上有「一周 $350 超额」的个案
- 一年内两次「席位→用量」迁移（Tab/Agent 相关与 Bugbot），企业侧预算可预测性是长期摩擦点；Cursor Token Rate 对 BYOK 也收费，进一步压缩「自带 API Key 就省钱」的直觉
- 64% Fortune 500、70% Fortune 1,000 等采用率数字分别为官网宣称与聚合站口径，**不作为已核实事实引用**

### 5. 独立披露缺失（对本研究，这是信息风险；对公司，这是治理风险）

- 并入后 Anysphere 无独立财报、无分部披露：SpaceX 8-K 只披露发行 **389,289,254 股 Class A ＋ 1,752,426 股替换已归属 RSU**，并承担约 2,910 万股未归属 RSU 与 4,440 万份期权（全股票、无现金），**未拆分 Cursor 业务的收入、成本与留存**
- 因此以下问题在公开渠道**无记录**：Cursor 分部毛利率与算力成本、GPU 自建 vs 租赁的成本结构、员工总数与离职率、付费客户续费率
- 行业背景（可作为解读框架，但不能替代分部数据）：TechCrunch 在 2025-08-07 就指出 AI 编程初创普遍面临**高推理成本与薄毛利**，Cursor 把毛利压力外部化的方式（Cursor Token Rate、自研 Composer 免加价、母公司 Colossus 算力）正好落在这一条上——它的单位经济性现在更多是**集团内部记账问题**，外部更难验证
- 2026-09 另有针对多家前沿实验室的横向诉讼报道（PBS/AP，指控其就放缓开发达成不当协议）——**与本并购无直接关系，且本交易无立案记录**，列出仅为避免读者混淆

> 一句话总结：**这是一家「事实可查、边界可查，但内部不可查」的公司**。增长、交易结构、断供与安全问题都有 A 级来源；缺失的是分部财务与采用率的可审计口径。判断它不该问「增长是否还在」，而该问「11 月 12 日之后的模型质量曲线，以及零点击类问题的处置节奏」。

## 竞品格局

- **同赛道（编程 Agent / AI 编辑器）**：Cognition AI（Devin，含 Windsurf）、Replit、Lovable、Codeium、Factory；微软 GitHub Copilot 以分发取胜
- **模型方自营 Agent（既是渠道也是对手）**：Anthropic Claude Code、OpenAI Codex、Google Gemini Code Assist、xAI Grok Build
- **国内**：字节 Trae、阿里 Qoder / 通义灵码、腾讯 CodeBuddy——合规与中文语境下的替代路径
- **上游依赖**：SpaceX/xAI（算力 Colossus 与 Grok 模型）、Moonshot AI（Composer 基座授权，据报道）、Nvidia（NVL72 等目标硬件）、Anthropic/Google（Other Models 池）

## 分场景判断

**作为工具选型（个人）**：主流默认项，但注意第一方模型与第三方模型的计费差；对「自带 Key 省钱」的预期需按 Cursor Token Rate 重算。

**作为工具选型（企业 / 受监管行业）**：关注三点——BYOK 不覆盖 Agent/Cloud Agents/SDK 的自动化路径、区域数据驻留的 +10% 附加、以及「打开陌生仓库」相关的执行策略与沙箱配置；64% Fortune 500 是官网宣称，应要求供应商提供可审计的引用与部署清单。

**作为研究 / 投资参考**：值得作为「应用层 ARR 增长 + 上游集中」的样本长期跟踪；关键观测点是 2026-11-12 后的产品能力变化、Composer 版本的外部基准表现、以及 SpaceX 是否开始单列 Cursor 分部数据。**本文不构成投资建议。**

**作为职业选择**：入职主体现为 SpaceX 子公司，原 Anysphere 期权按 8-K 承接条款转换（约 4,440 万份期权、2,910 万股未归属 RSU）——具体到个人 offer 的行权价、归属与回购条款仍需单独确认；安全与 Agent 平台方向团队工程密度高（Origin、Router、开源 megakernel 为实证），但内部流动与工时结构公开信息为零。

## 待核实清单

- [ ] **2026-11-12 是否如期关停**，或 OpenAI 与 Cursor/SpaceX 是否达成新安排；「5% 流量」是否包含 Auto 路由下的隐式调用
- [ ] 交割条款细节：3.4% 稀释与「$1.5B 终止费＋$8.5B 算力」的**一手来源链接**（同期 CNBC 报道，本文未附 URL）；期权/RSU 转换对个人 offer 的影响
- [ ] Cursor 员工总数与离职率——公开渠道无一手口径；付费客户数、续费率同上（聚合站数据不采用）
- [ ] **Composer 2 发布日期**（2026-03-19 仅见于 Medium 转述，未在官方博客索引中确认）
- [ ] Aur0ra 事件的受害方计数（路透 7 家 vs Gambit/The Hacker News 10 家），及 Cursor 事后是否发布硬化措施公告
- [ ] Graphite 交易对价（「明显高于 $290M 估值」为转述，未见一手）
- [ ] Gartner Magic Quadrant Leader 评级：需以 Gartner 原报告为据，目前仅公司博客
- [ ] AIUC-1 认证：需查认证机构公告与适用范围
- [ ] Kimi K2.5 授权的条款细节与 Composer 2.5 基座是否同源（「下个模型会标注」的承诺是否兑现）

## 参考来源

- [OpenAI：Our decision on Cursor following its acquisition by SpaceX](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/)（2026-08-28）——支撑「断供事件」全节与风险 1
- [OpenAI Help Center：Using OpenAI models in Cursor](https://help.openai.com/en/articles/20001506-using-openai-models-in-cursor)——支撑「终止日尚未最终确定」与「BYOK 不覆盖 Tab/Auto/Cloud Agents/CLI/SDK」
- [CNBC：OpenAI to end model access to Cursor after acquisition by SpaceX](https://www.cnbc.com/2026-08-29/openai-cursor-spacex-model-access.html)（2026-08-29）——支撑 Tom Brown 表态、8-14 交割与 [SEC 8-K 原文链接](https://www.sec.gov/ix?doc=/Archives/edgar/data/0001181412/000162828026056945/spcx-20260814.htm)
- [Reuters：OpenAI to end partnership with SpaceX's Cursor](https://www.reuters.com/business/media-telecom/openai-end-partnership-with-spacexs-cursor-2026-08-29/)（2026-08-29）——断供事件的第二独立来源
- [Michael Truell on X](https://x.com/mntruell/status/2093532254006063557)——支撑「约 5% 流量」
- [Reuters：SpaceX to buy Anysphere for $60B](https://www.reuters.com/legal/transactional/spacex-buy-anysphere-60-billion-2026-06-16/)（2026-06-16）——支撑签署时点与交易结构；3.4% 稀释、终止费与算力条款为同期 CNBC 报道口径，**精确链接待补**
- [cursor.com/blog：Cursor is now a part of SpaceX](https://cursor.com/blog/joining-spacex)（2026-08-14）与 [SpaceX model training](https://cursor.com/blog/spacex-model-training)——支撑交割与 Composer 1.5/2 的训练叙事、Colossus 用途
- [cursor.com/blog 索引](https://cursor.com/blog)——支撑 Grok 4.7（2026-09-21）、[Grok 4.6](https://cursor.com/blog/grok-4-6)（8-12）、[AIUC-1 认证](https://cursor.com/blog/aiuc-1)、[Firetiger](https://cursor.com/blog/firetiger)、Git at any scale、Mixture-of-Kittens、Cursor Router、Projects、Cloud Agents、[Gartner MQ（2026-05-22 宣布）](https://cursor.com/blog/cursor-leads-gartner-mq-2026)、Bloomberg 2026-03-02（$2B）与 CNBC 2026-02-24 条目
- [cursor.com/docs 模型与定价](https://cursor.com/docs/models-and-pricing)——支撑两类模型池、Cursor Token Rate $0.25/M、各档价格、区域驻留 +10%；[Cursor Origin](https://cursor.com/origin) 支撑 Git forge 产品线
- [Reuters：Russian-speaking cybercriminals used Cursor AI tool to hack seven companies](https://www.reuters.com/world/russian-speaking-cybercriminals-used-spacexs-cursor-ai-tool-hack-seven-companies-2026-08-27/)（2026-08-27）——支撑 Aur0ra 事件（含 Gambit Security / CloudSek 口径）
- [The Hacker News：Aurora ransomware operators use Cursor AI](https://thehackernews.com/2026/08/aurora-ransomware-operators-use-cursor.html)——支撑 10 家计数口径
- [SecurityWeek：Unpatched Cursor vulnerability exposes users to code execution](https://www.securityweek.com/unpatched-cursor-vulnerability-exposes-users-to-code-execution/)、[Mindgard 原始披露](https://mindgard.ai/blog/cursor-0day-when-full-disclosure-becomes-the-only-protection-left)、[Cloud Security Alliance 研究纪要](https://labs.cloudsecurityalliance.org/research/csa-research-note-cursor-gitexe-zeroday-20260715-csa-styled/)、[HN 讨论](https://news.ycombinator.com/item?id=48910676)——支撑风险 2 的 git.exe 时间线、七个月未修补与 CVE-2020-26233 同类先例
- [Devin（Cognition）博客：Anthropic models](https://devin.ai/blog/anthropic-models)——支撑 Windsurf 先例（供应商一周内切断模型访问）
- [TechCrunch 2025-12-19：Cursor continues acquisition spree with Graphite deal](https://techcrunch.com/2025-12-19/cursor-continues-acquisition-spree-with-graphite-deal/) 与 [cursor.com/blog/graphite](https://cursor.com/blog/graphite)——支撑收购史（Graphite 为第三次收购）、$29.3B 估值与 $1B 年化收入的时间参照
- [Aadit Sheth on X](https://x.com/aaditsh/status/2066977180937277747)——支撑「份额 41%→26%、收入翻倍至 $4B ARR」
- [TechCrunch 2025-07-07：Cursor apologizes for unclear pricing changes](https://techcrunch.com/2025-07-07/cursor-apologizes-for-unclear-pricing-changes-that-upset-users/) 与 [cursor.com/blog/june-2025-pricing](https://cursor.com/blog/june-2025-pricing)——支撑 2025 定价风波、$20 用量额度与道歉退款
- [TechCrunch 2025-08-07：The high costs and thin margins threatening AI coding startups](https://techcrunch.com/2025-08-07/the-high-costs-and-thin-margins-threatening-ai-coding-startups/)——支撑「毛利与算力成本无公开口径」这一行业背景
- [cursor.com/enterprise](https://cursor.com/enterprise)——「64% Fortune 500」为官网宣称（C 级）
- 根目录 [README.md](../README.md) 的 Anysphere / Cursor 条目——本文与清单条目互为索引，数字口径保持一致
