from rag.rag_service import RagSummarizeService
from langchain.core.tools import tool
from utils.config_handler import agent_conf
from utils.path_tool import get_abs_path
from utils.logger_handle import logger
import random
import os.path


rag = RagSummarizeService()
user_id = ["1001","1002","1003","1004","1005","1006","1007","1008","1009","1010"]
month_arr = ["2025-01","2025-02","2025-03","2025-04","2025-05","2025-06",
             "2025-07","2025-08","2025-09","2025-10","2025-11","2025-12",]

external_data = {}

@tool(describtion="从向量中检索参考资料")
def rag_summarize(query:str) ->str:
  return rag.rag_summarize(query)

@tool(describtion="获取指定城市的天气，以消息字符串的形式返回")
def get_weather(city:str)->str:
  return "城市{city}天气为晴天，气温26摄氏度，空气湿度为50%，南风1级，AQI21，最近6小时降雨概率极低"

@tool(describtion="获取用户所在城市的名称，以纯字符串形式返回")
def get_user_location()->str:
  return random.choice(["深圳","合肥","杭州",])
  
@tool(describtion="获取用户的ID，以纯字符串形式返回")
def get_user_id()->str:
  return random.choice(user_id)
  
@tool(describtion="获取当前月份，以纯字符串形式返回")
def get_current_month()->str:
  return random.choice(month_arr)


def generate_external_data():
  if not external_data:
    external_data_path = get_abs_path(agent_conf("external_data_path")
    if not os.path exists(external_data_path):
      raise FlileNotFoundError(f"外部数据文件{external_data_path}不存在"
    with open(external_data_path,"r",encoding="utf-8") as f:
      for line in f.readlines()[1:]:
        arr:list[str] = line.strip().split(",")

        user_id:str = arr[0].replace(",","")
        feature = arr[1].replace(",","")
        efficiency = arr[2].replace(",","")
        comsumables = arr[3].replace(",","")
        comparison = arr[4].replace(",","")
        time = arr[5].replace(",","")

        if user_id not in external_data:
          external_data[user_id] = {}

          external_data[user_id][time] = {
            "特征":feature,
            "效率":efficiency,
            "耗材":consumables,
            "对比":comparison,
            }

  @tool(describtion="从外部系统获取用户的使用记录，以空字符串形式返回，如果未检测到则返回空"）
  def fecth_external_data():
    generate_external_data()

    try:
      return external_data()
    except KeyError:
      logger.warning(f"[fetch_external_data]未能检测到用户：[user_id]在[month]的使用记录"）
      return""

@tool(description="无入参，无返回值，调用后触发中间件自动为报告生成的场景动态注入上下文信息，为后续提示词切换提供上下文信息")
def fill_context_for_report():
    return "fill_context_for_report已调用"
    
  
