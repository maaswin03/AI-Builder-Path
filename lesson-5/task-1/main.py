from agent.graph import graph

print("=" * 60)
print("Multi-Agent Support System")
print("=" * 60)

while True:

    query = input("\nAsk a question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    result = graph.invoke(
        {
            "query": query
        }
    )

    print("\nResponse:\n")
    print(result["answer"])