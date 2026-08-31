# 课时 5：tools 工具开发

## 功能说明

本课时为 Agent 准备了一系列可调用的工具函数：

| 工具函数 | 功能 | 装饰器 |
| :--- | :--- | :--- |
| `rag_summarize` | 从向量库检索参考资料并生成总结 | `@tool` |
| `get_weather` | 获取指定城市天气 | `@tool` |
| `get_user_location` | 获取用户所在城市 | `@tool` |
| `get_user_id` | 获取用户ID | `@tool` |
| `get_current_month` | 获取当前月份 | `@tool` |
| `fetch_external_data` | 从外部CSV获取用户使用记录 | 无（内部辅助） |

## 文件结构
05_tools/
├── tools.py # 工具函数库（主程序）
├── model/
│ └── factory.py # 模型工厂（从课时3复制）
├── config/
│ ├── agent.yml # Agent 配置
│ ├── rag.yml # RAG 配置
│ ├── chroma.yml # Chroma 配置
│ └── prompts.yml # 提示词配置
├── prompts/
│ └── rag_summarize_prompt.txt # RAG 提示词模板
├── data/
│ └── external_data.csv # 外部用户数据
└── README.md # 本说明文档

## 依赖文件（需从前面课时复制）
- `rag_summarize_service.py`（课时4）
- `vector_store_service.py`（课时3）
- `config_handler.py`（课时2）
- `prompt_loader.py`（课时2）
- `path_tool.py`（课时1）
- `logger_handler.py`（课时1）
- `file_handler.py`（课时2）

## 运行测试
```bash
cd 05_tools
python tools.py
