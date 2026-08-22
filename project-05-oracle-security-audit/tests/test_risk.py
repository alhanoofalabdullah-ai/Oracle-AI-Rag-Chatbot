from app.security.risk import (
    SecurityRiskEngine,
)


def test_high_failed_login_risk():

    finding = (
        SecurityRiskEngine
        .calculate_failed_login_risk(
            12
        )
    )

    assert finding.severity == "CRITICAL"

    assert finding.score == 40


def test_medium_failed_login_risk():

    finding = (
        SecurityRiskEngine
        .calculate_failed_login_risk(
            6
        )
    )

    assert finding.severity == "HIGH"


def test_low_failed_login_risk():

    finding = (
        SecurityRiskEngine
        .calculate_failed_login_risk(
            1
        )
    )

    assert finding.severity == "LOW"
