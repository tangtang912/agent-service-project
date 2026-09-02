import streamlit as st
from agent.react_agent import ReactAgent
from streamlit import session_state
import time

st.title("智扫通扫地机器人"）
st.divider()

if "agent" not in st.session_state:
  st.session_state["agent"] = ReactAgent()

if "message" not in st.session_state:
  st.session_state["message"] = []

for message in st.session_state["message"]:
  st.chat_message(message["role"]).write(message["content"])

  prompt = st.chat_input()

  if prompt:
    st.chat_message(user).write(prompt)
    st.session_state(message["role"].append("role":"user","content":prompt)

    response_message = []
    with st.spinner("智能客服思考中...")


    res_stream = st.session_state["agent"].execute_stream(prompt)

    def capture(generator,catch_list):
      for chunk in generator:
        catch_list.append(chunk)
        for char in chunk:
          time.sleep(0.01)
          yielf char

      st.chat_message(message["assistant"].write_stream(capture(res_stream,response_message)
      st.session_state(message["role"]).append({"role":"assiatant","content":response_message[-1]})
      st.rerun()
          
