# Getting started With Langchain And Open AI
# In this quickstart we'll see how to:

# - Get setup with LangChain, LangSmith and LangServe
# - Use the most basic and common components of LangChain: prompt templates, models, and output parsers.
# - Build a simple application with LangChain
# - Trace your application with LangSmith
# - Serve your application with LangServe

## Tab 1
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

## Tab 2
from langchain_openai import ChatOpenAI
llm=ChatOpenAI(model="gpt-4o")
print(llm)

## Tab 3
## Input and get response form LLM

result=llm.invoke("What is generative AI?")

## Tab 4
print(result)

## Tab 5
### Chatprompt Template
from langchain_core.prompts import ChatPromptTemplate

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are an expert AI Engineer. Provide me answers based on the questions"),
        ("user","{input}")
    ]

)
prompt

## Tab 6
## chain 
chain=prompt|llm

response=chain.invoke({"input":"Can you tell me about Langsmith?"})
print(response)

## Tab 7
type(response)

## Tab 8
## stroutput Parser

from langchain_core.output_parsers import StrOutputParser
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

response=chain.invoke({"input":"Can you tell me about Langsmith?"})
print(response)