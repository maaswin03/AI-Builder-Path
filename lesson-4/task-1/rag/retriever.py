import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("vector_db/hr_index.faiss")

with open("vector_db/hr_chunks.pkl", "rb") as f:
    chunks = pickle.load(f)


def search_hr_documents(question, top_k=3):
    query_embedding = model.encode([question]).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:
        results.append(chunks[idx])

    return "\n\n".join(results)