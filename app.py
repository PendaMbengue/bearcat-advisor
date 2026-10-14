import streamlit as st
import requests

API_URL = "https://r3byumdlj2.execute-api.us-east-1.amazonaws.com/ask"

st.set_page_config(
    page_title="Bearcat Advisor",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 Bearcat Advisor")
st.subheader("Your guide to registration at Saint Vincent College")

st.write("Ask questions about Computer Science, Information Systems, and Cybersecurity courses.")

question = st.text_area(
    "What would you like to know?",
    placeholder="Example: What courses do I need for Cybersecurity?"
)

if st.button("Ask Bearcat Advisor"):
    if not question.strip():
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Bearcat Advisor is thinking..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=60
                )

                data = response.json()

                if response.ok:
                    st.markdown("### Bearcat Advisor's Answer")
                    st.write(data.get("answer", "No answer was returned."))
                else:
                    st.error(data.get("error", "Something went wrong."))

            except requests.RequestException as error:
                st.error(f"Could not connect to Bearcat Advisor: {error}")