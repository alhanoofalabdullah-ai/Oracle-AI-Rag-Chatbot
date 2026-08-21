from app.database.repository import OracleRepository


TOP_SQL_ELAPSED_QUERY = """
SELECT
    sql_id,
    parsing_schema_name,
    executions,

    ROUND(
        elapsed_time / 1000000,
        2
    ) AS elapsed_seconds,

    ROUND(
        CASE
            WHEN executions = 0 THEN 0
            ELSE elapsed_time / executions / 1000000
        END,
        4
    ) AS avg_elapsed_seconds,

    ROUND(
        cpu_time / 1000000,
        2
    ) AS cpu_seconds,

    buffer_gets,
    disk_reads,
    rows_processed,

    ROUND(
        CASE
            WHEN executions = 0 THEN 0
            ELSE buffer_gets / executions
        END,
        2
    ) AS avg_buffer_gets

FROM v$sql

WHERE executions > 0

ORDER BY elapsed_time DESC

FETCH FIRST 25 ROWS ONLY
"""


TOP_SQL_CPU_QUERY = """
SELECT
    sql_id,
    parsing_schema_name,
    executions,

    ROUND(
        cpu_time / 1000000,
        2
    ) AS cpu_seconds,

    ROUND(
        CASE
            WHEN executions = 0 THEN 0
            ELSE cpu_time / executions / 1000000
        END,
        4
    ) AS avg_cpu_seconds,

    elapsed_time,
    buffer_gets,
    disk_reads,
    rows_processed

FROM v$sql

WHERE executions > 0

ORDER BY cpu_time DESC

FETCH FIRST 25 ROWS ONLY
"""


TOP_SQL_IO_QUERY = """
SELECT
    sql_id,
    parsing_schema_name,
    executions,
    disk_reads,
    buffer_gets,
    rows_processed,

    ROUND(
        CASE
            WHEN executions = 0 THEN 0
            ELSE disk_reads / executions
        END,
        2
    ) AS avg_disk_reads

FROM v$sql

WHERE executions > 0

ORDER BY disk_reads DESC

FETCH FIRST 25 ROWS ONLY
"""


class SQLAnalysisMonitor:
    """
    SQL performance and tuning analysis.
    """

    def __init__(
        self,
        repository: OracleRepository,
    ) -> None:

        self.repository = repository

    def get_top_sql_by_elapsed(self):

        return self.repository.fetch_dataframe(
            TOP_SQL_ELAPSED_QUERY
        )

    def get_top_sql_by_cpu(self):

        return self.repository.fetch_dataframe(
            TOP_SQL_CPU_QUERY
        )

    def get_top_sql_by_io(self):

        return self.repository.fetch_dataframe(
            TOP_SQL_IO_QUERY
        )

    @staticmethod
    def classify_sql(
        elapsed_seconds: float,
        warning: float = 5.0,
        critical: float = 30.0,
    ) -> str:

        if elapsed_seconds >= critical:
            return "CRITICAL"

        if elapsed_seconds >= warning:
            return "WARNING"

        return "HEALTHY"
