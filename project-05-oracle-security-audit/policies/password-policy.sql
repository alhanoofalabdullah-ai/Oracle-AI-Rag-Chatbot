-- =========================================================
-- Password Policy Example
-- =========================================================

-- Review current profiles first.

SELECT
    profile,
    resource_name,
    limit

FROM dba_profiles

WHERE resource_name IN (
    'PASSWORD_LIFE_TIME',
    'PASSWORD_REUSE_TIME',
    'PASSWORD_REUSE_MAX',
    'FAILED_LOGIN_ATTEMPTS',
    'PASSWORD_LOCK_TIME'
)

ORDER BY
    profile,
    resource_name;
