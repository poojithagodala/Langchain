from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()

def main():
    print("Hello from langchain-course!")

    info = """
Elon Reeve Musk is a businessman and entrepreneur known 
for Tesla, SpaceX, X, and xAI.
    """

    summary_template = """
Given the info: {info} about a person, create:
1. A short summary
2. Two interesting facts about them
    """

    prompt = PromptTemplate.from_template(summary_template)

    llm = ChatOllama(temperature=0, model="gemma3:270m")
    ##llm = ChatOllama(temperature=0, model="gpt-5")
    chain = prompt | llm

    response = chain.invoke({"info": info})

    print(response.content)

if __name__ == "__main__":
    main()