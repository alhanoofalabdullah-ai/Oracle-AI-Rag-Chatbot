-- ==========================================================
-- Oracle Performance Monitoring
-- ==========================================================


-- System metrics

SELECT
    metric_name,
    value,
    metric_unit
FROM v$sysmetric
WHERE group_id = 2
ORDER BY metric_name;


-- Top SQL by elapsed time

SELECT
    sql_id,
    executions,
    ROUND(
        elapsed_time / 1000000,
        2
    ) AS elapsed_seconds,

    ROUND(
        cpu_time / 1000000,
        2
    ) AS cpu_seconds,

    buffer_gets,
    disk_reads

FROM v$sql

WHERE executions > 0

ORDER BY elapsed_time DESC

FETCH FIRST 20 ROWS ONLY;


-- Top SQL by CPU

SELECT
    sql_id,
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

FETCH FIRST 20 ROWS ONLY;


-- Top SQL by physical reads

SELECT
    sql_id,
    executions,
    disk_reads,
    buffer_gets

FROM v$sql

WHERE executions > 0

ORDER BY disk_reads DESC

FETCH FIRST 20 ROWS ONLY;


-- Wait events

SELECT
    event,
    total_waits,
    time_waited

FROM v$system_event

ORDER BY time_waited DESC

FETCH FIRST 20 ROWS ONLY;
