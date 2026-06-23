from agent.graph import graph

print("=" * 60)
print("Internal Research Agent")
print("=" * 60)

while True:

    query = input("\nAsk a question (type exit): ")

    if query.lower() == "exit":
        break

    result = graph.invoke(
        {
            "query": query
        }
    )

    print("\nAnswer:\n")

    print(result["answer"])