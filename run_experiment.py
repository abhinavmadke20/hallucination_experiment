import json
import csv
from openai import OpenAI

client = OpenAI()

with open("data/questions.json", "r") as f:
    questions = json.load(f)

print("Questions loaded:", len(questions))


def baseline_prompt(question):
    return f"Answer the given questions accurately:\n\n{question}"


def verification_prompt(question, answer):
    return f"""
Question: {question}
Answer: {answer}

Verify if the answer is factually correct, if not, provide the corrected answer.
"""


def call_model(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content.strip()


print("Writing results to CSV...")
with open("data/results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "id",
        "question",
        "ground_truth",
        "baseline_answer",
        "verified_answer"
    ])
    f.flush()

    for q in questions:
        print("Question:", q.get("question"))

        baseline = call_model(baseline_prompt(q["question"]))
        print("Baseline answer:", baseline)

        verified = call_model(verification_prompt(q["question"], baseline))
        print("Verified answer:", verified)

        writer.writerow([
            q["id"],
            q["question"],
            q["answer"],
            baseline,
            verified
        ])
        f.flush()

print("Experiment completed successfully")
