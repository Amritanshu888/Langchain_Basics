# How to split JSON data
# This json splitter splits json data while allowing control over chunk sizes. It traverses json data depth first and builds smaller json chunks. It attempts to keep nested json objects whole but will split them if needed to keep chunks between a min_chunk_size and the max_chunk_size.

# If the value is not a nested json, but rather a very large string the string will not be split. If you need a hard cap on the chunk size consider composing this with a Recursive Text splitter on those chunks. There is an optional pre-processing step to split lists, by first converting them to json (dict) and then splitting them as such.

# How the text is split: json value.
# How the chunk size is measured: by number of characters.

## Tab 1
import json
import requests

json_data=requests.get("https://api.smith.langchain.com/openapi.json").json()

## Tab 2
json_data

## Tab 3
from langchain_text_splitters import RecursiveJsonSplitter
json_splitter=RecursiveJsonSplitter(max_chunk_size=300)
json_chunks=json_splitter.split_json(json_data)

## Tab 4
json_chunks

## Tab 5
for chunk in json_chunks[:3]:
    print(chunk)

## Tab 6
## The splitter can also output documents
docs=json_splitter.create_documents(texts=[json_data])
for doc in docs[:3]:
    print(doc)

## Tab 7
texts=json_splitter.split_text(json_data)
print(texts[0])
print(texts[1])        