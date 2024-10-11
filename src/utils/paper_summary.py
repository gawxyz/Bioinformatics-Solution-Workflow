from utils.bridge_llm.llm_ollama import (
    chat_ollama_llama31_json,
    chat_ollama_llama31,
    chat_ollama_llama31_fp16,
)
from utils.bridge_llm.llm_doubao import chat_doubao

from langgraph.graph import StateGraph, END , START

from typing import Annotated
from typing_extensions import TypedDict
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from utils.config.prompts import (
    TOOL_TYPE_LIST_SIMPLE,
    BIOSCIENCE_TOPIC_LIST_SIMPLE,
    COMBINED_PROMPT_TEMPLATE
)

# 可切换不同的LLM
current_llm = chat_doubao

# 修改合并后的提示
combined_prompt = PromptTemplate(
    input_variables=["paper_content", "tool_type_list", "bioscience_topic_list"],
    template=COMBINED_PROMPT_TEMPLATE,
)

# 修改处理链
paper_processor = combined_prompt | current_llm | JsonOutputParser()

# 修改 GraphState 类定义
class GraphState(TypedDict):
    paper_content: str
    result: dict

# 修改处理函数
def process_paper_combined(state) -> GraphState:
    print("---processing_paper---")
    result = paper_processor.invoke({
        "paper_content": state["paper_content"],
        "tool_type_list": TOOL_TYPE_LIST_SIMPLE,
        "bioscience_topic_list": BIOSCIENCE_TOPIC_LIST_SIMPLE
    })
    state["result"] = result
    return state

# 修改图结构
workflow = StateGraph(GraphState)
workflow.add_node("process", process_paper_combined)
workflow.add_edge(START, "process")
workflow.add_edge("process", END)

# 编译图
paper_summary_graph = workflow.compile()

# 修改主函数
def process_paper(paper_content: str) -> GraphState:
    initial_state: GraphState = {
        "paper_content": paper_content,
        "result": None
    }
    result = paper_summary_graph.invoke(initial_state)
    return result

# 示例使用
if __name__ == "__main__":
    paper_content = """
    Abstract
    Motivation
    Symptom-based automatic diagnostic system queries the patient's potential symptoms through continuous interaction with the patient and makes predictions about possible diseases. A few studies use reinforcement learning (RL) to learn the optimal policy from the joint action space of symptoms and diseases. However, existing RL (or Non-RL) methods focus on disease diagnosis while ignoring the importance of symptom inquiry. Although these systems have achieved considerable diagnostic accuracy, they are still far below its performance upper bound due to few turns of interaction with patients and insufficient performance of symptom inquiry. To address this problem, we propose a new automatic diagnostic framework called DxFormer, which decouples symptom inquiry and disease diagnosis, so that these two modules can be independently optimized. The transition from symptom inquiry to disease diagnosis is parametrically determined by the stopping criteria. In DxFormer, we treat each symptom as a token, and formalize the symptom inquiry and disease diagnosis to a language generation model and a sequence classification model, respectively. We use the inverted version of Transformer, i.e. the decoder–encoder structure, to learn the representation of symptoms by jointly optimizing the reinforce reward and cross-entropy loss.

    Results
    We conduct experiments on three real-world medical dialogue datasets, and the experimental results verify the feasibility of increasing diagnostic accuracy by improving symptom recall. Our model overcomes the shortcomings of previous RL-based methods. By decoupling symptom query from the process of diagnosis, DxFormer greatly improves the symptom recall and achieves the state-of-the-art diagnostic accuracy.

    Availability and implementation
    Both code and data are available at https://github.com/lemuria-wchen/DxFormer.

    Supplementary information
    Supplementary data are available at Bioinformatics online.
    """  # 这里是论文的内容
    result = process_paper(paper_content)
    print(result)