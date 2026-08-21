from dataclasses import dataclass


@dataclass
class SecurityFinding:

    category: str

    severity: str

    score: int

    description: str

    recommendation: str


class SecurityRiskEngine:
    """
    Calculate security risk based on
    database security findings.
    """

    def calculate_user_risk(
        self,
        account_status: str,
        expiry_days: int | None,
    ) -> SecurityFinding:

        score = 0

        severity = "LOW"

        description = (
            "User account appears healthy."
        )

        recommendation = (
            "Continue regular account reviews."
        )

        if "LOCKED" in account_status.upper():

            score += 10

            description = (
                "User account is locked."
            )

            recommendation = (
                "Review the reason for account lock."
            )

        if "EXPIRED" in account_status.upper():

            score += 20

            description = (
                "User password is expired."
            )

            recommendation = (
                "Review and reset the account "
                "according to security policy."
            )

        if (
            expiry_days is not None
            and expiry_days <= 14
        ):

            score += 15

            description = (
                "User password is approaching expiration."
            )

            recommendation = (
                "Review password expiration policy."
            )

        if score >= 30:

            severity = "HIGH"

        elif score >= 15:

            severity = "MEDIUM"

        return SecurityFinding(
            category="USER_SECURITY",
            severity=severity,
            score=score,
            description=description,
            recommendation=recommendation,
        )

    @staticmethod
    def calculate_failed_login_risk(
        failed_attempts: int,
    ) -> SecurityFinding:

        if failed_attempts >= 10:

            return SecurityFinding(
                category="AUTHENTICATION",
                severity="CRITICAL",
                score=40,
                description=(
                    "High number of failed "
                    "authentication attempts."
                ),
                recommendation=(
                    "Investigate source IP, "
                    "user account and authentication "
                    "activity."
                ),
            )

        if failed_attempts >= 5:

            return SecurityFinding(
                category="AUTHENTICATION",
                severity="HIGH",
                score=25,
                description=(
                    "Elevated failed authentication "
                    "attempts detected."
                ),
                recommendation=(
                    "Review authentication events "
                    "and source hosts."
                ),
            )

        return SecurityFinding(
            category="AUTHENTICATION",
            severity="LOW",
            score=0,
            description=(
                "No significant authentication "
                "risk detected."
            ),
            recommendation=(
                "Continue monitoring."
            ),
        )
