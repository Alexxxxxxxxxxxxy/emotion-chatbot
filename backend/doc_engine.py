import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.dashscope import DashScope, DashScopeGenerationModels
from llama_index.embeddings.dashscope import DashScopeEmbedding

load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")
if not api_key:
    raise ValueError("请设置环境变量 DASHSCOPE_API_KEY")

Settings.llm = DashScope(
    model_name=DashScopeGenerationModels.QWEN_TURBO,
    api_key=api_key,
    temperature=0.3
)

Settings.embed_model = DashScopeEmbedding(
    model_name="text-embedding-v2",
    api_key=api_key
)

documents = SimpleDirectoryReader("data").load_data()

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

def query_document(query: str) -> str:
    response = query_engine.query(query)
    return str(response)