from functools import lru_cache

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Central application configuration.

    Values are loaded from environment variables
    and the local .env file.
    """

    app_name: str = Field(
        default="Oracle AI RAG Chatbot",
        alias="APP_NAME",
    )

    log_level: str = Field(
        default="INFO",
        alias="LOG_LEVEL",
    )

    # --------------------------------------------------
    # OpenAI
    # --------------------------------------------------

    openai_api_key: str = Field(
        default="",
        alias="OPENAI_API_KEY",
    )

    embedding_model: str = Field(
        default="text-embedding-3-small",
        alias="EMBEDDING_MODEL",
    )

    chat_model: str = Field(
        default="gpt-4.1-mini",
        alias="CHAT_MODEL",
    )

    embedding_dimensions: int = Field(
        default=1536,
        alias="EMBEDDING_DIMENSIONS",
    )

    # --------------------------------------------------
    # Oracle
    # --------------------------------------------------

    oracle_user: str = Field(
        default="",
        alias="ORACLE_USER",
    )

    oracle_password: str = Field(
        default="",
        alias="ORACLE_PASSWORD",
    )

    oracle_dsn: str = Field(
        default="",
        alias="ORACLE_DSN",
    )

    # --------------------------------------------------
    # RAG
    # --------------------------------------------------

    top_k: int = Field(
        default=5,
        alias="TOP_K",
    )

    chunk_size: int = Field(
        default=900,
        alias="CHUNK_SIZE",
    )

    chunk_overlap: int = Field(
        default=150,
        alias="CHUNK_OVERLAP",
    )

    max_upload_mb: int = Field(
        default=20,
        alias="MAX_UPLOAD_MB",
    )

    # --------------------------------------------------
    # Oracle Connection Pool
    # --------------------------------------------------

    pool_min: int = Field(
        default=1,
        alias="POOL_MIN",
    )

    pool_max: int = Field(
        default=5,
        alias="POOL_MAX",
    )

    pool_increment: int = Field(
        default=1,
        alias="POOL_INCREMENT",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        populate_by_name=True,
        extra="ignore",
    )

    @field_validator("chunk_overlap")
    @classmethod
    def validate_chunk_overlap(
        cls,
        value: int,
        info,
    ) -> int:

        chunk_size = info.data.get(
            "chunk_size",
            900,
        )

        if value < 0:
            raise ValueError(
                "CHUNK_OVERLAP cannot be negative."
            )

        if value >= chunk_size:
            raise ValueError(
                "CHUNK_OVERLAP must be smaller "
                "than CHUNK_SIZE."
            )

        return value

    def validate_runtime(self) -> list[str]:
        """
        Validate required production configuration.
        """

        errors: list[str] = []

        if not self.openai_api_key:
            errors.append(
                "OPENAI_API_KEY is not configured."
            )

        if not self.oracle_user:
            errors.append(
                "ORACLE_USER is not configured."
            )

        if not self.oracle_password:
            errors.append(
                "ORACLE_PASSWORD is not configured."
            )

        if not self.oracle_dsn:
            errors.append(
                "ORACLE_DSN is not configured."
            )

        return errors


@lru_cache
def get_settings() -> Settings:
    """
    Return a cached Settings instance.
    """

    return Settings()
