from typing import Any

import pandas as pd

from app.database.connection import (
    OracleConnectionManager,
)


class OracleRepository:
    """
    Repository for Oracle queries.
    """

    def __init__(
        self,
        connection_manager: OracleConnectionManager,
    ) -> None:

        self.connection_manager = (
            connection_manager
        )

    def fetch_dataframe(
        self,
        query: str,
        params: dict[str, Any] | None = None,
    ) -> pd.DataFrame:

        with self.connection_manager.connection() as connection:

            return pd.read_sql(
                query,
                connection,
                params=params or {},
            )

    def fetch_one(
        self,
        query: str,
        params: dict[str, Any] | None = None,
    ) -> tuple | None:

        with self.connection_manager.connection() as connection:

            cursor = connection.cursor()

            cursor.execute(
                query,
                params or {},
            )

            return cursor.fetchone()
