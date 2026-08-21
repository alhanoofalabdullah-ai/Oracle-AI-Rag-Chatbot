-- =========================================================
-- Performance Health Checks
-- =========================================================


-- Database status

SELECT
    name,
    open_mode,
    database_role
FROM v$database;


-- Instance status

SELECT
    instance_name,
    status,
    host_name,
    version,
    startup_time
FROM v$instance;


-- Invalid objects

SELECT
    owner,
    object_type,
    COUNT(*) AS invalid_count

FROM dba_objects

WHERE status = 'INVALID'

GROUP BY
    owner,
    object_type

ORDER BY invalid_count DESC;


-- Database statistics

SELECT
    name,
    value

FROM v$sysstat

WHERE name IN (
    'session logical reads',
    'physical reads',
    'physical writes',
    'user commits',
    'user rollbacks'
)

ORDER BY name;
