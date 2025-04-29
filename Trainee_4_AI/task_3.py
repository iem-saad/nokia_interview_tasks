#*******************************************************
# NOKIA INTERVIEW TASK 3 CODE                          *
#                                                      *
# Author: Saad Abdullah                                *
# E-mail: iem.saad@hotmail.com                         *
# Created: 29 APR 2025                                 *
# Last modification: 29 APR 2025                       *
#******************************************************/
"""
This code implements a simple chat application using Streamlit and 
OpenAI's GPT-3.5-turbo and GPT-4 models.
"""

import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="")

st.set_page_config(page_title="Nokia-Task-GPT", layout="centered")
  
with st.sidebar:
    st.title("Settings")
    model = st.selectbox(
        "Select Model",
        ["gpt-3.5-turbo", "gpt-4"],
        index=0,
        key="openai_model"
    )

st.markdown("<h1 style='text-align: center;'>Nokia-Task-GPT</h1>", unsafe_allow_html=True)
st.divider()

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat history display
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        bubble_color = "#393E46" if message["role"] == "user" else "#222831"
        st.markdown(
            f"<div style='background-color: {bubble_color}; padding: 10px 15px; border-radius: 10px; margin-bottom: 10px;'>{message['content']}</div>",
            unsafe_allow_html=True
        )

# Chat input
prompt = st.chat_input("Type your message here...")

if prompt:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(
            f"<div style='background-color: #393E46; padding: 10px 15px; border-radius: 10px; margin-bottom: 10px;'>{prompt}</div>",
            unsafe_allow_html=True
        )

    # Assistant response
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
