## Tab 1
# Embedding Techniques
# Converting text into vectors

import os
from dotenv import load_dotenv
load_dotenv()  #load all the environment variables

## Tab 2
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

## Tab 3
from langchain_openai import OpenAIEmbeddings
embeddings=OpenAIEmbeddings(model="text-embedding-3-large")
embeddings

## Tab 4
text="This is a tutorial on OPENAI embedding"
query_result=embeddings.embed_query(text)
query_result

## Tab 5
len(query_result)

## Tab 6
embeddings_1024=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=1024)

## Tab 7
embeddings_1024

## Tab 8
text="This is a tutorial on OPENAI embedding"
query_result=embeddings_1024.embed_query(text)
len(query_result)

## Tab 9
query_result

## Tab 10
from langchain_community.document_loaders import TextLoader

loader=TextLoader('speech.txt')
docs=loader.load()
docs

## Tab 11
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
final_documents=text_splitter.split_documents(docs)
final_documents

## Tab 12
## Vector Embedding And Vector StoreDB
from langchain_community.vectorstores import Chroma

db=Chroma.from_documents(final_documents,embeddings_1024)
db

## Tab 13
### Retrieve the results from query vectorstore db
query="It will be all the easier for us to conduct ourselves as belligerents"
retrieved_results=db.similarity_search(query)
print(retrieved_results)