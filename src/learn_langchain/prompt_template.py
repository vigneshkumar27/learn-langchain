from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain.prompts import ChatPromptTemplate   
from dotenv import load_dotenv

load_dotenv()

llm = AzureChatOpenAI(model="ssdi-dev-4o")


# if it a just a string template
# template = "You are an helpfull assistant"
# prompt = ChatPromptTemplate.from_template(template)

# ---------------------------------------------------------------------------------------

# if its a tuple of prompts with system and ahuman and assistant messages

# template = [
#     ('system',"you are an helpfull assistant"),
#     ('human','what is node')
# ]

# prompt_template = ChatPromptTemplate.from_messages(template)

# prompt = prompt_template.invoke({})

# -----------------------------------------------------------------------------------------

# if its a tuple of prompts with system and ahuman and assistant messages with place holders
# template = [
#     ('system',"you are an helpfull assistant, You responsd to user queries related to {topic}"),
#     ('human','Query : {query}')
# ]

# prompt_template = ChatPromptTemplate.from_messages(template)

# prompt = prompt_template.invoke({"topic":"hindrance","query":"how to comeover"})
# ------------------------------------------------------------------------------------------

# if its a tuple of prompts with system and ahuman and assistant messages with place holders and without placeholders
# if placeholders are not there in any message we canuse messge template also.
template = [
    SystemMessage(content="You are a helpfull assistant."),
    ('human','Query : {query}')
]

prompt_template = ChatPromptTemplate.from_messages(template)

prompt = prompt_template.invoke({"query":"how to comeover"})

# -------------------------------------------------------------------------------------------

result = llm.invoke(prompt)

print(result.content)