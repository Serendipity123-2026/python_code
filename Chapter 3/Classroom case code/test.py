# import os
# from openai import OpenAI
#
# client = OpenAI(
#     api_key=os.environ.get('DEEPSEEK_API_KEY'),
#     base_url="https://api.deepseek.com")
# messages = [{"role": "system", "content": "你是一个非常热爱二次元的AI"}]
#
# while True:
#     user_input = input("用户请输入：")
#     messages.append({"role": "user", "content": user_input})
#     response = client.chat.completions.create(
#         model="deepseek-flash",
#         messages=messages,
#         stream=False,
#         reasoning_effort="high",
#         extra_body={"thinking": {"type": "enabled"}}
#     )
#     messages.append({"role": "assistant", "content": response.choices[0].message.content})
#     print(response.choices[0].message.content)




# import streamlit as st
#
# st.title("AI对话Demo")
# user_input = st.chat_input("请提问")
# if user_input:
#     st.write(f"用户：{user_input}")
#     st.write(f"AI回复：这是回答")
#     # st.audio(audio_bytes, autoplay=True)


