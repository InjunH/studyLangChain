from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import openai
import os
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
llm = OpenAI()
chat_model = ChatOpenAI()

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
chain = prompt | model

# stream 실시간으로 보여줌
# print('result stream : ')
# for s in chain.stream({"topic": "bears"}):
#     print(s.content, end="", flush=True)

# print('result invoke : ')
# chain.invoke({"topic": "bears"})
# Why don't bears wear shoes?

# Because they have bear feet!%     

print('result batch : ')
chain.batch([{"topic": "bears"}, {"topic": "cats"}])
print(chain.batch([{"topic": "bears"}, {"topic": "cats"}]))