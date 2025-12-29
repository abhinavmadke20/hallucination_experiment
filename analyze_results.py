import pandas as pd
import json

with open("data/questions.json") as f:
    questions = json.load(f)


df = pd.read_csv("data/results.csv")

baseline_acc = df["baseline_correct"].mean()
verified_acc = df["verified_correct"].mean()

print("Baseline accuracy:", baseline_acc)
print("Verified accuracy:", verified_acc)
print("Improvement:", verified_acc - baseline_acc)

fixed = ((df["baseline_correct"] == 0) & (df["verified_correct"] == 1)).sum()
broken = ((df["baseline_correct"] == 1) & (df["verified_correct"] == 0)).sum()

print("Fixed hallucinations:", fixed)
print("Verification made worse:", broken)

df["difficulty"] = df["id"].map(
    {q["id"]: q["difficulty"] for q in questions}
)

print(df.groupby("difficulty")[["baseline_correct", "verified_correct"]].mean())
