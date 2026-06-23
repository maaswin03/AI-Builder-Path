from typing import TypedDict

from langgraph.graph import StateGraph, END

from agent.supervisor import supervisor
from agent.it_agent import it_agent
from agent.finance_agent import finance_agent


class AgentState(TypedDict):
    query: str
    category: str
    answer: str


def supervisor_node(state):
    category = supervisor(state["query"])
    return {"category": category}


def it_node(state):
    return {"answer": it_agent(state["query"])}


def finance_node(state):
    return {"answer": finance_agent(state["query"])}


workflow = StateGraph(AgentState)

workflow.add_node("supervisor", supervisor_node)
workflow.add_node("it", it_node)
workflow.add_node("finance", finance_node)

workflow.set_entry_point("supervisor")


def router(state):
    if "FINANCE" in state["category"]:
        return "finance"
    return "it"


workflow.add_conditional_edges(
    "supervisor",
    router,
    {
        "it": "it",
        "finance": "finance",
    },
)

workflow.add_edge("it", END)
workflow.add_edge("finance", END)

graph = workflow.compile()