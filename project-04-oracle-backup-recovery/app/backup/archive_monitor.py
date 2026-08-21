from app.database.repository import OracleRepository


ARCHIVE_SUMMARY_QUERY = """
SELECT
    thread#,
    COUNT(*) AS archive_count,
    MIN(sequence#) AS minimum_sequence,
    MAX(sequence#) AS maximum_sequence

FROM v$archived_log

WHERE archived = 'YES'

GROUP BY thread#

ORDER BY thread#
"""


ARCHIVE_DESTINATION_QUERY = """
SELECT
    dest_id,
    status,
    target,
    destination,
    error

FROM v$archive_dest

WHERE status <> 'INACTIVE'

ORDER BY dest_id
"""


ARCHIVE_GAP_QUERY = """
SELECT
    thread#,
    low_sequence#,
    high_sequence#

FROM v$archive_gap
"""


class ArchiveMonitor:
    """
    Monitor Oracle archive logs.
    """

    def __init__(
        self,
        repository: OracleRepository,
    ) -> None:

        self.repository = repository

    def get_archive_summary(self):

        return self.repository.fetch_dataframe(
            ARCHIVE_SUMMARY_QUERY
        )

    def get_archive_destinations(self):

        return self.repository.fetch_dataframe(
            ARCHIVE_DESTINATION_QUERY
        )

    def get_archive_gaps(self):

        return self.repository.fetch_dataframe(
            ARCHIVE_GAP_QUERY
        )
