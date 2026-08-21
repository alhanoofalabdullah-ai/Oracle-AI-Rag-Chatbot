-- =========================================================
-- System Privileges
-- =========================================================

SELECT
    grantee,
    privilege,
    admin_option

FROM dba_sys_privs

ORDER BY
    grantee,
    privilege;


-- =========================================================
-- Object Privileges
-- =========================================================

SELECT
    grantee,
    owner,
    table_name,
    privilege,
    grantor

FROM dba_tab_privs

ORDER BY
    grantee,
    owner,
    table_name;
