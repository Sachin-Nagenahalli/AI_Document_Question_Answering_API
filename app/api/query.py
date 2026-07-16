import os

from fastapi import APIRouter, HTTPException

from app.core.config import settings
from app.models.query_models import QueryRequest, QueryResponse
from app.services.retrieval_service import find_relevant_chunks
from app.services.llm_service import generate_answer

router = APIRouter()


@router.post("/ask", response_model=QueryResponse)
def ask_question(request: QueryRequest):

    if not os.path.exists(settings.PDF_PATH):
        raise HTTPException(
            status_code=404,
            detail="No document has been uploaded yet."
        )

    retrieved = find_relevant_chunks(request.question)

    answer = generate_answer(
        request.question,
        retrieved["documents"]
    )

    return {
        "question": request.question,
        "answer": answer,
        "sources": retrieved["metadatas"]
    }