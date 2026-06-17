<p align="center">
  <img src="assets/cover.png" alt="Awesome Vibe Research" width="800"/>
</p>

<h1 align="center">🔬 Awesome Vibe Research</h1>

<p align="center">
  <em>面向 AI 辅助科研的开放共建仓库</em><br/>
  收集和沉淀科研全流程中的 agents、skills、workflows、tools 与最佳实践
</p>

<p align="center">
  <strong>🇨🇳 中文版</strong> | <a href="./README_en.md">🇬🇧 English</a>
</p>

<p align="center">
  <a href="#0--全流程端到端自动科研">🧪 全流程</a> •
  <a href="#1--方向扫描与问题定义">🔭 方向扫描</a> •
  <a href="#2--文献研究检索精读综述与引用网络">📚 文献研究</a> •
  <a href="#3--方法设计">🧩 方法设计</a> •
  <a href="#4--实验执行与分析">⚗️ 实验执行</a> •
  <a href="#5--科学可视化论文插图科学绘图与可视化表达">📊 可视化</a> •
  <a href="#6--论文写作投稿与同行评审">✍️ 写作</a> •
  <a href="#7--复现发布与归档">📦 复现发布</a> •
  <a href="#8--传播教学与影响力分析">📡 传播</a> •
  <a href="#-如何贡献">🤝 贡献</a>
</p>

---

我们关注能在科研工作中**反复复用**、能被同行**验证**、能逐步**演化**、表现**最优**的 AI 辅助能力。

本仓库从「与 Agent 共事做研究」系列沙龙出发，希望把 speaker 的实践经验、观众的使用反馈、开源项目与可复用流程沉淀成一个社区可维护的知识库。

---

## 🗺️ 科研流程地图

下表是我们对科研生命周期的 **9 阶段**拆分。每个阶段列出了"典型问题"和"可沉淀的 AI 辅助组件类型"。正文按阶段展开条目表，收录已知最好的项目、skill、workflow。

> 💡 **如果你觉得某个阶段的条目缺失或可以补充——直接在对应表格中添加一行。**

| 阶段 | 典型问题 | 范围 |
|:---:|---|---|
| 🔄 0.全流程 | 覆盖以下多个环节和问题 | — |
| 🔭 1. 方向扫描和问题定义 | 这个领域最近发生了什么？什么问题值得做、可做、能验证？ | trend scanner、paper radar、venue tracker；idea generator、novelty checker、hypothesis workflow |
| 📚 2. 文献研究 | 相关工作怎么找、读、比、写？ | literature review workflow、paper reading skill、citation graph agent |
| 🧩 3. 方法设计 | 方案、实验和评价指标如何设计？ | experiment design skill、ablation planner、protocol checker |
| ⚗️ 4. 实验执行与分析 | 如何写代码、跑实验、记录失败？结果是否可信，误差来自哪里？ | experiment runner、statistical analysis skill、failure analysis workflow、robustness checker |
| 📊 5. 可视化 | 图表是否讲清楚了科学问题？ | figure generation agent、visualization critique skill |
| ✍️ 6. 论文写作 | 如何组织论文、引用、补实验？ | paper writing workflow、citation verifier、rebuttal assistant |
| 📦 7. 复现发布 | 如何让别人复现和使用？ | artifact packaging workflow、model card、data card、reproducibility checklist |
| 📡 8. 传播影响 | 论文发表后如何追踪影响？如何构造自己的学术影响力 | impact analysis tool、social summary skill、citation monitor |

---

## 0 🔄 全流程（端到端自动科研）

覆盖从想法到论文的端到端系统。跨三个以上阶段的 agent 放这里，单阶段工具请放到对应阶段。

