import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("kg_embeddings.faiss")

# Load original texts
with open("embedding_texts.json", "r", encoding="utf-8") as f:
    texts = json.load(f)

def semantic_search(query, top_k=5):
    # Convert query to embedding
    query_embedding = model.encode([query]).astype("float32")

    # Search FAISS
    distances, indices = index.search(query_embedding, top_k)

    results = []
    for idx in indices[0]:
        results.append(texts[idx])

    return results

# Test
if __name__ == "__main__":
    query = "employee working in company"
    results = semantic_search(query)

    print("\nTop relevant knowledge:")
    for r in results:
        print("-", r)