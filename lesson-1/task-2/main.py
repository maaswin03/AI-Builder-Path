import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3-flash-preview")


def run_test(context_file, prompt_file, output_file):
    """Read context and prompt, send to Gemini, save response."""

    with open(context_file, "r", encoding="utf-8") as f:
        context = f.read()

    with open(prompt_file, "r", encoding="utf-8") as f:
        prompt = f.read()

    full_prompt = f"""
You are an AI assistant.

Use ONLY the following context to answer the question.

========================
CONTEXT
========================

{context}

========================
QUESTION
========================

{prompt}

Provide a clear and concise answer.
"""

    response = model.generate_content(full_prompt)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(response.text)

    print(f"✅ Saved: {output_file}")


def main():
    tests = [
        (
            "context/coding_standards.md",
            "prompts/prompt1.txt",
            "results/output1.txt",
        ),
        (
            "context/hr_policy.md",
            "prompts/prompt2.txt",
            "results/output2.txt",
        ),
        (
            "context/troubleshooting_guide.md",
            "prompts/prompt3.txt",
            "results/output3.txt",
        ),
    ]

    for context_file, prompt_file, output_file in tests:
        run_test(context_file, prompt_file, output_file)

    print("\n🎉 All tests completed successfully!")


if __name__ == "__main__":
    main()