# 课时 4：RAG 总结服务开发

## 功能说明

`RagSummarizeService` 是一个完整的 RAG 问答服务类：

1. **向量检索**：从 Chroma 向量库中检索与用户问题最相关的文档
2. **上下文构建**：将检索到的文档格式化为结构化的参考资料
3. **提示词填充**：将用户问题和参考资料填入提示词模板
4. **LLM 生成**：调用通义千问生成专业、准确的回答

## 文件结构
04_rag_summarize/
├── rag_summarize_service.py # RAG 总结服务（主程序）
├── model/
│ └── factory.py # 模型工厂（从课时3复制）
├── config/
│ └── prompts.yml # 提示词配置文件
├── prompts/
│ └── rag_summarize_prompt.txt # RAG 总结提示词模板
└── README.md # 本说明文档

## 依赖文件（需从前面课时复制）
- `vector_store_service.py`（课时3）
- `prompt_loader.py`（课时2）
- `config_handler.py`（课时2）
- `path_tool.py`（课时1）
- `logger_handler.py`（课时1）
- `file_handler.py`（课时2）

## 运行
```bash
cd 04_rag_summarize
python rag_summarize_service.py
