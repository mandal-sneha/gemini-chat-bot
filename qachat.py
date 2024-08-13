from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

st.set_page_config(page_title="GEMINI CHAT BOT")

st.header("Gemini Chat Bot")

if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the Question")

if submit and input_text:
    response = get_gemini_response(input_text)
    st.session_state["chat_history"].append(("You", input_text))
    st.subheader("The response is: ")

    for chunk in response:
        st.write(chunk.text)
        st.session_state["chat_history"].append(("Bot", chunk.text))

st.subheader("Chat History")

for role, text in st.session_state["chat_history"]:
    st.write(f"{role} : {text}")
