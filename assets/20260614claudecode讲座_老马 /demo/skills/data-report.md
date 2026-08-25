---
name: data-report
description: 扫描 results/ 目录下所有实验 JSON，生成周报草稿：实验汇总表、最佳结果、趋势分析、下周建议。
metadata:
  type: skill
---

# Skill: Data Report

## Trigger Phrases
- `/data-report`
- `generate weekly report`
- `生成周报`
- `帮我整理这周的实验`

## What This Skill Does

### Step 1 — Collect all results
Use Bash to list all JSON files in `results/`:
```bash
ls results/*.json
```
Read each file with the Read tool.

### Step 2 — Build a summary table
Format as a markdown table:

| Run | lr | epochs | hidden | seed | best_acc | final_loss |
|-----|----|--------|--------|------|----------|------------|
| ... | .. | ...    | ...    | ...  | ...      | ...        |

Sort by `best_acc` descending.

### Step 3 — Highlight best run
State which run performed best and why (based on hyperparameters).

### Step 4 — Trend analysis
If there are ≥3 runs, note any visible trends (e.g., "larger hidden size consistently improves accuracy").
If <3 runs, skip this section.

### Step 5 — Next steps suggestion
Suggest 2-3 concrete next experiments based on the data (e.g., "try lr=0.01 to see if the current lr is too conservative").

### Output
Write the full report to `weekly-report.md` using the Write tool, then confirm with the file path.

## Constraints
- Base all observations on actual numbers — no speculation beyond what the data shows
- If results/ is empty, say so and stop
