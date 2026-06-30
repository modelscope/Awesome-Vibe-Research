---
marp: true
theme: default
paginate: true
style: |
  section {
    font-family: "PingFang SC", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif;
    font-size: 28px;
    padding: 48px 64px;
  }
  section.title {
    background: #0f172a;
    color: #f8fafc;
    text-align: center;
  }
  section.title h1 { font-size: 52px; color: #38bdf8; margin-bottom: 16px; }
  section.title p  { color: #94a3b8; font-size: 22px; }
  section.part {
    background: #1e293b;
    color: #f8fafc;
  }
  section.part h1 { color: #38bdf8; font-size: 44px; }
  section.part p  { color: #94a3b8; }
  h1 { color: #0f172a; }
  h2 { color: #0369a1; border-bottom: 2px solid #bae6fd; padding-bottom: 6px; }
  code { background: #f1f5f9; padding: 2px 6px; border-radius: 4px; font-size: 0.9em; }
  pre  { background: #0f172a; color: #f8fafc; border-radius: 8px; font-size: 0.85em; padding: 16px 20px; line-height: 1.6; }
  pre code { background: transparent; padding: 0; }
  pre .hljs-section, pre .hljs-title { color: #7dd3fc; }
  pre .hljs-bullet, pre .hljs-name { color: #f8fafc; }
  pre .hljs-strong { color: #fde68a; font-weight: bold; }
  pre .hljs-emphasis { color: #c4b5fd; }
  pre .hljs-string { color: #86efac; }
  pre .hljs-comment { color: #94a3b8; font-style: italic; }
  pre .hljs-keyword { color: #c084fc; }
  pre .hljs-attr { color: #7dd3fc; }
  pre .hljs-number { color: #fb923c; }
  section.part h2 { color: #cbd5e1; border-bottom: 1px solid #334155; font-size: 32px; }
  .columns { display: grid; grid-template-columns: 1fr 1fr; gap: 2em; }
  table { font-size: 0.85em; }
  th { background: #0369a1; color: white; }
  section.small { font-size: 22px; }
  section.small pre { font-size: 0.78em; }
---

<!-- _class: title -->

# Claude Code 工程化实践

## 从「聊天」到「可编程的 Agent Runtime」

**魔搭社区 · 2026-06-14**
老马

---

<!-- _class: small -->

## 讲者简介 — 马煜曦

**北京大学人工智能研究院 博士生** · [mayuxi.com](https://mayuxi.com/)

北京通用人工智能研究院 高级项目经理，负责学术合作与国际交流。执行主编出版《通用人工智能人才培养体系》（北京大学出版社），参与编撰《通用人工智能标准、评级、测试与架构》（人民邮电出版社）。

曾任全球研究方法与数据科学协会（洛杉矶）高级教育经理。宾夕法尼亚大学发展心理学硕士，浙江大学心理学学士。

**研究方向：** 计算社会科学（Computational Social Science）与认知科学（Cognitive Science）——用计算建模解码人类在历史记忆、语言行为及叙事创作中的潜在认知结构与社会规律。

成果发表于 **Nature Machine Intelligence、CHI、ACL、CogSci、Engineering** 等顶级期刊与会议，被人民日报、光明日报、新华社等媒体报道。

---

# 今天讲什么

不是「AI 是什么」——是「怎么工程化地用好它」

| 序号  | 内容                          |
| --- | --------------------------- |
| 1   | **心智模型** — Harness 架构       |
| 2   | **CLAUDE.md 工程** — 三层配置系统   |
| 3   | **创建 Skill** — 可复用工作流       |
| 4   | **Hooks & 自动化** — Shell 级拦截 |
| 5   | **MCP** — 接入外部世界            |
| 6   | **串联演示** — 完整研究流水线          |

---

<!-- _class: part -->

# Part 0

## 心智模型

---

## 大多数人怎么用 Claude Code

```
用户: 帮我调一下这个 bug
Claude: [看代码，修复，解释]
用户: 帮我润色这段话
Claude: [改文字]
```

**问题：** 每次对话都从零开始。Claude 不知道你的项目规范、你的偏好、你的工作流。

本质上是在「反复驯化一个失忆的助手」。

---

## 工程化的思路

把「告诉 Claude 怎么做」这件事**持久化**。

```
你的指令
    ↓
CLAUDE.md  ←─── 持久化「规则层」
    ↓
Harness    ←─── 运行时（hooks / permissions / settings）
    ↓
Claude     ←─── 模型本身（黑盒）
    ↓
Tools      ←─── Bash / Read / Edit / MCP / ...
```

**核心洞察：** 大多数人只在和模型层打交道。  
工程化的方法是**设计 Harness**。

---

## Claude Code 的完整架构

```
~/.claude/
├── CLAUDE.md          # 全局规则（所有项目生效）
├── settings.json      # 全局 harness 配置
└── skills/            # 可复用 skill 库
    ├── exp-logger.md
    └── paper-digest.md

my-project/
├── .claude/
│   ├── CLAUDE.md      # 项目规则（覆盖全局）
│   └── settings.json  # 项目 harness（hooks / permissions）
└── src/
    └── ...
```

这些文件就是你在「给 Claude Code 编程」。

---

## Harness 是什么：实验室类比

把 Claude Code 的运行环境想象成一个实验室：

| 概念              | 实验室类比       | 效果            |
| --------------- | ----------- | ------------- |
| **Claude**      | 你（学生）       | 负责思考、决策、写东西   |
| **Permissions** | 老板划定的权限边界   | 哪些事直接做，哪些事要请示 |
| **Hooks**       | 白板上的 SOP 流程 | 做完自动触发，不靠自觉   |

> **Permissions 是门禁卡，Hooks 是 SOP。**  
> Harness 保证 Claude 能干活，又不会乱来。

---

## Harness 配置长什么样

**Permissions** — 定义允许 / 拒绝的工具操作

```json
"allow": ["WebSearch"]      // 直接用，不用请示
"deny":  ["BudgetEdit"]     // 老板亲自来
// 未配置 → 弹窗确认         // 投稿前发给老板看一眼
```

**Hooks** — 事件驱动的自动 Shell 触发

```json
"PostToolUse": {
  "matcher": "Write",
  "command": "check_latex_format.sh $CLAUDE_FILE_PATH"
}
```

Claude 写完文件 → Hook 自动触发 → 格式没过不算完成

---

<!-- _class: part -->

# Part 1

## CLAUDE.md 工程

---

## CLAUDE.md 是什么

每次 Claude Code 启动，自动加载 CLAUDE.md 进上下文。

不是备忘录——是**约束注入**。

> 写得越精准，幻觉越少，重复纠正越少。

三个层级，按优先级从低到高叠加：

| 层级  | 路径                      | 作用域  |
| --- | ----------------------- | ---- |
| 全局  | `~/.claude/CLAUDE.md`   | 所有项目 |
| 项目  | `.claude/CLAUDE.md`     | 当前项目 |
| 子模块 | `src/.claude/CLAUDE.md` | 子目录  |

---

## 全局 CLAUDE.md 示例

```markdown
# Global Rules

## Output Language
Always respond in Chinese. Keep code and commands in English.

## Code Quality
- Write the minimum code that solves the problem.
- Touch only what you must. Never refactor adjacent code.
- State assumptions before writing any code.

## Research Standards
- When reporting numerical results, always include mean ± std.
- Never fabricate citations.

## Tone
- Be direct. Skip preamble like "Certainly!" or "Great question!".
```

**演示：** 修改这一行，立刻影响所有后续对话。

---

## 项目级 CLAUDE.md 示例

```markdown
# Project Rules — Image Classification Repo

## Project Context
PyTorch image classification project.
- Experiment results → results/run_XXX.json
- Canonical log → experiments.md (append only, never overwrite)
- Checkpoints → checkpoints/ (never delete without asking)

## Experiment Conventions
- Always state which split (train/val/test) when reporting accuracy
- Log hyperparameters alongside results

## What NOT to do
- Do not modify train.py unless explicitly asked
- Do not install packages without listing them first
```

---

## CLAUDE.md 写什么

<div class="columns">
<div>

**✅ 写这些**

- 项目背景和约定
- 你的代码风格偏好
- 禁止动的文件/行为
- 输出格式要求
- 领域特定规范

</div>
<div>

**❌ 不要写这些**

- 文件路径和代码结构（读代码就知道）
- Git 历史（`git log` 更准确）
- 临时任务状态
- 已在代码中体现的规范

</div>
</div>

> 一句话原则：写那些「Claude 不读代码就无法推断的事情」。

---

<!-- _class: part -->

# Part 2

## 创建 Skill

---

## Skill 是什么

Skill = 带结构的 prompt 模板 + 工具调用描述

存放在 `~/.claude/skills/` 目录，用 Markdown 写。  
触发方式：`/skill-name` 或自然语言触发短语。

```
~/.claude/skills/
├── exp-logger.md      # 实验记录
├── paper-digest.md    # 论文摘要
└── data-report.md     # 周报生成
```

**关键优势：** 一次写好，反复复用，可分享给团队。

---

<!-- _class: small -->

## Skill 文件结构

```markdown
---
name: exp-logger
description: 读取最新实验 JSON，追加写入 experiments.md
---

## Trigger Phrases
- `/exp-logger`  · `记录实验结果`

## Steps
- Step 1 — 找最新结果 [bash]
- Step 2 — 格式化日志条目 [模板]
- Step 3 — 追加写入 [工具]

## Constraints
- 只追加，不覆盖
```

---

## 核心演示：exp-logger

**场景：** 实验跑完了，用 `/exp-logger` 自动记录

```bash
$ cd fake-project
$ claude
> /exp-logger
```

**Claude 自动执行：**

1. `ls -t results/*.json | head -1` → 找最新结果
2. 读取 JSON，提取指标
3. 生成带时间戳的 Markdown 条目
4. Append 到 `experiments.md`

**你省了什么：** 打开文件 → 找到末尾 → 格式化数字 → 写备注。每次实验都要做一遍。

---

## exp-logger 输出示例

```markdown
## Run — 2026-05-28 14:32

**Hyperparameters:** lr=0.001, epochs=20, hidden=256, seed=2
**Results:** best_acc=0.9023, final_loss=0.2514
**Train time:** 1.0s

**Notes:** 相比 hidden=128 的基线（acc=0.8842），
扩大 hidden 层提升了约 2% 的准确率，
值得进一步探索更大的 hidden size。
```

---

## paper-digest Skill

```markdown
## Trigger
/paper-digest path/to/paper.pdf

## Output Format
### Research Question
### Method
### Key Results
### Limitations
### Relevance to My Work   ← 自动结合 CLAUDE.md 上下文
### Open Questions
```

**演示：** `/paper-digest` 读一篇本地 PDF  
→ 5 秒出结构化摘要，自动关联你的研究方向

---

## Skill 设计原则

| 原则                | 说明                          |
| ----------------- | --------------------------- |
| **Step-by-step**  | 明确每一步用什么工具                  |
| **Constraints 节** | 写不能做什么，防止越界                 |
| **输出格式模板**        | 给具体的 Markdown 模板，不要说「格式化输出」 |
| **触发短语**          | 中英文都写，降低触发门槛                |
| **Fail-fast**     | 前置条件不满足时立刻停止并说明             |

> Skill 文件越具体，执行越稳定。

---

<!-- _class: part -->

# Part 3

## Hooks & 自动化

---

## Hooks 是什么

Hooks = **模型之外**的 Shell 命令，由 Harness 在特定事件触发。

```json
// .claude/settings.json
{
  "hooks": {
    "afterToolUse": [...],
    "beforeToolUse": [...],
    "Stop": [...]
  }
}
```

**关键点：** Hooks 是 Shell 执行，不经过模型。  
速度快、确定性强、可以做任何 Shell 能做的事。

---

## Hook 事件类型

| 事件              | 触发时机              |
| --------------- | ----------------- |
| `beforeToolUse` | Claude 调用工具**之前** |
| `afterToolUse`  | Claude 调用工具**之后** |
| `Stop`          | Claude 完成整个任务后    |

`matcher` 字段用正则匹配工具名：

```json
{ "matcher": "Edit|Write" }   // 匹配文件修改
{ "matcher": "Bash" }         // 匹配所有 Shell 命令
{ "matcher": ".*" }           // 匹配所有工具
```

---

<!-- _class: small -->

## 实用 Hook 示例

**① 改完代码自动检查语法**

```json
{
  "matcher": "Edit|Write",
  "command": "python3 -m py_compile \"$FILE\" 2>&1 | head -5"
}
```

**② 任务完成后桌面通知（Mac）**

```json
{
  "command": "osascript -e 'display notification \"Claude finished\" with title \"Claude Code\"'"
}
```

**③ beforeToolUse 拦截危险操作**

```json
{
  "matcher": "Bash",
  "command": "echo \"[审计] 即将执行: $CLAUDE_TOOL_INPUT\""
}
```

---

## Hooks 让 Claude Code 变成什么

```
Claude 修改代码
    → afterToolUse hook 触发
    → 自动跑 lint / 测试
    → 如果失败，错误输出回到 Claude 上下文
    → Claude 看到错误，自动修复

Claude 完成任务
    → Stop hook 触发
    → 发桌面通知
    → 写操作日志到文件
```

**本质：** 把 Claude 接入你的 CI-like 反馈循环。  
不只是聊天，是一个**有副作用的自动化系统**。

---

<!-- _class: part -->

# Part 4

## MCP — 接入外部世界

---

## 内置工具的边界

Claude Code 默认能做的：

```
Bash / Read / Edit / Write / WebSearch / WebFetch
```

无法直接做的：

- 访问需要鉴权的 API（你的数据库、Zotero、Slack）
- 维持跨会话的连接状态
- 调用自定义的内部服务

---

<!-- _class: small -->

## MCP 是什么

**Model Context Protocol** — 让 Claude 调用任意外部服务的标准协议。

```
Claude Code
├── 内置 Tools
└── MCP Servers（独立进程，通过 stdio/SSE 通信）
        ├── filesystem-extended   # 扩展文件操作
        ├── your-lab-database     # 你自己写的
        ├── zotero                # 文献管理
        └── google-drive          # 云端文件
```

配置在 `~/.claude/settings.json`：

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/data"]
    }
  }
}
```

---

## 什么时候用 MCP vs Bash

| 场景                    | 用什么               |
| --------------------- | ----------------- |
| 简单命令行操作               | **Bash hook 就够**  |
| 需要 OAuth / API key 管理 | **MCP Server**    |
| 需要持久连接（数据库）           | **MCP Server**    |
| 复杂查询、返回结构化数据          | **MCP Server**    |
| 调用你自己写的 Python 脚本     | **Bash 或 MCP 均可** |

> 判断标准：如果一行 Shell 命令能解决，不要引入 MCP 的复杂度。

---

## 演示：配置 Google Drive MCP

```json
// ~/.claude/settings.json
{
  "mcpServers": {
    "gdrive": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gdrive"]
    }
  }
}
```

配置后 Claude 能：

- 列出你的 Drive 文件
- 读取 Google Docs 内容
- 搜索文件

**演示：** 让 Claude 找到实验相关的文档并摘要

---

<!-- _class: part -->

# Part 5

## 串联：完整研究流水线

---

<!-- _class: small -->

## 把所有东西接在一起

```
跑实验 (train.py)
    ↓
/exp-logger skill
    → 读 results/*.json
    → 追加写 experiments.md
    ↓
afterToolUse hook
    → 检查 Python 语法（如有代码改动）
    ↓
Stop hook
    → 桌面通知「实验已记录」
    ↓
/data-report skill（周末）
    → 扫描所有 runs
    → 生成 weekly-report.md
    → [可选] MCP 发送到邮件/Slack
```

---

## 演示：一键记录实验

```bash
$ cd fake-project
$ python3 train.py --lr 0.001 --hidden 256 --seed 2
[训练输出...]

$ claude
> /exp-logger
```

**结果：**

- `experiments.md` 自动更新
- 桌面收到通知
- 实验记录格式统一，不需要手动整理

---

## 你的「可编程研究助手」

<div class="columns">
<div>

**你需要维护的：**

- `~/.claude/CLAUDE.md` — 全局偏好
- `.claude/CLAUDE.md` — 项目规范
- `skills/` — 你的 skill 库
- `settings.json` — hook 规则

</div>
<div>

**你得到的：**

- 每次对话自动带项目上下文
- 重复任务一条命令完成
- 编辑后自动校验
- 结果自动记录，格式统一

</div>
</div>

---

## 实际上，这就是 Prompt Engineering 的终点

```
Level 1: 每次把问题描述清楚
Level 2: 保存好的 prompt，下次复制粘贴
Level 3: 写 CLAUDE.md，让规则自动加载       ← 大多数人在这里
Level 4: 写 Skill，让工作流可调用、可分享
Level 5: 写 Hooks，让系统有反馈循环         ← 工程化
Level 6: 写 MCP，接入你的整个工作生态       ← 基础设施
```

---

## 从今天起可以做的

1. **本周：** 写一个 `~/.claude/CLAUDE.md`，把你最常纠正 Claude 的事情写进去

2. **下周：** 找你最重复的研究任务，写成一个 Skill

3. **本月：** 给你的项目加一个 `afterToolUse` hook，跑完自动检查

---

# 资源

- **Claude Code 文档：** `claude.ai/code`
- **MCP 社区 Servers：** `github.com/modelcontextprotocol/servers`
- **今天的 demo 文件：** 见发给你们的 `demo/` 目录
- **速查卡：** `reference-card.md`

---

<!-- _class: title -->

# Q & A

**问题？现在打开终端，我们一起试。**
