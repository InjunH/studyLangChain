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

print(chain.input_schema.schema())
# {'title': 'PromptInput', 'type': 'object', 'properties': {'topic': {'title': 'Topic'}}}


print(model.input_schema.schema())
# {
#    "title":"ChatOpenAIInput",
#    "anyOf":[
#       {
#          "type":"string"
#       },
#       {
#          "$ref":"#/definitions/StringPromptValue"
#       },
#       {
#          "$ref":"#/definitions/ChatPromptValueConcrete"
#       },
#       {
#          "type":"array",
#          "items":{
#             "anyOf":[
#                {
#                   "$ref":"#/definitions/AIMessage"
#                },
#                {
#                   "$ref":"#/definitions/HumanMessage"
#                },
#                {
#                   "$ref":"#/definitions/ChatMessage"
#                },
#                {
#                   "$ref":"#/definitions/SystemMessage"
#                },
#                {
#                   "$ref":"#/definitions/FunctionMessage"
#                }
#             ]
#          }
#       }
#    ],
#    "definitions":{
#       "StringPromptValue":{
#          "title":"StringPromptValue",
#          "description":"String prompt value.",
#          "type":"object",
#          "properties":{
#             "text":{
#                "title":"Text",
#                "type":"string"
#             }
#          },
#          "required":[
#             "text"
#          ]
#       },
#       "AIMessage":{
#          "title":"AIMessage",
#          "description":"A Message from an AI.",
#          "type":"object",
#          "properties":{
#             "content":{
#                "title":"Content",
#                "type":"string"
#             },
#             "additional_kwargs":{
#                "title":"Additional Kwargs",
#                "type":"object"
#             },
#             "type":{
#                "title":"Type",
#                "default":"ai",
#                "enum":[
#                   "ai"
#                ],
#                "type":"string"
#             },
#             "example":{
#                "title":"Example",
#                "default":false,
#                "type":"boolean"
#             }
#          },
#          "required":[
#             "content"
#          ]
#       },
#       "HumanMessage":{
#          "title":"HumanMessage",
#          "description":"A Message from a human.",
#          "type":"object",
#          "properties":{
#             "content":{
#                "title":"Content",
#                "type":"string"
#             },
#             "additional_kwargs":{
#                "title":"Additional Kwargs",
#                "type":"object"
#             },
#             "type":{
#                "title":"Type",
#                "default":"human",
#                "enum":[
#                   "human"
#                ],
#                "type":"string"
#             },
#             "example":{
#                "title":"Example",
#                "default":false,
#                "type":"boolean"
#             }
#          },
#          "required":[
#             "content"
#          ]
#       },
#       "ChatMessage":{
#          "title":"ChatMessage",
#          "description":"A Message that can be assigned an arbitrary speaker (i.e. role).",
#          "type":"object",
#          "properties":{
#             "content":{
#                "title":"Content",
#                "type":"string"
#             },
#             "additional_kwargs":{
#                "title":"Additional Kwargs",
#                "type":"object"
#             },
#             "type":{
#                "title":"Type",
#                "default":"chat",
#                "enum":[
#                   "chat"
#                ],
#                "type":"string"
#             },
#             "role":{
#                "title":"Role",
#                "type":"string"
#             }
#          },
#          "required":[
#             "content",
#             "role"
#          ]
#       },
#       "SystemMessage":{
#          "title":"SystemMessage",
#          "description":"A Message for priming AI behavior, usually passed in as the first of a sequence\nof input messages.",
#          "type":"object",
#          "properties":{
#             "content":{
#                "title":"Content",
#                "type":"string"
#             },
#             "additional_kwargs":{
#                "title":"Additional Kwargs",
#                "type":"object"
#             },
#             "type":{
#                "title":"Type",
#                "default":"system",
#                "enum":[
#                   "system"
#                ],
#                "type":"string"
#             }
#          },
#          "required":[
#             "content"
#          ]
#       },
#       "FunctionMessage":{
#          "title":"FunctionMessage",
#          "description":"A Message for passing the result of executing a function back to a model.",
#          "type":"object",
#          "properties":{
#             "content":{
#                "title":"Content",
#                "type":"string"
#             },
#             "additional_kwargs":{
#                "title":"Additional Kwargs",
#                "type":"object"
#             },
#             "type":{
#                "title":"Type",
#                "default":"function",
#                "enum":[
#                   "function"
#                ],
#                "type":"string"
#             },
#             "name":{
#                "title":"Name",
#                "type":"string"
#             }
#          },
#          "required":[
#             "content",
#             "name"
#          ]
#       },
#       "ChatPromptValueConcrete":{
#          "title":"ChatPromptValueConcrete",
#          "description":"Chat prompt value which explicitly lists out the message types it accepts.\nFor use in external schemas.",
#          "type":"object",
#          "properties":{
#             "messages":{
#                "title":"Messages",
#                "type":"array",
#                "items":{
#                   "anyOf":[
#                      {
#                         "$ref":"#/definitions/AIMessage"
#                      },
#                      {
#                         "$ref":"#/definitions/HumanMessage"
#                      },
#                      {
#                         "$ref":"#/definitions/ChatMessage"
#                      },
#                      {
#                         "$ref":"#/definitions/SystemMessage"
#                      },
#                      {
#                         "$ref":"#/definitions/FunctionMessage"
#                      }
#                   ]
#                }
#             }
#          },
#          "required":[
#             "messages"
#          ]
#       }
#    }
# }