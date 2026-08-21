-- =========================================================
-- Top SQL by elapsed time
-- =========================================================

SELECT
    sql_id,
    parsing_schema_name,
    executions,

    ROUND(
        elapsed_time / 1000000,
        2
    ) AS elapsed_seconds,

    ROUND(
        CASE
            WHEN executions = 0 THEN 0
            ELSE
                elapsed_time /
                executions /
                1000000
        END,
        4
    ) AS avg_elapsed_seconds,

    ROUND(
        cpu_time / 1000000,
        2
    ) AS cpu_seconds,

    buffer_gets,
    disk_reads,
    rows_processed

FROM v$sql

WHERE executions > 0

ORDER BY elapsed_time DESC

FETCH FIRST 25 ROWS ONLY;
