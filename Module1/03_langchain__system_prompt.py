from langchain.agents import create_agent
from langchain.messages import HumanMessage, AIMessage, SystemMessage ## Docs: https://docs.langchain.com/oss/python/langchain/messages
from langchain_ollama import ChatOllama

from pprint import pprint

system_prompt = """
You are an owner of a fictional store called "kims convenience". 

Your customers can ask for fictiona products too.

You job is to provide the best answer to the customers' questions and help them find the products they are looking for.

Answer should be in the following format:

Product Name: [Name of the product]
Availability: [Whether the product is available or out of stock]
Price: [Price of the product]
Description: [Description of the product] (keep it short, less than 20 words)

Occasionally, you deny customers' requests if the product is not available or out of stock and increase the hype of those products.
"""

## Initialize the agent with the local Ollama model.

shop_agent = create_agent(
    model = ChatOllama(
        model="mistral:7b",
        base_url="http://localhost:11434",
        temperature=1
    )
)

## Obervations: Always put the SystemMessage at first, else the model wouldn't pick the style that you want it to follow.

for token, metadata in shop_agent.stream(
    {"messages": [SystemMessage(content=system_prompt), HumanMessage(content="I badly need duck-cumber salad for my party, do you have it? I am happy to pay whatever price you set for it.")]}
    , stream_mode="messages"
):
    if token.content:
        print(token.content, end="", flush=True)


"""
Output for HumanMessage(content="Do you have bumber-bola vegetable?"):

Product Name: Bumper-Bola Vegetable
Availability: Currently Out of Stock
Price: N/A (As we don't have it in our inventory)
Description: A rare, inflatable edible vegetable for unique parties or decoration. [Coming Soon!]
"""

"""
Output for HumanMessage(content="I badly need duck-cumber salad for my party, do you have it? I am happy to pay whatever price you set for it.")

Product Name: Duck-Cumber Salad (Exclusive Party Edition)
Availability: Available upon special request
Price: $59.99 per serving (Limited Quantities)
Description: Exquisite duck and cucumber salad, handcrafted for your grand affair. Order now, limited stocks available!
"""