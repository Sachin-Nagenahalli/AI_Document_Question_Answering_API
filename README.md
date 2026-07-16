## 📄 AI Document Question Answering API

A local Retrieval-Augmented Generation (RAG) API built with FastAPI, Ollama, and ChromaDB that allows users to upload PDF documents and ask natural language questions based on their content.
## 📖 Project Overview

This project is a local Retrieval-Augmented Generation (RAG) application that enables users to upload PDF documents and ask questions about their content.

The application extracts text from uploaded PDFs, divides the text into overlapping chunks, generates vector embeddings using Ollama's EmbeddingGemma model, and stores them in ChromaDB. When a user submits a question, the system retrieves the most relevant chunks from the vector database and uses the Qwen 2.5 language model running locally through Ollama to generate an accurate answer.

The entire application runs locally without requiring any paid APIs or cloud services.

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