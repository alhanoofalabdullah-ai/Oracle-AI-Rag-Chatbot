import json
from datetime import datetime, timezone
from pathlib import Path


class SecurityReportGenerator:

    def __init__(
        self,
        output_directory: str = "reports",
    ):

        self.output_directory = Path(
            output_directory
        )

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def generate(
        self,
        users,
        privileged_users,
        failed_logins,
        audit_events,
        findings,
    ):

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        report = {

            "generated_at": datetime.now(
                timezone.utc
            ).isoformat(),

            "users": users,

            "privileged_users": privileged_users,

            "failed_logins": failed_logins,

            "audit_events": audit_events,

            "security_findings": findings,
        }

        path = (
            self.output_directory
            / f"security_report_{timestamp}.json"
        )

        with open(
            path,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                report,
                file,
                indent=4,
                default=str,
            )

        return path
