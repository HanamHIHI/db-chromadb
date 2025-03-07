from chromadb.server.fastapi import FastAPI
from chromadb.config import Settings

# ChromaDB 서버 설정
settings = Settings()

# FastAPI 서버 실행
server = FastAPI(settings)
app = server.app