-- =========================================================
-- RMAN Backup History
-- =========================================================

SELECT
    session_key,
    input_type,
    status,
    start_time,
    completion_time,
    elapsed_seconds,
    input_bytes,
    output_bytes,
    compression_ratio

FROM v$rman_backup_job_details

ORDER BY start_time DESC

FETCH FIRST 50 ROWS ONLY;
