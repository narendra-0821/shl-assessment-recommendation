if st.button("Get Recommendation") and query:
    try:
        response = requests.post(
            "https://shl-backend-rbiy.onrender.com/recommend",
            json={"query": query},
            timeout=10
        )

        st.write("Status Code:", response.status_code)
        st.write("Response:", response.text)

        if response.status_code == 200:
            assessments = response.json().get("recommended_assessments", [])
            for a in assessments:
                st.success(f"Recommended: {a['description']}\nDuration: {a['duration']} min")
        else:
            st.error("Failed to get recommendation.")
    except Exception as e:
        st.error(f"Error: {e}")
