
from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

tavily = TavilyClient()                               #NONSTATIC

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
       query: The query to search for
    Returns:
       The search result
    """
    print(f"Searching for {query}")   # f-string
    return tavily.search(query=query)                       # NON STATIC PART


llm = ChatOpenAI(model="gpt5")
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain")
    
    result = agent.invoke({
        "messages": [HumanMessage(content="What is the weather in Tokyo")]  # list added
    })
    
    print(result)   # print output


if __name__ == "__main__":  
    main()
