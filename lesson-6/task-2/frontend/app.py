import os
import uuid
import boto3
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Web Crawler Agent")

st.title("🕷️ Web Crawler Agent")
st.write("Ask the Bedrock Agent to crawl a webpage.")

agent_id = os.getenv("BEDROCK_AGENT_ID")
agent_alias_id = os.getenv("BEDROCK_AGENT_ALIAS_ID")

client = boto3.client(
    "bedrock-agent-runtime",
    region_name=os.getenv("AWS_REGION", "eu-north-1")
)

query = st.text_input(
    "Example:",
    "Crawl this URL: https://example.com"
)

if st.button("Submit"):

    with st.spinner("Thinking..."):

        response = client.invoke_agent(
            agentId=agent_id,
            agentAliasId=agent_alias_id,
            sessionId=str(uuid.uuid4()),
            inputText=query
        )

        answer = ""

        for event in response["completion"]:
            if "chunk" in event:
                answer += event["chunk"]["bytes"].decode()

        st.success(answer)