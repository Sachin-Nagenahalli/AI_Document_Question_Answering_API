from app.core.logger import logger

from app.services.embedding_service import create_embedding
from app.services.vector_service import search_chunks


def find_relevant_chunks(question):
    question_embedding = create_embedding(question)

    relevant_chunks = search_chunks(question_embedding)

    logger.info(
        f"Retrieved {len(relevant_chunks['documents'])} relevant chunks"
    )

    return relevant_chunks