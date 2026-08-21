-- =========================================================
-- Security Findings
-- =========================================================


-- Users with powerful privileges

SELECT
    grantee,
    privilege

FROM dba_sys_privs

WHERE privilege IN (
    'ALTER SYSTEM',
    'CREATE USER',
    'DROP USER',
    'GRANT ANY PRIVILEGE',
    'GRANT ANY ROLE',
    'SELECT ANY DICTIONARY'
)

ORDER BY
    grantee,
    privilege;


-- DBA role assignments

SELECT
    grantee,
    granted_role,
    admin_option,
    default_role

FROM dba_role_privs

WHERE granted_role = 'DBA'

ORDER BY grantee;


-- Locked accounts

SELECT
    username,
    account_status,
    lock_date

FROM dba_users

WHERE account_status LIKE '%LOCKED%'

ORDER BY lock_date DESC;
