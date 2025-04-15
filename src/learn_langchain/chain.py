from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain.schema import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableLambda, RunnableParallel, RunnableBranch
from langchain.schema import StrOutputParser

from dotenv import load_dotenv

load_dotenv()

llm = AzureChatOpenAI(model="ssdi-dev-4o")

message_template = [
    (SystemMessage(content='You are a helpfull assistant. You respond to questions shortly and precisely')),
    ('human','Query : {query}')
]

prompt_template = ChatPromptTemplate.from_messages(message_template)

parser = StrOutputParser()

#  1.--------------- Simple Actual chain -------------------------

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

# 2.--------------------- Running parallel chain --------------------------

# Example

# chain1= RunnableSequence(first=RunnableLambda(lambda x:print("chain 1 runnable 1")),last=RunnableLambda(lambda x :"c1"))

# chain2 = RunnableSequence(first=RunnableLambda(lambda x:print("chain 2 runnable 1")),last=RunnableLambda(lambda x:"c2"))

# mainchain = RunnableSequence(first=RunnableLambda(lambda x:print("main chain runnable 1")),middle=[RunnableParallel(chain1=chain1,chain2=chain2)],last=RunnableLambda(lambda x:print(x)))

# mainchain.invoke({})

# Example 2

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

# 3.------------------------Chain branching ---------------------------------

# chain1 = RunnableSequence(first=RunnableLambda(lambda x:print("chain 1 runnable first")),last=RunnableLambda(lambda x:print("chain1 runnable last")))
# chain2 = RunnableSequence(first=RunnableLambda(lambda x:print("chain 2 runnable first")),last=RunnableLambda(lambda x:print("chain2 2runnable last")))
# chain3 = RunnableSequence(first=RunnableLambda(lambda x:print("chain 3 runnable first")),last=RunnableLambda(lambda x:print("chain3 runnable last")))
# chain4 = RunnableSequence(first=RunnableLambda(lambda x:print("chain 4 runnable first")),last=RunnableLambda(lambda x:print("chain4 runnable last")))

# chain = RunnableLambda(lambda x:x) | RunnableBranch((lambda x:x==1,chain1),(lambda x:x==2,chain2),(lambda x:x==3,chain3),(lambda x:x==4,chain4),(lambda x:x==1,chain1),lambda x:x)

# chain.invoke(1)

# Example

feedback_positive = "Absolutely love this backpack! The material feels durable, the zippers are smooth, and it has enough compartments to keep everything organized. Totally worth the price!"

feedback_negative = "The headphones stopped working after just two weeks. The sound quality was poor from the beginning, and the battery life was nothing like what was advertised. Very disappointed."

feedback_neutral = "The jacket looks okay and fits as expected. Nothing special about the quality, but it does the job for the price. Might consider other brands next time."

message_template = [
    SystemMessage(content="You are an assistant who evalute the user feedback and provide a response either of the codes given as follows \n Codes : 1.Positive 2.Negative 3.Neutral"),
    ('human','Feedback to be analysed :  {feedback}')
]

prompt_template = ChatPromptTemplate.from_messages(message_template)

positve_prompt_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="You are a helpfull assistant who generate a thankfull note to the user who provided a positive feedback to the product base on the feedback"),
        ('human','feedback : {feedback}')
    ]
)

negative_prompt_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="You are a helpfull assistant who generate a sorry note to the user who provided a negative feedback to the product base on the feedback"),
        ('human','feedback : {feedback}')
    ]
)

negative_prompt_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="You are a helpfull assistant who generate a note to the user who provided a neutral feedback to the product base on the feedback"),
        ('human','feedback : {feedback}')
    ]
)

positive_chain = positve_prompt_template | llm

negative_chain = negative_prompt_template | llm

neutral_chain = negative_prompt_template | llm

branch = RunnableBranch((lambda x : 'positive' in x['response'].lower(),positive_chain),(lambda x:'negative' in x['response'].lower(),negative_chain),neutral_chain)

combine_runnable = RunnableLambda( lambda x: {"response" : x , "feedback": feedback_neutral}) # change **************

chain = prompt_template | llm | StrOutputParser() | combine_runnable | branch | StrOutputParser()


print(chain.invoke({"feedback":feedback_neutral})) # chainge **********