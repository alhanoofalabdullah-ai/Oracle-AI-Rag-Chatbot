from app.database.repository import (
    OracleRepository,
)


COMPLIANCE_QUERY = """
SELECT
    username,
    account_status,
    profile,
    authentication_type,
    expiry_date

FROM dba_users

ORDER BY username
"""


class ComplianceMonitor:

    def __init__(
        self,
        repository: OracleRepository,
    ):

        self.repository = repository

    def get_account_compliance(self):

        return self.repository.fetch_dataframe(
            COMPLIANCE_QUERY
        )

    def evaluate(
        self,
        users,
    ):

        findings = []

        for _, user in users.iterrows():

            username = user["USERNAME"]

            status = str(
                user["ACCOUNT_STATUS"]
            )

            if (
                status == "OPEN"
                and user["EXPIRY_DATE"]
            ):

                findings.append(
                    {
                        "username": username,
                        "finding": (
                            "Account requires "
                            "periodic password review."
                        ),
                        "severity": "LOW",
                    }
                )

            if "EXPIRED" in status:

                findings.append(
                    {
                        "username": username,
                        "finding": (
                            "Expired account detected."
                        ),
                        "severity": "MEDIUM",
                    }
                )

            if "LOCKED" in status:

                findings.append(
                    {
                        "username": username,
                        "finding": (
                            "Locked account detected."
                        ),
                        "severity": "LOW",
                    }
                )

        return findings
