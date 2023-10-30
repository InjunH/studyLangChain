from langchain.llms import OpenAI
# from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import openai
import os
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.runnable import RunnableParallel
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
llm = OpenAI()
# chat_model = ChatOpenAI()

# # from langchain.embeddings import OpenAIEmbeddings
# # from langchain.schema.output_parser import StrOutputParser
# # # from langchain.schema.runnable import RunnablePassthrough
# # from langchain.vectorstores import FAISS


# # prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
# # chain = prompt | model


model = ChatOpenAI()

chain1 = ChatPromptTemplate.from_template("tell me a joke about {topic}") | model
chain2 = (
    ChatPromptTemplate.from_template("write a short (2 line) poem about {topic}")
    | model
)
combined = RunnableParallel(joke=chain1, poem=chain2)

print(chain1.invoke({"topic": "bears"}))
# content="Why don't bears wear shoes?\n\nBecause they have bear feet!"
print(chain2.invoke({"topic": "bears"}))
# content="Gentle giants roam,\nNature's guardians of home."

print(combined.invoke({"topic": "bears"}))
# {'joke': AIMessage(content="Why don't bears wear shoes?\n\nBecause they already have bear feet!"), 'poem': AIMessage(content='In woods they roam, majestic and wild,\nBears embody strength, fierce and untamed.')}

# model = ChatOpenAI()

# joke_prompt = ChatPromptTemplate.from_template("{topic}에 대한 농담을 해줘")
# poem_prompt = ChatPromptTemplate.from_template("{topic}에 대한 2행 시를 써줘") 

# parallel = RunnableParallel(
#     joke=joke_prompt | model,
#     poem=poem_prompt | model
# )

# print(parallel.invoke({"topic": "곰"}))