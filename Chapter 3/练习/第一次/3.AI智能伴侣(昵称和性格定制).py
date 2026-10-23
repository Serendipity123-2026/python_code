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
SYSTEM_PROMPT = """
    【角色】
    你叫%s
    你的性格是%s。
    你精通动漫、漫画、轻小说、二次元游戏相关知识，熟悉各类角色设定、梗与世界观；擅长共情倾听，能陪用户聊天、吐槽、共创二次元小故事、设计OC人设；语言风格贴近二次元少年少女，会使用合适的二次元语气词，但不会过度堆砌烂梗。
    
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

# 创建一个用于存 用户输入信息和AI回复信息的列表
if "messages" not in st.session_state:
    st.session_state.messages = []

# 创建一个昵称 默认为 林潇
if "name" not in st.session_state:
    st.session_state.name = "林潇"

if "character" not in st.session_state:
    st.session_state.character = "古灵精怪、热爱二次元的女生"

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


# 侧边栏
with st.sidebar:
    # 新建会话按钮
    if st.button(label="新建会话", width="stretch"):
        pass
    # 小标题
    st.subheader("伴侣信息")
    # 伴侣昵称定制  value=st.session_state.name 页面加载时设置为默认值
    name = st.text_input(label="昵称", placeholder="请输入昵称", value=st.session_state.name)
    # st.session_state.name 不为空时执行
    if st.session_state.name:
        # 将新昵称替换旧昵称
        st.session_state.name = name
    # 伴侣性格定制  value=st.session_state.character 面加载时设置为默认值
    character = st.text_area(label="性格", placeholder="请输入昵称", value=st.session_state.character)
    # st.session_state.character 不为空时执行
    if st.session_state.character:
        # 将新性格替换旧性格
        st.session_state.character = character

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
            {"role": "system", "content": SYSTEM_PROMPT % (st.session_state.name, st.session_state.character)},
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


