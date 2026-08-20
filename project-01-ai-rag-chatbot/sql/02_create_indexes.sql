-- ============================================================
-- Project 01 - Oracle AI RAG Chatbot
-- Vector Index
-- ============================================================

CREATE VECTOR INDEX rag_documents_vector_idx

ON rag_documents (
    embedding
)

ORGANIZATION INMEMORY NEIGHBOR GRAPH

DISTANCE COSINE

WITH TARGET ACCURACY 90;
