# 课时 2：配置工具、文件工具和提示词加载

## 功能说明

### 1. 配置工具 (`config_handler.py`)
- 加载 YAML 格式的配置文件
- 支持 RAG、Chroma、Prompts、Agent 四种配置
- 使用 `yaml.FullLoader` 安全加载

### 2. 文件工具 (`file_handler.py`)
- `get_file_md5_hex()`：计算文件的 MD5 值（分片读取，支持大文件）
- `listdir_with_allowed_type()`：列出指定后缀的文件
- `pdf_loader()` / `txt_loader()`：PDF 和 TXT 文档加载

### 3. 提示词加载 (`prompt_loader.py`)
- `load_system_prompts()`：加载系统提示词
- `load_rag_prompts()`：加载 RAG 总结提示词
- `load_report_prompts()`：加载报告生成提示词

## 文件结构
02_config_file_prompt/
├── config_handler.py # YAML 配置加载
├── file_handler.py # 文件处理工具
├── prompt_loader.py # 提示词加载工具
└── README.md # 本说明文档

## 依赖关系
- `config_handler.py` → 依赖 `path_tool`（课时1）
- `file_handler.py` → 依赖 `logger_handler`（课时1）
- `prompt_loader.py` → 依赖 `config_handler`、`path_tool`、`logger_handler`

## 配置文件模板

需要在项目根目录创建 `config/` 文件夹，并添加以下 YAML 文件：

### `config/rag.yml`
```yaml
chat_model_name: qwen-max
embedding_model_name: text-embedding-v4
similarity_threshold: 3
