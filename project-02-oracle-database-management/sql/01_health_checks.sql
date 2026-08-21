-- ==========================================================
-- Oracle Database Health Checks
-- Project 02
-- ==========================================================

-- Database status
SELECT
    name,
    db_unique_name,
    open_mode,
    database_role,
    protection_mode
FROM v$database;


-- Instance status
SELECT
    instance_name,
    host_name,
    version,
    status,
    startup_time
FROM v$instance;


-- Database role
SELECT
    database_role
FROM v$database;


-- Open mode
SELECT
    open_mode
FROM v$database;
