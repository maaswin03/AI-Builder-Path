from langchain_core.tools import tool
from rag.retriever import search_hr_documents


@tool
def rag_tool(query: str) -> str:
    """
    Search Presidio HR Policy documents.
    """

    return search_hr_documents(query)