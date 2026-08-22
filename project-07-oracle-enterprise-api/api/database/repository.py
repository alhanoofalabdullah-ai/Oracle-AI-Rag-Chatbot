class Repository:

    def __init__(self, database):

        self.database = database


    def fetch_all(
        self,
        sql,
        parameters=None
    ):

        with self.database.acquire() as conn:

            cursor = conn.cursor()

            cursor.execute(
                sql,
                parameters or {}
            )

            columns = [
                column[0].lower()
                for column in cursor.description
            ]

            rows = cursor.fetchall()

            return [
                dict(zip(columns, row))
                for row in rows
            ]


    def execute(
        self,
        sql,
        parameters=None
    ):

        with self.database.acquire() as conn:

            cursor = conn.cursor()

            cursor.execute(
                sql,
                parameters or {}
            )

            conn.commit()
