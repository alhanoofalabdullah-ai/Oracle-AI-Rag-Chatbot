-- =========================================================
-- Password Expiration
-- =========================================================

SELECT
    username,
    account_status,
    expiry_date,
    profile

FROM dba_users

WHERE expiry_date IS NOT NULL

ORDER BY expiry_date;
