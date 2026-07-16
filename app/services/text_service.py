from app.core.config import settings


def chunk_text(text):
    chunks = []

    chunk_size = settings.CHUNK_SIZE
    overlap = settings.CHUNK_OVERLAP

    step = chunk_size - overlap

    for i in range(0, len(text), step):
        chunk = text[i:i + chunk_size]

        if chunk:
            chunks.append(chunk)

    return chunks