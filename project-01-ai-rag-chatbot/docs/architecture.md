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

---

Question
   |
   v
Query Embedding
   |
   v
Oracle Vector Search
   |
   v
Relevant Chunks
   |
   v
Prompt Context
   |
   v
LLM
   |
   v
Grounded Answer

---

---

# 33. `docs/implementation.md`

```markdown
# Implementation Notes

## Document Ingestion

Documents are loaded using format-specific parsers.

Supported formats:

- PDF
- DOCX
- TXT
- Markdown

---

## Chunking

Documents are normalized and divided into overlapping chunks.

Default:

```text
Chunk size: 900
Overlap: 150

---

The implementation attempts to preserve natural boundaries such as paragraphs and sentences.

Embeddings

Each chunk is transformed into a numerical embedding.

The same embedding model is used to transform user questions.

This allows semantic comparison between:

---

Question Vector
        |
        v
Oracle Vector Search
        |
        v
Document Vectors

---

Retrieval

The application uses Oracle vector distance with cosine distance.

The top K results are passed to the generation layer.

Generation

The LLM receives:

- System instructions
- Retrieved context
- User question

The model is instructed to avoid unsupported information.

Source Attribution

Each retrieved chunk is assigned a source number:

---


Production Improvements

Potential future improvements:

- Hybrid search
- Reranking
- Query rewriting
- Conversation memory
- Access control
- Document versioning
- Observability
- Evaluation
- Prompt-injection detection








