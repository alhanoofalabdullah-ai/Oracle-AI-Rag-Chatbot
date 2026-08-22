import os

import oracledb

from dotenv import load_dotenv


load_dotenv()


class Database:

    def __init__(self):

        self.pool = oracledb.create_pool(

            user=os.getenv(
                "ORACLE_USER"
            ),

            password=os.getenv(
                "ORACLE_PASSWORD"
            ),

            dsn=os.getenv(
                "ORACLE_DSN"
            ),

            min=1,

            max=10,

            increment=1,
        )


    def acquire(self):

        return self.pool.acquire()


    def close(self):

        self.pool.close()
