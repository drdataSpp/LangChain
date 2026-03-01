from langchain.agents import create_agent
from langchain.messages import HumanMessage, AIMessage, SystemMessage ## Docs: https://docs.langchain.com/oss/python/langchain/messages
from langchain_ollama import ChatOllama

from pprint import pprint

## Initialize the agent with the local Ollama model.

agent = create_agent(
    model = ChatOllama(
        model="mistral:7b",
        base_url="http://localhost:11434"
    )
)


"""
What is Streaming Agent Messages?

* There is going to be latency when calling a model, especially if the model is running locally and the resources are limited.
* LangChain provides a way to stream the responses from the model, allowing you to see the response as it is being generated, rather than waiting for the entire response to be generated before seeing anything.
"""

for token, metadata in agent.stream(
    {"messages": [
        HumanMessage(content="What is 2+2?")
        , AIMessage(content="2 plus 2 is equal to 5.")
        , HumanMessage(content="Are you sure?")
        ]
    }
    , stream_mode="messages"
):
    if token.content:
        print(token.content, end="", flush=True)