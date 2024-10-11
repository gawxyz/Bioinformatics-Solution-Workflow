import requests
import json
from typing import List, Dict, Any
import csv
import sqlite3
import os
from utils.paper_summary import process_paper
import logging
from datetime import datetime

# 设置日志
def setup_logging():
    log_dir = '../logs'
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f'paper_processor_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
    
    # 创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # 创建文件处理器
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    
    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # 创建格式器
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # 将处理器添加到logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# 在文件开头调用此函数
setup_logging()

def get_paper_from_pmc(pmcid: str) -> Dict[str, Any]:
    logging.info(f"正在获取PMCID为{pmcid}的论文...")
    url = f"https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC{pmcid}/ascii"
    response = requests.get(url)
    if response.status_code == 200:
        logging.info(f"成功获取PMCID为{pmcid}的论文")
        return response.json()
    else:
        error_msg = f"获取PMCID为{pmcid}的论文失败"
        logging.error(error_msg)
        raise Exception(error_msg)

def extract_full_text(paper_info: Dict[str, Any]) -> str:
    full_text = ""
    for document in paper_info[0].get("documents", []):
        for passage in document.get("passages", []):
            full_text += passage.get("text", "") + "\n"
    return full_text.strip()

def extract_full_text_filtered(paper_info: Dict[str, Any]) -> str:
    """
    提取论文各部分的文本 去除和主题无关部分 减少token消耗。如 METHODS,REF,SUPPL,DISCUSS,ACK_FUND等   
    """
    # paper_info[0]['documents'][0]['passages']

    sections = {}
    for passage in paper_info[0]['documents'][0]['passages']:
        section_type = passage['infons'].get('section_type')
        if section_type:
            if section_type not in sections:
                sections[section_type] = passage['text']
            else:
                sections[section_type] += '\n' + passage['text']
    sections_filtered = {k: v for k, v in sections.items() if k not in ['METHODS', 'REF','ACK_FUND']}
    # 将 sections 中的所有值拼接成一个字符串    
    full_text_filtered = '\n'.join(sections_filtered.values())
    return full_text_filtered.strip()

def extract_metadata(paper_info: Dict[str, Any]) -> Dict[str, str]:
    metadata = {}
    for document in paper_info[0].get("documents", []):
        for passage in document.get("passages", []):
            infons = passage.get("infons", {})
            if "article-id_doi" in infons:
                metadata["article-id_doi"] = infons["article-id_doi"]
            if "article-id_pmc" in infons:
                metadata["article-id_pmc"] = infons["article-id_pmc"]
            if "article-id_pmid" in infons:
                metadata["article-id_pmid"] = infons["article-id_pmid"]
            if "section_type" in infons and infons["section_type"] == "TITLE":
                metadata["article_title"] = passage.get("text", "")
    return metadata

def process_and_summarize_paper(pmcid: str) -> Dict[str, Any]:
    logging.info(f"开始处理和总结PMCID为{pmcid}的论文...")
    paper_info = get_paper_from_pmc(pmcid)
    metadata = extract_metadata(paper_info)
    full_text = extract_full_text_filtered(paper_info)
    
    logging.info(f"正在生成PMCID为{pmcid}的论文摘要...")
    summary_result = process_paper(full_text)
    
    result = {
        **metadata,
        "article_content": full_text,
        "article_description": summary_result["result"].get("description", ""),
        "article_function": summary_result["result"].get("function", ""),
        "article_homepage": summary_result["result"].get("homepage", ""),
        "article_keyword": summary_result["result"].get("keywords", ""),
        "article_tooltype": summary_result["result"].get("toolType", []),
        "article_topic": summary_result["result"].get("Topic", [])
    }
    
    logging.info(f"完成PMCID为{pmcid}的论文处理和总结")
    return result

def save_to_csv(data: List[Dict[str, Any]], filename: str):
    logging.info(f"正在将数据保存到CSV文件: {filename}")
    os.makedirs('../db', exist_ok=True)
    filepath = os.path.join('../db', filename)
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            "article-id_doi", "article-id_pmc", "article-id_pmid", "article_title",
            "article_content", "article_description", "article_function",
            "article_homepage", "article_keyword", "article_tooltype", "article_topic"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    logging.info(f"数据已成功保存到CSV文件: {filename}")

def save_to_database(data: List[Dict[str, Any]], db_name: str):
    logging.info(f"正在将数据保存到数据库: {db_name}")
    os.makedirs('../db', exist_ok=True)
    db_path = os.path.join('../db', db_name)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS articles
                 (doi TEXT, pmc TEXT, pmid TEXT, title TEXT, content TEXT,
                  description TEXT, function TEXT, homepage TEXT, keyword TEXT,
                  tooltype TEXT, topic TEXT)''')
    
    for article in data:
        c.execute('''INSERT INTO articles VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (article.get("article-id_doi"), article.get("article-id_pmc"),
                   article.get("article-id_pmid"), article.get("article_title"),
                   article.get("article_content"), article.get("article_description"),
                   article.get("article_function"), article.get("article_homepage"),
                   article.get("article_keyword"), json.dumps(article.get("article_tooltype")),
                   json.dumps(article.get("article_topic"))))
    
    conn.commit()
    conn.close()
    logging.info(f"数据已成功保存到数据库: {db_name}")

def main(pmcids: List[str]):
    logging.info(f"开始处理{len(pmcids)}篇论文...")
    results = []
    for pmcid in pmcids:
        try:
            result = process_and_summarize_paper(pmcid)
            results.append(result)
        except Exception as e:
            error_msg = f"处理PMCID {pmcid}时出错: {str(e)}"
            logging.error(error_msg)
    
    save_to_csv(results, "paper_summaries.csv")
    save_to_database(results, "paper_summaries.db")
    logging.info("所有论文处理完成")

if __name__ == "__main__":
    pmcids = ["10164590","10767903","4213956"]  # 根据需要添加更多PMCID
    main(pmcids)