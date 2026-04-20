import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# -----------------------------
# LOAD ENV
# -----------------------------
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# -----------------------------
# UI
# -----------------------------
st.set_page_config(page_title="AI Mental Model Generator", layout="wide")
st.title("🧠 AI Mental Model Generator")
st.caption("Learn how to think, not just what to think")

# -----------------------------
# SESSION STATE
# -----------------------------
if "saved_models" not in st.session_state:
    st.session_state.saved_models = []

# -----------------------------
# INPUT
# -----------------------------
topic = st.text_input("🔍 Enter a topic (e.g., money, career, decision-making)")

mode = st.selectbox("⚙️ Mode", ["Standard", "Simple Explanation"])

# -----------------------------
# GENERATE MODELS
# -----------------------------
if st.button("🚀 Generate Mental Models"):

    if not topic.strip():
        st.warning("⚠️ Please enter a topic")
        st.stop()

    with st.spinner("🧠 Thinking deeply..."):

        prompt = f"""
        Generate 4 powerful mental models for the topic: {topic}

        For each model include:
        - Name
        - Explanation
        - Real-life example
        - When to use it

        Keep it {mode.lower()}.
        """

        response = model.generate_content(prompt)
        output = response.text

        st.subheader("📊 Mental Models")
        st.write(output)

        if st.button("💾 Save Models"):
            st.session_state.saved_models.append(output)

# -----------------------------
# DECISION FRAMEWORK
# -----------------------------
st.subheader("⚖️ Apply Mental Models")

problem = st.text_area("Describe your problem")

if st.button("🧠 Analyze Problem"):
    if problem.strip():
        prompt = f"""
        Apply relevant mental models to solve this problem:

        {problem}

        Provide:
        - 2-3 mental models
        - How they apply
        - Final decision advice
        """

        response = model.generate_content(prompt)
        st.write(response.text)

# -----------------------------
# SAVED MODELS
# -----------------------------
if st.session_state.saved_models:
    st.subheader("💾 Saved Models")
    for m in st.session_state.saved_models:
        st.info(m)