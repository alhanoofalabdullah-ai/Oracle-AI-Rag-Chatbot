from app.monitoring.storage import StorageMonitor


def test_storage_status_healthy():

    result = StorageMonitor.calculate_status(
        utilization=50
    )

    assert result == "HEALTHY"


def test_storage_status_warning():

    result = StorageMonitor.calculate_status(
        utilization=80
    )

    assert result == "WARNING"


def test_storage_status_critical():

    result = StorageMonitor.calculate_status(
        utilization=95
    )

    assert result == "CRITICAL"


def test_storage_status_boundary_warning():

    result = StorageMonitor.calculate_status(
        utilization=75
    )

    assert result == "WARNING"


def test_storage_status_boundary_critical():

    result = StorageMonitor.calculate_status(
        utilization=90
    )

    assert result == "CRITICAL"
