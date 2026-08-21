from datetime import datetime, timezone

from app.database.repository import OracleRepository


HEALTH_QUERY = """
SELECT
    name,
    open_mode,
    database_role,
    protection_mode
FROM v$database
"""


INSTANCE_QUERY = """
SELECT
    instance_name,
    host_name,
    version,
    status,
    startup_time
FROM v$instance
"""


class HealthMonitor:

    def __init__(self, repository: OracleRepository):
        self.repository = repository

    def check_database(self) -> dict:
        database = self.repository.fetch_one(HEALTH_QUERY)
        instance = self.repository.fetch_one(INSTANCE_QUERY)

        if not database or not instance:
            return {
                "status": "UNHEALTHY",
                "message": "Unable to retrieve Oracle database status.",
                "checked_at": datetime.now(
                    timezone.utc
                ).isoformat(),
            }

        return {
            "status": (
                "HEALTHY"
                if instance[3] == "OPEN"
                and database[1] in ("READ WRITE", "READ ONLY")
                else "WARNING"
            ),
            "database_name": database[0],
            "open_mode": database[1],
            "database_role": database[2],
            "protection_mode": database[3],
            "instance_name": instance[0],
            "host_name": instance[1],
            "oracle_version": instance[2],
            "instance_status": instance[3],
            "startup_time": str(instance[4]),
            "checked_at": datetime.now(
                timezone.utc
            ).isoformat(),
        }
