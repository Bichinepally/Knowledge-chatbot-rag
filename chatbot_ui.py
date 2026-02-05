import streamlit as st
from rag_pipeline import rag_answer

st.set_page_config(layout="wide")
st.title("🧠 Knowledge Chatbot")

# ==============================
# SESSION STATE
# ==============================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "last_score" not in st.session_state:
    st.session_state.last_score = None
    st.session_state.last_distance = None
    st.session_state.last_sources = None

# ==============================
# LAYOUT
# ==============================

col1, col2 = st.columns([3, 1])

# ==============================
# 💬 LEFT SIDE — CHATBOT
# ==============================

with col1:
    st.header("💬 Chatbot")

    user_question = st.text_input("Ask a question")

    if st.button("Ask") and user_question:
        response = rag_answer(user_question)

        st.session_state.chat_history.append(
            (user_question, response["answer"])
        )

        st.session_state.last_score = response["confidence"]
        st.session_state.last_distance = response["distance"]
        st.session_state.last_sources = response["sources"]

    for q, a in reversed(st.session_state.chat_history):
        st.markdown(f"**🧑 You:** {q}")
        st.markdown(f"**🤖 AI:** {a}")
        st.markdown("---")

# ==============================
# 📊 RIGHT SIDE — ACCURACY PANEL
# ==============================

with col2:
    st.subheader("📊 Answer Accuracy Panel")

    if st.session_state.last_score is not None:
        st.metric(
            "Model Confidence",
            f"{st.session_state.last_score * 100:.1f}%"
        )

        st.write("**Retrieval Distance (Lower = Better):**")
        st.write(st.session_state.last_distance)

        st.write("**Sources Used:**")
        for src in st.session_state.last_sources:
            st.write(f"📄 {src}")
    else:
        st.info("Ask a question to see accuracy metrics.")