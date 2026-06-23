from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def load_document(file_path):
    """Read text document."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def chunk_text(text, chunk_size=300):
    """Split text into smaller chunks."""
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


def create_embeddings(chunks):
    """Generate embeddings."""
    embeddings = model.encode(chunks)

    return embeddings


if __name__ == "__main__":

    text = load_document("documents/company_policy.txt")

    chunks = chunk_text(text)

    embeddings = create_embeddings(chunks)

    print("Number of Chunks:", len(chunks))
    print("Embedding Shape:", embeddings.shape)