from models import ChatRequest
from chat_engine import get_response
from crisis import contains_crisis, SAFETY_MESSAGE
from logger import log_chat
from doc_engine import query_document
import os 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "欢迎使用情绪聊天机器人"}

@app.post("/chat")
def chat_with_memory(request: ChatRequest):
    session_id = request.session_id
    query = request.query

    if contains_crisis(query):
        log_chat(session_id=session_id,query=query,response=SAFETY_MESSAGE)
        return {"response":SAFETY_MESSAGE}

    response = get_response(session_id=session_id,query=query)
    log_chat(session_id=session_id,query=query,response=response)
    return {"response":response}

@app.post("/doc_chat")
def chat_with_documents(request: ChatRequest):
    response = query_document(request.query)
    return {"response":response}

