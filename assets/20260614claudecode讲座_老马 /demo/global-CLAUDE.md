# CLAUDE.md

## File Output Conventions

- When working with Chinese text in files (Excel, CSV, Word, docx), always use UTF-8 with BOM encoding for CSV files, and test for encoding/escaping issues with CJK characters before delivering final output.
- When generating Word (.docx) documents, use python-docx (never raw XML). For Chinese/CJK text, set the CJK font via `w:rFonts eastAsia` XML attribute (SimSun fallback); set western font via `run.font.name`. After saving, always verify with: `python3 -c 'from docx import Document; d=Document("output.docx"); print(f"OK: {len(d.paragraphs)} paragraphs")'` — do not report completion until this passes.
- When modifying Excel files, preserve row heights and cell formatting metadata. After any insert/delete row operation, verify existing rows are still visible and properly formatted.

## Interaction Style

- When the user asks multiple questions, answer them one at a time unless explicitly told otherwise. Wait for confirmation before moving to the next question.

## Coding Behavior

**Think before coding:** State assumptions explicitly. If uncertain, ask. If multiple interpretations exist, present them. If a simpler approach exists, say so.

**Simplicity first:** Minimum code that solves the problem. No features beyond what was asked, no abstractions for single-use code, no speculative flexibility. If you write 200 lines and it could be 50, rewrite it.

**Surgical changes:** Touch only what you must. Don't improve adjacent code or formatting. Match existing style. If unrelated dead code is noticed, mention it — don't delete it. Remove only imports/variables/functions that your own changes made unused.

**Goal-driven execution:** Transform tasks into verifiable goals. For multi-step tasks, state a brief plan with success criteria before starting.

## Research & Academic Work

- For research brainstorming sessions outside of /seed: before developing any direction extensively, run a quick feasibility check with these three questions: (1) Is the core hypothesis testable with current methods? (2) What is the single biggest threat to this working? (3) Could advances in AI capabilities invalidate this within 2 years? Be brutally honest. Do not elaborate further until the user confirms the direction survives this check.
- When proposing theoretical frameworks, ground them in concrete examples immediately.
