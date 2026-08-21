from app.database.repository import OracleRepository


BACKUP_HISTORY_QUERY = """
SELECT
    session_key,
    input_type,
    status,
    start_time,
    completion_time,
    elapsed_seconds,
    input_bytes,
    output_bytes,
    compression_ratio

FROM v$rman_backup_job_details

ORDER BY start_time DESC

FETCH FIRST 50 ROWS ONLY
"""


BACKUP_SUMMARY_QUERY = """
SELECT
    status,
    input_type,
    COUNT(*) AS backup_count

FROM v$rman_backup_job_details

GROUP BY
    status,
    input_type

ORDER BY
    backup_count DESC
"""


LAST_BACKUP_QUERY = """
SELECT
    input_type,
    status,
    start_time,
    completion_time,
    elapsed_seconds,
    input_bytes,
    output_bytes

FROM v$rman_backup_job_details

ORDER BY completion_time DESC

FETCH FIRST 1 ROW ONLY
"""


class BackupMonitor:
    """
    Monitor Oracle RMAN backup operations.
    """

    def __init__(
        self,
        repository: OracleRepository,
    ) -> None:

        self.repository = repository

    def get_backup_history(self):

        return self.repository.fetch_dataframe(
            BACKUP_HISTORY_QUERY
        )

    def get_backup_summary(self):

        return self.repository.fetch_dataframe(
            BACKUP_SUMMARY_QUERY
        )

    def get_last_backup(self):

        return self.repository.fetch_dataframe(
            LAST_BACKUP_QUERY
        )
