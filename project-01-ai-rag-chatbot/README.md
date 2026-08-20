# Project 01 — Oracle AI RAG Chatbot

An enterprise-grade Retrieval-Augmented Generation (RAG) application powered by Python, LangChain, OpenAI, and Oracle AI Vector Search.

The solution enables users to upload enterprise documents and interact with organizational knowledge through natural-language questions.

---

## Overview

Traditional enterprise document repositories make it difficult for users to quickly locate relevant information.

This project addresses that challenge by combining:

- Large Language Models
- Retrieval-Augmented Generation
- Semantic vector search
- Oracle Database
- Document processing
- Enterprise-oriented application architecture

The system converts uploaded documents into semantic vector representations, stores them in Oracle Database, retrieves the most relevant content for a user's question, and generates a grounded response using the retrieved context.

---

## Business Objective

The primary objective is to provide an AI-powered enterprise knowledge assistant that can help users:

- Search large document repositories
- Retrieve relevant business information
- Ask questions using natural language
- Reduce manual document searching
- Improve knowledge accessibility
- Provide source-aware answers
- Establish a foundation for enterprise Generative AI

---

## Key Features

### Document Management

- PDF ingestion
- DOCX ingestion
- TXT ingestion
- Markdown ingestion
- Document validation
- Text extraction
- Metadata preservation

### AI & RAG

- Text chunking
- Chunk overlap
- OpenAI embeddings
- Semantic vector search
- Oracle AI Vector Search
- Context retrieval
- LLM-based answer generation
- Source attribution

### Enterprise Engineering

- Modular Python architecture
- Oracle connection pooling
- Environment-based configuration
- Logging
- Error handling
- Unit testing
- Docker support

---

# Architecture

