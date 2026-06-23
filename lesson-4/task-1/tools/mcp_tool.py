from langchain_core.tools import tool
from mcp.google_docs import get_google_doc

DOCUMENT_ID = "1psOL4TRmYc4IfWNQTc3ScxQP91PCrxoXzPL_mTH1QOs"


@tool
def google_docs_tool(query: str) -> str:
    """
    Reads company insurance documentation stored in Google Docs.
    """

    document = get_google_doc(DOCUMENT_ID)

    return document