| 项目名称 | 描述 | 类型 | Stars | 链接 | Demo | Paper |
|---|---|---|---|---|---|---|
| AI-Scientist | 端到端自动科学发现系统，覆盖想法生成、实验、论文和同行评审 | agent | [![GitHub stars](https://img.shields.io/github/stars/SakanaAI/AI-Scientist?style=social)](https://github.com/SakanaAI/AI-Scientist) | [GitHub](https://github.com/SakanaAI/AI-Scientist) | - | [Nature 2024](https://modelscope.cn/papers/2408.06292/) |
| AI-Scientist-v2 | 基于 agentic tree search 的自动科研系统，不依赖人类模板，面向更通用的 ML 研究探索 | agent | [![GitHub stars](https://img.shields.io/github/stars/SakanaAI/AI-Scientist-v2?style=social)](https://github.com/SakanaAI/AI-Scientist-v2) | [GitHub](https://github.com/SakanaAI/AI-Scientist-v2) | - | [arXiv 2025](https://modelscope.cn/papers/2504.08066/) |
| EvoScientist | 多 agent AI scientist 系统，强调持久记忆、技能演化和端到端科研协作 | agent | [![GitHub stars](https://img.shields.io/github/stars/EvoScientist/EvoScientist?style=social)](https://github.com/EvoScientist/EvoScientist) | [GitHub](https://github.com/EvoScientist/EvoScientist) | [Demo](https://evoscientist.ai) | [arXiv 2025](https://modelscope.cn/papers/2603.08127/) |
| nature-skills | 符合 nature 论文学术表达和科研绘图的 Skill | skill | [![GitHub stars](https://img.shields.io/github/stars/Yuan1z0825/nature-skills?style=social)](https://github.com/Yuan1z0825/nature-skills) | [GitHub](https://github.com/Yuan1z0825/nature-skills) · [魔搭 Skills](https://modelscope.cn/collections/stn54999/nature-skills) | - | - |
| AutoResearchClaw | 自主、自进化的多阶段研究流水线，从研究想法推进到论文产物 | agent | [![GitHub stars](https://img.shields.io/github/stars/aiming-lab/AutoResearchClaw?style=social)](https://github.com/aiming-lab/AutoResearchClaw) | [GitHub](https://github.com/aiming-lab/AutoResearchClaw) | [Demo](https://openclaw.ai) | [arXiv 2025](https://modelscope.cn/papers/2605.22662/) |
| autoresearch | Andrej Karpathy 的自主 ML 研究代理，在单 GPU 上自动运行实验并改进模型 | agent | [![GitHub stars](https://img.shields.io/github/stars/karpathy/autoresearch?style=social)](https://github.com/karpathy/autoresearch) | [GitHub](https://github.com/karpathy/autoresearch) | - | - |
| Auto Claude Code Research in Sleep | 自动化 Claude Code 科研工作流项目，面向自动实验与代码执行 | skill | [![GitHub stars](https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=social)](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | [GitHub](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | - | - |
| AgentLaboratory | 端到端的自主研究工作流程，由 LLM 驱动的专业代理支持完成从文献综述到报告撰写的全流程 | agent | [![GitHub stars](https://img.shields.io/github/stars/SamuelSchmidgall/AgentLaboratory?style=social)](https://github.com/SamuelSchmidgall/AgentLaboratory) | [GitHub](https://github.com/SamuelSchmidgall/AgentLaboratory) | - | - |
| Aether | 基于 OpenCode 的开源项目，面向科研人员提供 web 与桌面端统一的 AI 研究工作环境 | agent/应用 | [![GitHub stars](https://img.shields.io/github/stars/Science-Discovery/Aether?style=social)](https://github.com/Science-Discovery/Aether) | [GitHub](https://github.com/Science-Discovery/Aether) | - | - |
| EurekAgent | 环境工程驱动的自主科研系统，面向可度量任务协调 Claude Code 会话提出方案、实现代码、隔离评测并迭代优化 | agent | [![GitHub stars](https://img.shields.io/github/stars/THU-Team-Eureka/EurekAgent?style=social)](https://github.com/THU-Team-Eureka/EurekAgent) | [GitHub](https://github.com/THU-Team-Eureka/EurekAgent) | - | [arXiv 2026](https://arxiv.org/abs/2606.13662) |

---

## 1 🔭 方向扫描与问题定义

趋势追踪、选题灵感、新颖性验证、假说生成。与文献检索有交叉时，以"产出一个可做的研究问题"为核心判断归属。

*🚧 暂无条目，欢迎贡献！*

---

## 2 📚 文献研究：检索、精读、综述与引用网络

文献搜索、RAG 问答、自动综述生成、引用图谱分析。纯写作润色类放 6。

| 项目名称 | 描述 | 类型 | Stars | 链接 | Demo | Paper |
|---|---|---|---|---|---|---|
| STORM | 斯坦福开源知识整理系统，通过多视角问题生成和检索生成带引用报告 | agent | [![GitHub stars](https://img.shields.io/github/stars/stanford-oval/storm?style=social)](https://github.com/stanford-oval/storm) | [GitHub](https://github.com/stanford-oval/storm) | [Demo](https://storm.genie.stanford.edu) | [NAACL 2024](https://modelscope.cn/papers/2402.14207/) |
| paperseek | 面向研究者的文献发现工具，支持自然语言检索、自动迭代查询、扩展候选论文 | agent/skill | [![GitHub stars](https://img.shields.io/github/stars/MingfengHong/paperseek?style=social)](https://github.com/MingfengHong/paperseek) | [GitHub](https://github.com/MingfengHong/paperseek) | [魔搭创空间](https://modelscope.cn/studios/HongMingfeng/PaperSeek) | - |
| Lune | 通过 MCP 提供顶会 Paper 的 agentic search 能力，支持学术文献与科研最佳实践的 grounding | agent/tool | [![GitHub stars](https://img.shields.io/github/stars/RetrogradeLabs/lune-mcp-server?style=social)](https://github.com/RetrogradeLabs/lune-mcp-server) | [GitHub](https://github.com/RetrogradeLabs/lune-mcp-server) | [Demo](https://luneresearch.com) | - |

---

## 3 🧩 方法设计

实验方案、评价指标设计、ablation 规划、protocol 检查。纯代码实现与跑实验放 4。

*🚧 暂无条目，欢迎贡献！*

---

## 4 ⚗️ 实验执行与分析

代码编写、实验运行、统计分析、失败分析、鲁棒性检查。数据集构建放 3 或 2，可视化放 5。

| 项目名称 | 描述 | 类型 | Stars | 链接 | Demo | Paper |
|---|---|---|---|---|---|---|
| RD-Agent | 实现数据与模型高价值通用研发流程的自动化，让 AI 驱动数据驱动型 AI | agent | [![GitHub stars](https://img.shields.io/github/stars/microsoft/RD-Agent?style=social)](https://github.com/microsoft/RD-Agent) | [GitHub](https://github.com/microsoft/RD-Agent) | - | [arXiv 2025](https://arxiv.org/abs/2505.14738) |
| EurekAgent | 面向可度量科研任务的实验执行环境，支持 Claude Code 会话自动实现方案、Docker 隔离评测、日志追踪和迭代优化 | agent | [![GitHub stars](https://img.shields.io/github/stars/THU-Team-Eureka/EurekAgent?style=social)](https://github.com/THU-Team-Eureka/EurekAgent) | [GitHub](https://github.com/THU-Team-Eureka/EurekAgent) | - | [arXiv 2026](https://arxiv.org/abs/2606.13662) |

---

## 5 📊 科学可视化：论文插图、科学绘图与可视化表达

出版级图表、示意图生成、数据 dashboard。幻灯/海报放 8。

| 项目名称 | 描述 | 类型 | Stars | 链接 | Demo | Paper |
|---|---|---|---|---|---|---|
| PaperBanana | 多 agent 学术插图自动化生成框架，从文本描述生成出版级图表和统计图 | agent | [![GitHub stars](https://img.shields.io/github/stars/dwzhu-pku/PaperBanana?style=social)](https://github.com/dwzhu-pku/PaperBanana) | [GitHub](https://github.com/dwzhu-pku/PaperBanana) | [Demo](https://dwzhu-pku.github.io/PaperBanana/) | [arXiv 2025](https://modelscope.cn/papers/2601.23265/) |

---

## 6 ✍️ 论文写作、投稿与同行评审

起草、润色、引用验证、LaTeX 辅助、rebuttal、审稿。综述生成类放 2。

| 项目名称 | 描述 | 类型 | Stars | 链接 | Demo | Paper |
|---|---|---|---|---|---|---|
| Academic Research Skills | 覆盖学术写作、润色、投稿检查和发表流程的 Claude Code skill 套件，也覆盖文献调研 | skill | [![GitHub stars](https://img.shields.io/github/stars/Imbad0202/academic-research-skills?style=social)](https://github.com/Imbad0202/academic-research-skills) | [GitHub](https://github.com/Imbad0202/academic-research-skills) | - | - |

---

## 7 📦 复现、发布与归档

代码复现、demo 体验、模型 & 数据集发布。

| 项目名称 | 描述 | 类型 | 链接 | 使用指引 |
|---|---|---|---|---|
| ModelScope 创空间 | 承载科研 demo 复现、发布和体验 | platform | [ModelScope Studio](https://modelscope.cn/studios) | [文档](https://modelscope.cn/docs/studios/intro) |
| ModelScope Notebook | 免费的云端 Jupyter 环境，自带 GPU、持久化存储和 AI 编程辅助 | platform | [Gallery](https://modelscope.cn/gallery) | [指引](https://modelscope.cn/learn/434367) |
| ModelScope 科学智能 | 汇集开源 AI for Science 模型，覆盖生命/地球/物质/社会科学等方向 | platform | [Nexa Models](https://modelscope.cn/nexa/models) | [文档](https://modelscope.cn/docs/nexa/intro) |
| Paper2Code | 多智能体系统，将学术论文自动转化为可运行的代码仓库 | agent | [GitHub](https://github.com/going-doer/Paper2Code) | [Quick Start](https://github.com/going-doer/Paper2Code#-quick-start) |
| data-to-paper | 多 AI 智能体自主协作，从原始数据完成完整科研并生成可验证论文 | python 包 | [GitHub](https://github.com/Technion-Kishony-lab/data-to-paper) | - |

---

## 8 📡 传播、教学与影响力分析

幻灯、海报、博文、社交传播、引用分析、学术影响力工具。

| 项目名称 | 描述 | 类型 | Stars | 链接 | Demo/实践经验 | Paper |
|---|---|---|---|---|---|---|
| CitationClaw | 用 agent 挖掘可解释的论文影响力，适合论文发表后的引用画像和传播分析 | tool | [![GitHub stars](https://img.shields.io/github/stars/VisionXLab/CitationClaw?style=social)](https://github.com/VisionXLab/CitationClaw) | [GitHub](https://github.com/VisionXLab/CitationClaw) | [ModelScope Studio](https://modelscope.cn/studios/fork?target=VisionXLab/CitationClaw) | - |
| ModelScope AI 超级简历 | 科研个人主页建设，用于沉淀模型、数据集、paper、demo 和学术影响力 | platform | - | [ModelScope](https://modelscope.cn/) | 示例：[VoyagerX](https://modelscope.cn/profile/VoyagerX) · [陈谐](https://modelscope.cn/profile/chenxie95) | - |

---

## 🏆 最佳实践

| 标题 | 实践简介 | 文章 | Demo |
|---|---|---|---|
| DIY 你的蛋白质 — AlphaFold3 推理 | 用 AlphaFold3 在魔搭上做蛋白质结构推理的实操教程 | [魔搭研习社](https://modelscope.cn/learn/5526) | [创空间](https://modelscope.cn/studios/Z_biosketch/af3_infer_test/summary) |
| AI Ready 遥感：从开放数据到开源生态实践 | AI Ready 数据简介，以及 ModelScope 如何提升遥感研究的 AI 就绪程度 | [魔搭研习社](https://modelscope.cn/learn/434003) | - |
| Open Source GeoAI Practise with ModelScope | APGARSS 教程合集：基于 ModelScope 的开源地理人工智能实践 | [魔搭研习社](https://modelscope.cn/learn/434198) | - |

---

## 📋 收录原则

我们收录的标准：

- ✅ 明确面向科研场景（非通用 AI 助手）
- ✅ 有可运行代码或可复用流程
- ✅ 项目仍在维护（最近 6 个月有更新）
- ✅ 文档或 README 清晰可上手
- ✅ 解决科研痛点有实际案例
- ✅ 开源或有免费可用版本

加分项：有论文支撑 · 有在线 demo · 被科研社区引用 · 已在实际项目中验证

---

## 🤝 如何贡献

除了推荐已有的开源项目，我们**更鼓励**沉淀自己在科研中实际跑通的 AI 辅助流程。

**贡献形态：**

- 🔗 **推荐 Resource**：推荐一个你用过的工具/论文/agent/skill…门槛：在对应阶段表格加一行，写一句话说明你用在什么场景。
- 📝 **分享最佳实践**：分享你自己写的可复用流程，示例：
  - 真实科研任务场景（"我用它做了 XXX 方向的文献综述，节省了约 X 小时"）
  - 失败案例与边界（"在 Y 场景下表现不好，原因是 Z"）

**贡献方式：** 直接在对应阶段的表格末尾添加一行，在 "Demo/实践经验" 列填入链接。建议发布在 [魔搭研习社](https://modelscope.cn/learn) 并带上 tag `#vibe-research`，让同行更容易发现；如果已发布在其他平台，也欢迎直接填外链。如果你的实践横跨多个阶段，先放进最核心的那个阶段，在描述里注明"也覆盖 x 阶段"。

---

## 🙏 致谢

感谢所有贡献者的参与和分享！

<p align="center">
  <a href="https://github.com/modelscope/Awesome-Vibe-Research/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=modelscope/Awesome-Vibe-Research" />
  </a>
</p>

---

<p align="center">
  <a href="https://modelscope.cn">
    <img src="https://img.shields.io/badge/ModelScope-魔搭社区-blueviolet?style=flat-square" alt="ModelScope"/>
  </a>
  <a href="https://github.com/modelscope/Awesome-Vibe-Research">
    <img src="https://img.shields.io/github/stars/modelscope/Awesome-Vibe-Research?style=social" alt="GitHub stars"/>
  </a>
  <a href="https://github.com/modelscope/Awesome-Vibe-Research/issues">
    <img src="https://img.shields.io/github/issues/modelscope/Awesome-Vibe-Research?style=flat-square" alt="Issues"/>
  </a>
</p>
