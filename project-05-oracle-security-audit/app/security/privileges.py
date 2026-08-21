from app.database.repository import (
    OracleRepository,
)


SYSTEM_PRIVILEGES_QUERY = """
SELECT
    grantee,
    privilege,
    admin_option

FROM dba_sys_privs

ORDER BY
    grantee,
    privilege
"""


OBJECT_PRIVILEGES_QUERY = """
SELECT
    grantee,
    owner,
    table_name,
    privilege,
    grantor

FROM dba_tab_privs

ORDER BY
    grantee,
    owner,
    table_name
"""


DIRECT_DBA_PRIVILEGES_QUERY = """
SELECT
    grantee,
    privilege,
    admin_option

FROM dba_sys_privs

WHERE privilege IN (
    'ALTER SYSTEM',
    'CREATE USER',
    'DROP USER',
    'GRANT ANY PRIVILEGE',
    'GRANT ANY ROLE',
    'SELECT ANY DICTIONARY',
    'CREATE ANY TABLE',
    'DROP ANY TABLE'
)

ORDER BY
    grantee,
    privilege
"""


class PrivilegeMonitor:

    def __init__(
        self,
        repository: OracleRepository,
    ):

        self.repository = repository

    def get_system_privileges(self):

        return self.repository.fetch_dataframe(
            SYSTEM_PRIVILEGES_QUERY
        )

    def get_object_privileges(self):

        return self.repository.fetch_dataframe(
            OBJECT_PRIVILEGES_QUERY
        )

    def get_high_risk_privileges(self):

        return self.repository.fetch_dataframe(
            DIRECT_DBA_PRIVILEGES_QUERY
        )
