# Architecture

## Overview

Oracle AI RAG Chatbot follows a modular enterprise-oriented architecture.

## Layers

### Presentation Layer

Streamlit provides:

- Document upload
- Chat interface
- System status
- Source display

### Application Layer

The RAG service coordinates:

- Document ingestion
- Embeddings
- Retrieval
- Answer generation

### Data Layer

Oracle Database provides:

- Document chunks
- Metadata
- Vector embeddings
- Vector similarity search

### AI Layer

OpenAI provides:

- Text embeddings
- Large Language Model generation

---

## Data Flow

```text
Document
   |
   v
Parser
   |
   v
Chunker
   |
   v
Embedding Model
   |
   v
Oracle Vector Database
