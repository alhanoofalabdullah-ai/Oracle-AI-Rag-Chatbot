from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration.
    """

    app_name: str = (
        "Oracle Backup, Recovery & Disaster Recovery Platform"
    )

    log_level: str = "INFO"

    oracle_user: str
    oracle_password: str
    oracle_dsn: str

    backup_warning_hours: int = 24
    backup_critical_hours: int = 48

    archive_warning_percent: float = 70.0
    archive_critical_percent: float = 90.0

    recovery_warning_days: int = 7
    recovery_critical_days: int = 30

    rman_executable: str = "rman"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
