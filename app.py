import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage

st.title("Chatbot Audit & Recommandations")

openai_api_key = st.text_input("Entrez votre clé API OpenAI", type="password")

if openai_api_key:
    chat = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_input = st.text_input("Votre question :")

    if user_input:
        st.session_state.messages.append({"role": "human", "content": user_input})
        with st.chat_message("human"):
            st.write(user_input)

        response = chat([HumanMessage(content=user_input)])

        with st.chat_message("ai"):
            st.write(response.content)

        st.session_state.messages.append({"role": "ai", "content": response.content})
