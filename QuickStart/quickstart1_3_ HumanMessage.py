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

text = "컬러풀한 양말을 만드는 회사의 회사명은 어떤 것이 좋을까요?"
messages = [HumanMessage(content=text)]

print("result 5 :", llm.predict_messages(messages))
# result 5 : content='\n\nRobot: 컬러풀한 양말 코리아, 색다른 양말 샵, 컬러플라워 양말 디자인, 다크색 양말 디자인 등이 있습니다.'
print("result 5_1 :", llm.predict_messages(messages).content)
# Robot: 당신이 창업하고자 하는 회사명이신가요? 멋진 회사명 생각해보기 가능한 아이디어로는 "Rainbow Socks", "Colorful Toes", "Splashy Hues", "Vibrant Hues" 등이 있을 수 있습니다.



print("result 6 :", chat_model.predict_messages(messages))
print("result 6_1 :", chat_model.predict_messages(messages).content)
# result 6 : content='1. "Rainbow Socks"\n2. "Vivid Threads"\n3. "Chroma Sox"\n4. "Colorful Stitches"\n5. "Spectrum Socks"\n6. "Brilliant Hues"\n7. "Dazzling Designs"\n8. "Chromatic Sox"\n9. "Vibrant Footwear"\n10. "Prismatic Socks"'
# result 6_1 : 1. 레인보우 소크스 (Rainbow Socks)
# 2. 컬러풀 피트 (Colorful Feet)
# 3. 브라이트 스타킹 (Bright Stockings)
# 4. 플레이풀 소크스 (Playful Socks)
# 5. 컬러파이브 (Color Five)
# 6. 패션풀 양말 (Fashionful Socks)
# 7. 러블리 삭스 (Lovely Socks)
# 8. 비비드 소크스 (Vivid Socks)
# 9. 매직소크스 (Magic Socks)
# 10. 새로미 (Saromi)