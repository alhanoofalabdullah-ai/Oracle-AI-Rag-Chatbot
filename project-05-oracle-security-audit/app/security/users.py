from app.database.repository import (
    OracleRepository,
)


USERS_QUERY = """
SELECT
    username,
    account_status,
    created,
    lock_date,
    expiry_date,
    profile,
    authentication_type,
    default_tablespace,
    temporary_tablespace

FROM dba_users

ORDER BY username
"""


LOCKED_USERS_QUERY = """
SELECT
    username,
    account_status,
    lock_date

FROM dba_users

WHERE account_status LIKE '%LOCKED%'

ORDER BY lock_date DESC
"""


EXPIRED_USERS_QUERY = """
SELECT
    username,
    account_status,
    expiry_date

FROM dba_users

WHERE account_status LIKE '%EXPIRED%'

ORDER BY expiry_date
"""


class UserSecurityMonitor:

    def __init__(
        self,
        repository: OracleRepository,
    ):

        self.repository = repository

    def get_users(self):

        return self.repository.fetch_dataframe(
            USERS_QUERY
        )

    def get_locked_users(self):

        return self.repository.fetch_dataframe(
            LOCKED_USERS_QUERY
        )

    def get_expired_users(self):

        return self.repository.fetch_dataframe(
            EXPIRED_USERS_QUERY
        )
