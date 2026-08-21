from typing import Any

import pandas as pd

from app.database.connection import (
    OracleConnectionManager,
)


class OracleRepository:
    """
    Repository used to execute Oracle queries.
    """

    def __init__(
        self,
        connection_manager:
        OracleConnectionManager,
    ):

        self.connection_manager = (
            connection_manager
        )

    def fetch_dataframe(
        self,
        query: str,
        params: dict[str, Any] | None = None,
    ) -> pd.DataFrame:

        connection = (
            self.connection_manager.acquire()
        )

        try:

            return pd.read_sql(
                query,
                connection,
                params=params or {},
            )

        finally:

            self.connection_manager.release(
                connection
            )

    def fetch_one(
        self,
        query: str,
        params: dict[str, Any] | None = None,
    ):

        connection = (
            self.connection_manager.acquire()
        )

        try:

            cursor = connection.cursor()

            cursor.execute(
                query,
                params or {},
            )

            return cursor.fetchone()

        finally:

            self.connection_manager.release(
                connection
            )
