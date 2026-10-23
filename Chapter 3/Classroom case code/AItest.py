import streamlit as st

st.title("欢迎来阿到")

st.text("这是纯文本")

st.divider()

if st.button("点我"):
    st.image(
        r"E:\AI智能应用开发\code\The first stage\pythonProject\Chapter 3\Classroom case code\resources\images\img.png")

v = st.chat_input("请输入：")
if v:
    st.chat_message("user").write(v)

# 表格
data = {
    "姓名": ["王林", "李慕婉", "贝罗", "莫厉海", "石萧", "红蝶", "十三"],
    "学号": ["20230001", "20230002", "20230003", "20230004", "20230005", "20230006", "20230007"],
    "语文": [80, 90, 85, 70, 95, 90, 85],
    "数学": [87, 92, 87, 81, 92, 69, 83],
    "英语": [90, 85, 90, 95, 80, 85, 90],
    "总分": [257, 267, 262, 241, 267, 244, 258]
}

# 创建表格
st.table(data, border=True, width="stretch", height="content")

# 纯文本输入框
st.text_input(label="姓名", placeholder="请输入你的名字")
# 密码输入框
st.text_input(label="密码", placeholder="请输入你的密码", type="password")

# 单选框
st.radio(label="性别", options=["男", "女"])

# 复选框
st.checkbox(label="唱歌", value=True)
st.checkbox(label="跳舞")
st.checkbox(label="打球")

# 下拉框
st.selectbox("请选择城市", options=["上海", "广州", "杭州"])

# 滑动条
st.slider("滑动条", 0, 20)

# 数字输入框
st.number_input("数字输入", min_value=0)