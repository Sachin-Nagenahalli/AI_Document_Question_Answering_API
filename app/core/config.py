class Settings:
    MODEL_NAME = "qwen2.5:3b"
    EMBEDDING_MODEL = "embeddinggemma"

    OLLAMA_HOST = "http://host.docker.internal:11434"

    CHROMA_DB_PATH = "./chroma_db"
    COLLECTION_NAME = "documents"

    PDF_PATH = "uploads/sample.pdf"

    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200

settings = Settings()