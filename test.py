from langserve import RemoteRunnable
from langchain_core.messages import HumanMessage

chain = RemoteRunnable("http://localhost:8085/chat/")

# InputChat의 올바른 형식으로 메시지 리스트를 구성
messages = [
    HumanMessage(content="너무 당황스럽네 라는 말의 감정을 분류해 영어로 결과를 말하고 부가적인 말 없이 결과만 말해")  # HumanMessage로 감싸서 전달
]

for token in chain.stream({"messages": messages}):
    print(token, end="")
