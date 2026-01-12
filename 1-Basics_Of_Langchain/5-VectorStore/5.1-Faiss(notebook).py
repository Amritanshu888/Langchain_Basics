# Faiss
# Facebook AI Similarity Search (Faiss) is a library for efficient similarity search and clustering of dense vectors. It contains algorithms that search in sets of vectors of any size, up to ones that possibly do not fit in RAM. It also contains supporting code for evaluation and parameter tuning.

## Tab 1
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import CharacterTextSplitter

loader=TextLoader("speech.txt")
documents=loader.load()
text_splitter=CharacterTextSplitter(chunk_size=1000,chunk_overlap=30)
docs=text_splitter.split_documents(documents)

## Tab 2
docs

## Tab 3
embeddings=OllamaEmbeddings()
db=FAISS.from_documents(docs,embeddings)
db

## Tab 4
### querying 
query="How does the speaker describe the desired outcome of the war?"
docs=db.similarity_search(query)
docs[0].page_content

## Tab 5
# As a Retriever
# We can also convert the vectorstore into a Retriever class. This allows us to easily use it in other LangChain methods, which largely work with retrievers

retriever=db.as_retriever()
docs=retriever.invoke(query)
docs[0].page_content

## Tab 6
# Similarity Search with score
# There are some FAISS specific methods. One of them is similarity_search_with_score, which allows you to return not only the documents but also the distance score of the query to them. The returned distance score is L2 distance. Therefore, a lower score is better.

docs_and_score=db.similarity_search_with_score(query)
docs_and_score

## Tab 7
embedding_vector=embeddings.embed_query(query)
embedding_vector

## Tab 8
docs_score=db.similarity_search_by_vector(embedding_vector)
docs_score

## Tab 9
### Saving And Loading
db.save_local("faiss_index")

## Tab 10
new_db=FAISS.load_local("faiss_index",embeddings,allow_dangerous_deserialization=True)
docs=new_db.similarity_search(query)

## Tab 11
docs