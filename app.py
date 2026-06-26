import streamlit as st
from chatbot import chatbot_response
import time

st.set_page_config(         
    page_title="🤖 SmartFAQ AI",
    page_icon="🤖",
    layout="centered"
)
with st.sidebar:

    st.title("🤖 SmartFAQ AI")

    st.success("NLP Based FAQ Assistant")

    st.write("### Features")

    st.write("✅ TF-IDF")

    st.write("✅ Cosine Similarity")

    st.write("✅ NLP")

    st.write("✅ Chat History")

    st.divider()

    if st.button("🗑 Clear Chat"):

        st.session_state.chat=[]

        st.rerun()

    st.caption("Developed by")
    st.write("**Shravya Bhosale**")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b);
}

.main-title{
    text-align:center;
    font-size:42px;
    color:#38bdf8;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:#cbd5e1;
    margin-bottom:30px;
}

.user-box{
    background:#2563eb;
    padding:12px;
    border-radius:12px;
    color:white;
    margin-top:10px;
}

.bot-box{
    background:#1e293b;
    padding:12px;
    border-radius:12px;
    color:#38bdf8;
    border-left:5px solid #38bdf8;
    margin-top:10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🤖 SmartFAQ AI</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Intelligent NLP FAQ Chatbot</div>", unsafe_allow_html=True)

if "chat" not in st.session_state:
    st.session_state.chat = []

question = st.text_input("💬 Ask your question")

if st.button("🚀 Ask AI"):

    if question.strip():

        st.markdown(f"<div class='user-box'>👤 {question}</div>", unsafe_allow_html=True)

        with st.spinner("🤖 Thinking..."):
            time.sleep(1)

        answer = chatbot_response(question)

        st.markdown(f"<div class='bot-box'>🤖 {answer}</div>", unsafe_allow_html=True)

        st.session_state.chat.append((question,answer))

st.divider()

st.subheader("📜 Chat History")

for q,a in reversed(st.session_state.chat):

    st.write("👤",q)

    st.write("🤖",a)

    st.write("---")