-- =========================================================
-- Oracle System Performance Metrics
-- =========================================================

SELECT
    metric_name,
    value,
    metric_unit,
    begin_time,
    end_time
FROM v$sysmetric
WHERE group_id = 2
ORDER BY metric_name;
