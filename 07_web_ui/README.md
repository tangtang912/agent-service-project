# 课时 7：用户界面开发

## 功能说明

基于 Streamlit 构建的智能客服 Web 界面：

- **聊天界面**：支持多轮对话
- **流式输出**：逐字显示 AI 回复（打字机效果）
- **会话保持**：使用 `session_state` 保持 Agent 实例和聊天历史
- **集成 Agent**：调用 `ReactAgent` 处理用户问题

## 文件结构
07_web_ui/
├── app.py # Streamlit 主程序
├── react_agent.py # ReactAgent（从课时6复制）
├── middleware.py # 中间件（从课时6复制）
├── tools.py # 工具函数（从课时5复制）
├── model/
│ └── factory.py # 模型工厂（从课时3复制）
├── config/
│ ├── agent.yml
│ ├── rag.yml
│ ├── chroma.yml
│ └── prompts.yml
├── prompts/
│ ├── system_prompt.txt
│ └── report_prompt.txt
└── README.md

## 依赖文件（需从前面课时复制）
- `react_agent.py`（课时6）
- `middleware.py`（课时6）
- `tools.py`（课时5）
- `rag_summarize_service.py`（课时4）
- `vector_store_service.py`（课时3）
- `config_handler.py`（课时2）
- `prompt_loader.py`（课时2）
- `path_tool.py`（课时1）
- `logger_handler.py`（课时1）
- `file_handler.py`（课时2）

## 运行
```bash
cd 07_web_ui
streamlit run app.py
