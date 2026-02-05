import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("kg_embeddings.faiss")

# Load texts
with open("embedding_texts.json", "r") as f:
    texts = json.load(f)

# Test queries with expected answers
test_cases = [
    ("Who works in IT department?", "works_in IT"),
    ("Employees in HR", "works_in HR"),
    ("Who is employee 1", "Employee_1")
]

def evaluate(top_k=5):
    correct = 0

    for query, expected in test_cases:
        q_emb = model.encode([query]).astype("float32")
        _, indices = index.search(q_emb, top_k)

        retrieved_texts = [texts[i]["text"] for i in indices[0]]

        if any(expected in t for t in retrieved_texts):
            correct += 1

    accuracy = correct / len(test_cases)
    print(f"Top-{top_k} Retrieval Accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    evaluate()