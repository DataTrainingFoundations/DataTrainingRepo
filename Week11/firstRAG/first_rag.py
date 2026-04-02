#https://ollama.com/download to download ollama so you can have local LLMs
#ollama pull llama3.2
#pip install langchain-ollama langchain-core
#pip install torch
#pip install -U langchain-community langchain-text-splitters langchain-chroma chromadb
#NOTE:used venv for virtual environment for this example with Python 3.10.11


################################################################
#Now for the RAG:
##################################################################
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

# -----------------------------
# 1. Load documents
# -----------------------------
loader = TextLoader("data.txt")  # your local file
documents = loader.load()

# -----------------------------
# 2. Split documents
# -----------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)

# -----------------------------
# 3. Create embeddings + vector store
# -----------------------------
embeddings = OllamaEmbeddings(model="llama3.2")

vectorstore = Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

retriever = vectorstore.as_retriever()

# -----------------------------
# 4. Setup LLM 
# -----------------------------
llm = OllamaLLM(model="llama3.2")

# -----------------------------
# 5. Prompt (RAG style)
# -----------------------------
template = """
You are an assistant that answers questions using the provided context.

Context:
{context}

Question:
{question}

Answer: Let's think step by step.
"""

prompt = ChatPromptTemplate.from_template(template)

# -----------------------------
# 6. Build RAG chain (pipe style)
# -----------------------------
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def get_context(input):
    docs = retriever.invoke(input["question"])
    return format_docs(docs)

rag_chain = (
    {
        "context": RunnableLambda(get_context),
        "question": lambda x: x["question"]
    }
    | prompt
    | llm
    | StrOutputParser()
)

# -----------------------------
# 7. Run it
# -----------------------------
response1 = rag_chain.invoke({
    "question": "What is this document about?"
})

#evidence that the RAG works outside the scope of the underlying model Scope
response2 = rag_chain.invoke({
    "question": "Who wrote the Python programming language?"
})

#evidence that the RAG still can use the underlying model not just the extra docs
response3 = rag_chain.invoke({
    "question": "What is the largest ocean in the world?"
})


print(response1)
print(response2)
print(response3)



###########################################################













#useful but may not need:
#127.0.0.1:11434
#taskkill /IM ollama.exe /F
#ollama serve
#ollama run llama3.2