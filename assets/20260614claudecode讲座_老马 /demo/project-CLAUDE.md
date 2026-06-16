# Project Rules — .claude/CLAUDE.md
# (这个文件放在项目根目录，进入目录后自动生效)

## Project Context
This is an image classification research project using PyTorch.
- All experiments write JSON results to `results/run_XXX.json`
- The canonical experiment log is `experiments.md` — always append, never overwrite
- Model checkpoints live in `checkpoints/` — never delete without asking

## Experiment Conventions
- When reporting accuracy, always state which split (train/val/test)
- Hyperparameters must be logged alongside results
- Never compare runs trained on different random seeds without noting the seed

## Coding Style
- Python 3.10+, type hints required on all function signatures
- No bare `except:` — catch specific exceptions
- Use `pathlib.Path`, not `os.path`

## What NOT to do
- Do not modify `train.py` unless explicitly asked — it is shared with other team members
- Do not install new packages without listing them and asking for approval first
