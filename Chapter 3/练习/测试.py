"""
deepseek调用代码

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)

"""

import streamlit as st
import os
from openai import OpenAI
from datetime import datetime as dt
import json


def save_session():
    session_data = {
        "name": st.session_state.name,
        "character": st.session_state.character,
        "messages": st.session_state.messages,
        "current_session": st.session_state.current_session
    }

    if not os.path.exists("sessions"):
        os.makedirs("sessions")

    with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=2)


def load_sessions():
    pass

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

SYSTEM_PROMPT = """
    昵称：%s
    性格：%s
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

if "name" not in st.session_state:
    st.session_state.name = "alice"

if "character" not in st.session_state:
    st.session_state.character = "活泼可爱的女生"

if "current_session" not in st.session_state:
    st.session_state.current_session = dt.now().strftime("%Y-%m-%d_%H-%M-%S")

st.title("AI智能体")

for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            # 用键 掉 对应的值
            st.write(message["content"])
    if message["role"] == "assistant":
        with st.chat_message("assistant"):
            # 用键 掉 对应的值
            st.write(message["content"])

with st.sidebar:
    if st.button(label="新建会话", width="stretch",  icon="✏️"):
        save_session()



    st.text("历史会话")



    st.divider()

    st.subheader("伴侣信息")
    name = st.text_input(label="昵称", value=st.session_state.name)
    if st.session_state.name:
        st.session_state.name = name
    character = st.text_area(label="性格", value=st.session_state.character)
    if st.session_state.character:
        st.session_state.character = character

prompt = st.chat_input("请输入您的问题")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT % (st.session_state.name, st.session_state.character)},
            *st.session_state.messages,
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    response_message = st.empty()

    full_response = ""

    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            response = chunk.choices[0].delta.content
            full_response += response

            response_message.chat_message("assistant").write(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
