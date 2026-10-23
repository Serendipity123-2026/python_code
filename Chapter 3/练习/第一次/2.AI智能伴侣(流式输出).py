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
from openai import OpenAI
import os

# 大标题
st.title("AI智能伴侣")

# 连接 deepseekAPI
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# 系统提示词常量
SYSTEM_PROMPT = "你是一个活泼的女生"

# 创建一个用于存 用户输入信息和AI回复信息的列表
if "messages" not in st.session_state:
    st.session_state.messages = []

# 通过循环遍历 messages 列表
for message in st.session_state.messages:
    if message["role"] == "user":
        # 生成用户聊天气泡框
        with st.chat_message("user"):
            # 将 message字典中 content对应的值 的内容写入 用户聊天气泡框
            st.write(message["content"])
    if message["role"] == "assistant":
        # 生成AI聊天气泡框
        with st.chat_message("assistant"):
            # 将 message 字典中 content对应的值 的内容写入 AI聊天气泡框
            st.write(message["content"])


# # 侧边栏
# with st.sidebar:
#     # 新建会话按钮
#     if st.button(label="新建会话", width="stretch"):
#         pass
#     # 伴侣昵称定制
#     st.text_input(label="昵称")
#     # 伴侣性格定制
#     st.text_area(label="性格")

# 用户输入框
prompt = st.chat_input("请您输入问题")

# 判断用户是否输入了问题
if prompt:
    # 将用户输入的问题写入 用户聊天气泡框
    with st.chat_message("user"):
        st.write(prompt)
    # 将用户输入的内容以字典形式存入messages列表中 {"role": "user", "content": prompt}
    st.session_state.messages.append({"role": "user", "content": prompt})
    # 实现 AI伴侣会话功能
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            # 将 messages列表中的字典进行解包  实现上下文关联
            *st.session_state.messages,
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    # """
    #     "choices": [
    #     {
    #         "index": 0,
    #         "delta": {
    #             "content": "绝对",
    #             "reasoning_content": null
    #         },
    #         "logprobs": null,
    #         "finish_reason": null
    #     }
    # ]
    # """
    # 创建一个空白占位容器 让内容只在容器中输出  防止内容竖着输出
    response_message = st.empty()
    # 定义一个空的字符串 用于接收 流式输入的内容
    full_response = ""
    # 遍历数据包
    for chunk in response:
        # 判断数据包中是否存在内容  一般数据包中 choices[0].delta.content 为两个字符
        if chunk.choices[0].delta.content is not None:
            # 接收数据包中的内容
            response = chunk.choices[0].delta.content
            # 将数据包中的内容拼接起来
            full_response += response
            # 将 AI聊天气泡框中写入的内容添加到 response_message空容器中
            response_message.chat_message("assistant").write(full_response)

    # 将 AI的回答以字典的形式存入messages列表中 {"role": "assistant", "content": response.choices[0].message.content}
    st.session_state.messages.append({"role": "assistant", "content": full_response})


