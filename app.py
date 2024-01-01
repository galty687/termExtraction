import streamlit as st
from openai import OpenAI
import os

openai_api_key = st.secrets["openai_api_key"]
cliet = OpenAI(openai_api_key)

st.title('术语提取')
st.write('这是一个文本提取系统，基于ChatGLM开发')

prompt = st.text_input("请输入术语提取提示词：", value="请提取术语：")

input_text=st.text_area("请输入需要提取的文本，注意长度需要少于500字：")

combined_input = f"{prompt}\n\n{input_text}"



def process_with_openai(text):
    try:
        # 使用 OpenAI 聊天模型进行处理
        response = client.chat.completion.create(
            model="gpt-3.5-turbo-16k",  # 模型名称
            messages=[
                {"role": "user", "content": text}
            ],
            max_tokens=8000  # 设置最大令牌数
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return str(e)

if st.button('提取术语'):
    with st.spinner('正在处理中，请稍候...'):



        if input_text:
            result = process_with_openai(combined_input)
            st.write(result)
        else:
            st.write("请输入一些文本。")

    st.success('处理完成！')    
