from tavily import TavilyClient
import os

tavily_api_key = os.getenv("tavily_api_key")

tavily_client = TavilyClient(api_key=tavily_api_key)

response = tavily_client.extract("https://en.wikipedia.org/wiki/Artificial_intelligence")

print(response)

## If you get an web scrapped info, then the test is successful. Otherwise, check your API key & py script and try again.