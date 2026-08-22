-- =========================================================
-- Account Lock Policy Review
-- =========================================================

SELECT
    profile,
    resource_name,
    limit

FROM dba_profiles

WHERE resource_name IN (
    'FAILED_LOGIN_ATTEMPTS',
    'PASSWORD_LOCK_TIME'
)

ORDER BY
    profile,
    resource_name;
