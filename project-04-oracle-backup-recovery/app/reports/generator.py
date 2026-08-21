import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class BackupReportGenerator:
    """
    Generate operational backup and recovery reports.
    """

    def __init__(
        self,
        output_directory: str = "reports",
    ) -> None:

        self.output_directory = Path(
            output_directory
        )

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def generate(
        self,
        health: dict[str, Any],
        backups: list[dict[str, Any]],
        recovery: list[dict[str, Any]],
        archive_logs: list[dict[str, Any]],
    ) -> Path:

        report = {
            "generated_at": datetime.now(
                timezone.utc
            ).isoformat(),

            "backup_health": health,

            "backup_history": backups,

            "recovery_status": recovery,

            "archive_logs": archive_logs,
        }

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        output = (
            self.output_directory
            / f"oracle_backup_report_{timestamp}.json"
        )

        with open(
            output,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                report,
                file,
                indent=4,
                default=str,
            )

        return output
