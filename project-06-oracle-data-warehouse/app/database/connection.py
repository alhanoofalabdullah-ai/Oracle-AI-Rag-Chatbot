import oracledb

from app.config import (
    ORACLE_USER,
    ORACLE_PASSWORD,
    ORACLE_DSN,
)


class OracleConnection:

    def __init__(self):

        self.pool = oracledb.create_pool(

            user=ORACLE_USER,

            password=ORACLE_PASSWORD,

            dsn=ORACLE_DSN,

            min=1,

            max=5,

            increment=1,
        )

    def acquire(self):

        return self.pool.acquire()

    def close(self):

        self.pool.close()
