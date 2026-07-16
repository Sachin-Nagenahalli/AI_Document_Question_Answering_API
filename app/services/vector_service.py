import chromadb

from app.core.config import settings
from app.core.logger import logger


client = chromadb.PersistentClient(
    path=settings.CHROMA_DB_PATH
)

collection = client.get_or_create_collection(
    name=settings.COLLECTION_NAME
)


def store_chunks(chunks, embeddings):
    ids = []
    metadata_list = []

    for i in range(len(chunks)):
        ids.append(f"chunk_{i}")

        metadata_list.append({
            "chunk_id": f"chunk_{i}"
        })

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadata_list
    )

    logger.info(f"Stored {len(chunks)} chunks in ChromaDB")


def search_chunks(query_embedding, top_k=3):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return {
        "documents": results["documents"][0],
        "metadatas": results["metadatas"][0]
    }