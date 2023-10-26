from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import openai
import os
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
llm = OpenAI()
chat_model = ChatOpenAI()

text = "What would be a good company name for a company that makes colorful socks? in korean"

print("result3 : ", llm.predict(text))
# 색깔채운 양말 제조업체
print("result4 :", chat_model.predict(text))
# A good company name for a company that makes colorful socks in Korean could be "무지개 양말" (Mujigae Yangmal), which translates to "Rainbow Socks" in English.
