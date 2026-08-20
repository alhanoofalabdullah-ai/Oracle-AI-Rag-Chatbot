-- ============================================================
-- Project 01 - Oracle AI RAG Chatbot
-- Database Schema
-- ============================================================

CREATE TABLE rag_documents (

    chunk_id
        RAW(16)
        DEFAULT SYS_GUID()
        PRIMARY KEY,

    document_id
        VARCHAR2(64)
        NOT NULL,

    file_name
        VARCHAR2(512)
        NOT NULL,

    chunk_index
        NUMBER(10)
        NOT NULL,

    content
        CLOB
        NOT NULL,

    metadata
        JSON,

    embedding
        VECTOR(1536, FLOAT32),

    created_at
        TIMESTAMP
        DEFAULT SYSTIMESTAMP
        NOT NULL
);


-- Document lookup
CREATE INDEX rag_documents_document_idx
ON rag_documents (
    document_id
);


-- File lookup
CREATE INDEX rag_documents_filename_idx
ON rag_documents (
    file_name
);


-- Timestamp lookup
CREATE INDEX rag_documents_created_idx
ON rag_documents (
    created_at
);
