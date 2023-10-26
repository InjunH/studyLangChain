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

from langchain.schema import BaseOutputParser

class CommaSeparatedListOutputParser(BaseOutputParser):
    """Parse the output of an LLM call to a comma-separated list."""


    def parse(self, text: str):
        """Parse the output of an LLM call."""
        return text.strip().split(", ")


# print(help(CommaSeparatedListOutputParser.parse))

CommaSeparatedListOutputParser().parse("hi, bye")
print(CommaSeparatedListOutputParser().parse("hi, bye, sakldjfklsdf, askldjksd"))
# >> ['hi', 'bye']