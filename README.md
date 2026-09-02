# 🤖 Agent 智能体项目

> 面向消费者的智能客服系统 —— 提供全周期闭环机器人相关服务

---

## 🎯 项目概述

本项目是一个基于 **LangChain Agent** + **RAG** + **ReAct** 框架的智能客服系统，包含两大核心功能模块：

### 1️⃣ 智能问答服务
- 处理用户的产品咨询（功能、价格、对比等）
- 解决使用问题、故障排除、维护建议
- 基于 RAG 技术，从知识库检索信息并生成自然语言回答

### 2️⃣ 使用报告与优化建议
- 自动分析扫地机器人使用数据（清洁频率、耗材状态、错误记录）
- 生成个性化报告，提供优化建议（清洁计划调整、部件更换提醒）
- 支持用户主动查询或系统定期推送

---

## 🧩 技术架构

| 层级 | 技术 |
| :--- | :--- |
| **Web 界面** | Streamlit |
| **Agent 框架** | LangChain Agent + ReAct |
| **LLM 模型** | 通义千问 (ChatTongyi) |
| **嵌入模型** | text-embedding-v4 |
| **向量数据库** | Chroma |
| **RAG 引擎** | LangChain RAG 链路 |
| **日志监控** | Agent Middleware |

---

## 📂 项目结构
agent-service-project/
├── README.md
├── .gitignore
├── LICENSE
├── requirements.txt
│
├── 01_log_path_tools/ # 课时1：日志和路径工具
│ ├── logger_handler.py # 日志工具
│ └── path_tool.py # 路径工具
│
├── 02_config_file_prompt/ # 课时2：配置/文件/提示词
│ ├── config_handler.py # 配置管理
│ ├── file_handler.py # 文件处理工具
│ └── prompt_loader.py # 提示词加载器
│
├── 03_vector_store/ # 课时3：向量存储服务
│ ├── VectorStoreService.py # 向量存储服务
└── SetVectorStore.py # 向量存储配置
│
├── 04_rag_summarize/ # 课时4：RAG总结服务
│ ├── rag_service.py # RAG主服务
│ └── rag_summarize_service.py # RAG总结服务
│
├── 05_tools/ # 课时5：tools工具开发
│ ├── agent_tool.py # Agent工具定义
│ └── SetPromptTemplate.py # 提示词模板
│
├── 06_middleware_agent/ # 课时6：中间件和Agent创建
│ ├── react_agent.py # ReAct Agent实现
│ └── middleware.py # Agent中间件
│
├── 07_web_ui/ # 课时7：用户界面开发
│ ├── app.py # Streamlit主程序
│ └── pages/
├── chat.py # 智能问答页面
└── report.py # 报告分析页面
└── data/ # 运行时生成
├── knowledge/
├── chroma_db/
└── reports/

---

## 📚 学习路线

| 课时 | 文件夹 | 内容 | 核心知识点 |
| :---: | :--- | :--- | :--- |
| 01 | [01_log_path_tools](./01_log_path_tools) | 日志和路径工具 | `logging` 配置, `os.path` 处理 | ✅ 已完成 |
| 02 | [02_config_file_prompt](./02_config_file_prompt) | 配置/文件/提示词 | 配置加载, 文件读写, 提示词模板 |✅ 已完成 |
| 03 | [03_vector_store](./03_vector_store) | 向量存储服务 | Chroma 封装, 向量检索 |✅ 已完成 |
| 04 | [04_rag_summarize](./04_rag_summarize) | RAG总结服务 | RAG 链路, 文档总结 |✅ 已完成 |
| 05 | [05_tools](./05_tools) | tools工具开发 | `@tool` 装饰器, 工具定义 |✅ 已完成 |
| 06 | [06_middleware_agent](./06_middleware_agent) | 中间件和Agent创建 | Agent 生命周期, 中间件 |✅ 已完成 |
| 07 | [07_web_ui](./07_web_ui) | 用户界面开发 | Streamlit 多页面, 交互设计 |✅ 已完成 |

---

## 🚀 快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/你的用户名/agent-service-project.git
cd agent-service-project
### 2. 安装依赖
pip install -r requirements.txt
