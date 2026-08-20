# 课时 1：日志和路径工具开发

## 功能说明
- **`path_tool.py`**：为整个工程提供统一的绝对路径处理
  - `get_project_root()`：获取项目根目录
  - `get_abs_path(relative_path)`：将相对路径转换为绝对路径
- **`logger_handler.py`**：提供统一的日志管理
  - 同时支持控制台输出和文件输出
  - 按日期自动命名日志文件
  - 支持自定义日志级别

## 文件结构
01_log_path_tools/
├── logger_handler.py # 日志管理器
├── path_tool.py # 路径工具
└── README.md # 本说明文档

## 核心知识点
- **`logging` 模块**：Python 标准日志库的使用
- **`os.path`**：路径处理
- **`os.makedirs`**：递归创建目录
- **`datetime`**：日期格式化（用于日志文件名）

## 运行测试
```bash
cd 01_log_path_tools
python logger_handler.py
