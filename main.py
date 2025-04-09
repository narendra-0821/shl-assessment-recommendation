from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize FastAPI
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
def health():
    return {"status": "healthy"}

# Input format for POST
class RecommendRequest(BaseModel):
    query: str

# Output format
class Assessment(BaseModel):
    url: str
    adaptive_support: str
    description: str
    duration: int
    remote_support: str
    test_type: List[str]

class RecommendResponse(BaseModel):
    recommended_assessments: List[Assessment]

# Dummy recommendation logic
@app.post("/recommend", response_model=RecommendResponse)
def recommend(data: RecommendRequest):
    query = data.query.lower()

    if "data" in query:
        return {
            "recommended_assessments": [
                {
                    "url": "https://www.shl.com/solutions/products/product-catalog/view/data-analysis/",
                    "adaptive_support": "No",
                    "description": "Test that measures analytical skills and data interpretation.",
                    "duration": 25,
                    "remote_support": "Yes",
                    "test_type": ["Cognitive Ability"]
                }
            ]
        }
    elif "software" in query or "developer" in query:
        return {
            "recommended_assessments": [
                {
                    "url": "https://www.shl.com/solutions/products/product-catalog/view/python-new/",
                    "adaptive_support": "No",
                    "description": "Multi-choice test that measures Python knowledge.",
                    "duration": 11,
                    "remote_support": "Yes",
                    "test_type": ["Knowledge & Skills"]
                }
            ]
        }
    else:
        return {
            "recommended_assessments": [
                {
                    "url": "https://www.shl.com/solutions/products/product-catalog/view/general-cognitive/",
                    "adaptive_support": "Yes",
                    "description": "General cognitive assessment to evaluate problem-solving ability.",
                    "duration": 20,
                    "remote_support": "Yes",
                    "test_type": ["Cognitive Ability"]
                }
            ]
        }
