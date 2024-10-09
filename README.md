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

## 项目结构
.
├── src/
│ ├── paper_processor.py
│ └── utils/
│ └── paper_summary.py
├── db/
│ ├── paper_summaries.csv
│ └── paper_summaries.db
└── README.md

## 使用方法

1. 确保已安装所有必要的依赖项。
2. 在`main`函数中提供要处理的PMCID列表。
3. 运行`paper_processor.py`脚本：

## 依赖项

- requests
- sqlite3
- csv
- json
- typing
- langgraph

安装依赖：
```bash
pip install requests langgraph
```

## 依赖项

- requests
- sqlite3
- csv
- json
- typing
- langgraph


## 输出

- `db/paper_summaries.csv`: 包含所有处理过的论文信息的CSV文件。
- `db/paper_summaries.db`: 包含所有处理过的论文信息的SQLite数据库。

## 注意事项

- 确保您有足够的权限访问PMC API并下载论文内容。
- 脚本会过滤掉一些与主题无关的部分（如方法、参考文献等），以减少token消耗。
- 如果遇到任何问题，请检查控制台输出以获取错误信息。

## 贡献

欢迎提交问题和拉取请求。对于重大更改，请先开issue讨论您想要更改的内容。

## 许可证

[MIT](https://choosealicense.com/licenses/mit/)