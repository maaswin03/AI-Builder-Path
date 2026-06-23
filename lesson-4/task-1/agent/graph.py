from typing import TypedDict

from langgraph.graph import StateGraph, END

from agent.nodes import (
    supervisor,
    rag_node,
    google_node,
    web_node,
)


class AgentState(TypedDict):
    query: str
    tool: str
    answer: str


workflow = StateGraph(AgentState)

workflow.add_node("supervisor", supervisor)
workflow.add_node("rag", rag_node)
workflow.add_node("google", google_node)
workflow.add_node("web", web_node)


workflow.set_entry_point("supervisor")


def router(state):

    return state["tool"]


workflow.add_conditional_edges(
    "supervisor",
    router,
    {
        "rag": "rag",
        "google": "google",
        "web": "web",
    },
)

workflow.add_edge("rag", END)
workflow.add_edge("google", END)
workflow.add_edge("web", END)

graph = workflow.compile()