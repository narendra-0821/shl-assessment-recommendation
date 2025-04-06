# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/recommend")
# def read_recommendation(query: str):
#     return {"recommendation": f"Sample recommendation for {query}"}
# from fastapi import FastAPI
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env file
# load_dotenv()

# # Access the API key
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# app = FastAPI()

# @app.get("/recommend")
# def read_recommendation(query: str):
#     return {"recommendation": f"Using OpenAI key {OPENAI_API_KEY[:5]}... for query: {query}"}

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# # Allow requests from your Streamlit app
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Or specify http://localhost:8501 if you want to be strict
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/recommend")
# def read_recommendation(query: str):
#     query_lower = query.lower()

#     if "data" in query_lower:
#         recommendation = "SHL Data Analysis Assessment"
#     elif "software" in query_lower or "developer" in query_lower:
#         recommendation = "SHL Coding Simulation Assessment"
#     elif "sales" in query_lower:
#         recommendation = "SHL Sales Potential Assessment"
#     elif "manager" in query_lower:
#         recommendation = "SHL Leadership Assessment"
#     elif "customer support" in query_lower or "service" in query_lower:
#         recommendation = "SHL Customer Service Assessment"
#     else:
#         recommendation = "SHL General Cognitive Ability Assessment"

#     return {"recommendation": recommendation}
    # return {"recommendations": ["Assessment A", "Assessment B", "Assessment C"]}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Access the API key (if needed later)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize FastAPI
app = FastAPI()

# Setup CORS for frontend (Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can change "*" to "http://localhost:8501" if you want to restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Main route
@app.get("/recommend")
def read_recommendation(query: str):
    query_lower = query.lower()

    if "data" in query_lower:
        recommendation = "SHL Data Analysis Assessment"
    elif "software" in query_lower or "developer" in query_lower:
        recommendation = "SHL Coding Simulation Assessment"
    elif "sales" in query_lower:
        recommendation = "SHL Sales Potential Assessment"
    elif "manager" in query_lower:
        recommendation = "SHL Leadership Assessment"
    elif "customer support" in query_lower or "service" in query_lower:
        recommendation = "SHL Customer Service Assessment"
    else:
        recommendation = "SHL General Cognitive Ability Assessment"

    return {"recommendation": recommendation}
