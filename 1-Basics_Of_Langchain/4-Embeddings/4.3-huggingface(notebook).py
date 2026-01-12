## Tab 1
# Embedding Techniques Using HuggingFace
import os
from dotenv import load_dotenv
load_dotenv()  #load all the environment variables

## Tab 2
os.environ['HF_TOKEN']=os.getenv("HF_TOKEN")

## Tab 3
# Sentence Transformers on Hugging Face
# Hugging Face sentence-transformers is a Python framework for state-of-the-art sentence, text and image embeddings. One of the embedding models is used in the HuggingFaceEmbeddings class. We have also added an alias for SentenceTransformerEmbeddings for users who are more familiar with directly using that package.
from langchain_huggingface import HuggingFaceEmbeddings
embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

## Tab 4
text="this is atest documents"
query_result=embeddings.embed_query(text)
query_result

## Tab 5
len(query_result)

## Tab 6
doc_result = embeddings.embed_documents([text, "This is not a test document."])
doc_result[0]

