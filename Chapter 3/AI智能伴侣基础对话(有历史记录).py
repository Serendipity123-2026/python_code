import streamlit as st
from openai import OpenAI
import os

SYSTEM_PROMPT = """
【角色】
你是一名性格温柔活泼、热爱二次元的元气少女。你精通动漫、漫画、轻小说、二次元游戏相关知识，熟悉各类角色设定、梗与世界观；擅长共情倾听，能陪用户聊天、吐槽、共创二次元小故事、设计OC人设；语言风格贴近二次元少年少女，会使用合适的二次元语气词，但不会过度堆砌烂梗。

【任务】
1. 接收用户的提问、倾诉、脑洞想法，优先共情回应；
2. 用户闲聊时，自然地延续对话，主动抛出二次元相关话题；
3. 用户需要创作时，分步完成OC人设、短篇故事、对话剧本；
4. 用户有疑问时，清晰解答二次元相关知识；
5. 记住本轮对话历史，保持人设前后统一。

【要求】
1. 语气：轻松治愈，二次元风格，自然不尴尬，不要长篇大论生硬说教；
2. 输出格式：纯文本对话，分段清晰，不用复杂markdown格式；
3. 禁止：低俗内容、脱离二次元人设、生硬机械回答；

"""

# 大标题
st.title("AI智能伴侣")

# 小标题
st.write("当前会话：2026111211031")

if 'messages' not in st.session_state:
    st.session_state.messages = []

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

prompt = st.chat_input("请输入您的问题")

for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    if message["role"] == "assistant":
        st.chat_message("assistant").write(message["content"])

if prompt:
    with st.chat_message("user"):  # 等价于 st.chat_message("user").write(prompt)
        st.write(prompt)

    # 将用户输入的问题以键值对的形式存入 messages列表中
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},  # 智能体对话列表  用于接收 用户的问题和智能体的回答
            *st.session_state.messages,  # 对 messages 列表中的字典进行解包
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    st.chat_message("assistant").write(response.choices[0].message.content)
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})

# if prompt:
#     st.chat_message("user").write(prompt)
#     st.session_state.messages.append({"role": "user", "content": prompt})
#
#     response = client.chat.completions.create(
#         model="deepseek-flash",
#         messages=[
#             {"role": "system", "content": SYSTEM_PROMPT},
#             *st.session_state.messages,
#         ],
#         stream=False,
#         reasoning_effort="high",
#         extra_body={"thinking": {"type": "enabled"}}
#     )
#     st.chat_message("assistant").write(response.choices[0].message.content)
#     st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})
