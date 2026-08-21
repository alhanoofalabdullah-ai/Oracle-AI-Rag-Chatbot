-- =========================================================
-- Archive Log Monitoring
-- =========================================================

SELECT
    thread#,
    COUNT(*) AS archive_count,
    MIN(sequence#) AS minimum_sequence,
    MAX(sequence#) AS maximum_sequence

FROM v$archived_log

WHERE archived = 'YES'

GROUP BY thread#

ORDER BY thread#;


-- Archive destinations

SELECT
    dest_id,
    status,
    target,
    destination,
    error

FROM v$archive_dest

WHERE status <> 'INACTIVE'

ORDER BY dest_id;


-- Archive gaps

SELECT
    thread#,
    low_sequence#,
    high_sequence#

FROM v$archive_gap;
