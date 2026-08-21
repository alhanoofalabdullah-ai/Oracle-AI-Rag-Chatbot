import logging
from contextlib import contextmanager
from typing import Iterator

import oracledb

from app.config import get_settings


logger = logging.getLogger(__name__)


class OracleConnectionManager:
    """
    Oracle connection pool manager.
    """

    def __init__(self) -> None:
        self.settings = get_settings()
        self.pool = None

    def initialize(self) -> None:
        """
        Initialize Oracle connection pool.
        """

        if self.pool is not None:
            return

        logger.info(
            "Initializing Oracle connection pool"
        )

        self.pool = oracledb.create_pool(
            user=self.settings.oracle_user,
            password=self.settings.oracle_password,
            dsn=self.settings.oracle_dsn,
            min=1,
            max=10,
            increment=1,
        )

    @contextmanager
    def connection(self) -> Iterator:
        """
        Acquire and release a database connection.
        """

        if self.pool is None:
            self.initialize()

        connection = self.pool.acquire()

        try:
            yield connection

        finally:
            self.pool.release(connection)

    def close(self) -> None:
        """
        Close the connection pool.
        """

        if self.pool is not None:
            self.pool.close()
            self.pool = None
