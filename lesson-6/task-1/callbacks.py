import os
from dotenv import load_dotenv

from langfuse import Langfuse
from langfuse.langchain import CallbackHandler

load_dotenv()

# Configure the Langfuse client
Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST"),
)

# Create the callback handler
langfuse_handler = CallbackHandler()