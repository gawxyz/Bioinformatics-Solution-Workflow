import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 加载.env文件
load_dotenv(dotenv_path="/home/awgao/bioSolution_RAG_LLM/langchain_Tutorial/LangGraph_20240905/backend/llm_bridge/.env")


chat_doubao = ChatOpenAI(
    model=os.getenv("DOUBAO_MODEL_ID"),
    openai_api_key=os.getenv("ARK_API_KEY"),
    openai_api_base=os.getenv("ARK_API_BASE_URL"),
    temperature=0.1,  # 可以根据需要调整
)


# 示例用法（如果直接运行此文件）
if __name__ == "__main__":
    question = "常见的十字花科植物有哪些？"
    answer = chat_doubao.invoke(question)
    print(f"问题：{question}")
    print(f"回答：{answer.content}")
 
