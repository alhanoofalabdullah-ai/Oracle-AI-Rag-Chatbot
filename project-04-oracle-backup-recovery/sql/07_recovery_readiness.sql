-- =========================================================
-- Recovery Readiness
-- =========================================================


-- Database state

SELECT
    name,
    open_mode,
    database_role,
    protection_mode,
    protection_level

FROM v$database;


-- Instance state

SELECT
    instance_name,
    status,
    host_name,
    startup_time

FROM v$instance;


-- Archive destination health

SELECT
    dest_id,
    status,
    target,
    destination,
    error

FROM v$archive_dest

WHERE target = 'PRIMARY';


-- Archive gaps

SELECT
    thread#,
    low_sequence#,
    high_sequence#

FROM v$archive_gap;
