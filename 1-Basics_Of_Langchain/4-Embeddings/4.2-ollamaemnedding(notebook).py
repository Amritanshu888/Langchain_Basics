# Ollama
# Ollama supports embedding models, making it possible to build retrieval augmented generation (RAG) applications that combine text prompts with existing documents or other data.

## Tab 1
from langchain_community.embeddings import OllamaEmbeddings

## Tab 2
embeddings=(
    OllamaEmbeddings(model="gemma:2b")  ##by default it ues llama2
)

## Tab 3
embeddings

## Tab 4
r1=embeddings.embed_documents(
    [
       "Alpha is the first letter of Greek alphabet",
       "Beta is the second letter of Greek alphabet", 
    ]
)

## Tab 5
len(r1[0])

## Tab 6
r1[1]

## Tab 7
embeddings.embed_query("What is the second letter of Greek alphabet ")

## Tab 8
### Other Embedding Models
### https://ollama.com/blog/embedding-models
embeddings = OllamaEmbeddings(model="mxbai-embed-large")
text = "This is a test document."
query_result = embeddings.embed_query(text)
query_result

## Tab 9
len(query_result)