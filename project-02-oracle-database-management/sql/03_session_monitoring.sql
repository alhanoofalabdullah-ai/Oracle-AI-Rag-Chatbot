-- ==========================================================
-- Session Monitoring
-- ==========================================================

-- Session summary
SELECT
    status,
    COUNT(*) AS session_count
FROM v$session
GROUP BY status
ORDER BY session_count DESC;


-- Active sessions
SELECT
    sid,
    serial#,
    username,
    status,
    machine,
    program,
    sql_id,
    event,
    last_call_et
FROM v$session
WHERE status = 'ACTIVE'
AND username IS NOT NULL
ORDER BY last_call_et DESC;


-- Sessions by username
SELECT
    username,
    COUNT(*) AS session_count
FROM v$session
WHERE username IS NOT NULL
GROUP BY username
ORDER BY session_count DESC;


-- Sessions by machine
SELECT
    machine,
    COUNT(*) AS session_count
FROM v$session
WHERE username IS NOT NULL
GROUP BY machine
ORDER BY session_count DESC;
