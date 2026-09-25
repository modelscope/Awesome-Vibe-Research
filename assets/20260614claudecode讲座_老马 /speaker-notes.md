# 讲稿 & Demo 脚本

> 格式说明：**[DEMO]** = 切换到终端操作，**[SLIDE]** = 切换幻灯片，*(斜体)* = 过渡语。

---

## 开场（Slide 1-2，共 3 分钟）

今天我想和大家聊一个稍微不一样的话题。不是「AI 能做什么」——大家都见过 ChatGPT，不稀奇了。我想聊的是：**怎么工程化地用好 Claude Code**，让它成为你研究流程里真正的基础设施，而不只是一个偶尔问问的聊天窗口。

今天的内容分五个部分，每部分都会有实际的演示。*[SLIDE]* 你们可以看到时间安排，我们大概 55 分钟内能走完，留 5 分钟给 Q&A 和现场尝试。

---

## Part 0：心智模型（Slide 3-5，共 10 分钟）

*(先不急着开终端，这段是建立认知框架)*

我先问大家一个问题——你们现在用 Claude Code 或者 ChatGPT，有没有发现一个很烦的事情：每次新开一个对话，都要重新解释一遍「我这个项目是做什么的」、「我喜欢什么代码风格」、「这个文件不能动」？

*[SLIDE]* 这就是最典型的问题——你在反复驯化一个失忆的助手。

我画了一个图。*[SLIDE]* Claude Code 的架构其实分几层：最底下是工具层（Bash、读写文件、网络搜索），上面是模型本身，但在模型和你之间，还有一个叫做 **Harness** 的运行时层。

大多数人只在和模型层打交道：输入问题，看回答，再输入。但 Harness 层才是真正可以工程化的地方——它决定了 Claude 每次启动时知道什么、不能做什么、做完后触发什么。

今天我们主要讲三件事：如何设计 CLAUDE.md（规则注入）、如何写 Skill（工作流封装）、如何配置 Hooks（反馈闭环）。

*[SLIDE]* 这是完整的目录结构。你把这些文件写好，Claude Code 每次启动就自动加载——这就是「给 Claude 编程」的核心思路。

---

## Part 1：CLAUDE.md 工程（Slide 6-9，共 10 分钟）

*[SLIDE]* CLAUDE.md 是 Claude Code 每次启动自动读取的配置文件。它不是备忘录，它是约束注入——写进去的东西会影响 Claude 每一次回答。

有三个层级。全局层放在 `~/.claude/CLAUDE.md`，对你所有项目生效。项目层放在 `.claude/CLAUDE.md`，进入这个目录才生效，可以覆盖全局规则。子目录层用于大型项目，一般研究项目用不到。

**[DEMO 1] — 展示全局 CLAUDE.md（1 分钟）**

```bash
cat demo/global-CLAUDE.md
```

这里我写了几类规则：输出语言、代码质量要求、研究规范（比如汇报数字必须带标准差）、回答风格。注意最后一条——「不要说 Certainly! 或 Great question!」。这种细节写进去，每次对话都生效，再也不用纠正它。

**[DEMO 2] — 展示项目级 CLAUDE.md（1 分钟）**

```bash
cat demo/project-CLAUDE.md
```

项目级的更具体：告诉 Claude 结果文件在哪、日志怎么维护、哪些文件不能碰。这相当于把你们实验室的 onboarding 文档写给 Claude 看。

*[SLIDE]* 最后一张 CLAUDE.md 的原则——写那些「Claude 不读代码就无法推断的事情」。目录结构、代码风格，它通过读文件能知道。但你的偏好、实验约定、禁区，只有你能告诉它。

---

## Part 2：创建 Skill（Slide 10-16，共 15 分钟）

*[SLIDE]* Skill 是今天最核心的部分，花时间最多。

Skill 本质上是什么？是一个有结构的 prompt 模板，但它描述的不只是「说什么」，而是「做什么」——包括调用哪些工具、按什么顺序、输出什么格式、什么情况下停止。

*[SLIDE]* 文件结构很简单。Frontmatter 里写名字和描述，正文写触发短语和执行步骤。

**[DEMO 3] — 展示 exp-logger skill 文件（2 分钟）**

```bash
cat demo/skills/exp-logger.md
```

这个 skill 做一件很具体的事：实验跑完，自动把结果记录到 `experiments.md`。步骤非常明确：找最新 JSON → 读取 → 格式化 → Append。注意 Constraints 节，我写了「只追加，不覆盖」——这种约束写进 Skill 里，比每次在对话里提醒要可靠得多。

**[DEMO 4] — 核心演示：实际运行 /exp-logger（3 分钟）**

*切换到终端，进入 fake-project 目录*

```bash
cd demo/fake-project
```

*打开 Claude Code*

```bash
claude
```

*在 Claude Code 里输入：*

```
/exp-logger
```

*(等 Claude 执行，展示 experiments.md 被更新)*

看这里——它自动找到了最新的 `run_002.json`，提取了超参数和指标，写了一条带时间戳的日志，还写了一句观察。这个流程手动做要多久？打开文件、找到末尾、格式化数字、写备注，每次实验做一遍，一个月下来是相当可观的时间。

