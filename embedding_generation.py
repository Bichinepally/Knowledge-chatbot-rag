import os
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader

DATA_PATH = "source_docs"
CHUNK_SIZE = 500

print("🔹 Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

texts = []
metadata = []

def read_pdf(file_path):
    reader = PdfReader(file_path)
    content = ""
    for page in reader.pages:
        content += page.extract_text() + "\n"
    return content

print("🔹 Reading documents...")
for file in os.listdir(DATA_PATH):
    path = os.path.join(DATA_PATH, file)
    if file.endswith(".pdf"):
        text = read_pdf(path)
        for i in range(0, len(text), CHUNK_SIZE):
            chunk = text[i:i+CHUNK_SIZE]
            texts.append(chunk)
            metadata.append({"source": file})

print(f"🔹 Total chunks created: {len(texts)}")

print("🔹 Generating embeddings...")
embeddings = model.encode(texts)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

faiss.write_index(index, "faiss_index.bin")

with open("embedding_texts.json", "w", encoding="utf-8") as f:
    json.dump({"texts": texts, "metadata": metadata}, f)

print("✅ Embeddings + FAISS index saved successfully!")