from app.database.repository import (
    OracleRepository,
)


AUDIT_EVENTS_QUERY = """
SELECT
    event_timestamp,
    dbusername,
    action_name,
    object_schema,
    object_name,
    return_code,
    unified_audit_policies,
    os_username,
    userhost

FROM unified_audit_trail

ORDER BY event_timestamp DESC

FETCH FIRST 500 ROWS ONLY
"""


FAILED_LOGINS_QUERY = """
SELECT
    event_timestamp,
    dbusername,
    os_username,
    userhost,
    return_code

FROM unified_audit_trail

WHERE action_name = 'LOGON'

AND return_code <> 0

ORDER BY event_timestamp DESC

FETCH FIRST 200 ROWS ONLY
"""


SUCCESSFUL_LOGINS_QUERY = """
SELECT
    event_timestamp,
    dbusername,
    os_username,
    userhost,
    return_code

FROM unified_audit_trail

WHERE action_name = 'LOGON'

AND return_code = 0

ORDER BY event_timestamp DESC

FETCH FIRST 200 ROWS ONLY
"""


class AuditMonitor:

    def __init__(
        self,
        repository: OracleRepository,
    ):

        self.repository = repository

    def get_audit_events(self):

        return self.repository.fetch_dataframe(
            AUDIT_EVENTS_QUERY
        )

    def get_failed_logins(self):

        return self.repository.fetch_dataframe(
            FAILED_LOGINS_QUERY
        )

    def get_successful_logins(self):

        return self.repository.fetch_dataframe(
            SUCCESSFUL_LOGINS_QUERY
        )