*[SLIDE]* 这是实际输出的样子。重点不是好看，是**格式统一、自动触发、不需要你记着做**。

**[DEMO 5] — 快速展示 paper-digest（1 分钟）**

```bash
cat demo/skills/paper-digest.md
```

这个 skill 的特别之处是最后一节：`Relevance to My Work`——它会自动结合项目级 CLAUDE.md 的内容来说明这篇论文和你研究的关联。这就是分层配置的好处，不同 skill 都能用同一个项目上下文。

*[SLIDE]* Skill 设计原则。最重要的两点：Step 越具体执行越稳定，Constraints 节越详细越安全。

---

## Part 3：Hooks & 自动化（Slide 17-20，共 10 分钟）

*[SLIDE]* Hooks 是 Harness 层最强的杠杆。

和 Skill 不同，Hooks 不经过模型——是 Shell 直接执行。速度更快，确定性更强。

*[SLIDE]* 三个事件：`beforeToolUse`、`afterToolUse`、`Stop`。

**[DEMO 6] — 展示 settings.json（1 分钟）**

```bash
cat demo/settings.json
```

我配了三个 hook：Edit/Write 之后自动检查 Python 语法；任务完成后发桌面通知；Bash 执行前打印日志。

*[SLIDE]* 这里重点讲 afterToolUse + Stop 的组合：

- Claude 改了代码 → `afterToolUse` 触发 → 自动 lint
- 如果报错，错误输出回到 Claude 的上下文 → Claude 看到了，自动修复
- 任务全部完成 → `Stop` 触发 → 你收到通知

这就把 Claude Code 变成了一个有反馈闭环的系统，而不只是一个单次问答。你可以挂着它跑一个长任务，去做别的事，完成了它会通知你。

---

## Part 4：MCP（Slide 21-24，共 10 分钟）

*[SLIDE]* MCP 是用来突破内置工具边界的机制。

Claude Code 自带的工具能做大部分事情，但有一类场景不行：需要鉴权的 API。你的实验数据库、Zotero 文献库、Slack、Google Drive——这些都需要 OAuth 或 API key，用 Bash 调起来很麻烦，状态管理也复杂。

MCP Server 是一个独立进程，Claude Code 通过标准协议和它通信。你或者社区写好 Server，Claude Code 就能像调用内置工具一样调用它。

*[SLIDE]* 判断标准：一行 Shell 能解决的，不要引入 MCP。需要鉴权、持久连接、结构化数据查询，才值得用 MCP。

**[DEMO 7] — 展示 MCP 配置（1 分钟）**

展示 Google Drive MCP 的配置片段，说明 npx 启动的方式。

*(如果网络允许，演示 Claude 搜索 Drive 文件)*

---

## Part 5：串联演示（Slide 25-28，共 5 分钟）

*[SLIDE]* 把所有东西接在一起，展示一个完整的研究流水线。

*[SLIDE]* 整个流程图。实验跑完 → exp-logger 记录 → hook 验证 → 通知到桌面 → 周末用 data-report 生成周报。

**[DEMO 8] — 完整流水线（2 分钟）**

```bash
cd demo/fake-project
python3 train.py --lr 0.001 --hidden 256 --seed 2
# 跑完后
claude
> /exp-logger
# 展示 experiments.md 更新 + 桌面通知
> /data-report
# 展示 weekly-report.md 生成
```

*[SLIDE]* 总结那张「Level 1 到 Level 6」的图。大多数人停在 Level 3——写好 CLAUDE.md。今天讲完，大家至少能走到 Level 5。Level 6（MCP）按需来。

*[SLIDE]* 从今天起可以做的三件事。强调第一件事最简单，今天晚上就能做：写 `~/.claude/CLAUDE.md`，把你最常纠正 Claude 的 3 件事写进去。

---

## Q&A 结尾（5 分钟）

留 5 分钟。鼓励大家现场打开终端，把 `~/.claude/CLAUDE.md` 创建出来，写第一条规则。

备用问题（如果没人问）：
- 「你们实验室最重复的操作是什么？」→ 引导思考哪个任务适合做成 Skill
- 「有谁用过 CLAUDE.md 类似的工具？」→ 类比 `.editorconfig`、`.prettierrc`

---

## Demo 顺序速查

| # | 动作 | 文件/命令 |
|---|------|-----------|
| 1 | 展示全局 CLAUDE.md | `cat demo/global-CLAUDE.md` |
| 2 | 展示项目 CLAUDE.md | `cat demo/project-CLAUDE.md` |
| 3 | 展示 exp-logger skill | `cat demo/skills/exp-logger.md` |
| 4 | **核心** 运行 /exp-logger | `cd demo/fake-project && claude` → `/exp-logger` |
| 5 | 展示 paper-digest | `cat demo/skills/paper-digest.md` |
| 6 | 展示 settings.json | `cat demo/settings.json` |
| 7 | MCP 配置说明 | 幻灯片 + 代码块 |
| 8 | 完整流水线 | `python3 train.py` → `/exp-logger` → `/data-report` |
