-- ==========================================================
-- Tablespace Monitoring
-- ==========================================================

SELECT
    df.tablespace_name,

    ROUND(
        df.total_mb,
        2
    ) AS total_mb,

    ROUND(
        df.total_mb - NVL(fs.free_mb, 0),
        2
    ) AS used_mb,

    ROUND(
        NVL(fs.free_mb, 0),
        2
    ) AS free_mb,

    ROUND(
        CASE
            WHEN df.total_mb = 0 THEN 0
            ELSE
                (
                    (df.total_mb - NVL(fs.free_mb, 0))
                    / df.total_mb
                ) * 100
        END,
        2
    ) AS utilization_percent

FROM
(
    SELECT
        tablespace_name,
        SUM(bytes) / 1024 / 1024 AS total_mb
    FROM dba_data_files
    GROUP BY tablespace_name
) df

LEFT JOIN
(
    SELECT
        tablespace_name,
        SUM(bytes) / 1024 / 1024 AS free_mb
    FROM dba_free_space
    GROUP BY tablespace_name
) fs

ON df.tablespace_name = fs.tablespace_name

ORDER BY utilization_percent DESC;
