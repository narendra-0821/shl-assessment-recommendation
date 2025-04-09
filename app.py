import streamlit as st
import requests

st.title("SHL Assessment Recommendation")

query = st.text_input("Enter role or job description")

if st.button("Get Recommendation") and query:
    try:
        response = requests.post("https://shl-backend-rbiy.onrender.com/recommend", json={"query": query})

        if response.status_code == 200:
            assessments = response.json().get("recommended_assessments", [])
            for a in assessments:
                st.success(f"Recommended: {a['description']}\nDuration: {a['duration']} min")
        else:
            st.error("Failed to get recommendation.")
    except Exception as e:
        st.error(f"Error: {e}")
