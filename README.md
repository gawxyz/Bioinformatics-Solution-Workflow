# 论文摘要生成器

这个项目是一个基于Python的论文摘要生成器，它可以从PubMed Central (PMC)获取论文全文，使用LLM-agent来生成论文信息和总结，并将结果保存到CSV文件和SQLite数据库中。

## 主要功能

1. 从PMC获取论文全文
2. 使用LangGraph构建的流程生成论文总结
3. 提取论文的关键信息，包括：
   - 文章ID（DOI, PMC, PMID）
   - 文章标题
   - 文章内容
   - 摘要描述
   - 功能
   - 主页
   - 关键词
   - 工具类型
   - 主题
4. 将提取的信息保存到`db`文件夹中的CSV文件和SQLite数据库
5. 提供详细的日志记录，同时输出到文件和控制台
6. 在处理多篇论文时显示进度信息

## 项目结构

```
paper-summary-generator/
├── src/
│   ├── paper_processor.py
│   └── utils/
│       ├── paper_summary.py
│       └── bridge_llm/
│           └── .env
├── db/
│   ├── paper_summaries.csv
│   └── paper_summaries.db
├── logs/
│   └── paper_processor_YYYYMMDD_HHMMSS.log
��── README.md
├── LICENSE
├── .gitignore
└── environment.yml
```

## 环境配置

### 使用 Conda 配置环境

1. 确保已安装 Conda。如果没有，请从 [Conda 官网](https://docs.conda.io/en/latest/miniconda.html) 下载并安装。

2. 克隆项目仓库：
   ```bash
   git clone https://github.com/your-username/paper-summary-generator.git
   cd paper-summary-generator
   ```

3. 使用 environment.yml 文件创建新的 Conda 环境：
   ```bash
   conda env create -f environment.yml
   ```

4. 激活环境：
   ```bash
   conda activate langgraph_paper_summary
   ```

### 配置环境变量

在 `src/utils/bridge_llm/.env` 文件中配置以下环境变量：

```
DOUBAO_MODEL_ID=your_entrypoint_id
ARK_API_KEY=your_ark_api_key
ARK_API_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
OLLAMA_BASE_URL1=http://your_ollama_url1:port
OLLAMA_BASE_URL2=http://your_ollama_url2:port
```

请确保将 `your_ark_api_key`、`your_ollama_url1` 和 `your_ollama_url2` 替换为实际的值。环境变量文件现在使用相对路径加载，无需手动指定完整路径。

## 使用方法

1. 确保已完成环境配置和依赖安装。
2. 在 `src/paper_processor.py` 的 `main` 函数中提供要处理的PMCID列表。
3. 运行 `paper_processor.py` 脚本：
   ```bash
   python src/paper_processor.py
   ```

## 输出

- `db/paper_summaries.csv`: 包含所有处理过的论文信息的CSV文件。
- `db/paper_summaries.db`: 包含所有处理过的论文信息的SQLite数据库。
- `logs/paper_processor_YYYYMMDD_HHMMSS.log`: 包含详细运行日志的文件。

## 注意事项

- 确保您有足够的权限访问PMC API并下载论文内容。
- 脚本会过滤掉一些与主题无关的部分（如方法、参考文献等），以减少token消耗。
- 日志信息会同时输出到控制台和日志文件，方便实时查看处理进度和调试。
- 处理多篇论文时，程序会显示当前处理进度，如"正在处理第 X/Y 篇论文"。
- 如果遇到任何问题，请检查控制台输出和日志文件以获取详细信息。

## 贡献

欢迎提交问题和拉取请求。对于重大更改，请先开issue讨论您想要更改的内容。

## 许可证

[MIT](https://choosealicense.com/licenses/mit/)