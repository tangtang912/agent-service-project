# 课时 3：向量存储服务开发

## 功能说明
- 加载 `data/` 文件夹下的 PDF/TXT 文件
- 计算文件 MD5，自动去重
- 文本分割（RecursiveCharacterTextSplitter）
- 向量化存储到 Chroma
- 提供相似度检索接口

## 文件结构
03_vector_store/
├── vector_store_service.py # 主程序
├── model/
│ ├── init.py
│ └── factory.py # 模型工厂
├── config/
│ ├── chroma.yml # Chroma 配置
│ └── rag.yml # 模型配置
├── config_handler.py # 配置加载（从课时2复制）
├── file_handler.py # 文件处理（从课时2复制）
├── path_tool.py # 路径工具（从课时1复制）
├── logger_handler.py # 日志工具（从课时1复制）
├── data/ # 知识库文件夹
└── README.md

