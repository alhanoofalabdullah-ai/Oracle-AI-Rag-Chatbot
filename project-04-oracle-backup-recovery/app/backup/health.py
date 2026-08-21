from datetime import datetime, timezone

from app.database.repository import OracleRepository


LAST_SUCCESSFUL_BACKUP_QUERY = """
SELECT
    MAX(completion_time)

FROM v$rman_backup_job_details

WHERE status = 'COMPLETED'
"""


CONTROLFILE_BACKUP_QUERY = """
SELECT
    MAX(completion_time)

FROM v$rman_backup_job_details

WHERE input_type = 'CONTROLFILE'

AND status = 'COMPLETED'
"""


class BackupHealthMonitor:
    """
    Determine backup readiness and backup health.
    """

    def __init__(
        self,
        repository: OracleRepository,
    ) -> None:

        self.repository = repository

    def get_last_successful_backup(self):

        return self.repository.fetch_one(
            LAST_SUCCESSFUL_BACKUP_QUERY
        )

    def get_last_controlfile_backup(self):

        return self.repository.fetch_one(
            CONTROLFILE_BACKUP_QUERY
        )

    def evaluate(self) -> dict:

        last_backup = (
            self.get_last_successful_backup()
        )

        last_controlfile = (
            self.get_last_controlfile_backup()
        )

        now = datetime.now(timezone.utc)

        result = {
            "status": "UNKNOWN",
            "last_backup": None,
            "last_controlfile_backup": None,
        }

        if last_backup and last_backup[0]:

            backup_time = last_backup[0]

            if backup_time.tzinfo is None:
                backup_time = (
                    backup_time.replace(
                        tzinfo=timezone.utc
                    )
                )

            age_hours = (
                now - backup_time
            ).total_seconds() / 3600

            result["last_backup"] = (
                backup_time.isoformat()
            )

            if age_hours <= 24:
                result["status"] = "HEALTHY"

            elif age_hours <= 48:
                result["status"] = "WARNING"

            else:
                result["status"] = "CRITICAL"

            result["backup_age_hours"] = round(
                age_hours,
                2,
            )

        if last_controlfile and last_controlfile[0]:

            controlfile_time = (
                last_controlfile[0]
            )

            if controlfile_time.tzinfo is None:
                controlfile_time = (
                    controlfile_time.replace(
                        tzinfo=timezone.utc
                    )
                )

            result[
                "last_controlfile_backup"
            ] = controlfile_time.isoformat()

        return result
