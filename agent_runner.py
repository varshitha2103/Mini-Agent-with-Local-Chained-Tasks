from langchain_community.chat_models import ChatOllama
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOllama(model="mistral")

def generate_subtasks(goal: str) -> str:
    messages = [
        SystemMessage(content="You are a task planner. Break the goal into 3 steps with reasoning."),
        HumanMessage(content=f"My goal is: {goal}")
    ]
    result = llm(messages)
    return result.content
