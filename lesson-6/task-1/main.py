from agent.graph import graph
# from guardrails_loader import rails

print("=" * 60)
print("Multi-Agent Support System")
print("=" * 60)

while True:

    query = input("\nAsk a question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    # guarded = rails.generate(messages=[
    #     {
    #         "role": "user",
    #         "content": query
    #     }
    # ])

    # # If Guardrails blocks the request
    # if guarded and guarded.get("content"):
    #     if "can't" in guarded["content"].lower() or "cannot" in guarded["content"].lower():
    #         print("\nResponse:\n")
    #         print(guarded["content"])
    #         continue

    result = graph.invoke({"query": query})

    print("\nResponse:\n")
    print(result["answer"])