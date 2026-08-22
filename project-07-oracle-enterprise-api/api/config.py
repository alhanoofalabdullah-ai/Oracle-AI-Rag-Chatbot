import os

from dotenv import load_dotenv


load_dotenv()


class Settings:

    ORACLE_USER = os.getenv(
        "ORACLE_USER"
    )

    ORACLE_PASSWORD = os.getenv(
        "ORACLE_PASSWORD"
    )

    ORACLE_DSN = os.getenv(
        "ORACLE_DSN"
    )

    API_SECRET_KEY = os.getenv(
        "API_SECRET_KEY"
    )

    API_ENV = os.getenv(
        "API_ENV",
        "development"
    )


settings = Settings()
