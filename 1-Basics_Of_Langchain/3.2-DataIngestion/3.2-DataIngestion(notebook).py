## Tab 1
# Data Ingestion- Documentloaders
# https://python.langchain.com/v0.2/docs/integrations/document_loaders/

## Text Loader

from langchain_community.document_loaders import TextLoader

loader=TextLoader('speech.txt')
loader

## Tab 2
text_documents=loader.load()
text_documents

## Tab 3
## Reading a PDf File
from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader('attention.pdf')
docs=loader.load()
docs

## Tab 4
type(docs[0])

## Tab 5
## Web based loader
from langchain_community.document_loaders import WebBaseLoader
import bs4
loader=WebBaseLoader(web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
                     bs_kwargs=dict(parse_only=bs4.SoupStrainer(
                         class_=("post-title","post-content","post-header")
                     ))
                     )

## Tab 6
loader.load()

## Tab 7
## Arxiv
from langchain_community.document_loaders import ArxivLoader
docs = ArxivLoader(query="1706.03762", load_max_docs=2).load()
len(docs)

## Tab 8
docs

## Tab 9
from langchain_community.document_loaders import WikipediaLoader
docs = WikipediaLoader(query="Generative AI", load_max_docs=2).load()
len(docs)
print(docs)

## Tab 10
docs

