import os
import pickle
import faiss
import numpy as np

from embeddings import (
    load_document,
    chunk_text,
    create_embeddings
)

# Create vector_db folder if it doesn't exist
os.makedirs("vector_db", exist_ok=True)

# Load document
text = load_document("documents/company_policy.txt")

# Split into chunks
chunks = chunk_text(text)

# Create embeddings
embeddings = create_embeddings(chunks)

# Convert to float32 for FAISS
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Add embeddings
index.add(embeddings)

# Save index
faiss.write_index(index, "vector_db/company_index.faiss")

# Save chunks
with open("vector_db/chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("✅ Vector database created successfully!")
print(f"Total Chunks: {len(chunks)}")
print(f"Embedding Dimension: {dimension}")