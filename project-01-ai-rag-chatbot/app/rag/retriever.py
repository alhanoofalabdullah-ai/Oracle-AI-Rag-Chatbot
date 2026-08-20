from app.config import get_settings
from app.database.repository import (
    DocumentRepository,
    SearchResult,
)
from app.embeddings.openai_embeddings import (
    embed_query,
)


class VectorRetriever:
    """
    Converts a question into an embedding
    and retrieves relevant document chunks
    from Oracle Vector Search.
    """

    def __init__(
        self,
        repository: DocumentRepository | None = None,
    ):

        self.settings = get_settings()

        self.repository = (
            repository
            or DocumentRepository()
        )

    def retrieve(
        self,
        question: str,
        top_k: int | None = None,
    ) -> list[SearchResult]:

        question = question.strip()

        if not question:

            return []

        vector = embed_query(
            question
        )

        return self.repository.search(
            query_embedding=vector,
            top_k=(
                top_k
                or self.settings.top_k
            ),
        )
