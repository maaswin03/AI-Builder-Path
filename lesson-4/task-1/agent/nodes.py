import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from tools.rag_tool import rag_tool
from tools.web_search_tool import web_search_tool
from tools.mcp_tool import google_docs_tool

load_dotenv()

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0,
)

def extract_text(response):
    """
    Extract plain text from a Gemini response.
    """
    # If content is already a string
    if isinstance(response.content, str):
        return response.content

    # If content is a list of content blocks
    if isinstance(response.content, list):
        text = ""
        for block in response.content:
            # LangChain content blocks are dictionaries
            if isinstance(block, dict):
                if block.get("type") == "text":
                    text += block.get("text", "")
            # Or objects with a .text attribute
            elif hasattr(block, "text"):
                text += block.text
        return text.strip()

    return str(response.content)


def supervisor(state):
    """
    Decide which tool should handle the query.
    """

    query = state["query"].lower()

    # Google Docs Tool
    if any(word in query for word in [
        "insurance",
        "claim",
        "coverage",
        "premium",
        "refund"
    ]):
        return {"tool": "google"}

    # HR RAG Tool
    elif any(word in query for word in [
        "leave",
        "employee",
        "hr",
        "casual",
        "work from home",
        "working hours",
        "medical insurance",
        "performance"
    ]):
        return {"tool": "rag"}

    # Default to Web Search
    return {"tool": "web"}


def rag_node(state):
    """
    Search HR documents and let Gemini answer.
    """

    context = rag_tool.invoke(state["query"])

    prompt = f"""
You are an HR assistant.

Answer ONLY using the context below.

Context:
{context}

Question:
{state["query"]}

Provide a short, accurate answer.
"""

    response = llm.invoke(prompt)

    return {
        "answer": extract_text(response)
    }


def google_node(state):
    """
    Read Google Docs and let Gemini summarize/answer.
    """

    context = google_docs_tool.invoke(state["query"])

    prompt = f"""
You are an insurance assistant.

Answer ONLY using the document below.

Document:
{context}

Question:
{state["query"]}

Provide a short, accurate answer.
"""

    response = llm.invoke(prompt)

    return {
        "answer": extract_text(response)
    }


def web_node(state):
    """
    Search the web and summarize results.
    """

    search_results = web_search_tool.invoke(state["query"])

    prompt = f"""
You are a research assistant.

Use the search results below to answer the user's question.

Search Results:
{search_results}

Question:
{state["query"]}

Provide a concise summary.
"""

    response = llm.invoke(prompt)

    return {
        "answer": extract_text(response)
    }