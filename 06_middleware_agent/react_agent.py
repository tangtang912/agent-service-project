from langchain.agents import create_agent
from model_factory import chat_model
from utils.prompt_loader import load_system_prompt
from agent.tools.agent_tools import (rag_summarize, get_weather, get_user_id, get_user_location, get_current_month,fetch_external_data,fill_context_for_report)
from agent.tools.middleware import monitor_tool,log_before_model,report_prompt_switch


class ReactAgent:
  def __init__(self):
    self.agent = create_agent(
      model = chat_model,
      system_prompt = load_system_prompts(),
      tools = rag_summarize, get_weather, get_user_id, get_user_location, get_current_month,fetch_external_data,fill_context_for_report ,
      middleware = monitor_tool,log_before_model,report_prompt_switch,
    )

def execute_stream(self,query):
  input_dict = {
    "messages":[
      {"role":"user","content":query}
    ]
  }

for chunk in self.agent.stream(input_dict,stream_mode=values,context={"report":False}):
  lastest_message = chunk['message'][-1]
  if lastest_message.content:
    yeild lastest_message,content.strip()+"\n"

if __name__ == '__main__':
  agent =ReactAgent()
  for chunk in agent.execute_stream("生成我的使用报告")
  print(chunk,end="",flush=True)
