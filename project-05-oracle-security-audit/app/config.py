from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration.
    """

    app_name: str = (
        "Oracle Database Security & Audit Platform"
    )

    log_level: str = "INFO"

    oracle_user: str
    oracle_password: str
    oracle_dsn: str

    inactive_days: int = 90
    password_warning_days: int = 14

    failed_login_warning: int = 5
    failed_login_critical: int = 10

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
