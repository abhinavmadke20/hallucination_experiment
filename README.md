# Evaluating Self-Verification for Reducing LLM Hallucinations

## Overview
Large Language Models (LLMs) are known to produce **hallucinations**, they are confident but factually incorrect statements.  

A commonly proposed mitigation is **self-verification**, where the model is asked to review and verify its own answer before finalizing it.


This project evaluates a simple question:
> **Does adding an explicit self-verification step reduce factual hallucinations in LLM responses?**

Rather than training models, this work focuses on **behavioral evaluation** through controlled experiments and quantitative analysis.

---
## Research Question
**Does prompting an LLM to verify its own answer reduce factual hallucinations compared to answering directly?**

---

## Hypothesis
Self-verification may reduce hallucinations by encouraging more cautious reasoning.  
However, it may also introduce new errors by over-correcting or adding unnecessary ambiguity.

---

## Model Used
The experiment was conducted using **`gpt-4o-mini`**.

---

## Results

![Effect of Self-Verification on Hallucinations](result_chart.png)

The chart above compares baseline accuracy against accuracy after self-verification.
Despite correcting some hallucinations, self-verification also introduced new errors,
resulting in no net improvement in overall accuracy despite localized gains and regressions.

---

## Key Takeaway
Self-verification can both correct and introduce hallucinations.
Without selectivity or uncertainty awareness, its overall benefit is inconsistent.

---

## Experimental Setup
- ~50 factual, single-answer questions
- Questions were manually curated
- Each question has a **fixed ground-truth answer**
- Ambiguous or opinion-based questions were avoided
- Human evaluation was used for labeling correctness


Example:
```json
{
  "question": "What is the capital of Australia?",
  "answer": "Canberra",
  "difficulty": "easy"
}