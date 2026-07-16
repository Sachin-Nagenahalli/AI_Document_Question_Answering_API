from ollama import Client

from app.core.config import settings

client = Client(host=settings.OLLAMA_HOST)


def create_embedding(text):
    response = client.embed(
        model=settings.EMBEDDING_MODEL,
        input=text
    )

    embeddings = response["embeddings"]

    if isinstance(text, str):
        return embeddings[0]

    return embeddings