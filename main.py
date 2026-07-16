from fastapi import FastAPI

from app.api.documents import router as documents_router
from app.api.query import router as query_router
from app.core.exceptions import global_exception_handler

app = FastAPI(
    title="AI Document Question Answering API",
    version="1.0.0",
    description=(
        "A local Retrieval-Augmented Generation (RAG) API "
        "built with FastAPI, Ollama, and ChromaDB."
    ),
)

app.add_exception_handler(
    Exception,
    global_exception_handler
)

app.include_router(documents_router)
app.include_router(query_router)


@app.get("/")
def root():
    return {
        "project": "AI Document Question Answering API",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }