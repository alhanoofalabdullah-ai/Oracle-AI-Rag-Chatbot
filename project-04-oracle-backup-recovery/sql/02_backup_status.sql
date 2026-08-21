-- =========================================================
-- Backup Status
-- =========================================================

SELECT
    status,
    input_type,
    COUNT(*) AS backup_count

FROM v$rman_backup_job_details

GROUP BY
    status,
    input_type

ORDER BY
    backup_count DESC;


-- Last successful backup

SELECT
    MAX(completion_time) AS last_successful_backup

FROM v$rman_backup_job_details

WHERE status = 'COMPLETED';
