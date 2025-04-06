import streamlit as st
import requests

st.title("SHL Assessment Recommendation")

query = st.text_input("Enter role or job description")

if st.button("Get Recommendation") and query:
    try:
        response = requests.get(
            "https://shl-backend-rbiy.onrender.com/recommend",
            params={"query": query}
        )
        if response.status_code == 200:
            recommendation = response.json().get("recommendation")
            st.success(f"Recommended Assessment: {recommendation}")
        else:
            st.error("Failed to get recommendation.")
    except Exception as e:
        st.error(f"Error: {e}")
