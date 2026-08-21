-- =========================================================
-- Unified Audit Events
-- =========================================================

SELECT
    event_timestamp,
    dbusername,
    action_name,
    object_schema,
    object_name,
    return_code,
    unified_audit_policies,
    os_username,
    userhost

FROM unified_audit_trail

ORDER BY event_timestamp DESC

FETCH FIRST 500 ROWS ONLY;
