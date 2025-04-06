# import streamlit as st
# import requests

# st.title("SHL Assessment Recommendation System")

# query = st.text_area("Enter job description or query", height=150)

# if st.button("Get Recommendations"):
#     if not query.strip():
#         st.warning("Please enter a job description or query.")
#     else:
#         with st.spinner("Fetching results..."):
#             try:
#                 response = requests.get("http://127.0.0.1:8000/recommend", params={"query": query})
#                 response.raise_for_status()
#                 data = response.json()
#                 recommendation = data.get("recommendation", "No recommendation found.")
#                 st.success(f"**Recommendation**: {recommendation}")
#             except requests.exceptions.RequestException as e:
#                 st.error(f"An error occurred: {e}")
import streamlit as st
import requests
from io import StringIO

# --- Logo or Banner ---
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/SHL_logo.svg/512px-SHL_logo.svg.png", width=150)
st.markdown("<h1 style='color: #4CAF50;'>SHL Assessment Recommendation System</h1>", unsafe_allow_html=True)

# --- Sidebar Info ---
st.sidebar.title("About")
st.sidebar.info("""
This tool helps you get assessment recommendations based on a job description or title.  
It communicates with a FastAPI backend running locally.
""")

st.sidebar.markdown("---")
st.sidebar.write("✅ Developed by Narendra")

# --- Input Box ---
st.markdown("### 📝 Enter Job Description or Title")
query = st.text_area(label=" ", height=150, label_visibility="collapsed")

# --- Output and Download ---
if st.button("🔍 Get Recommendations"):
    with st.spinner("Fetching recommendation..."):
        try:
            response = requests.get("http://127.0.0.1:8000/recommend", params={"query": query})
            response.raise_for_status()
            data = response.json()
            recommendation = data.get("recommendation", "No recommendation found.")

            # --- Layout: 2 columns ---
            col1, col2 = st.columns([3, 1])
            with col1:
                st.success(f"💡 **Recommendation:** {recommendation}")
            with col2:
                # Downloadable .txt version
                buffer = StringIO()
                buffer.write(f"Job Query: {query}\nRecommendation: {recommendation}")
                st.download_button("📥 Download", buffer.getvalue(), file_name="recommendation.txt", mime="text/plain")

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Error: {e}")
