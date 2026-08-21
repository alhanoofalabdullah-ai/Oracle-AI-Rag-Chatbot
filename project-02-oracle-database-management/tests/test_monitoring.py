from app.monitoring.storage import StorageMonitor


def test_storage_status_custom_thresholds():

    result = StorageMonitor.calculate_status(
        utilization=70,
        warning=70,
        critical=85,
    )

    assert result == "WARNING"


def test_storage_status_below_custom_threshold():

    result = StorageMonitor.calculate_status(
        utilization=60,
        warning=70,
        critical=85,
    )

    assert result == "HEALTHY"


def test_storage_status_above_custom_critical():

    result = StorageMonitor.calculate_status(
        utilization=95,
        warning=70,
        critical=85,
    )

    assert result == "CRITICAL"
