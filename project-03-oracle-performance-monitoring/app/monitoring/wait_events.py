from app.database.repository import OracleRepository


WAIT_EVENTS_QUERY = """
SELECT
    event,
    wait_class,
    total_waits,
    time_waited,
    average_wait,
    time_waited_micro
FROM v$system_event

WHERE wait_class <> 'Idle'

ORDER BY time_waited DESC

FETCH FIRST 30 ROWS ONLY
"""


class WaitEventMonitor:
    """
    Oracle wait-event analysis.
    """

    def __init__(
        self,
        repository: OracleRepository,
    ) -> None:

        self.repository = repository

    def get_wait_events(self):

        return self.repository.fetch_dataframe(
            WAIT_EVENTS_QUERY
        )
