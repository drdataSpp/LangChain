
"""
Script demonstrates initializing and using a local Ollama chat model
with LangChain. It sets up the model, invokes a simple query, and
prints the response. Illustrates how to pull/run Ollama and invoking a response from the model. Make sure to have Ollama installed and the model pulled before running this script.
"""

## ========================================================
## Step 1: Invoking a local Ollama model using LangChain.
## ========================================================

from langchain.chat_models import init_chat_model ## Docs: https://reference.langchain.com/python/langchain/chat_models/base/init_chat_model 
from pprint import pprint

## Ensure Ollama is installed, pull the mistral:7b model, and running in local.

v_local_model = "mistral:7b"

model = init_chat_model(
    model=v_local_model
    , model_provider="ollama"
    , base_url="http://localhost:11434"
)

response = model.invoke("What is the capital of Mars?")

print("=" * 60)
print(f"Response from Local Ollama Model {v_local_model}:\n")
print((response.content).strip())
print("=" * 60)

"""
Output:

============================================================
Response from Local Ollama Model mistral:7b:

Mars, being a planet in our solar system and not a country, does not have a capital. Only sovereign states or territories can have capitals.
============================================================

"""

## Check the response metadata.

print("Response Metadata:\n")
pprint(response.response_metadata)

"""
Output:
Response Metadata:

{'created_at': '2026-02-28T23:47:23.0387666Z',
 'done': True,
 'done_reason': 'stop',
 'eval_count': 55,
 'eval_duration': 5538440800,
 'load_duration': 82657700,
 'logprobs': None,
 'model': 'mistral:7b',
 'model_name': 'mistral:7b',
 'model_provider': 'ollama',
 'prompt_eval_count': 11,
 'prompt_eval_duration': 147212200,
 'total_duration': 5824647200}

"""

## =============================================================================
## Step 2: Tweaking model parameters (e.g., temperature) when invoking the model.
## =============================================================================

model_temp_1 = init_chat_model(
    model=v_local_model
    , model_provider="ollama"
    , base_url="http://localhost:11434"
    , temperature=1
)

response_temp_1 = model.invoke("What is the capital of Mars?")

print("=" * 60)
print(f"Response from Local Ollama Model {v_local_model} with temperature=1:\n")
print((response_temp_1.content).strip())
print("=" * 60)

"""
Output:

============================================================
Response from Local Ollama Model mistral:7b with temperature=1:

Mars, as a planet, does not have a capital city because it is not a sovereign state. 
However, in science fiction and popular culture, often the fictional city of Olympus Mons or Hellas Planitia are referred to humorously as the "capital" of Mars.
============================================================

"""

model_temp_0 = init_chat_model(
    model=v_local_model
    , model_provider="ollama"
    , base_url="http://localhost:11434"
    , temperature=0
)

model_temp_0 = model_temp_0.invoke("What is the capital of Mars?")

print("=" * 60)
print(f"Response from Local Ollama Model {v_local_model} with temperature=0:\n")
print((model_temp_0.content).strip())
print("=" * 60)

"""
Output:

============================================================
Response from Local Ollama Model mistral:7b with temperature=0:

Mars, as a planet, does not have a capital city. It's an astronomical body and not a sovereign state. Only planets within our solar system that are inhabited by humans have capitals, such as Earth with its capital being variously defined as Rome, London, Washington D.C., or Ottawa depending on the context of political organization.
============================================================

"""