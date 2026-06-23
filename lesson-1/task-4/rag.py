import os
import pickle
import faiss
import numpy as np
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from google import genai

# Load environment variables
load_dotenv()

# Gemini Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("vector_db/company_index.faiss")

# Load document chunks
with open("vector_db/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)


def retrieve_context(question, top_k=3):
    """Retrieve the most relevant document chunks."""

    question_embedding = embedding_model.encode([question]).astype("float32")

    distances, indices = index.search(question_embedding, top_k)

    retrieved_chunks = []

    for idx in indices[0]:
        retrieved_chunks.append(chunks[idx])

    return "\n\n".join(retrieved_chunks)


def ask_rag(question):
    """Generate answer using retrieved context."""

    context = retrieve_context(question)

    prompt = f"""
You are an AI assistant.

Answer ONLY using the context below.

If the answer is not present, reply:
"I couldn't find that information in the provided documents."

------------------------
Context
------------------------

{context}

------------------------
Question
------------------------

{question}
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )

    return response.text