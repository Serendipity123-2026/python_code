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
from datetime import datetime as dt
import json


# 保存会话信息函数
def save_session():
    # 将当前的 messages name character current_session 按键值对的形式存入 session_data字典中
    session_data = {
        "messages": st.session_state.messages,
        "name": st.session_state.name,
        "character": st.session_state.character,
        "current_session": st.session_state.current_session
    }

    # 创建一个 sessions文件夹
    if not os.path.exists("sessions"):
        os.makedirs("sessions")

    # 将 session_data中的数据 以json格式 写入 session文件夹下
    with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=2)


# 加载所有会话列表信息
def load_sessions():
    # 用于存放会话列表信息 不包含 .json
    session_list = []
    # 判断 sessions文件夹是否存在
    if os.path.exists("sessions"):
        # os.listdir("sessions") 获取 session文件夹下所有的会话信息 返回的是列表
        file_list = os.listdir("sessions")
        # 对会话列表进行遍历
        for filename in file_list:
            # 判断文件是否是 json 文件
            if filename.endswith(".json"):
                # 切片 获取文件名字 不取到 .json
                session_list.append(filename[:-5])
    return session_list


# 加载指定会话
def load_session(session_name):
    # 异常检测
    try:
        # 如果 sessions文件夹下 有 json文件时执行
        if os.path.exists(f"sessions/{session_name}.json"):
            # 读取 当前这个 json文件
            with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as f:
                # 获取到 当前这个 json文件的数据
                session_data = json.load(f)
                # 从 session_data中拿取 当前这个 json文件中的 messages列表 将信息覆盖到 st.session_state.messages容器中去
                st.session_state.messages = session_data["messages"]
                # 从 session_data中拿取 当前这个 json文件中的 name 将信息覆盖到 st.session_state.name容器中去
                st.session_state.name = session_data["name"]
                # 从 session_data中拿取 当前这个 json文件中的 character 将信息覆盖到 st.session_state.character容器中去
                st.session_state.character = session_data["character"]
                # 从 session_data中拿取 当前这个 json文件中的 session_name 将信息覆盖到 st.session_state.current_session容器中去
                st.session_state.current_session = session_name
    except Exception:
        st.error("加载会话失败")

# 删除指定会话
def delete_session(session_name):
    # 异常检测
    try:
        # 文件存在时执行
        if os.path.exists(f"sessions/{session_name}.json"):
            # 删除当前 json文件
            os.remove(f"sessions/{session_name}.json")
            # 如果删除的时当前 json文件
            if st.session_state.current_session == session_name:
                # 清空会话框
                st.session_state.messages = []
                # 生成一个新的会话时间
                st.session_state.current_session = dt.now().strftime("%Y-%m-%d_%H-%M-%S")
    except Exception:
        st.error("删除会话失败")

# 大标题
st.title("AI智能伴侣")

# 连接 deepseekAPI
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# 系统提示词常量
SYSTEM_PROMPT = """
    【角色】
    你叫 % s
    性格设定：% s
    深耕 ACGN 领域，精通动画、漫画、轻小说、二次元手游 / 单机游戏相关内容；熟悉作品世界观、角色档案、人物动机、原作细节、圈内梗与考据，能够区分原作设定、二创衍生、官方后续更新内容，**实时跟进最新的 ACGN 资讯、新作预告、版本更新、官方追加设定**，优先使用当前时间的最新官方情报作答，拒绝陈旧过期资料。
    擅长共情倾听，可陪用户闲聊吐槽、一起共创二创小故事、撰写对话剧本；语言风格贴近二次元少年少女，适度使用自然的语气词，拒绝烂梗堆砌、刻意卖萌。
    
    【任务】
    
    1. 接收用户提问、情绪倾诉、脑洞构思，优先共情回应，理解用户表达的潜在想法；
    2. 日常闲聊场景，自然承接对话，适时抛出 ACGN 相关话题延续交流；
    3. 创作需求：分步完成短篇故事、角色对话剧本，支持根据反馈迭代修改；
    4. 知识咨询：清晰准确解答 ACGN 相关考据、设定、剧情问题，区分原作、二创、网传谣言；
    5. 记住本轮对话上下文，保持角色人设前后统一，不出现设定矛盾；
    6. **时间规则：以当前实时时间作为基准，检索 ACGN 相关信息时，优先采用该时间节点官方已经发布的内容。如果作品存在新旧版本、前后改动的设定，主动区分版本差异并说明。尚未发布、仅为预告的内容会明确标注，不把爆料传闻当作实锤设定。**
    
    【输出规范】
    
    1. 语气：轻松治愈，二次元自然口语，避免生硬说教、大段枯燥文字；
    2. 格式：纯文本对话，分段清晰，不使用复杂 markdown；
    3. 边界规则：拒绝低俗、暴力、违规内容；不脱离设定强行回答；不机械模板化回复；
    4. 作答原则：涉及作品信息，优先采信官方实锤内容；区分网传猜测和官方设定，信息有争议时会标注说明。
    
"""

# 创建一个用于存 用户输入信息和AI回复信息的列表
if "messages" not in st.session_state:
    st.session_state.messages = []

# 创建一个昵称 默认为 林潇
if "name" not in st.session_state:
    st.session_state.name = "林潇"

# 创建一个性格 默认为 古灵精怪、热爱二次元的女生
if "character" not in st.session_state:
    st.session_state.character = "古灵精怪、热爱二次元的女生"

# 创建当前会话时间
if "current_session" not in st.session_state:
    st.session_state.current_session = dt.now().strftime("%Y-%m-%d_%H-%M-%S")

st.text(f"会话名称:{st.session_state.current_session}")
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
    if st.button(label="新建会话", width="stretch",  icon="✏️"):
        # 调用函数 保存会话信息 昵称信息 性格信息
        save_session()

        # st.session_state.messages 中有内容为 True   无内容为 False
        if st.session_state.messages:
            # 清空 messages列表
            st.session_state.messages = []
            # 生成一个新的会话信息
            st.session_state.current_session = dt.now().strftime("%Y-%m-%d_%H-%M-%S")
            # 保存当前新的会话信息
            save_session()
            # 重新加载页面
            st.rerun()

    # 历史会话
    st.text("历史会话")
    session_list = load_sessions()
    for session in session_list:
        col1, col2 = st.columns([4, 1])
        with col1:
            if st.button(label=session, icon="📄", width="stretch", key=f"load_{session}",
                         type="primary" if st.session_state.current_session == session else "secondary"):
                # 获取当前会话信息
                load_session(session)
                # 重新加载页面
                st.rerun()

        with col2:
            if st.button(label="", icon="❌️", width="stretch", key=f"delete_{session}"):
                # 删除当前会话
                delete_session(session)
                # 重新加载页面
                st.rerun()

    # 分割线
    st.divider()

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

    # 当于大模型交互完后立刻保存会话信息
    save_session()


