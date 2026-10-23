import streamlit as st
from openai import OpenAI
import os

SYSTEM_PROMPT = "你是一个非常热爱二次元的AI"

# 大标题
st.title("AI智能伴侣")

# 小标题
st.write("当前会话：2026111211031")

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

prompt = st.chat_input("请输入您的问题")

if prompt:
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    st.chat_message("assistant").write(response.choices[0].message.content)


