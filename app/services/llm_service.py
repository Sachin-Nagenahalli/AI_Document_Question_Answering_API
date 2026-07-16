from ollama import Client

from app.core.config import settings

client = Client(host=settings.OLLAMA_HOST)


def generate_answer(question, relevant_chunks):

    context = "\n".join(relevant_chunks)

    response = client.chat(
        model=settings.MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a document question-answering assistant. "
                    "Answer ONLY from the provided document context. "
                    "If the answer is not present in the context, say: "
                    "'The provided document does not contain enough information to answer this question.'"
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Document Context:\n{context}\n\n"
                    f"Question:\n{question}"
                ),
            },
        ],
    )

    return response["message"]["content"]