import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from tools.read_file_tool import read_file
from tools.web_search_tool import web_search_tool

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0,
)


def finance_agent(query):
    """
    Handles Finance-related queries.
    """

    policy = read_file("finance")

    web_results = web_search_tool.invoke(query)

    prompt = f"""
You are a Finance Support Agent.

Answer the user's question using BOTH the finance policy and the web search results.

Finance Policy:
{policy}

Web Search Results:
{web_results}

Question:
{query}

Provide a clear and concise answer.
"""

    response = llm.invoke(prompt)

    if isinstance(response.content, str):
        return response.content

    if isinstance(response.content, list):
        return "".join(
            block.get("text", "")
            for block in response.content
            if isinstance(block, dict)
        )

    return str(response.content)