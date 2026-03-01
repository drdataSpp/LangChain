# LangChain Local Agent Examples

A small collection of example scripts showing how to run local LLMs (Mistral via Ollama), create agents, stream responses, and use a web-search tool backed by Tavily.

**Key features**

- Local Mistral (`mistral:7b`) via `langchain-ollama` (Ollama running on `http://localhost:11434`).
- Examples showcasing message types: `SystemMessage`, `HumanMessage`, `AIMessage` and streaming.
- A `web_search` tool implemented with Tavily; reads API key from `tavily_api_key` environment variable.

## Repo structure

- Module1/
  - `00_langchain__invoking_a_local_model.py` — basic single-call example invoking a local model.
  - `01_langchain__creating_an_agent_with_local_model.py` — demonstrates creating an agent and passing messages, including system prompts.
  - `02_langchain__streaming_agent_messages.py` — shows how to stream tokens/messages from the agent.
  - `03_langchain__system_prompt.py` — example of using a `SystemMessage` to steer assistant behavior.

- Module2/
  - `Using_tools/01_langchain_agent_with_web_search_tool.py` — agent with a `web_search` tool (uses Tavily).
  - `personal_chef.py` — small example (utility/demo script).
  - `Using_short_memory/` — examples showing agents with and without short-term memory and threaded usage:
    - `02_1_langchain_agent_wo_memory.py`
    - `02_2_langchain_agent_w_memory.py`
    - `02_3_langchain_agent_w_different_threads.py`
  - `Tavily/test_tavily.py` — minimal Tavily client example; demonstrates reading the API key from the environment.

## Prerequisites

- Python 3.12
- Ollama running locally (if you want to run local `mistral:7b`) on `http://localhost:11434`.
- A Tavily API key (set in environment variable `tavily_api_key`) if you plan to use the `web_search` tool.

## Installation (recommended)

This repo includes a `Pipfile`. Using `pipenv` is recommended:

```bash
pipenv install
pipenv shell
```

Alternatively, use `pip` in a virtualenv and install `langchain`, `langchain-ollama`, and `tavily`.

## Environment

On Windows PowerShell, set the Tavily key like:

```powershell
$env:tavily_api_key = "tvly-YOUR_API_KEY"
```

On macOS/Linux:

```bash
export tavily_api_key="tvly-YOUR_API_KEY"
```

## Running examples

- Streamed agent example (Module1 streaming):

```bash
python Module1/02_langchain__streaming_agent_messages.py
```

- Create agent and run a query (Module2 web-search agent):

```bash
python Module2/Using_tools/01_langchain_agent_with_web_search_tool.py
```

- Tavily quick test:

```bash
python Module2/Tavily/test_tavily.py
```

## Notes & next steps

- The `web_search` tool uses Tavily and selects the top-scoring result; adjust formatting or include multiple results if desired.
- Feel free to add `README` sections for any new scripts or clarify usage examples.

---

If you want a prettier README (badges, screenshots, or usage GIFs), tell me which examples you care most about and I will enhance it further.