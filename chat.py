from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# LangChain이 지원하는 다른 채팅 모델을 사용합니다. 여기서는 Ollama를 사용합니다.
llm = ChatOllama(model="llama3Ko:latest")

# Prompt 설정
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI Assistant."
            "You will receive the user's uttered sentence in Korean. "
            "In that sentence, classify the emotion as Happy, Sad, Angry, Anxious, Hurt, or Embrassed"
            "tell me only the classified results. "
            "If it is not classified as one of the six emotions, return the result as Not Classified. "
            "Prints only the results without any additional words",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# LangChain 표현식 언어 체인 구문을 사용합니다.
chain = prompt | llm | StrOutputParser()