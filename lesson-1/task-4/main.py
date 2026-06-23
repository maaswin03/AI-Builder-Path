from rag import ask_rag

print("=" * 50)
print("🤖 RAG Chatbot")
print("Type 'exit' to quit.")
print("=" * 50)

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    answer = ask_rag(question)

    print("\nBot:")
    print(answer)