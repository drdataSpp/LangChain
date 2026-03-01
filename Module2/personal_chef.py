import os
from pprint import pprint

from langchain.agents import create_agent
from langchain.messages import HumanMessage, AIMessage, SystemMessage ## Docs: https://docs.langchain.com/oss/python/langchain/messages
from langchain_ollama import ChatOllama

from langgraph.checkpoint.memory import InMemorySaver

from langchain.tools import tool
from typing import Dict, Any
from tavily import TavilyClient

api_key = os.getenv("tavily_api_key")

client = TavilyClient(api_key=api_key)

@tool
def web_search(query: str) -> Dict[str, Any]:

    """Search the web for information"""

    return client.search(query)


system_prompt = """

You are a personal chef. The user will give you a list of ingredients they have left over in their house.

Using the web search tool, search the web for recipes that can be made with the ingredients they have.

Return recipe suggestions and eventually the recipe instructions to the user, if requested.

"""

agent = create_agent(
    model = ChatOllama(
        model="mistral:7b",
        base_url="http://localhost:11434"
    )
    , tools=[web_search]
    , system_prompt=system_prompt
    , checkpointer=InMemorySaver()
)

config = {"configurable": {"thread_id": "1"}}

response = agent.invoke(
    {"messages": [HumanMessage(content="I have some leftover paneer and rice. What can I make?")]},
    config
)

print(response['messages'][-1].content)

# pprint(response)