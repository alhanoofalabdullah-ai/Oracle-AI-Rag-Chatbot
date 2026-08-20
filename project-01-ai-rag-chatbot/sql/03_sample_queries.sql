-- ============================================================
-- Project 01 - Sample Oracle Queries
-- ============================================================


-- ------------------------------------------------------------
-- 1. Count all chunks
-- ------------------------------------------------------------

SELECT COUNT(*) AS total_chunks
FROM rag_documents;


-- ------------------------------------------------------------
-- 2. Count unique documents
-- ------------------------------------------------------------

SELECT COUNT(
    DISTINCT document_id
) AS total_documents
FROM rag_documents;


-- ------------------------------------------------------------
-- 3. List indexed documents
-- ------------------------------------------------------------

SELECT
    document_id,
    file_name,
    COUNT(*) AS chunks,
    MIN(created_at) AS indexed_at
FROM rag_documents
GROUP BY
    document_id,
    file_name
ORDER BY indexed_at DESC;


-- ------------------------------------------------------------
-- 4. Show recent chunks
-- ------------------------------------------------------------

SELECT
    file_name,
    chunk_index,
    created_at
FROM rag_documents
ORDER BY created_at DESC
FETCH FIRST 20 ROWS ONLY;


-- ------------------------------------------------------------
-- 5. Delete a document
-- ------------------------------------------------------------

DELETE FROM rag_documents
WHERE document_id = 'DOCUMENT-ID-HERE';

COMMIT;


-- ------------------------------------------------------------
-- 6. Vector search example
-- ------------------------------------------------------------

SELECT
    file_name,
    chunk_index,
    content,
    VECTOR_DISTANCE(
        embedding,
        TO_VECTOR(
            :query_embedding
        ),
        COSINE
    ) AS distance
FROM rag_documents
ORDER BY distance
FETCH FIRST 5 ROWS ONLY;
