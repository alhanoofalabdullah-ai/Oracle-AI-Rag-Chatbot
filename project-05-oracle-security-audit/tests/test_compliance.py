import pandas as pd

from app.security.compliance import (
    ComplianceMonitor,
)


class DummyRepository:
    pass


def test_expired_account_finding():

    monitor = ComplianceMonitor(
        DummyRepository()
    )

    data = pd.DataFrame(
        [
            {
                "USERNAME": "TEST_USER",
                "ACCOUNT_STATUS": "EXPIRED",
                "PROFILE": "DEFAULT",
                "AUTHENTICATION_TYPE": "PASSWORD",
                "EXPIRY_DATE": None,
            }
        ]
    )

    findings = monitor.evaluate(data)

    assert len(findings) == 1

    assert (
        findings[0]["severity"]
        == "MEDIUM"
    )
