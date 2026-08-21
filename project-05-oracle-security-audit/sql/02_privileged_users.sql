-- =========================================================
-- Privileged Users
-- =========================================================

SELECT DISTINCT
    grantee AS username,
    privilege,
    admin_option

FROM dba_sys_privs

WHERE privilege IN (
    'ALTER SYSTEM',
    'CREATE USER',
    'DROP USER',
    'GRANT ANY PRIVILEGE',
    'GRANT ANY ROLE',
    'SELECT ANY DICTIONARY',
    'CREATE ANY TABLE',
    'DROP ANY TABLE'
)

ORDER BY
    grantee,
    privilege;
