SELECT

    COUNT(*) AS total_requests,

    SUM(
        CASE
            WHEN status_code BETWEEN 200 AND 299
            THEN 1
            ELSE 0
        END
    ) AS successful_requests,

    SUM(
        CASE
            WHEN status_code >= 400
            THEN 1
            ELSE 0
        END
    ) AS failed_requests,

    ROUND(
        AVG(response_time_ms),
        2
    ) AS avg_response_time

FROM api_audit_log;
