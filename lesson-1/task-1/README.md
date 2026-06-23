# AI Model Comparison

## Overview

This repository contains a comparative evaluation of four Large Language Models (LLMs) across three software engineering use cases:

* Application Development
* Data & SQL Generation
* DevOps & Infrastructure Automation

The same prompts were provided to each model, and the generated outputs were collected and compared without manual modification.

---

## Objectives

* Compare code generation capabilities.
* Evaluate SQL generation accuracy.
* Assess infrastructure automation using Docker and related files.
* Analyze the quality of project structure, documentation, and generated artifacts.

---

## Repository Structure

```text
AI-Model-Comparison/
│
├── prompts/
│   ├── appdev.md
│   ├── data.md
│   └── devops.md
│
├── output/
│   ├── gpt-5-mini/
│   ├── claude-haiku-4.5/
│   ├── gemini/
│   └── deepseek-r1:7b/
│
├── screenshots/
│
└── README.md
```

---

## Comparison Criteria

The models were evaluated based on the following criteria:

* Code Quality
* SQL Generation
* Infrastructure Automation
* Ease of Use
* Speed / Latency

---

## Results

| Model | Code Quality | SQL Generation | Infrastructure Automation | Ease of Use | Speed / Latency | Comments |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **GPT-5 Mini** | Good | Excellent | Good | High | Fast | Robust API and SQL; good boilerplate Dockerfile. |
| **Claude Haiku 4.5** | Excellent | Excellent | Good | High | Fast | Identical to GPT-5 Mini; consistent and high quality. |
| **Gemini Flash** | Good | Excellent | Basic | High | Medium | Focus on explainability and clean code. |
| **DeepSeek-R1:7B** | Basic | Basic | Excellent | Low | Slow | Broken Python code and missing SQL; exceptional Dockerfile. |

---

## Conclusion

This comparison provides an overview of how each model performs across common software engineering tasks, highlighting their strengths and areas for improvement.
