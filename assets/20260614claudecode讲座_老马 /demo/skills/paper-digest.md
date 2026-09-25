---
name: paper-digest
description: 读取一篇论文（PDF路径或文本），输出结构化摘要：研究问题、方法、核心结论、局限性、与我研究的关联。
metadata:
  type: skill
---

# Skill: Paper Digest

## Trigger Phrases
- `/paper-digest [文件路径或论文标题]`
- `digest this paper`
- `帮我读这篇论文`
- `summarize paper`

## What This Skill Does

Given a paper (as a file path or pasted text), produce a structured digest.

### Output Format

```markdown
## [Paper Title] — Digest

**Citation:** Authors (Year). Title. Venue.

### Research Question
[One sentence: what problem does this paper solve?]

### Method
[2-3 sentences: what did they actually do? Be specific about the technical approach.]

### Key Results
- [Quantitative finding 1, with numbers]
- [Quantitative finding 2, with numbers]
- [Qualitative finding if relevant]

### Limitations Acknowledged by Authors
- [Limitation 1]
- [Limitation 2]

### Relevance to My Work
[1-2 sentences: how does this connect to the current project context from CLAUDE.md?]

### Open Questions This Raises
- [Question 1 worth investigating]
- [Question 2]
```

## Constraints
- Do not fabricate results or citations. If you cannot read the file, say so.
- "Relevance to My Work" must refer to the actual project context — if no CLAUDE.md context exists, write "No project context loaded."
- Keep the entire digest under 400 words.
