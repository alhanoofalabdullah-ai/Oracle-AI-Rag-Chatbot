-- =========================================================
-- Recovery Status
-- =========================================================

SELECT
    recovery_status,
    db_unique_name,
    thread,
    sequence#,
    resetlogs_change#,
    resetlogs_time

FROM v$database;


-- Database role

SELECT
    name,
    db_unique_name,
    database_role,
    open_mode,
    protection_mode,
    protection_level

FROM v$database;
