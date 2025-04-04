import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def create_index():
    with open("assessments.json") as f:
        data = json.load(f)

    texts = [item['description'] for item in data]
    embeddings = model.encode(texts, show_progress_bar=True)

    index = faiss.IndexFlatL2(embeddings[0].shape[0])
    index.add(np.array(embeddings))

    faiss.write_index(index, "faiss_index.bin")

    with open("meta.json", "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    create_index()