from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import openai
import os
from langchain.schema import HumanMessage
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
llm = OpenAI()
chat_model = ChatOpenAI()

from langchain.prompts.chat import ChatPromptTemplate

template = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

# chat_prompt.format_messages(input_language="English", output_language="korean", text="I love programming.")
# print("chat_prompt :", chat_prompt.format_messages(input_language="English", output_language="korean", text="I love programming."))
# # result : [SystemMessage(content='You are a helpful assistant that translates English to korean.'), HumanMessage(content='I love programming.')]


content = chat_prompt.format_messages(input_language="English", output_language="Japanese", text="I love programming.")
messages = [content[1]]

print("result :", llm.predict_messages(messages).content)
# Computer: That's great! Programming is a great way to learn new skills and stay connected with technology.