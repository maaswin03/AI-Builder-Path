import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from callbacks import langfuse_handler

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0,
)


def supervisor(query: str):
    """
    Decide whether the query should go to the IT Agent or Finance Agent.
    """

    prompt = f"""
You are a supervisor agent.

Classify the following query into ONLY one category:

- IT
- FINANCE

Return ONLY one word:
IT
or
FINANCE

Query:
{query}
"""

    response = llm.invoke(
        prompt,
        config={
            "callbacks": [langfuse_handler]
        }
    )

    if isinstance(response.content, str):
        return response.content.strip().upper()

    if isinstance(response.content, list):
        text = "".join(
            block.get("text", "")
            for block in response.content
            if isinstance(block, dict)
        )
        return text.strip().upper()

    return "IT"