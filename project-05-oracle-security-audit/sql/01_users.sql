-- =========================================================
-- Oracle Database Users
-- =========================================================

SELECT
    username,
    account_status,
    created,
    lock_date,
    expiry_date,
    profile,
    authentication_type,
    default_tablespace,
    temporary_tablespace

FROM dba_users

ORDER BY username;
