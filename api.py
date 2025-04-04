from fastapi import FastAPI, Query
from pydantic import BaseModel
import faiss, json
from sentence_transformers import SentenceTransformer
import numpy as np

app = FastAPI()
model = SentenceTransformer('all-MiniLM-L6-v2')

index = faiss.read_index("faiss_index.bin")
with open("meta.json") as f:
    meta = json.load(f)

class QueryModel(BaseModel):
    query: str

@app.get("/recommend")
def recommend(query: str = Query(...)):
    embedding = model.encode([query])
    D, I = index.search(np.array(embedding), 10)

    results = []
    for idx in I[0]:
        item = meta[idx]
        results.append({
            "name": item['name'],
            "url": item['url'],
            "remote_testing": item['remote_testing'],
            "adaptive_irt": item['adaptive_irt'],
            "duration": item['duration'],
            "test_type": item['test_type']
        })

    return {"query": query, "recommendations": results}