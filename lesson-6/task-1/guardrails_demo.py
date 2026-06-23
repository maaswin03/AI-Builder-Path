from nemoguardrails import RailsConfig, LLMRails

config = RailsConfig.from_path("./guardrails")

rails = LLMRails(config)

while True:
    q = input("User: ")

    if q.lower() == "exit":
        break

    response = rails.generate(
        messages=[
            {
                "role": "user",
                "content": q
            }
        ]
    )

    print(response)