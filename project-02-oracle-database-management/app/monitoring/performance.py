from app.database.repository import OracleRepository


SYSTEM_METRICS_QUERY = """
SELECT
    metric_name,
    value,
    metric_unit
FROM v$sysmetric
WHERE group_id = 2
ORDER BY metric_name
"""


TOP_SQL_QUERY = """
SELECT
    sql_id,
    executions,
    ROUND(
        elapsed_time / 1000000,
        2
    ) AS elapsed_seconds,
    ROUND(
        cpu_time / 1000000,
        2
    ) AS cpu_seconds,
    buffer_gets,
    disk_reads
FROM v$sql
WHERE executions > 0
ORDER BY elapsed_time DESC
FETCH FIRST 20 ROWS ONLY
"""


WAIT_EVENTS_QUERY = """
SELECT
    event,
    total_waits,
    time_waited
FROM v$system_event
ORDER BY time_waited DESC
FETCH FIRST 20 ROWS ONLY
"""


class PerformanceMonitor:

    def __init__(self, repository: OracleRepository):
        self.repository = repository

    def get_system_metrics(self):
        return self.repository.fetch_dataframe(
            SYSTEM_METRICS_QUERY
        )

    def get_top_sql(self):
        return self.repository.fetch_dataframe(
            TOP_SQL_QUERY
        )

    def get_wait_events(self):
        return self.repository.fetch_dataframe(
            WAIT_EVENTS_QUERY
        )
