import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class HealthReportGenerator:

    def __init__(self, output_directory: str = "reports"):
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def generate(
        self,
        health: dict[str, Any],
        storage: list[dict[str, Any]],
        sessions: dict[str, Any],
        performance: dict[str, Any],
    ) -> Path:

        report = {
            "generated_at": datetime.now(
                timezone.utc
            ).isoformat(),

            "health": health,

            "storage": storage,

            "sessions": sessions,

            "performance": performance,
        }

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        file_path = (
            self.output_directory
            / f"oracle_health_{timestamp}.json"
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
