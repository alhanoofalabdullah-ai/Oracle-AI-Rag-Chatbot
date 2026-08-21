from app.database.repository import OracleRepository


RECOVERY_STATUS_QUERY = """
SELECT
    recovery_status,
    db_unique_name,
    thread,
    sequence#,
    resetlogs_change#,
    resetlogs_time

FROM v$database
"""


DATABASE_ROLE_QUERY = """
SELECT
    name,
    db_unique_name,
    database_role,
    open_mode,
    protection_mode,
    protection_level

FROM v$database
"""


INSTANCE_QUERY = """
SELECT
    instance_name,
    host_name,
    status,
    version,
    startup_time

FROM v$instance
"""


class RecoveryMonitor:
    """
    Oracle database recovery monitoring.
    """

    def __init__(
        self,
        repository: OracleRepository,
    ) -> None:

        self.repository = repository

    def get_recovery_status(self):

        return self.repository.fetch_dataframe(
            RECOVERY_STATUS_QUERY
        )

    def get_database_role(self):

        return self.repository.fetch_dataframe(
            DATABASE_ROLE_QUERY
        )

    def get_instance_status(self):

        return self.repository.fetch_dataframe(
            INSTANCE_QUERY
        )
