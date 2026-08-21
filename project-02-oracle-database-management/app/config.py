from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.
    """

    app_name: str = "Oracle Database Management & Health Monitoring"
    log_level: str = "INFO"

    oracle_user: str
    oracle_password: str
    oracle_dsn: str

    tablespace_warning_percent: float = 75.0
    tablespace_critical_percent: float = 90.0

    session_warning_count: int = 100
    session_critical_count: int = 200

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
