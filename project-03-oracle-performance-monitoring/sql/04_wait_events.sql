-- =========================================================
-- Oracle Wait Event Analysis
-- =========================================================

SELECT
    event,
    wait_class,
    total_waits,
    time_waited,
    average_wait,
    time_waited_micro

FROM v$system_event

WHERE wait_class <> 'Idle'

ORDER BY time_waited DESC

FETCH FIRST 30 ROWS ONLY;
