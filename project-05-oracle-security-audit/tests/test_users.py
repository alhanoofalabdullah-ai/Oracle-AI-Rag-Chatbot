from app.security.risk import (
    SecurityRiskEngine,
)


def test_locked_user_risk():

    engine = SecurityRiskEngine()

    finding = engine.calculate_user_risk(
        account_status="LOCKED",
        expiry_days=None,
    )

    assert finding.score >= 10


def test_expired_user_risk():

    engine = SecurityRiskEngine()

    finding = engine.calculate_user_risk(
        account_status="EXPIRED",
        expiry_days=None,
    )

    assert finding.score >= 20
