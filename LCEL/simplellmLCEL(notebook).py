## Tab 1
# Build a Simple LLM Application with LCEL
# In this quickstart we'll show you how to build a simple LLM application with LangChain. This application will translate text from English into another language. This is a relatively simple LLM application - it's just a single LLM call plus some prompting. Still, this is a great way to get started with LangChain - a lot of features can be built with just some prompting and an LLM call!

# After seeing this video, you'll have a high level overview of:

# - Using language models

# - Using PromptTemplates and OutputParsers

# - Using LangChain Expression Language (LCEL) to chain components together

# - Debugging and tracing your application using LangSmith

# - Deploying your application with LangServe

# !pip install langchain

## Tab 2
### Open AI API Key and Open Source models--Llama3,Gemma2,mistral--Groq

import os
from dotenv import load_dotenv
load_dotenv()

import openai
openai.api_key=os.getenv("OPENAI_API_KEY")

groq_api_key=os.getenv("GROQ_API_KEY")
groq_api_key

## Tab 3
# !pip install langchain_groq

## Tab 4
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
model=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)
model

## Tab 5
# !pip install langchain_core

## Tab 6
from langchain_core.messages import HumanMessage,SystemMessage

messages=[
    SystemMessage(content="Translate the following from English to French"),
    HumanMessage(content="Hello How are you?")
]

result=model.invoke(messages)

## Tab 7
result

## Tab 8
from langchain_core.output_parsers import StrOutputParser
parser=StrOutputParser()
parser.invoke(result)

## Tab 9
### Using LCEL- chain the components
chain=model|parser
chain.invoke(messages)

## Tab 10
### Prompt Templates
from langchain_core.prompts import ChatPromptTemplate

generic_template="Trnaslate the following into {language}:"

prompt=ChatPromptTemplate.from_messages(
    [("system",generic_template),("user","{text}")]
)

## Tab 11
result=prompt.invoke({"language":"French","text":"Hello"})

## Tab 12
result.to_messages()

## Tab 13
##Chaining together components with LCEL
chain=prompt|model|parser
chain.invoke({"language":"French","text":"Hello"})

## Tab 14
# !pip install streamlit