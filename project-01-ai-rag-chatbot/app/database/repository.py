import json
import logging

from dataclasses import dataclass
from typing import Any

from app.database.connection import (
    get_connection
)


logger = logging.getLogger(__name__)


@dataclass
class SearchResult:
    """
    Represents one retrieved document chunk.
    """

    chunk_id: str
    document_id: str
    file_name: str
    chunk_index: int
    content: str
    distance: float
    metadata: dict[str, Any]


class DocumentRepository:
    """
    Repository responsible for document persistence
    and vector retrieval.
    """

    # --------------------------------------------------
    # Insert
    # --------------------------------------------------

    def insert_chunk(
        self,
        document_id: str,
        file_name: str,
        chunk_index: int,
        content: str,
        metadata: dict[str, Any],
        embedding: list[float],
    ) -> None:

        sql = """
            INSERT INTO rag_documents (
                chunk_id,
                document_id,
                file_name,
                chunk_index,
                content,
                metadata,
                embedding
            )
            VALUES (
                SYS_GUID(),
                :document_id,
                :file_name,
                :chunk_index,
                :content,
                :metadata,
                TO_VECTOR(:embedding)
            )
        """

        embedding_json = json.dumps(
            embedding
        )

        metadata_json = json.dumps(
            metadata
        )

        with get_connection() as connection:

            with connection.cursor() as cursor:

                cursor.execute(
                    sql,
                    {
                        "document_id": document_id,
                        "file_name": file_name,
                        "chunk_index": chunk_index,
                        "content": content,
                        "metadata": metadata_json,
                        "embedding": embedding_json,
                    },
                )

            connection.commit()

    # --------------------------------------------------
    # Delete
    # --------------------------------------------------

    def delete_document(
        self,
        document_id: str,
    ) -> int:

        sql = """
            DELETE FROM rag_documents
            WHERE document_id = :document_id
        """

        with get_connection() as connection:

            with connection.cursor() as cursor:

                cursor.execute(
                    sql,
                    {
                        "document_id": document_id
                    },
                )

                deleted = cursor.rowcount

            connection.commit()

        return deleted

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(
        self,
        query_embedding: list[float],
        top_k: int,
    ) -> list[SearchResult]:

        sql = """
            SELECT
                RAWTOHEX(chunk_id),
                document_id,
                file_name,
                chunk_index,
                content,
                VECTOR_DISTANCE(
                    embedding,
                    TO_VECTOR(:query_embedding),
                    COSINE
                ) AS distance,
                metadata
            FROM rag_documents
            ORDER BY distance
            FETCH FIRST :top_k ROWS ONLY
        """

        embedding_json = json.dumps(
            query_embedding
        )

        results: list[SearchResult] = []

        with get_connection() as connection:

            with connection.cursor() as cursor:

                cursor.execute(
                    sql,
                    {
                        "query_embedding": embedding_json,
                        "top_k": top_k,
                    },
                )

                rows = cursor.fetchall()

        for row in rows:

            metadata = row[6]

            if hasattr(
                metadata,
                "read",
            ):
                metadata = metadata.read()

            if isinstance(
                metadata,
                str,
            ):

                try:

                    metadata = json.loads(
                        metadata
                    )

                except json.JSONDecodeError:

                    metadata = {}

            results.append(
                SearchResult(
                    chunk_id=str(row[0]),
                    document_id=str(row[1]),
                    file_name=str(row[2]),
                    chunk_index=int(row[3]),
                    content=str(row[4]),
                    distance=float(row[5]),
                    metadata=metadata or {},
                )
            )

        return results

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def count_chunks(self) -> int:

        sql = """
            SELECT COUNT(*)
            FROM rag_documents
        """

        with get_connection() as connection:

            with connection.cursor() as cursor:

                cursor.execute(sql)

                row = cursor.fetchone()

                return int(row[0])

    def count_documents(self) -> int:

        sql = """
            SELECT COUNT(
                DISTINCT document_id
            )
            FROM rag_documents
        """

        with get_connection() as connection:

            with connection.cursor() as cursor:

                cursor.execute(sql)

                row = cursor.fetchone()

                return int(row[0])

    def list_documents(self):

        sql = """
            SELECT
                document_id,
                file_name,
                COUNT(*) AS chunk_count,
                MIN(created_at) AS created_at
            FROM rag_documents
            GROUP BY
                document_id,
                file_name
            ORDER BY created_at DESC
        """

        with get_connection() as connection:

            with connection.cursor() as cursor:

                cursor.execute(sql)

                return cursor.fetchall()
