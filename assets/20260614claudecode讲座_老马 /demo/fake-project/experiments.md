# Experiment Log

<!-- entries appended by /exp-logger skill -->

## Run — 2026-05-31 10:00

**Hyperparameters:** lr=0.001, epochs=20, hidden=256, seed=2
**Results:** best_acc=0.9023, final_loss=0.2514
**Train time:** 1.0s

**Notes:** Hidden size 256 with lr=0.001 achieves 90.2% val accuracy; doubling hidden size from a baseline of 128 would likely explain a ~2% gain if prior runs used smaller networks.

## Run — 2026-05-31 13:57

**Hyperparameters:** lr=0.001, epochs=20, hidden=256, seed=2
**Results:** best_acc=0.9023, final_loss=0.2514
**Train time:** 1.0s

**Notes:** 与上一次运行超参数完全一致，结果稳定在 90.2% 准确率，表明模型在此配置下收敛行为可重现。
