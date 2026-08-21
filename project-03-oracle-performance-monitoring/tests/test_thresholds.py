from app.monitoring.sql_analysis import (
    SQLAnalysisMonitor,
)


def test_custom_thresholds():

    result = (
        SQLAnalysisMonitor
        .classify_sql(
            elapsed_seconds=15,
            warning=10,
            critical=20,
        )
    )

    assert result == "WARNING"


def test_custom_critical_threshold():

    result = (
        SQLAnalysisMonitor
        .classify_sql(
            elapsed_seconds=25,
            warning=10,
            critical=20,
        )
    )

    assert result == "CRITICAL"
