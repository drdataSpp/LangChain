from langchain.agents import create_agent

from langchain.messages import HumanMessage, SystemMessage
from langchain.tools import tool
from langchain_ollama import ChatOllama

import os
from tavily import TavilyClient


@tool("web_search")
def web_search(query: str) -> str:
    """ Search the web for up-to-date information. """

    api_key = os.getenv("tavily_api_key")
    
    if not api_key:
        return "Tavily API key not configured. Set the tavily_api_key environment variable."

    client = TavilyClient(api_key=api_key)
    
    try:
        response = client.search(query=query, max_results=5)
    except Exception as e:
        return f"Error during web search: {e}"

    # If the response contains a list of results, pick the one with highest score
    if isinstance(response, dict):
        results = response.get("results") or []
        if results:
            best = max(results, key=lambda r: r.get("score", 0))
            title = best.get("title", "")
            url = best.get("url", "")
            content = best.get("content", "")
            return f"{title}\n{url}\n\n{content}"
        
    # fallback: just stringify the response
    return str(response)


# ---------------------------------------------------------------------------
# Agent setup
# ---------------------------------------------------------------------------

system_prompt = SystemMessage(content="""
You are a helpful assistant. Answer user questions directly when you know the
answer. If you are uncertain or require up-to-date information, invoke the
`web_search` tool with the user's query.

Always stream your responses so the caller can process tokens as they arrive.
""" )

agent = create_agent(
    model=ChatOllama(
        model="mistral:7b",
        base_url="http://localhost:11434",
        # you can tweak temperature / other settings here if desired
    ),
    #tools=[web_search],
)

query = "What is the current USD to NZD dollar exchange rate?"

for token, metadata in agent.stream(
    {"messages": [system_prompt, HumanMessage(content=query)]},
    stream_mode="messages",
):
    if token.content:
        print(token.content, end="", flush=True)


"""
Output (Without tool use):

 I am unable to provide real-time data or services directly. However, I can help you find the current exchange rate. Here is a web search query that could give you the information: "Current USD to NZD exchange rate". You can copy this query into your preferred search engine for the most recent rates.

"""

"""
Output (With tool use):

1 USD to NZD - US Dollars to New Zealand Dollars Exchange Rate
https://www.xe.com/en-us/currencyconverter/convert/?Amount=1&From=USD&To=NZD

1 USD equals 1.66 NZD using the current mid-market exchange rate of $1.6679. If you're looking to send 1 USD to NZD, check if Xe could save you money on your Based on the information provided by xe.com, the current exchange rate for 1 USD is approximately 1.66 NZD as of today. This rate is subject to change due to market fluctuations. For accurate and up-to-date exchange rates, I recommend checking a reliable currency converter website like XE.com before making any financial transactions.
PS D:\Github\langchain\Module2> python .\01_langchain_model_with_web_search_tool.py
USD NZD | US Dollar New Zealand Dollar
https://www.investing.com/currencies/usd-nzd

What Is the Current USD/NZD Exchange Rate? The current USD/NZD exchange rate is 1.6677, with a previous close of 1.6723. What Is the Daily Range for USD/NZD? As of my last search, the current USD to NZD exchange rate is approximately 1.6677, with a previous close of 1.6723. The daily range for USD/NZD is not provided in the source, but it can be determined by checking historical data on various financial websites such as Investing.com or XE.com.
PS D:\Github\langchain\Module2> 

"""