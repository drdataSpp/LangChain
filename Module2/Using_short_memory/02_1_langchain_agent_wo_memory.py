from langchain.agents import create_agent
from langchain.messages import HumanMessage, AIMessage, SystemMessage ## Docs: https://docs.langchain.com/oss/python/langchain/messages
from langchain_ollama import ChatOllama
import time

## Initialize the agent with the local Ollama model.

agent = create_agent(
    model = ChatOllama(
        model="mistral:7b",
        base_url="http://localhost:11434"
    )
)

response1 = agent.invoke(
    {"messages": [
        HumanMessage(content="My name is Soorya.")
        , SystemMessage(content="You helpful and a kind assistant.")
        ]
    }
)

print("Human Message:", response1['messages'][-3].content)
print("AI Response:", response1['messages'][-1].content)


time.sleep(3) # Pauses the program for 3 second before sending the next message to the agent.

agent = create_agent(
    model = ChatOllama(
        model="mistral:7b",
        base_url="http://localhost:11434"
    )
)

response2 = agent.invoke(
    {"messages": [
        HumanMessage(content="What is my name?")
        , SystemMessage(content="You helpful and a kind assistant.")
        ]
    }
)

print("Human Message:", response2['messages'][-3].content)
print("AI Response:", response2['messages'][-1].content)


"""

Output:

PS D:\Github\langchain\Module2> python .\02_1_langchain_agent_wo_memory.py

Human Message: My name is Soorya.
AI Response:  Hello Soorya, it's nice to meet you! How can I assist you today?

Human Message: What is my name?
AI Response:  I don't have personal knowledge, but if we're continuing our conversation from before, your name (as per your last message) was Emily. How can I assist you today, Emily?

"""