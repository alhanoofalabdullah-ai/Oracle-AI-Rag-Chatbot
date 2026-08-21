-- =========================================================
-- Database Files
-- =========================================================

SELECT
    file_id,
    file_name,
    tablespace_name,
    bytes / 1024 / 1024 AS size_mb,
    autoextensible

FROM dba_data_files

ORDER BY
    tablespace_name,
    file_id;


-- Redo logs

SELECT
    group#,
    thread#,
    sequence#,
    bytes / 1024 / 1024 AS size_mb,
    status

FROM v$log

ORDER BY group#;
