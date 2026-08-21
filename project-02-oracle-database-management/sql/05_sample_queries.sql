-- ==========================================================
-- Additional Oracle Monitoring Queries
-- ==========================================================


-- Current database time

SELECT
    SYSDATE AS current_database_time
FROM dual;


-- Oracle version

SELECT
    banner
FROM v$version;


-- Number of users

SELECT
    COUNT(*) AS total_users
FROM dba_users;


-- Invalid objects

SELECT
    owner,
    object_type,
    COUNT(*) AS invalid_count
FROM dba_objects
WHERE status = 'INVALID'
GROUP BY owner, object_type
ORDER BY invalid_count DESC;


-- Data files

SELECT
    file_name,
    tablespace_name,
    bytes / 1024 / 1024 AS size_mb,
    autoextensible,
    maxbytes / 1024 / 1024 AS max_size_mb
FROM dba_data_files
ORDER BY tablespace_name;


-- Temporary files

SELECT
    file_name,
    tablespace_name,
    bytes / 1024 / 1024 AS size_mb
FROM dba_temp_files
ORDER BY tablespace_name;
