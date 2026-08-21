from app.monitoring.sql_analysis import (
    SQLAnalysisMonitor,
)


def test_sql_warning_boundary():

    result = (
        SQLAnalysisMonitor
        .classify_sql(
            elapsed_seconds=5
        )
    )

    assert result == "WARNING"


def test_sql_critical_boundary():

    result = (
        SQLAnalysisMonitor
        .classify_sql(
            elapsed_seconds=30
        )
    )

    assert result == "CRITICAL"


def test_sql_below_warning():

    result = (
        SQLAnalysisMonitor
        .classify_sql(
            elapsed_seconds=4.99
        )
    )

    assert result == "HEALTHY"
