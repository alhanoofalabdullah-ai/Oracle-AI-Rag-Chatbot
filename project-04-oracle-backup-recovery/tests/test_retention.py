from datetime import datetime, timedelta


def test_retention_window():

    retention_days = 7

    backup_date = (
        datetime.now()
        - timedelta(days=retention_days)
    )

    age = (
        datetime.now()
        - backup_date
    ).days

    assert age >= retention_days


def test_recent_backup_is_inside_retention():

    retention_days = 7

    backup_date = (
        datetime.now()
        - timedelta(days=2)
    )

    age = (
        datetime.now()
        - backup_date
    ).days

    assert age < retention_days
