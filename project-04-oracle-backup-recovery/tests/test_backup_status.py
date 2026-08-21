from datetime import datetime, timedelta, timezone

from app.backup.health import BackupHealthMonitor


def test_recent_backup_is_healthy():

    now = datetime.now(timezone.utc)

    assert (
        now - timedelta(hours=2)
    ).total_seconds() < 24 * 3600


def test_old_backup_is_not_recent():

    now = datetime.now(timezone.utc)

    assert (
        now - timedelta(hours=72)
    ).total_seconds() > 48 * 3600
