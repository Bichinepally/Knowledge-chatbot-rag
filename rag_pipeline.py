import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# ==============================
# LOAD EMBEDDING MODEL
# ==============================
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# ==============================
# LOAD FAISS INDEX + TEXT DATA
# ==============================
index = faiss.read_index("faiss_index.bin")

with open("embedding_texts.json", "r", encoding="utf-8") as f:
    data = json.load(f)

texts = data["texts"]
metadata = data["metadata"]

# ==============================
# LOAD GENERATIVE LLM
# ==============================
generator = pipeline("text2text-generation", model="google/flan-t5-large")

# ==============================
# RETRIEVE CONTEXT FROM FAISS
# ==============================
def retrieve_context(question, k=3):
    question_embedding = embedding_model.encode([question])
    distances, indices = index.search(np.array(question_embedding), k)

    context_chunks = []
    sources = []

    for i in indices[0]:
        context_chunks.append(texts[i])
        sources.append(metadata[i]["source"])

    best_distance = float(distances[0][0])

    context = " ".join(context_chunks)
    return context, best_distance, sources


# ==============================
# RAG ANSWER FUNCTION
# ==============================
def rag_answer(question):
    context, best_distance, sources = retrieve_context(question)

    prompt = f"""
You are an intelligent enterprise knowledge assistant.

Answer the question using ONLY the information from the context below.
If the answer is not present in the context, respond:
"Information not found in the provided documents."

Provide a clear, complete, and professional answer.

Context:
{context}

Question: {question}
Answer:
"""

    result = generator(prompt, max_length=300)
    answer = result[0]["generated_text"].strip()

    # Convert retrieval distance to confidence score
    confidence = 1 / (1 + best_distance)

    return {
        "answer": answer,
        "confidence": confidence,
        "distance": best_distance,
        "sources": list(set(sources))
    }