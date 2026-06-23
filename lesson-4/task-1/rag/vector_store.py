import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def load_document(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def chunk_text(text, chunk_size=300):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


text = load_document("documents/hr_policy.txt")
chunks = chunk_text(text)

embeddings = model.encode(chunks)
embeddings = np.array(embeddings).astype("float32")

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

os.makedirs("vector_db", exist_ok=True)

faiss.write_index(index, "vector_db/hr_index.faiss")

with open("vector_db/hr_chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("✅ HR Vector Database Created")