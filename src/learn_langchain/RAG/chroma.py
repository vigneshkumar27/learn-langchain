from langchain_chroma import Chroma
from dotenv import load_dotenv
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import AzureChatOpenAI
from langchain.schema import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableMap
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage

load_dotenv()
import os

from langchain_openai import AzureOpenAIEmbeddings
from langchain_core.documents import Document

embedding_client = AzureOpenAIEmbeddings(model="text-embedding")

vector_store = Chroma(
    collection_name="country_collection",
    embedding_function=embedding_client,
    persist_directory="./chroma_db"
)

# ----------------------------
# filepath = Path.joinpath(Path(__file__).resolve().parent,"documents","terraform.txt")

# with open(filepath) as file:
#     content=file.read()
    
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=100,
#     chunk_overlap=20,
#     length_function=len,
#     is_separator_regex=False,
# )
# chunks = text_splitter.create_documents([content])
# for chunk in chunks:
#     vector_store.add_documents([Document(
#         page_content=chunk.page_content,
#     )])

# print(len(vector_store.get()['ids']))

#  ---------------------------------------------------

# llm = AzureChatOpenAI(azure_endpoint="https://ssdidev.openai.azure.com/",api_key="05d806f31335424c8d28bda612bb2ca6",azure_deployment="ssdi-dev-4o",api_version="2024-02-01")

# message_template = [
#     SystemMessage(content="You are a helpfull assistant. You respond to user queries only with provided information, just in short 5 to 10 sentences, If information is not provided or it's irrelevant to the query. Please respond that you don't have sufficent information and please restrict you knowledge to answer the queries"),
#     ('human',"Query : {query} : supporting information : {doc}")
# ]

# def check_val(input):
#     if(input and len(input['doc'])):
#         return input
#     input['doc'] = ""
#     return input
# prompt_template = ChatPromptTemplate.from_messages(message_template)

# prompt = prompt_template.invoke({"query":"rvr","doc":"rbvetr"})

# retriever = vector_store.as_retriever(search_type ="similarity_score_threshold",search_kwargs={"k":1,"score_threshold":0.1})

# chain = RunnableMap({"query":lambda x:x,"doc":lambda x: retriever.invoke(x)}) | RunnableLambda(check_val) | prompt_template | llm | StrOutputParser()

# print(chain.invoke("china"))

from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(web_path=["https://www.blu-smart.com/"])

doc = loader.load()

print(doc[0])