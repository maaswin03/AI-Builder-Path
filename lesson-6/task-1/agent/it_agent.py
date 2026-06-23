import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from callbacks import langfuse_handler

from tools.read_file_tool import read_file
from tools.web_search_tool import web_search_tool

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0,
)


def it_agent(query):
    """
    Handles IT-related queries.
    """

    # Read internal IT document
    policy = read_file("it")

    # Search web for additional information
    web_results = web_search_tool.invoke(query)

    prompt = f"""
You are an IT Support Agent.

Answer the user's question using BOTH the internal IT policy and the web search results.

Internal IT Policy:
{policy}

Web Search Results:
{web_results}

Question:
{query}

Provide a clear and concise answer.
"""

    response = llm.invoke(
        prompt,
        config={
            "callbacks": [langfuse_handler]
        }
    )

    # Handle Gemini response
    if isinstance(response.content, str):
        return response.content

    if isinstance(response.content, list):
        return "".join(
            block.get("text", "")
            for block in response.content
            if isinstance(block, dict)
        )

    return str(response.content)