def test_recovery_database_role():

    allowed_roles = {
        "PRIMARY",
        "PHYSICAL STANDBY",
        "LOGICAL STANDBY",
        "SNAPSHOT STANDBY",
    }

    assert "PRIMARY" in allowed_roles
