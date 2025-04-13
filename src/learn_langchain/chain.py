from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain.schema import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableLambda, RunnableParallel
from langchain.schema import StrOutputParser

from dotenv import load_dotenv

load_dotenv()

llm = AzureChatOpenAI(model="")

message_template = [
    (SystemMessage(content='You are a helpfull assistant. You respond to questions shortly and precisely')),
    ('human','Query : {query}')
]

prompt_template = ChatPromptTemplate.from_messages(message_template)

parser = StrOutputParser()

#  --------------- Simple Actual chain -------------------------

# upper_case = RunnableLambda(lambda x : x.upper()print(len(x)))

# chain = prompt_template | llm | parser | upper_case

# result = chain.invoke({"query":"how to view nature"})

# print(result)

# -----------------Behind the scenes -----------------------------

# format_prompt = RunnableLambda(lambda x:prompt_template.format_messages(**x))

# llm_invoke = RunnableLambda(lambda prompt : llm.invoke(prompt))

# output_parser = RunnableLambda(lambda x : x.content)

# chain = RunnableSequence(first=format_prompt,middle=[llm_invoke],last=output_parser)

# print(chain.invoke({"query":"ieurve"}))

# --------------------- Running parallel chain --------------------------

# Example

# chain1= RunnableSequence(first=RunnableLambda(lambda x:print("chain 1 runnable 1")),last=RunnableLambda(lambda x :"c1"))

# chain2 = RunnableSequence(first=RunnableLambda(lambda x:print("chain 2 runnable 1")),last=RunnableLambda(lambda x:"c2"))

# mainchain = RunnableSequence(first=RunnableLambda(lambda x:print("main chain runnable 1")),middle=[RunnableParallel(chain1=chain1,chain2=chain2)],last=RunnableLambda(lambda x:print(x)))

# mainchain.invoke({})

# pros_message_template = [
#     ('system','You are a helpfull assistant. You provide the pros of the given action in point wise 5 points'),
#     ('human','action : {action}')
# ]

# cons_message_template = [
#     ('system','you are a helpfull assistant. You provide the cons of the given action point wise 5 points'),
#     ('human','action : {action}')
# ]



# summarize_message_template = [
#     ('system','You are a helpfull assistant. You give a suggestion based on the given pros and cons, whether action is doable or not suggested precisely'),
#     ('human','pros:: {pros} cons:: {cons}')
# ]

# pros_prompt_template = ChatPromptTemplate.from_messages(pros_message_template)

# cons_prompt_template = ChatPromptTemplate.from_messages(cons_message_template)

# summarize_prompt_template = ChatPromptTemplate.from_messages(summarize_message_template)

# pros_chain = pros_prompt_template | llm | StrOutputParser()

# cons_chain = cons_prompt_template | llm | StrOutputParser()

# chain = RunnableParallel(pros_chain=pros_chain,cons_chain=cons_chain) | RunnableLambda(lambda x: {"pros":x['pros_chain'],"cons":x['cons_chain']}) | summarize_prompt_template | llm | StrOutputParser()

# query = input("Enter your query : ")

# print(chain.invoke({"action":query}))