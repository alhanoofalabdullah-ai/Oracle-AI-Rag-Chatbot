-- =========================================================
-- Database Roles
-- =========================================================

SELECT
    role,
    password_required

FROM dba_roles

ORDER BY role;


-- =========================================================
-- Role Membership
-- =========================================================

SELECT
    grantee,
    granted_role,
    admin_option,
    default_role

FROM dba_role_privs

ORDER BY
    grantee,
    granted_role;
