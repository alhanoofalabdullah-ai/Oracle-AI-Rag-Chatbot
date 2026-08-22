-- =========================================================
-- Unified Audit Policy Review
-- =========================================================

SELECT
    policy_name,
    enabled_option,
    entity_name,
    entity_type

FROM audit_unified_enabled_policies

ORDER BY
    policy_name;
