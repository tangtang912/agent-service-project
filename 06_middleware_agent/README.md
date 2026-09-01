# 课时 6：中间件和 Agent 创建

## 功能说明

本课时创建了完整的 ReAct Agent，并集成了三个核心中间件：

| 中间件 | 类型 | 功能 |
| :--- | :--- | :--- |
| `monitor_tool` | `@wrap_tool_call` | 监控工具调用，记录日志，设置报告标志 |
| `log_before_model` | `@before_model` | 模型调用前记录消息数量和内容 |
| `report_prompt_switch` | `@dynamic_prompt` | 根据上下文动态切换提示词 |

## 动态提示词切换流程
用户请求"生成我的使用报告"
↓
Agent 调用 fill_context_for_report()
↓
monitor_tool 检测到该工具调用
↓
设置 runtime.context["report"] = True
↓
report_prompt_switch 检测到 report=True
↓
加载 report_prompt.txt 替代 system_prompt.txt
↓
Agent 使用报告提示词生成回答

## 文件结构
06_middleware_agent/
├── react_agent.py # Agent 主程序
├── middleware.py # 中间件模块
├── model/
│ └── factory.py # 模型工厂（从课时3复制）
├── config/
│ ├── agent.yml # Agent 配置
│ ├── rag.yml # RAG 配置
│ └── prompts.yml # 提示词配置
├── prompts/
│ ├── system_prompt.txt # 系统提示词（默认）
│ └── report_prompt.txt # 报告提示词（动态切换）
└── README.md

## 依赖文件（需从前面课时复制）
- `tools.py`（课时5）
- `rag_summarize_service.py`（课时4）
- `vector_store_service.py`（课时3）
- `config_handler.py`（课时2）
- `prompt_loader.py`（课时2）
- `path_tool.py`（课时1）
- `logger_handler.py`（课时1）

## 运行测试
```bash
cd 06_middleware_agent
python react_agent.py
