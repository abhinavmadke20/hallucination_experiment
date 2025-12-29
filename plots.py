import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/results.csv")

baseline_acc = df["baseline_correct"].mean()
verified_acc = df["verified_correct"].mean()

plt.bar(
    ["Baseline", "Verified"],
    [baseline_acc, verified_acc]
)

plt.ylabel("Accuracy")
plt.title("Effect of Self-Verification on Hallucinations")
plt.ylim(0, 1)
plt.show()