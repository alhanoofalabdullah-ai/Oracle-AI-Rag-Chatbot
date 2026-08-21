-- =========================================================
-- Inactive / Potentially Stale Accounts
-- =========================================================

SELECT
    username,
    account_status,
    created,
    lock_date,
    expiry_date,
    profile

FROM dba_users

WHERE account_status = 'OPEN'

ORDER BY created;
