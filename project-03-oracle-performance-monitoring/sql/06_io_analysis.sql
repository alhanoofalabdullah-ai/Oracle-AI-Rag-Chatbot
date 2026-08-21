-- =========================================================
-- Oracle I/O Analysis
-- =========================================================


-- Data file I/O

SELECT
    file_name,
    tablespace_name,
    bytes / 1024 / 1024 AS size_mb,
    autoextensible

FROM dba_data_files

ORDER BY tablespace_name;


-- File statistics

SELECT
    file#,
    phyrds,
    phywrts,
    readtim,
    writetim,
    singleblkrds,
    singleblkrdtim

FROM v$filestat

ORDER BY phyrds DESC;


-- Tablespace usage

SELECT
    tablespace_name,
    SUM(bytes) / 1024 / 1024 AS total_mb

FROM dba_data_files

GROUP BY tablespace_name

ORDER BY total_mb DESC;
