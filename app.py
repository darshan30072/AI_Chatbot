import streamlit as st

from conversation import Conversation
from llm_client import stream_reply

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Chatbot")

# Session State
if "conversation" not in st.session_state:
    st.session_state.conversation = Conversation()

convo = st.session_state.conversation

# Sidebar
st.sidebar.title("Settings")

selected_model = st.sidebar.selectbox(
    "Choose Model",
    [
        "llama3.2",
        "mistral",
        "gemma",
        "deepseek-r1"
    ]
)

if st.sidebar.button("🗑 Clear Chat"):
    convo.clear_history()
    st.rerun()

# Display Messages
for msg in convo.history:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])

    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(msg["content"])

# Chat Input
prompt = st.chat_input("Type your message...")

if prompt:
    convo.add_user(prompt)

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()

        response_text = ""

        for chunk in stream_reply(
            convo.history,
            selected_model
        ):
            response_text += chunk
            placeholder.markdown(response_text)

        convo.add_ai(response_text)