```text
                           ┌────────────────────┐
                           │       User         │
                           └─────────┬──────────┘
                                     │
                                     ▼
                           ┌────────────────────┐
                           │   Streamlit UI     │
                           └─────────┬──────────┘
                                     │
                  ┌──────────────────┴──────────────────┐
                  │                                     │
                  ▼                                     ▼
        ┌────────────────────┐              ┌────────────────────┐
        │ Document Upload    │              │ User Question      │
        └─────────┬──────────┘              └─────────┬──────────┘
                  │                                   │
                  ▼                                   ▼
        ┌────────────────────┐              ┌────────────────────┐
        │ Document Loader    │              │ Query Embedding    │
        └─────────┬──────────┘              └─────────┬──────────┘
                  │                                   │
                  ▼                                   │
        ┌────────────────────┐                         │
        │ Text Chunking      │                         │
        └─────────┬──────────┘                         │
                  │                                   │
                  ▼                                   │
        ┌────────────────────┐                         │
        │ OpenAI Embeddings  │                         │
        └─────────┬──────────┘                         │
                  │                                   │
                  └────────────────┬──────────────────┘
                                   ▼
                        ┌────────────────────────┐
                        │ Oracle AI Vector Search│
                        └────────────┬───────────┘
                                     │
                                     ▼
                           ┌────────────────────┐
                           │ Relevant Context   │
                           └─────────┬──────────┘
                                     │
                                     ▼
                           ┌────────────────────┐
                           │ OpenAI LLM          │
                           └─────────┬──────────┘
                                     │
                                     ▼
                           ┌────────────────────┐
                           │ Grounded Answer    │
                           └─────────┬──────────┘
                                     │
                                     ▼
                           ┌────────────────────┐
                           │ Source References  │
                           └────────────────────┘

---

## RAG Pipeline
The application follows the following pipeline:

Documents
    ↓
Text Extraction
    ↓
Text Normalization
    ↓
Chunking
    ↓
Embedding Generation
    ↓
Oracle Vector Storage
    ↓
User Question
    ↓
Query Embedding
    ↓
Vector Similarity Search
    ↓
Top-K Relevant Chunks
    ↓
Context Construction
    ↓
LLM
    ↓
Grounded Response
    ↓
Source References

---

## Technology Stack

| Technology              | Purpose                  |
| ----------------------- | ------------------------ |
| Python                  | Application development  |
| LangChain               | RAG orchestration        |
| OpenAI                  | Embeddings and LLM       |
| Oracle Database         | Enterprise data storage  |
| Oracle AI Vector Search | Semantic retrieval       |
| Streamlit               | Web interface            |
| PyPDF                   | PDF processing           |
| python-docx             | DOCX processing          |
| python-oracledb         | Oracle connectivity      |
| Pydantic                | Configuration management |
| Pytest                  | Automated testing        |
| Docker                  | Containerization         |

---

## Project Structure

project-01-ai-rag-chatbot/
│
├── app/
│   ├── database/
│   ├── documents/
│   ├── embeddings/
│   ├── rag/
│   └── ui/
│
├── sql/
├── tests/
├── docs/
├── screenshots/
│
├── .env.example
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── Dockerfile
├── docker-compose.yml
└── README.md

---

## Installation
Requirements
- Python 3.11+
- Oracle Database with Vector Search support
- OpenAI API key
- Oracle Database credentials
- Docker (optional)

---

## Clone Repository

git clone https://github.com/alhanoofalabdullah-ai/Oracle-System-Projects.git

cd Oracle-System-Projects/project-01-ai-rag-chatbot

---

## Python Environment
# Create a virtual environment:

python -m venv .venv

Activate it.

## Linux / macOS

source .venv/bin/activate

## Windows

.venv\Scripts\activate

# Install dependencies:

pip install -r requirements.txt

---

## Configuration

# Create the environment file:

cp .env.example .env

# Configure:

OPENAI_API_KEY=your-openai-api-key

ORACLE_USER=rag_user

ORACLE_PASSWORD=your-password

ORACLE_DSN=localhost:1521/FREEPDB1

EMBEDDING_MODEL=text-embedding-3-small

CHAT_MODEL=gpt-4.1-mini

EMBEDDING_DIMENSIONS=1536

TOP_K=5

CHUNK_SIZE=900

CHUNK_OVERLAP=150

MAX_UPLOAD_MB=20

---

## Oracle Database
# Run:

@sql/01_create_schema.sql

# Then:

@sql/02_create_indexes.sql

---

## Running the Application
# Start Streamlit:

streamlit run app/main.py

# The application provides:

- Document upload
- Document indexing
- Semantic search
- AI question answering
- Source references
- Database status

---

## Example Questions

After uploading enterprise documents, users can ask:

What is the company's annual leave policy?
What are the project approval requirements?
Who is responsible for the procurement process?
What is the escalation procedure?
What are the key project milestones?

---

## Example RAG Flow

Question:
"What is the project escalation process?"

        ↓

Question Embedding

        ↓

Oracle Vector Search

        ↓

Top 5 Relevant Chunks

        ↓

Context

        ↓

OpenAI LLM

        ↓

Answer

        ↓

[Source 1]
Project-Policy.pdf

[Source 2]
Governance-Manual.pdf

---

## Security Considerations

# Production implementations should include:

- Enterprise SSO
- Role-Based Access Control
- Secrets management
- Encryption
- TLS
- Database auditing
- Document-level authorization
- Prompt injection protection
- Data retention policies
- PII protection

---

## Future Enhancements

# Planned enhancements include:

- FastAPI backend
- React / Next.js frontend
- Enterprise SSO
- RBAC
- Hybrid Search
- Reranking
- Chat History
- Document Versionin
- Admin Dashboard
- Analytics
- Audit Logging
- Docker
- CI/CD
- Oracle Cloud deployment
- RAG evaluation
- AI observability

---


## Skills Demonstrated

# This project demonstrates practical knowledge in:

## Artificial Intelligence

- Generative AI
- RAG
- Embeddings
- LLMs
- Semantic Search
- Vector Search

## Oracle

- Oracle Database
- SQL
- Vector Data
- Vector Indexing
- Database Connectivity
- Query Optimization

## Software Engineering

- Python
- Modular Architecture
- Configuration Management
- Logging
- Testing
- Containerization
- Enterprise Technology
- Enterprise Search
- Knowledge Management
- Digital Transformation
- AI Integration
- Enterprise Architecture

---

## Portfolio Summary

Designed and developed an enterprise Retrieval-Augmented Generation (RAG) solution integrating Python, LangChain, OpenAI, and Oracle AI Vector Search to transform enterprise documents into an intelligent, searchable knowledge platform.

---

## Author

Alhanoof Alabdullah

Enterprise AI | Digital Transformation | Enterprise Systems | RAG | Oracle | Python
