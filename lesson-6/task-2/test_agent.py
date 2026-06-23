import boto3
import uuid

client = boto3.client(
    "bedrock-agent-runtime",
    region_name="eu-north-1"
)

response = client.invoke_agent(
    agentId="7GIOPRMNAL",
    agentAliasId="TSTALIASID",
    sessionId=str(uuid.uuid4()),
    inputText="Crawl this URL: https://example.com"
)

text = ""

for event in response["completion"]:
    if "chunk" in event:
        text += event["chunk"]["bytes"].decode()

print(text)