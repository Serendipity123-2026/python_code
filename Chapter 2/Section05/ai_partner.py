# ai_partner.py
import random
from datetime import datetime

import streamlit as st

from config import (
    PAGE_TITLE,
    PAGE_ICON,
    INITIAL_SIDEBAR_STATE,
    AI_RESPONSES,
)
from session import (
    load_session,
    save_session,
    load_session_messages,
    delete_session,
)

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    initial_sidebar_state=INITIAL_SIDEBAR_STATE,
)


def generate_new_session_name():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


if "current_session" not in st.session_state:
    st.session_state.current_session = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "sessions" not in st.session_state:
    st.session_state.sessions = load_session()

with st.sidebar:
    st.title(f"{PAGE_ICON} {PAGE_TITLE}")
    st.caption("在这里，倾诉你的心声 🌿")
    st.divider()

    if st.button("✏️ 新建会话", use_container_width=True):
        if st.session_state.current_session:
            save_session(st.session_state.current_session, st.session_state.messages)
        new_name = generate_new_session_name()
        st.session_state.current_session = new_name
        st.session_state.messages = []
        save_session(new_name, [])
        st.session_state.sessions = load_session()
        st.rerun()

    st.subheader("历史会话")
    st.session_state.sessions = load_session()

    if not st.session_state.sessions:
        st.info("暂无历史会话，点击上方按钮开始新对话~")

    for session_name in st.session_state.sessions:
        col_a, col_b = st.columns([4, 1])
        with col_a:
            label = f"📁 {session_name}"
            if st.session_state.current_session == session_name:
                label = f"▶️ {session_name}"
            if st.button(label, key=f"session_{session_name}", use_container_width=True):
                if st.session_state.current_session:
                    save_session(st.session_state.current_session, st.session_state.messages)
                st.session_state.current_session = session_name
                st.session_state.messages = load_session_messages(session_name)
                st.rerun()
        with col_b:
            if st.button("🗑️", key=f"del_{session_name}"):
                delete_session(session_name)
                if st.session_state.current_session == session_name:
                    st.session_state.current_session = None
                    st.session_state.messages = []
                st.session_state.sessions = load_session()
                st.rerun()

st.title(f"{PAGE_ICON} {PAGE_TITLE}")
st.caption("你好，我是你的AI树洞。有什么想说的，都可以告诉我 🍃")

if not st.session_state.current_session:
    st.session_state.current_session = generate_new_session_name()
    save_session(st.session_state.current_session, [])
    st.session_state.sessions = load_session()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("在这里说说你的心事...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown("💭 正在倾听...")
        reply = random.choice(AI_RESPONSES)
        placeholder.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    save_session(st.session_state.current_session, st.session_state.messages)
