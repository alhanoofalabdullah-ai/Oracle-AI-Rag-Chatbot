import logging
import uuid

from dataclasses import dataclass

from app.config import get_settings
from app.database.repository import (
    DocumentRepository,
    SearchResult,
)
from app.documents.chunker import (
    split_text,
)
from app.documents.loaders import (
    load_document,
)
from app.embeddings.openai_embeddings import (
    embed_documents,
)
from app.rag.generator import (
    AnswerGenerator,
)
from app.rag.retriever import (
    VectorRetriever,
)


logger = logging.getLogger(__name__)


@dataclass
class IngestionSummary:
    """
    Result of document ingestion.
    """

    document_id: str
    file_name: str
    chunks_created: int


class RAGService:
    """
    Main application service coordinating:

    Document ingestion
    Embedding generation
    Oracle persistence
    Vector retrieval
    LLM generation
    """

    def __init__(self):

        self.settings = get_settings()

        self.repository = (
            DocumentRepository()
        )

        self.retriever = (
            VectorRetriever(
                repository=self.repository
            )
        )

        self.generator = (
            AnswerGenerator()
        )

    # --------------------------------------------------
    # Document Ingestion
    # --------------------------------------------------

    def ingest(
        self,
        file_name: str,
        data: bytes,
    ) -> IngestionSummary:

        max_bytes = (
            self.settings.max_upload_mb
            * 1024
            * 1024
        )

        if len(data) > max_bytes:

            raise ValueError(
                f"File '{file_name}' exceeds "
                f"the maximum upload size of "
                f"{self.settings.max_upload_mb} MB."
            )

        document = load_document(
            file_name,
            data,
        )

        chunks = split_text(
            document.text,
            chunk_size=(
                self.settings.chunk_size
            ),
            chunk_overlap=(
                self.settings.chunk_overlap
            ),
        )

        if not chunks:

            raise ValueError(
                "The document did not produce "
                "any usable text chunks."
            )

        document_id = str(
            uuid.uuid4()
        )

        texts = [
            chunk.content
            for chunk in chunks
        ]

        vectors = embed_documents(
            texts
        )

        for chunk, vector in zip(
            chunks,
            vectors,
        ):

            metadata = {
                **document.metadata,
                **chunk.metadata,
                "document_id": document_id,
            }

            self.repository.insert_chunk(
                document_id=document_id,
                file_name=file_name,
                chunk_index=chunk.index,
                content=chunk.content,
                metadata=metadata,
                embedding=vector,
            )

        logger.info(
            "Document indexed successfully: "
            "file=%s document_id=%s chunks=%s",
            file_name,
            document_id,
            len(chunks),
        )

        return IngestionSummary(
            document_id=document_id,
            file_name=file_name,
            chunks_created=len(chunks),
        )

    # --------------------------------------------------
    # Retrieval
    # --------------------------------------------------

    def retrieve(
        self,
        question: str,
        top_k: int | None = None,
    ) -> list[SearchResult]:

        return self.retriever.retrieve(
            question=question,
            top_k=top_k,
        )

    # --------------------------------------------------
    # Question Answering
    # --------------------------------------------------

    def answer(
        self,
        question: str,
    ) -> tuple[
        str,
        list[SearchResult],
    ]:

        results = self.retrieve(
            question
        )

        answer = self.generator.generate(
            question=question,
            results=results,
        )

        return (
            answer,
            results,
        )

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(self) -> dict:

        return {
            "documents": (
                self.repository
                .count_documents()
            ),
            "chunks": (
                self.repository
                .count_chunks()
            ),
        }
