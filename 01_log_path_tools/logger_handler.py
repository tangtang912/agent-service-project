import os
import logging
from path_tool import get_abs_path
from datatime import datatime

# 日志保存的根目录
LOG_ROOT = get_abs_path("log")

# 确保日志的目录存在
os.makedirs(LOG_ROOT,exist_ok=True)

# 日志的格式配置
DEFAULT_LOGGING_FORMAT=logging.Format(
  %(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(messages)s
)

def get_logger(
  name = "agent",
  console_level = logging.INFO,
  file_level:int = logging.DEBUG,
  log_file = None,
)->logging.Logger:
  logger = logging.getlogger(name)
  logger.setLevel(logging.DEBUG)

  # 避免重复添加handler
  if logger.handlers:
    return logger
    
  # handler输出到控制台
  console_handler = logging.StreamHandler()
  console_handler.setLevel(console_level)
  console_handler.setFormat(DEFAULT_LOGGING_FORMAT)

  logger.add_Handler(console_handler)

  # handler输出到文件
  if not log_file:
    log_file = os.path.join(LOG_ROOT,f"{name}_{datatime.now().strftime('%Y%m%d').log")

  file_handler = logging.FileHandler(log_file,encoding="utf-8")
  file_handler.setLevel(file_level)
  file_handler.setFormatter(DEFAULT_LOGGING_FORMAT)

  logger.add_handler(file_handler)
    
  #快捷获取日志管理器
  logger = get_logger()

if __name__ == '__main__':
  logger.info('信息日志')
  logger.error('错误日志')
  logger.debug('调试日志‘）
  logger.warning('警告日志')
  

