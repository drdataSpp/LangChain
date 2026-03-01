from langchain.agents import create_agent
from langchain.messages import HumanMessage, AIMessage, SystemMessage ## Docs: https://docs.langchain.com/oss/python/langchain/messages
from langchain_ollama import ChatOllama

from langgraph.checkpoint.memory import InMemorySaver ## Docs: https://docs.langchain.com/oss/python/langchain/short-term-memory

import time

## Initialize the agent with the local Ollama model.

agent = create_agent(
    model = ChatOllama(
        model="mistral:7b",
        base_url="http://localhost:11434"
    )
    , checkpointer=InMemorySaver()
)

response1 = agent.invoke(
    {"messages": [
        HumanMessage(content="My name is Soorya.")
        , SystemMessage(content="You helpful and a kind assistant.")
        ]
    }
    , {"configurable": {"thread_id": "1"}}  ## Past conversations are grouped into threads. By specifying the same thread_id, the agent can recall past interactions in that thread.
)

print("Human Message:", response1['messages'][-3].content)
print("AI Response:", response1['messages'][-1].content)


time.sleep(3) # Pauses the program for 3 second before sending the next message to the agent.

response2 = agent.invoke(
    {"messages": [
        HumanMessage(content="What is my name?")
        , SystemMessage(content="You helpful and a kind assistant.")
        ]
    }    
    , {"configurable": {"thread_id": "1"}}
)

print("Human Message:", response2['messages'][-3].content)
print("AI Response:", response2['messages'][-1].content)


"""

Output:

PS D:\Github\langchain\Module2> python .\02_2_langchain_agent_wo_memory.py

Human Message: My name is Soorya.
AI Response:  Hello Soorya! It's nice to meet you. How can I assist you today? If you have any questions or need help with something, feel free to ask!

Human Message: What is my name?
AI Response:  Your name is Soorya, as that is what you introduced yourself as earlier in our conversation. Is there anything specific you would like to know about or discuss related to the name Soorya?

"""