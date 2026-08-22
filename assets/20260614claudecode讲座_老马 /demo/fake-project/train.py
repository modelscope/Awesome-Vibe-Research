import json, time, random, argparse
from pathlib import Path

def train(lr: float, epochs: int, hidden: int, seed: int):
    random.seed(seed)
    results = {"lr": lr, "epochs": epochs, "hidden": hidden, "seed": seed}

    print(f"Training: lr={lr}, epochs={epochs}, hidden={hidden}")
    best_acc = 0.0
    for ep in range(1, epochs + 1):
        loss = 1.0 / (ep ** 0.5) + random.gauss(0, 0.02)
        acc  = 1 - loss / 2 + random.gauss(0, 0.01)
        acc  = min(max(acc, 0), 1)
        best_acc = max(best_acc, acc)
        print(f"  epoch {ep:02d}  loss={loss:.4f}  acc={acc:.4f}")
        time.sleep(0.05)

    results["final_loss"] = round(loss, 4)
    results["best_acc"]   = round(best_acc, 4)
    results["train_time_s"] = round(epochs * 0.05, 2)

    out = Path("results") / f"run_{seed:03d}.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(results, indent=2))
    print(f"\nSaved → {out}")
    return results

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--lr",     type=float, default=1e-3)
    p.add_argument("--epochs", type=int,   default=20)
    p.add_argument("--hidden", type=int,   default=128)
    p.add_argument("--seed",   type=int,   default=1)
    args = p.parse_args()
    train(args.lr, args.epochs, args.hidden, args.seed)
