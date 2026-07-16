# 📄 AI Document Question Answering API

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.139-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Ollama](https://img.shields.io/badge/LLM-Ollama-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

A local Retrieval-Augmented Generation (RAG) API built with FastAPI, Ollama, and ChromaDB that allows users to upload PDF documents and ask natural language questions based on their content.
## 📖 Project Overview

This project is a local Retrieval-Augmented Generation (RAG) application that enables users to upload PDF documents and ask questions about their content.

The application extracts text from uploaded PDFs, divides the text into overlapping chunks, generates vector embeddings using Ollama's EmbeddingGemma model, and stores them in ChromaDB. When a user submits a question, the system retrieves the most relevant chunks from the vector database and uses the Qwen 2.5 language model running locally through Ollama to generate an accurate answer.

The entire application runs locally without requiring any paid APIs or cloud services.
## 🧠 Architecture

```
User
 │
 ▼
FastAPI
 │
 ▼
PDF Upload
 │
 ▼
Text Extraction
 │
 ▼
Chunking
 │
 ▼
EmbeddingGemma
 │
 ▼
ChromaDB
 │
 ▼
Semantic Search
 │
 ▼
Qwen2.5
 │
 ▼
Answer
```
## ✨ Features

- 📄 Upload PDF documents through a REST API.
- 📖 Extract text from PDF files using PyPDF.
- ✂️ Split extracted text into overlapping chunks.
- 🧠 Generate vector embeddings using Ollama EmbeddingGemma.
- 🗄️ Store embeddings in ChromaDB.
- 🔍 Perform semantic similarity search.
- 🤖 Generate answers using the locally running Qwen 2.5 model.
- 🚀 FastAPI-based REST API with automatic Swagger documentation.
- 🐳 Docker support for containerized deployment.
- 🧪 Unit testing using Pytest.
- 📝 Centralized logging and exception handling.

## 🛠️ Tech Stack

### Backend
- Python 3.12
- FastAPI
- Uvicorn

### AI & Machine Learning
- Ollama
- Qwen 2.5
- EmbeddingGemma

### Vector Database
- ChromaDB

### Document Processing
- PyPDF

### Testing
- Pytest

### Containerization
- Docker
- Docker Compose

## 🏗️ Project Workflow

```text
                Upload PDF
                     │
                     ▼
            Extract Text (PyPDF)
                     │
                     ▼
              Chunk Text
                     │
                     ▼
     Generate Embeddings (Ollama)
                     │
                     ▼
           Store in ChromaDB
                     │
                     ▼
              User Question
                     │
                     ▼
         Generate Question Embedding
                     │
                     ▼
      Retrieve Relevant Chunks
                     │
                     ▼
      Generate Answer (Qwen 2.5)
                     │
                     ▼
             Return Response
```

## 📂 Project Structure

```text
01_Local_RAG_API/
│
├── app/
│   ├── api/
│   │   ├── documents.py
│   │   └── query.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── exceptions.py
│   │   └── logger.py
│   │
│   ├── models/
│   │   └── query_models.py
│   │
│   └── services/
│       ├── embedding_service.py
│       ├── llm_service.py
│       ├── pdf_service.py
│       ├── retrieval_service.py
│       ├── text_service.py
│       └── vector_service.py
│
├── uploads/
├── chroma_db/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── main.py
```

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Sachin-Nagenahalli/AI_Document_Question_Answering_API.git
cd 01_Local_RAG_API
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Virtual Environment

#### macOS/Linux

```bash
source .venv/bin/activate
```

#### Windows

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 🚀 Running the Application

### Start Ollama

Make sure Ollama is running and the required models are available.

```bash
ollama serve
```

If the models are not installed:

```bash
ollama pull qwen2.5:3b
ollama pull embeddinggemma
```

### Start the FastAPI Server

```bash
python -m uvicorn main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000/docs
```
## 🐳 Docker

Build and run the application:

```bash
docker compose up --build
```

Open:

```
http://localhost:8000/docs
```
## 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API information |
| GET | `/health` | Health check |
| POST | `/upload` | Upload a PDF document |
| POST | `/ask` | Ask questions about the uploaded document |

## 🧪 Testing

Run the test suite:

```bash
pytest
```

Current test coverage includes:

- ✅ Root endpoint (`/`)
- ✅ Health endpoint (`/health`)
- ✅ PDF upload endpoint (`/upload`) using mocked dependencies
- ✅ Question answering endpoint (`/ask`) using mocked dependencies

### Testing Strategy

The project uses two complementary testing approaches:

- **Unit Tests:** External services such as Ollama and ChromaDB are mocked to test the application logic in isolation.
- **Integration Testing:** The complete application was manually tested using a real Ollama server, ChromaDB, uploaded PDF documents, and Docker deployment.

## 🚀 Future Improvements

- Support multiple PDF documents.
- Add document management (list and delete documents).
- User authentication and authorization.
- Streaming responses from the language model.
- Hybrid keyword and semantic search.
- Metadata-based filtering.
- Better chunking strategies.
- Conversation history and memory.
- Deploy using cloud infrastructure.
- CI/CD pipeline with GitHub Actions.

## 👨‍💻 Author

**Sachin Nagenahalli**

M.Sc. Biotechnology | AI Engineering & Bioinformatics Enthusiast

GitHub: (https://github.com/sachin-nagenahalli)

LinkedIn: (https://www.linkedin.com/in/sachin-nagenahalli/)
## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.