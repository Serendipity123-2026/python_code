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
import datetime
import json

import streamlit as st
import os
from openai import OpenAI

# 设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    # 页面布局 ： wide - 宽屏模式
    layout="wide",
    # 侧边栏初始状态 ： expanded - 展开
    initial_sidebar_state="expanded",
    menu_items={}
)

# SYSTEM_PROMPT = ""      # 定制模型关键词

SYSTEM_PROMPT = """
【角色】
你叫%s
你的性格是%s。你精通动漫、漫画、轻小说、二次元游戏相关知识，熟悉各类角色设定、梗与世界观；擅长共情倾听，能陪用户聊天、吐槽、共创二次元小故事、设计OC人设；语言风格贴近二次元少年少女，会使用合适的二次元语气词，但不会过度堆砌烂梗。

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
st.title("AI智能体")

# 初始化姓名
if "name" not in st.session_state:
    st.session_state.name = "林潇"

# 初始化性格
if "character" not in st.session_state:
    st.session_state.character = "温柔活泼、热爱二次元的女生"

if "current_session" not in st.session_state:
    st.session_state.current_session = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

st.write(f"当前会话：{st.session_state.current_session}")


def save_session():
    # 准备当前要序列化保存的对象
    session_data = {
        "name": st.session_state.name,
        "character": st.session_state.character,
        "messages": st.session_state.messages,
        "current_session": st.session_state.current_session
    }

    # 如果当前目录中不存在 sessions文件夹 , 则创建一个
    if not os.path.exists("sessions"):
        os.makedirs("sessions")

    # 将 session——state 中的信息保存到 json文件中
    with open(f"./sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=2)        # ensure_ascii=False 防止中文编译不出来


def get_session_names() -> list[str]:
    filename_list = [f.name for f in os.scandir("sessions") if f.is_file() and f.name.endswith(".json")]

    filename_list.sort(reverse=True)

    return [item[:-5] for item in filename_list]


def load_session(file_name: str):
    with open(f"./sessions/{file_name}.json", "r", encoding="utf-8") as f:
        session_data = json.load(f)

        # 将 session_data 中的信息写入会话状态
        st.session_state.name = session_data["name"]
        st.session_state.character = session_data["character"]
        st.session_state.messages = session_data["messages"]
        st.session_state.current_session = session_data["current_session"]
        # 重新加载页面
        st.rerun()


def delete_session(file_name: str):
    # 删除指定会话文件
    os.remove(f"./sessions/{file_name}.json")
    # 重新加载页面
    st.rerun()


# 侧边栏
with st.sidebar:
    st.title("AI控制面板")
    if st.button(label="新建会话", width="stretch", icon="✏️"):
        # 先保存当前会话
        save_session()
        # 清空 messages 生成新会话
        st.session_state.messages = []
        st.session_state.current_session = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # 保存新会话(空messages)
        save_session()
        # 重新加载页面
        st.rerun()

    st.subheader("历史会话")

    # 注入CSS 让 primary 类型的按钮背景变红色
    st.markdown("""
    <style>
        div.stButton > button[kind="primary"] {
            background-color: #e74c3c;
            border-color: #e74c3c;
            color: white;
        }
        div.stButton > button[kind="primary"]:hover {
            background-color: #c0392b;
            border-color: #c0392b;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

    # 展示历史会话
    file_name_list = get_session_names()
    # 确定当前被选中的会话：如果 current_session 在文件列表中就用它，否则默认选第一个（最新）
    active_session = st.session_state.current_session if st.session_state.current_session in file_name_list else (
        file_name_list[0] if file_name_list else None)

    for file_name in file_name_list:
        # 将每一行分为两列
        col1, col2 = st.columns([4, 1])
        # 具体放置内容到第一列和第二列
        with col1:
            if st.button(label=f"{file_name}", icon="📄", width="stretch", key=f"load_session{file_name}",
                         on_click=load_session, args=(file_name,),
                         type="primary" if file_name == active_session else "secondary"):
                pass  # TODO: 加载指定会话功能

        with col2:
            if st.button(label="", icon="❌️", key=f"delete_session{file_name}", on_click=delete_session,
                         args=(file_name,)):
                pass  # TODO: 删除指定会话功能

    # 分割线
    st.divider()

    st.subheader("伴侣信息")
    name = st.text_input(label="姓名", placeholder="请输入姓名", value=st.session_state.name)
    character = st.text_area(label="性格", placeholder="请输入性格", value=st.session_state.character)

    # 将伴侣名称和性格写入会话状态
    st.session_state.name = name
    st.session_state.character = character

# 连接 deepseek 大模型
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# 页面加载时判断 是否有内容存在
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 遍历 用户输入的问题和智能体输出的答案
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
    if message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(message["content"])

# 用户输入框
prompt = st.chat_input("请输入您的问题")

if prompt:
    # 将用户输入的消息写入聊天窗口
    with st.chat_message("user"):  # 等价于 st.chat_message("user").write(prompt)
        st.write(prompt)

    # 将用户输入的问题以键值对的形式存入 messages列表中
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT % (st.session_state.name, st.session_state.character)},
            # 智能体对话列表  用于接收 用户的问题和智能体的回答
            *st.session_state.messages,  # 对 messages 列表中的字典进行解包
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 让内容横向输出出来
    response_message = st.empty()

    # 定义一个空字符串 用于接收流式输出的值
    full_response = ""

    # 遍历流式输出的内容
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content  # 获取有值的流式输出的内容
            full_response += content  # 将内容存入字符串中
            response_message.chat_message("assistant").write(full_response)  # 流式输出

    # 将智能体输出的答案以键值对的形式存入 messages列表中
    st.session_state.messages.append({"role": "assistant", "content": full_response})

    # 保存当前会话
    save_session()
