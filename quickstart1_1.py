from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import openai
import os
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
llm = OpenAI()
chat_model = ChatOpenAI()

result1 = llm.predict("안녕!")
print('result1 : ',result1)

result2 = chat_model.predict("안녕!")
print('result2 : ',result2)