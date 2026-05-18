import os
import csv
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score




def evaluate(y_true: list, y_pred: list, approach: str) -> dict:
    return {
        "approach": approach,
        "accuracy": round(accuracy_score(y_true, y_pred), 4),
        "macro_f1": round(f1_score(y_true, y_pred, average="macro"), 4),
    }


def save_results(rows: list[dict]) -> None:
    result_path = os.path.join("results", "results.csv")
    os.makedirs("results", exist_ok=True)
    with open(result_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["approach", "accuracy", "macro_f1"])
        writer.writeheader()
        writer.writerows(rows)


def print_table(rows: list[dict]) -> None:
    print(f"\n{'Approach':<40} {'Accuracy':>10} {'Macro F1':>10}")
    print("-" * 62)
    for r in rows:
        print(f"{r['approach']:<40} {r['accuracy']:>10} {r['macro_f1']:>10}")
    print()
