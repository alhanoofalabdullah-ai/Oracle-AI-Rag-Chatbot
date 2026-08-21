from app.database.repository import OracleRepository


DATABASE_INFO_QUERY = """
SELECT
    name,
    db_unique_name,
    open_mode,
    database_role,
    protection_mode
FROM v$database
"""


INSTANCE_INFO_QUERY = """
SELECT
    instance_name,
    host_name,
    version,
    status,
    startup_time
FROM v$instance
"""


class DatabaseInfoMonitor:

    def __init__(self, repository: OracleRepository):
        self.repository = repository

    def get_database_info(self):
        return self.repository.fetch_dataframe(
            DATABASE_INFO_QUERY
        )

    def get_instance_info(self):
        return self.repository.fetch_dataframe(
            INSTANCE_INFO_QUERY
        )
