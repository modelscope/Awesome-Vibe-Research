# Claude Code 速查卡

> 今天 tutorial 的内容摘要，带走备用。

---

## 文件位置速查

```
~/.claude/
├── CLAUDE.md          # 全局规则（所有项目）
├── settings.json      # 全局 harness 配置
└── skills/            # 你的 skill 库
    └── my-skill.md

my-project/
└── .claude/
    ├── CLAUDE.md      # 项目规则（覆盖全局）
    └── settings.json  # 项目 hooks & permissions
```

---

## CLAUDE.md 常用写法

```markdown
## 输出语言
Always respond in Chinese. Keep code in English.

## 代码要求
- 写最少的代码解决问题，不引入多余抽象
- 只改必须改的，不重构周边代码
- 写代码前先说明假设

## 项目约定
- 实验结果 → results/run_XXX.json
- 日志 → experiments.md（只追加，不覆盖）

## 禁止
- 不修改 train.py 除非明确要求
- 汇报数值必须带 mean ± std
```

---

## Skill 文件模板

```markdown
---
name: my-skill
description: 一句话描述这个 skill 做什么
metadata:
  type: skill
---

## Trigger Phrases
- `/my-skill`
- `中文触发短语`

## What This Skill Does

### Step 1 — 具体操作
[工具 + 命令]

### Step 2 — 输出格式
```markdown
## 输出模板
[具体模板，不要写"格式化输出"]
```

## Constraints
- 不能做什么 1
- 不能做什么 2
- 前置条件不满足时立刻停止
```

Skill 文件保存到 `~/.claude/skills/my-skill.md`

---

## settings.json Hook 模板

```json
{
  "hooks": {
    "afterToolUse": [
      {
        "matcher": "Edit|Write",
        "command": "your-check-command 2>&1 | head -10"
      }
    ],
    "Stop": [
      {
        "command": "osascript -e 'display notification \"Done\" with title \"Claude\"'"
      }
    ],
    "beforeToolUse": [
      {
        "matcher": "Bash",
        "command": "echo \"[log] $CLAUDE_TOOL_INPUT\""
      }
    ]
  }
}
```

---

## Hook 事件参考

| 事件 | 触发时机 | 常见用途 |
|------|---------|---------|
| `beforeToolUse` | 工具调用前 | 审计、拦截、日志 |
| `afterToolUse` | 工具调用后 | lint、测试、格式化 |
| `Stop` | 任务全部完成 | 通知、清理、记录 |

**matcher 示例：**
- `"Edit|Write"` — 文件修改类工具
- `"Bash"` — 所有 Shell 命令
- `".*"` — 所有工具

---

## MCP 配置示例

```json
// ~/.claude/settings.json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/your/data/path"]
    }
  }
}
```

社区 MCP servers：`github.com/modelcontextprotocol/servers`

---

## 常用命令

```bash
claude                    # 启动 Claude Code
claude -p "do X"          # 非交互式单次执行
claude --dangerously-skip-permissions  # 跳过所有权限确认（慎用）
/exp-logger               # 调用 skill（在 Claude Code 内）
/help                     # 查看所有可用 skill 和命令
```

---

## 本周可以做的第一件事

1. 打开终端
2. `nano ~/.claude/CLAUDE.md`
3. 写下你最常纠正 Claude 的 3 件事
4. 保存，下次对话自动生效

---

*Claude Code Tutorial · 2026-05-28*
