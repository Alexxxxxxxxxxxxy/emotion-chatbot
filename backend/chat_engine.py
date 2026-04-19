import os
from dotenv import load_dotenv
from langchain_qwq import ChatQwen
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["DASHSCOPE_API_BASE"] = "https://dashscope.aliyuncs.com/compatible-mode/v1"
API_KEY = os.getenv("DASHSCOPE_API_KEY")

if not API_KEY:
    raise ValueError("请在.env文件中设置 DASHSCOPE_API_KEY")

llm = ChatQwen(
    api_key=API_KEY,
    temperature=0.7,
    model="qwen-turbo" 
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个友好的情绪聊天AI助手，请用中文回答用户的问题。"),
    # 🔥 这个占位符是关键：历史对话会自动插入到这里
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

chain = prompt | llm | StrOutputParser()

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

chain_with_memory = RunnableWithMessageHistory(
    runnable=chain, 
    get_session_history=get_session_history, 
    input_messages_key="input",
    history_messages_key="chat_history",
)

def get_response(session_id: str, query: str) -> str:
    """
    多会话聊天接口
    :param session_id: 会话ID（不同用户用不同ID，实现独立记忆）
    :param query: 用户的问题
    :return: AI的回答（直接返回字符串，不是字典）
    """
    response = chain_with_memory.invoke(
        {"input": query},
        config={"configurable": {"session_id": session_id}}
    )
    return response

