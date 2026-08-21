-- =========================================================
-- RMAN Health
-- =========================================================


-- Backup failures

SELECT
    session_key,
    input_type,
    status,
    start_time,
    completion_time

FROM v$rman_backup_job_details

WHERE status <> 'COMPLETED'

ORDER BY start_time DESC;


-- Controlfile backups

SELECT
    MAX(completion_time)
        AS last_controlfile_backup

FROM v$rman_backup_job_details

WHERE input_type = 'CONTROLFILE'

AND status = 'COMPLETED';


-- SPFILE backups

SELECT
    MAX(completion_time)
        AS last_spfile_backup

FROM v$rman_backup_job_details

WHERE input_type = 'SPFILE'

AND status = 'COMPLETED';
