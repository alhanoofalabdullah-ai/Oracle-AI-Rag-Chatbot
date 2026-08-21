from app.database.repository import OracleRepository


SESSION_SUMMARY_QUERY = """
SELECT
    status,
    COUNT(*) AS session_count
FROM v$session
GROUP BY status
ORDER BY session_count DESC
"""


ACTIVE_SESSION_QUERY = """
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
WHERE status = 'ACTIVE'
AND username IS NOT NULL
ORDER BY last_call_et DESC
"""


class SessionMonitor:

    def __init__(self, repository: OracleRepository):
        self.repository = repository

    def get_session_summary(self):
        return self.repository.fetch_dataframe(
            SESSION_SUMMARY_QUERY
        )

    def get_active_sessions(self):
        return self.repository.fetch_dataframe(
            ACTIVE_SESSION_QUERY
        )

    def get_total_sessions(self) -> int:
        df = self.get_session_summary()

        if df.empty:
            return 0

        return int(df["SESSION_COUNT"].sum())

    def get_active_session_count(self) -> int:
        df = self.get_session_summary()

        if df.empty:
            return 0

        active = df[
            df["STATUS"].str.upper() == "ACTIVE"
        ]

        if active.empty:
            return 0

        return int(active["SESSION_COUNT"].iloc[0])
