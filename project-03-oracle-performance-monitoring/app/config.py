from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration.
    """

    app_name: str = (
        "Oracle Performance Monitoring & SQL Tuning Platform"
    )

    log_level: str = "INFO"

    oracle_user: str
    oracle_password: str
    oracle_dsn: str

    cpu_warning_percent: float = 70.0
    cpu_critical_percent: float = 90.0

    tablespace_warning_percent: float = 75.0
    tablespace_critical_percent: float = 90.0

    active_session_warning: int = 50
    active_session_critical: int = 100

    sql_elapsed_warning_seconds: float = 5.0
    sql_elapsed_critical_seconds: float = 30.0

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
