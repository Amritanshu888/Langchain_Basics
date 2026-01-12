# Text Splitting from Documents- RecursiveCharacter Text Splitters
# This text splitter is the recommended one for generic text. It is parameterized by a list of characters. It tries to split on them in order until the chunks are small enough. The default list is ["\n\n", "\n", " ", ""]. This has the effect of trying to keep all paragraphs (and then sentences, and then words) together as long as possible, as those would generically seem to be the strongest semantically related pieces of text.

# How the text is split: by list of characters.
# How the chunk size is measured: by number of characters.

## Tab 1
## Reading a PDf File
from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader('attention.pdf')
docs=loader.load()
docs

## Tab 2
type(docs[0])

## Tab 3
# How to recursively split text by characters
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
final_documents=text_splitter.split_documents(docs)
final_documents

## Tab 4
print(final_documents[0])
print(final_documents[1])

## Tab 5
## Text Loader

from langchain_community.document_loaders import TextLoader

loader=TextLoader('speech.txt')
docs=loader.load()
docs

## Tab 6
speech=""
with open("speech.txt") as f:
    speech=f.read()


text_splitter=RecursiveCharacterTextSplitter(chunk_size=100,chunk_overlap=20)
text=text_splitter.create_documents([speech])
print(text[0])
print(text[1])

## Tab 7
type(text[0])