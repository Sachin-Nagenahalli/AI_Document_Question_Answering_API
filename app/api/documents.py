from fastapi import APIRouter, UploadFile, File

from app.core.config import settings
from app.core.logger import logger

from app.services.pdf_service import extract_text
from app.services.text_service import chunk_text
from app.services.embedding_service import create_embedding
from app.services.vector_service import store_chunks

router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    file_content = await file.read()

    with open(settings.PDF_PATH, "wb") as pdf_file:
        pdf_file.write(file_content)

    logger.info("PDF uploaded successfully")

    text = extract_text(settings.PDF_PATH)

    chunks = chunk_text(text)
    logger.info(f"Created {len(chunks)} chunks")

    embeddings = create_embedding(chunks)

    store_chunks(chunks, embeddings)

    logger.info("Embeddings stored successfully")

    return {
        "text_length": len(text),
        "number_of_chunks": len(chunks)
    }
    