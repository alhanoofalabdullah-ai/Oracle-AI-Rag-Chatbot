import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class PerformanceReportGenerator:
    """
    Generate JSON performance reports.
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
        system_metrics: list[dict[str, Any]],
        top_sql: list[dict[str, Any]],
        waits: list[dict[str, Any]],
        sessions: list[dict[str, Any]],
    ) -> Path:

        report = {
            "generated_at": datetime.now(
                timezone.utc
            ).isoformat(),

            "health": health,

            "system_metrics": system_metrics,

            "top_sql": top_sql,

            "wait_events": waits,

            "sessions": sessions,
        }

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        file_path = (
            self.output_directory
            / f"oracle_performance_{timestamp}.json"
        )

        with open(
            file_path,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                report,
                file,
                indent=4,
                default=str,
            )

        return file_path
