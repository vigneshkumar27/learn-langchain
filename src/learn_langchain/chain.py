# from langchain_openai import AzureChatOpenAI
# from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
# from langchain.schema import StrOutputParser
# from langchain.prompts import ChatPromptTemplate   
# from dotenv import load_dotenv

# load_dotenv()

# llm = AzureChatOpenAI(model="ssdi-dev-4o")

# message_template = [
#     (SystemMessage(content='You are a helpfull assistant. You respond to questions shortly and precisely')),
#     ('human','Query : {query}')
# ]

# prompt_template = ChatPromptTemplate.from_messages(message_template)

# chain = prompt_template | llm | StrOutputParser()

# result = chain.invoke({"query":"how to view chat history"})

# print(result)

c = lambda x,y : x + y
print(c(5,6))