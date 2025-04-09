from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage     
from dotenv import load_dotenv

load_dotenv()

llm = AzureChatOpenAI(model="ssdi-dev-4o")

# tuple prompt
# prompt = [
#     ("system","You are an helpfull assistant"),
#     ("human","What is node")
# ]

# formatted prompt
prompt = [
    SystemMessage(content="You are a helpfull assistant"),
    HumanMessage(content="what is node")
]

result = llm.invoke(prompt)

print(result.content)