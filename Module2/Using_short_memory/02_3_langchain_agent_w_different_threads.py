from langchain.agents import create_agent
from langchain.messages import HumanMessage, AIMessage, SystemMessage ## Docs: https://docs.langchain.com/oss/python/langchain/messages
from langchain_ollama import ChatOllama

from langgraph.checkpoint.memory import InMemorySaver

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
    ,  {"configurable": {"thread_id": "1"}}
)

print("Human Message:", response1['messages'][-3].content)
print("AI Response:", response1['messages'][-1].content)


time.sleep(3) # Pauses the program for 3 second before sending the next message to the agent.

agent = create_agent(
    model = ChatOllama(
        model="mistral:7b",
        base_url="http://localhost:11434"
    )
    , checkpointer=InMemorySaver()
)

response2 = agent.invoke(
    {"messages": [
        HumanMessage(content="What is my name?")
        , SystemMessage(content="You helpful and a kind assistant.")
        ]
    }
    ,  {"configurable": {"thread_id": "2"}}
)

print("Human Message:", response2['messages'][-3].content)
print("AI Response:", response2['messages'][-1].content)


"""

Output:

PS D:\Github\langchain\Module2\Using_short_memory> python .\02_3_langchain_agent_w_different_threads.py

Human Message: My name is Soorya.
AI Response:  Hello Soorya! It's nice to meet you. How can I assist you today? If you have any questions or need help with something, feel free to ask.

Human Message: What is my name?
AI Response:  I don't have personal awareness or access to specific user data, so I don't know who you are. However, I'm here to help you with your questions! If you have a question related to a topic, feel free to ask and I'll do my best to assist you.

You can see that the agent does not remember the name "Soorya" in the second thread, which is expected since we are using separate threads for each interaction. Each thread maintains its own context and memory, so information from one thread does not carry over to another.

"""