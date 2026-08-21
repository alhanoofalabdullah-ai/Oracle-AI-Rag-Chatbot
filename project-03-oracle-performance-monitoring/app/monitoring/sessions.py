from app.database.repository import OracleRepository


SESSION_SUMMARY_QUERY = """
SELECT
    status,
    type,
    COUNT(*) AS session_count

FROM v$session

GROUP BY
    status,
    type

ORDER BY
    session_count DESC
"""


ACTIVE_SESSIONS_QUERY = """
SELECT
    sid,
    serial#,
    username,
    status,
    machine,
    program,
    sql_id,
    event,
    wait_class,
    last_call_et

FROM v$session

WHERE status = 'ACTIVE'

AND username IS NOT NULL

ORDER BY
    last_call_et DESC
"""


LONG_RUNNING_SESSIONS_QUERY = """
SELECT
    sid,
    serial#,
    username,
    status,
    machine,
    program,
    sql_id,
    event,
    last_call_et

FROM v$session

WHERE username IS NOT NULL

AND last_call_et >= :minimum_seconds

ORDER BY
    last_call_et DESC
"""


class SessionPerformanceMonitor:
    """
    Monitor active and long-running Oracle sessions.
    """

    def __init__(
        self,
        repository: OracleRepository,
    ) -> None:

        self.repository = repository

    def get_summary(self):

        return self.repository.fetch_dataframe(
            SESSION_SUMMARY_QUERY
        )

    def get_active_sessions(self):

        return self.repository.fetch_dataframe(
            ACTIVE_SESSIONS_QUERY
        )

    def get_long_running_sessions(
        self,
        minimum_seconds: int = 300,
    ):

        return self.repository.fetch_dataframe(
            LONG_RUNNING_SESSIONS_QUERY,
            {
                "minimum_seconds": minimum_seconds
            },
        )

    def get_active_count(self) -> int:

        df = self.get_summary()

        if df.empty:
            return 0

        active = df[
            df["STATUS"].str.upper() == "ACTIVE"
        ]

        if active.empty:
            return 0

        return int(
            active["SESSION_COUNT"].sum()
        )
