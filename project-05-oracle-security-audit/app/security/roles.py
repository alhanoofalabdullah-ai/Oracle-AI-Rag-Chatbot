from app.database.repository import (
    OracleRepository,
)


ROLES_QUERY = """
SELECT
    role,
    password_required

FROM dba_roles

ORDER BY role
"""


ROLE_MEMBERS_QUERY = """
SELECT
    grantee,
    granted_role,
    admin_option,
    default_role

FROM dba_role_privs

ORDER BY
    grantee,
    granted_role
"""


DBA_ROLE_MEMBERS_QUERY = """
SELECT
    grantee,
    granted_role,
    admin_option,
    default_role

FROM dba_role_privs

WHERE granted_role IN (
    'DBA',
    'RESOURCE',
    'DATAPUMP_EXP_FULL_DATABASE',
    'DATAPUMP_IMP_FULL_DATABASE',
    'EXP_FULL_DATABASE',
    'IMP_FULL_DATABASE'
)

ORDER BY
    grantee
"""


class RoleMonitor:

    def __init__(
        self,
        repository: OracleRepository,
    ):

        self.repository = repository

    def get_roles(self):

        return self.repository.fetch_dataframe(
            ROLES_QUERY
        )

    def get_role_members(self):

        return self.repository.fetch_dataframe(
            ROLE_MEMBERS_QUERY
        )

    def get_privileged_roles(self):

        return self.repository.fetch_dataframe(
            DBA_ROLE_MEMBERS_QUERY
        )
