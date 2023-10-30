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

from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template("{product}을(를) 만드는 회사의 좋은 이름은 무엇인가요?")

print("result :", chat_model.predict(prompt.format(product="신발")))
# result : 좋은 신발 회사 이름은 다양한 요소를 고려하여 선택할 수 있습니다. 다음은 몇 가지 제안입니다:

# 1. 풋스텝 (Footstep) - 건강하고 편안한 신발을 만드는 회사를 나타내며, 사람들이 행복하게 걷는 모습을 상징합니다.
# 2. 워커스 (Walkers) - 신발을 통해 사람들이 걷는 것을 장려하는 회사로, 건강과 활동성을 강조합니다.
# 3. 에어솔 (Airsole) - 통풍이 잘되고 편안한 신발을 만드는 회사를 의미하며, 공기와 관련된 개념을 강조합니다.
# 4. 스텝코 (Stepco) - 사람들이 걸음마다 편안함을 느낄 수 있는 신발을 만드는 회사로, 편안함과 신뢰성을 나타냅니다.
# 5. 피트웨어 (Footwear) - 다양한 종류와 스타일의 신발을 제공하는 회사로, 신발에 대한 폭넓은 선택지를 강조합니다.
# 6. 소울라이프 (SoulLife) - 신발을 통해 사람들이 삶을 즐길 수 있는 회사로, 행복과 삶의 질을 나타냅니다.
# 7. 스텝스타일 (StepStyle) - 신발로 스타일을 완성하는 회사로, 패션과 개성을 강조합니다.
# 8. 컴포트웨어 (Comfortwear) - 편안한 신발을 만드는 회사로, 건강과 편안함을 중시합니다.
# 9. 푸트리퍼 (Footripper) - 고퀄리티의 신발을 만드는 회사로, 튼튼함과 내구성을 강조합니다.
# 10. 무브메이커 (Movemaker) - 사람들이 움직일 수 있는 기회를 제공하는 신발을 만드는 회사로, 활동과 도전을 의미합니다.

# 이름을 선택할 때는 회사의 가치, 제품 특징, 타겟 시장을 고려하여 고유하고 기억에 남는 이름을 선택하는 것이 좋습니다.