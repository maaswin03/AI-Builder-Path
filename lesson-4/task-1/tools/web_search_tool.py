from langchain_core.tools import tool
from ddgs import DDGS


@tool
def web_search_tool(query: str) -> str:
    """
    Search the web for industry benchmarks, trends, and regulatory updates.
    """

    results = DDGS().text(query, max_results=5)

    output = ""

    for i, result in enumerate(results, start=1):
        output += (
            f"{i}. {result['title']}\n"
            f"{result['body']}\n"
            f"{result['href']}\n\n"
        )

    if output == "":
        return "No results found."

    return output