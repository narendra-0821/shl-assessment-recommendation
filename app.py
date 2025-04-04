import streamlit as st
import requests

st.title("SHL Assessment Recommendation System")

query = st.text_area("Enter job description or query")

if st.button("Get Recommendations"):
    with st.spinner("Fetching results..."):
        response = requests.get("https://your-backend-api-url.com/recommend", params={"query": query})
        if response.status_code == 200:
            results = response.json()["recommendations"]
            st.success(f"Top {len(results)} Results:")
            for i, r in enumerate(results, 1):
                st.markdown(f"**{i}. [{r['name']}]({r['url']})**")
                st.markdown(f"- Duration: {r['duration']}")
                st.markdown(f"- Test Type: {r['test_type']}")
                st.markdown(f"- Remote: {r['remote_testing']} | Adaptive/IRT: {r['adaptive_irt']}")
                st.markdown("---")
        else:
            st.error("Failed to fetch results.")