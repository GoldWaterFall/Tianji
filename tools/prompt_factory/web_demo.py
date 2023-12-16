import json
import openai
import streamlit as st
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = "写入key"
openai.api_base = "https://api.zyai.online/v1"

with open("src/prompt/gpt_prompt/prompt.json", "r", encoding="utf-8") as f:
    system_prompt = json.load(f)["test_system"]


def get_completion(prompt, model="gpt-3.5-turbo", temperature=0, messages=[]):
    """
    prompt: 对应的提示词
    model: 调用的模型，默认为 gpt-3.5-turbo(ChatGPT)
    """
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # 模型输出的温度系数，控制输出的随机程度
    )
    # 调用 OpenAI 的 ChatCompletion 接口
    return response.choices[0].message["content"]


with st.sidebar:
    st.markdown("## 人情世故-天机")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, step=0.01)

st.title("💬 Chatbot")
st.caption("🚀 A streamlit chatbot powered by SociaAI")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": system_prompt}]

for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = get_completion(
        prompt,
        model="gpt-3.5-turbo",
        temperature=temperature,
        messages=st.session_state["messages"],
    )
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)