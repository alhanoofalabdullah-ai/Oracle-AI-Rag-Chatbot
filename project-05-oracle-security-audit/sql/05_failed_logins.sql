-- =========================================================
-- Failed Login Monitoring
-- =========================================================

SELECT
    event_timestamp,
    dbusername,
    os_username,
    userhost,
    return_code

FROM unified_audit_trail

WHERE action_name = 'LOGON'

AND return_code <> 0

ORDER BY event_timestamp DESC

FETCH FIRST 200 ROWS ONLY;
