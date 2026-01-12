# How to split by character-Character Text Splitter
# This is the simplest method. This splits based on a given character sequence, which defaults to "\n\n". Chunk length is measured by number of characters.

# How the text is split: by single character separator.
# How the chunk size is measured: by number of characters.

## Tab 1
from langchain_community.document_loaders import TextLoader

loader=TextLoader('speech.txt')
docs=loader.load()
docs

## Tab 2
from langchain_text_splitters import CharacterTextSplitter
text_splitter=CharacterTextSplitter(separator="\n\n",chunk_size=100,chunk_overlap=20)
text_splitter.split_documents(docs)

## Tab 3
speech=""
with open("speech.txt") as f:
    speech=f.read()


text_splitter=CharacterTextSplitter(chunk_size=100,chunk_overlap=20)
text=text_splitter.create_documents([speech])
print(text[0])
print(text[1])