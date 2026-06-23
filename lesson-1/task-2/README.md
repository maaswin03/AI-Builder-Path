# Test Model Performance with Larger Context

## Overview

This project demonstrates how providing a larger context improves the quality and relevance of AI-generated responses.

## Project Structure

```text
context/
prompts/
results/
screenshots/
main.py
requirements.txt
```

## Context Files

* Coding Standards
* HR Policy
* Infrastructure Troubleshooting Guide

## Workflow

1. Load a context document.
2. Load a related prompt.
3. Send both to the AI model.
4. Generate a response.
5. Save the response in the `results` folder.

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

## Output

The generated responses are saved in the `results/` directory.

## Conclusion

The experiment shows that providing a larger context enables the AI model to generate more accurate, relevant, and context-aware responses.
