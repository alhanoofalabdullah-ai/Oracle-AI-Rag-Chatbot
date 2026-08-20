from functools import lru_cache

from langchain_openai import (
    OpenAIEmbeddings,
)

from app.config import get_settings


@lru_cache
def get_embedding_model():
    """
    Return a cached OpenAI embedding client.
    """

    settings = get_settings()

    return OpenAIEmbeddings(
        model=settings.embedding_model,
        dimensions=settings.embedding_dimensions,
        api_key=settings.openai_api_key,
    )


def embed_documents(
    documents: list[str],
) -> list[list[float]]:

    model = get_embedding_model()

    return model.embed_documents(
        documents
    )


def embed_query(
    query: str,
) -> list[float]:

    model = get_embedding_model()

    return model.embed_query(
        query
    )
