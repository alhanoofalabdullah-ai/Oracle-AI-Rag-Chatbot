from app.database.repository import OracleRepository


SYSTEM_METRICS_QUERY = """
SELECT
    metric_name,
    value,
    metric_unit,
    begin_time,
    end_time
FROM v$sysmetric
WHERE group_id = 2
ORDER BY metric_name
"""


INSTANCE_QUERY = """
SELECT
    instance_name,
    host_name,
    version,
    status,
    startup_time
FROM v$instance
"""


DATABASE_QUERY = """
SELECT
    name,
    db_unique_name,
    open_mode,
    database_role,
    protection_mode
FROM v$database
"""


class PerformanceMonitor:
    """
    Collects high-level Oracle performance information.
    """

    def __init__(
        self,
        repository: OracleRepository,
    ) -> None:

        self.repository = repository

    def get_system_metrics(self):
        return self.repository.fetch_dataframe(
            SYSTEM_METRICS_QUERY
        )

    def get_instance_information(self):
        return self.repository.fetch_dataframe(
            INSTANCE_QUERY
        )

    def get_database_information(self):
        return self.repository.fetch_dataframe(
            DATABASE_QUERY
        )
