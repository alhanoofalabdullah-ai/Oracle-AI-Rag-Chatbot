from app.monitoring.sql_analysis import (
    SQLAnalysisMonitor,
)


def test_sql_classification_healthy():

    result = (
        SQLAnalysisMonitor
        .classify_sql(
            elapsed_seconds=2
        )
    )

    assert result == "HEALTHY"


def test_sql_classification_warning():

    result = (
        SQLAnalysisMonitor
        .classify_sql(
            elapsed_seconds=10
        )
    )

    assert result == "WARNING"


def test_sql_classification_critical():

    result = (
        SQLAnalysisMonitor
        .classify_sql(
            elapsed_seconds=60
        )
    )

    assert result == "CRITICAL"
