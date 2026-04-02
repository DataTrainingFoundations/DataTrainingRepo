# https://ollama.com/download to download ollama so you can have local LLMs
# ollama pull llama3.2
# pip install langchain-ollama langchain-core
# pip install torch
# NOTE:used venv for virtual environment for this example with Python 3.10.11



#try below first
###########################################################
from langchain_ollama import OllamaLLM

# Initialize the model (ensure the name matches what you pulled)
llm = OllamaLLM(model="llama3.2")

# Simple invocation
response = llm.invoke("Explain quantum computing in one sentence.")
print(response)

###########################################
#If first block worked, try this:
###########################################
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# 1. Setup the model
llm = OllamaLLM(model="llama3.2")

# 2. Define a template
template = """
Question: {question}
Answer: Let's think step by step.
"""
prompt = ChatPromptTemplate.from_template(template)

# 3. Create a chain (using the modern Pipe operator)
chain = prompt | llm

# 4. Run the chain
response = chain.invoke({"question": "Why is the sky blue?"})
print(response)
