
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
    TOOL_TYPE_LIST,
    BIOSCIENCE_TOPIC_LIST,
    SUMMARY_PAPER_TEMPLATE
)

# 可切换不同的LLM
current_llm = chat_doubao

# 工具类型标注器 
tooltype_prompt = PromptTemplate(
    template="""You are a software engineer tasked with classifying software tools. \n
    Here are the definitions of the tool types: \n\n {tool_type_list} \n\n 
    Here is the description of the tools: \n\n {paper_content} \n\n
    Classify the tools based on the definitions, allowing for multiple types per tool.\n
    Provide a JSON format with a single key for the "toolType", like {{"toolType": ["class1", "class2", ...]}}, without any premable or explanations.""",
    input_variables=["tool_type_list","paper_content"],
)

## 论文主题分类器
prompt_topic = PromptTemplate(
    template="""You are a life scientist tasked with assigning relevant bioscience topics to a paper. \n
    Here are the concepts of each bioscience topic: \n\n {bioscience_topic_list} \n\n
    Here is the paper's content: \n\n {paper_content} \n\n
    Assign the main relevant scientific topics based on the provided bioscience concepts, allowing for multiple topics per paper. \n
    Provide a JSON format with a single key for "Topic", like {{"Topic": ["topic1", "topic2", ...]}}, without any premable or explanations.""",
    input_variables=["bioscience_topic_list","paper_content"],
)

summary_paper_prompt = PromptTemplate(
    input_variables=["paper_content"],
    template=SUMMARY_PAPER_TEMPLATE
)

# label chains
tool_type_labeler = tooltype_prompt | current_llm | JsonOutputParser()
topic_labeler = prompt_topic | current_llm | JsonOutputParser()
paper_summary_generator = summary_paper_prompt | current_llm | JsonOutputParser()



# 定义GraphState
class GraphState(TypedDict):
    paper_content: str
    summary: str 
    tool_types: str 
    topics: str

# 修改节点函数
def summarize_paper(state) -> GraphState:
    print("---summarize_paper---")
    summary = paper_summary_generator.invoke({"paper_content": state["paper_content"]})
    state["summary"] = summary
    return state

def label_tool_type(state) -> GraphState:
    print("---label_tool_type---")
    tool_types = tool_type_labeler.invoke({
        "tool_type_list": TOOL_TYPE_LIST, 
        "paper_content": state["paper_content"]
    })
    state["tool_types"] = tool_types
    return state

def label_topic(state) -> GraphState:
    print("---label_topic---")
    topics = topic_labeler.invoke({
        "bioscience_topic_list": BIOSCIENCE_TOPIC_LIST, 
        "paper_content": state["paper_content"]
    })
    state["topics"] = topics
    return state

# 创建图
workflow = StateGraph(GraphState)

# 添加节点

workflow.add_node("summarize", summarize_paper)
workflow.add_node("label_tool_type", label_tool_type)
workflow.add_node("label_topic", label_topic)

# 定义边
workflow.add_edge(START, "summarize")
workflow.add_edge("summarize", "label_tool_type")
workflow.add_edge("label_tool_type", "label_topic")
workflow.add_edge("label_topic", END)

# 编译图
paper_summary_graph = workflow.compile()

# 使用函数
def process_paper(paper_content: str) -> GraphState:
    initial_state: GraphState = {
        "paper_content": paper_content,
        "summary": None,
        "tool_types": None,
        "topics": None
    }
    result = paper_summary_graph.invoke(initial_state)
    return result

# 示例使用
if __name__ == "__main__":
    paper_content = """
    Abstract
    Motivation
    Symptom-based automatic diagnostic system queries the patient’s potential symptoms through continuous interaction with the patient and makes predictions about possible diseases. A few studies use reinforcement learning (RL) to learn the optimal policy from the joint action space of symptoms and diseases. However, existing RL (or Non-RL) methods focus on disease diagnosis while ignoring the importance of symptom inquiry. Although these systems have achieved considerable diagnostic accuracy, they are still far below its performance upper bound due to few turns of interaction with patients and insufficient performance of symptom inquiry. To address this problem, we propose a new automatic diagnostic framework called DxFormer, which decouples symptom inquiry and disease diagnosis, so that these two modules can be independently optimized. The transition from symptom inquiry to disease diagnosis is parametrically determined by the stopping criteria. In DxFormer, we treat each symptom as a token, and formalize the symptom inquiry and disease diagnosis to a language generation model and a sequence classification model, respectively. We use the inverted version of Transformer, i.e. the decoder–encoder structure, to learn the representation of symptoms by jointly optimizing the reinforce reward and cross-entropy loss.

    Results
    We conduct experiments on three real-world medical dialogue datasets, and the experimental results verify the feasibility of increasing diagnostic accuracy by improving symptom recall. Our model overcomes the shortcomings of previous RL-based methods. By decoupling symptom query from the process of diagnosis, DxFormer greatly improves the symptom recall and achieves the state-of-the-art diagnostic accuracy.

    Availability and implementation
    Both code and data are available at https://github.com/lemuria-wchen/DxFormer.

    Supplementary information
    Supplementary data are available at Bioinformatics online.
    """  # 这里是论文的JSON内容
    result = process_paper(paper_content)
    print(result)

