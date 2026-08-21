-- =========================================================
-- Session Performance Analysis
-- =========================================================


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
    wait_class,
    last_call_et

FROM v$session

WHERE status = 'ACTIVE'

AND username IS NOT NULL

ORDER BY last_call_et DESC;


-- Long running sessions

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

WHERE username IS NOT NULL

AND last_call_et >= 300

ORDER BY last_call_et DESC;


-- Sessions by user

SELECT
    username,
    COUNT(*) AS session_count

FROM v$session

WHERE username IS NOT NULL

GROUP BY username

ORDER BY session_count DESC;
