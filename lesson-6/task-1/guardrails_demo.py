from dotenv import load_dotenv
load_dotenv()

import os
import re
from nemoguardrails import RailsConfig, LLMRails
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gemini-3-flash-preview",
    openai_api_key=os.getenv("GOOGLE_API_KEY"),
    openai_api_base="https://generativelanguage.googleapis.com/v1beta/openai/",
    temperature=0,
)

config = RailsConfig.from_path("./guardrails")
rails = LLMRails(config, llm=llm)

import logging
logging.disable(logging.CRITICAL)  # silence debug logs

while True:
    q = input("User: ")
    if q.lower() == "exit":
        break

    response = rails.generate(messages=[{"role": "user", "content": q}])

    # extract content
    if isinstance(response, dict):
        content = response.get("content", "")
    else:
        content = response

    # strip intent label like 'express greeting\n' before the quoted message
    content = re.sub(r'^[^\n"]*\n', '', content).strip().strip('"')

    print(f"Bot: {content}\n")