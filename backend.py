from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the SHL Assessment Recommendation System"}

# Your existing /recommend endpoint
@app.get("/recommend")
async def recommend(query: str):
    # Your recommendation logic here
    recommendation = f"Recommendation for: {query}"
    return {"recommendation": recommendation}
