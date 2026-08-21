-- =========================================================
-- SQL Tuning Analysis
-- =========================================================


-- SQL with highest CPU consumption

SELECT
    sql_id,
    parsing_schema_name,
    executions,

    ROUND(
        cpu_time / 1000000,
        2
    ) AS cpu_seconds,

    buffer_gets,
    disk_reads

FROM v$sql

WHERE executions > 0

ORDER BY cpu_time DESC

FETCH FIRST 25 ROWS ONLY;


-- SQL with highest buffer gets

SELECT
    sql_id,
    parsing_schema_name,
    executions,
    buffer_gets,

    ROUND(
        buffer_gets /
        NULLIF(executions, 0),
        2
    ) AS avg_buffer_gets

FROM v$sql

WHERE executions > 0

ORDER BY buffer_gets DESC

FETCH FIRST 25 ROWS ONLY;


-- SQL with highest physical reads

SELECT
    sql_id,
    parsing_schema_name,
    executions,
    disk_reads,

    ROUND(
        disk_reads /
        NULLIF(executions, 0),
        2
    ) AS avg_disk_reads

FROM v$sql

WHERE executions > 0

ORDER BY disk_reads DESC

FETCH FIRST 25 ROWS ONLY;
