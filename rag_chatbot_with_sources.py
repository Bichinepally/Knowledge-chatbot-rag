import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# Load models
embed_model = SentenceTransformer("all-MiniLM-L6-v2")
qa_model = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)

# Load FAISS index
index = faiss.read_index("kg_embeddings.faiss")

# Load chunks + metadata
with open("embedding_texts.json", "r", encoding="utf-8") as f:
    documents = json.load(f)

def retrieve_chunks(question, top_k=3):
    q_emb = embed_model.encode([question]).astype("float32")
    _, indices = index.search(q_emb, top_k)

    chunks = []
    for i in indices[0]:
        chunks.append(documents[i])

    return chunks

def chatbot():
    print("🤖 RAG Chatbot (type 'exit' to stop)\n")

    while True:
        question = input("You: ")
        if question.lower() == "exit":
            break

        chunks = retrieve_chunks(question)

        context = " ".join([c["text"] for c in chunks])

        answer = qa_model(
            question=question,
            context=context
        )["answer"]

        print("\n🤖 Answer:", answer)
        print("\n📄 Sources:")

        for c in chunks:
            meta = c["metadata"]
            print(
                f"- PDF: {meta['source']}, "
                f"Page: {meta.get('page','N/A')}, "
                f"Chunk ID: {meta.get('chunk_id','N/A')}"
            )

        print("\n" + "-"*50)

if __name__ == "__main__":
    chatbot()