from app.database.repository import OracleRepository


HEALTH_QUERY = """
SELECT
    name,
    open_mode,
    database_role

FROM v$database
"""


INSTANCE_HEALTH_QUERY = """
SELECT
    instance_name,
    status,
    host_name

FROM v$instance
"""


class PerformanceHealthMonitor:
    """
    Overall database performance health.
    """

    def __init__(
        self,
        repository: OracleRepository,
    ) -> None:

        self.repository = repository

    def check(self) -> dict:

        database = self.repository.fetch_one(
            HEALTH_QUERY
        )

        instance = self.repository.fetch_one(
            INSTANCE_HEALTH_QUERY
        )

        if not database or not instance:

            return {
                "status": "UNHEALTHY",
                "reason": (
                    "Unable to retrieve "
                    "database health information."
                ),
            }

        database_open = database[1]
        instance_status = instance[1]

        if (
            database_open in (
                "READ WRITE",
                "READ ONLY",
            )
            and instance_status == "OPEN"
        ):

            status = "HEALTHY"

        else:

            status = "WARNING"

        return {
            "status": status,
            "database_name": database[0],
            "open_mode": database_open,
            "database_role": database[2],
            "instance_name": instance[0],
            "instance_status": instance_status,
            "host_name": instance[2],
        }
