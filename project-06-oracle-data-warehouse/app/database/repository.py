import pandas as pd


class Repository:

    def __init__(
        self,
        connection,
    ):

        self.connection = connection

    def query(
        self,
        sql: str,
    ):

        with self.connection.acquire() as conn:

            return pd.read_sql(
                sql,
                conn,
            )

    def execute(
        self,
        sql: str,
    ):

        with self.connection.acquire() as conn:

            cursor = conn.cursor()

            cursor.execute(sql)

            conn.commit()
