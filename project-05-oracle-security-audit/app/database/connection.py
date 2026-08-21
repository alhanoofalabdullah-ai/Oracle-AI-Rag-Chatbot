import logging

import oracledb

from app.config import get_settings


logger = logging.getLogger(__name__)


class OracleConnectionManager:
    """
    Oracle connection pool manager.
    """

    def __init__(self):

        self.settings = get_settings()

        self.pool = None

    def initialize(self):

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

    def acquire(self):

        if self.pool is None:
            self.initialize()

        return self.pool.acquire()

    def release(self, connection):

        self.pool.release(connection)

    def close(self):

        if self.pool is not None:

            self.pool.close()

            self.pool = None
