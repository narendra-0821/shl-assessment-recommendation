# SHL Assessment Recommendation System

This is a simple AI-powered system that suggests relevant SHL assessments based on job descriptions or queries.

## 💻 Tech Stack
- FastAPI (Backend)
- Streamlit (Frontend)
- Python

## 🚀 How to Run the Project

### 1. Clone or unzip the project folder


	cd shl_recommender

### Install dependencies

	pip install -r requirements.txt

##Run the FastAPI backend

	uvicorn main:app --reload
	The backend will run at: http://127.0.0.1:8000

###Run the Streamlit frontend
In another terminal:
	streamlit run app.py
	The frontend will open in your browser at: http://localhost:8501

 ####Example
##Input (in Streamlit):
	Software Developer
##Output:
	SHL Coding Simulation Assessment

