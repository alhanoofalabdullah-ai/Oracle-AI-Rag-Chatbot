import streamlit as st

from app.database.connection import (
    OracleConnectionManager,
)

from app.database.repository import (
    OracleRepository,
)

from app.security.users import (
    UserSecurityMonitor,
)

from app.security.privileges import (
    PrivilegeMonitor,
)

from app.security.roles import (
    RoleMonitor,
)

from app.security.audit import (
    AuditMonitor,
)

from app.security.compliance import (
    ComplianceMonitor,
)

from app.reports.generator import (
    SecurityReportGenerator,
)


@st.cache_resource
def get_repository():

    manager = OracleConnectionManager()

    manager.initialize()

    return OracleRepository(manager)


def run_dashboard():

    st.set_page_config(
        page_title=(
            "Oracle Security & Audit"
        ),
        page_icon="🔐",
        layout="wide",
    )

    st.title(
        "🔐 Oracle Database Security & Audit Platform"
    )

    st.caption(
        "Security Monitoring • Auditing • "
        "Privileges • Compliance"
    )

    repository = get_repository()

    user_monitor = UserSecurityMonitor(
        repository
    )

    privilege_monitor = PrivilegeMonitor(
        repository
    )

    role_monitor = RoleMonitor(
        repository
    )

    audit_monitor = AuditMonitor(
        repository
    )

    compliance_monitor = ComplianceMonitor(
        repository
    )

    # =====================================================
    # USERS
    # =====================================================

    st.header("👤 Database Users")

    try:

        users = user_monitor.get_users()

        total_users = len(users)

        locked_users = len(
            users[
                users["ACCOUNT_STATUS"]
                .astype(str)
                .str.contains(
                    "LOCKED",
                    case=False,
                    na=False,
                )
            ]
        )

        expired_users = len(
            users[
                users["ACCOUNT_STATUS"]
                .astype(str)
                .str.contains(
                    "EXPIRED",
                    case=False,
                    na=False,
                )
            ]
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Total Users",
            total_users,
        )

        c2.metric(
            "Locked Users",
            locked_users,
        )

        c3.metric(
            "Expired Users",
            expired_users,
        )

        st.dataframe(
            users,
            use_container_width=True,
        )

    except Exception as exc:

        st.error(
            f"User monitoring failed: {exc}"
        )

    st.divider()

    # =====================================================
    # PRIVILEGES
    # =====================================================

    st.header("🛡️ Privilege Monitoring")

    try:

        high_risk_privileges = (
            privilege_monitor
            .get_high_risk_privileges()
        )

        system_privileges = (
            privilege_monitor
            .get_system_privileges()
        )

        tab1, tab2 = st.tabs(
            [
                "High-Risk Privileges",
                "System Privileges",
            ]
        )

        with tab1:

            if high_risk_privileges.empty:

                st.success(
                    "No high-risk privileges detected."
                )

            else:

                st.warning(
                    "High-risk privileges detected."
                )

                st.dataframe(
                    high_risk_privileges,
                    use_container_width=True,
                )

        with tab2:

            st.dataframe(
                system_privileges,
                use_container_width=True,
            )

    except Exception as exc:

        st.error(
            f"Privilege monitoring failed: {exc}"
        )

    st.divider()

    # =====================================================
    # ROLES
    # =====================================================

    st.header("🎭 Role Monitoring")

    try:

        roles = role_monitor.get_roles()

        privileged_roles = (
            role_monitor
            .get_privileged_roles()
        )

        tab1, tab2 = st.tabs(
            [
                "Roles",
                "Privileged Roles",
            ]
        )

        with tab1:

            st.dataframe(
                roles,
                use_container_width=True,
            )

        with tab2:

            if privileged_roles.empty:

                st.success(
                    "No privileged role assignments found."
                )

            else:

                st.warning(
                    "Privileged role assignments detected."
                )

                st.dataframe(
                    privileged_roles,
                    use_container_width=True,
                )

    except Exception as exc:

        st.error(
            f"Role monitoring failed: {exc}"
        )

    st.divider()

    # =====================================================
    # AUDIT
    # =====================================================

    st.header("📋 Audit Monitoring")

    try:

        audit_events = (
            audit_monitor
            .get_audit_events()
        )

        failed_logins = (
            audit_monitor
            .get_failed_logins()
        )

        successful_logins = (
            audit_monitor
            .get_successful_logins()
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Audit Events",
            len(audit_events),
        )

        c2.metric(
            "Failed Logins",
            len(failed_logins),
        )

        c3.metric(
            "Successful Logins",
            len(successful_logins),
        )

        tab1, tab2, tab3 = st.tabs(
            [
                "Audit Events",
                "Failed Logins",
                "Successful Logins",
            ]
        )

        with tab1:

            st.dataframe(
                audit_events,
                use_container_width=True,
            )

        with tab2:

            if failed_logins.empty:

                st.success(
                    "No failed login events detected."
                )

            else:

                st.error(
                    "Failed login events detected."
                )

                st.dataframe(
                    failed_logins,
                    use_container_width=True,
                )

        with tab3:

            st.dataframe(
                successful_logins,
                use_container_width=True,
            )

    except Exception as exc:

        st.error(
            f"Audit monitoring failed: {exc}"
        )

    st.divider()

    # =====================================================
    # COMPLIANCE
    # =====================================================

    st.header("📊 Security Compliance")

    try:

        compliance_data = (
            compliance_monitor
            .get_account_compliance()
        )

        findings = (
            compliance_monitor
            .evaluate(
                compliance_data
            )
        )

        if findings:

            st.warning(
                f"{len(findings)} security "
                "findings detected."
            )

            st.dataframe(
                findings,
                use_container_width=True,
            )

        else:

            st.success(
                "No compliance findings detected."
            )

    except Exception as exc:

        st.error(
            f"Compliance evaluation failed: {exc}"
        )

    st.divider()

    # =====================================================
    # REPORT
    # =====================================================

    st.header("📄 Security Report")

    if st.button(
        "Generate Security Report",
        type="primary",
    ):

        try:

            generator = (
                SecurityReportGenerator()
            )

            report = generator.generate(

                users=(
                    users.to_dict(
                        orient="records"
                    )
                    if "users" in locals()
                    else []
                ),

                privileged_users=(
                    privileged_roles.to_dict(
                        orient="records"
                    )
                    if "privileged_roles"
                    in locals()
                    else []
                ),

                failed_logins=(
                    failed_logins.to_dict(
                        orient="records"
                    )
                    if "failed_logins"
                    in locals()
                    else []
                ),

                audit_events=(
                    audit_events.to_dict(
                        orient="records"
                    )
                    if "audit_events"
                    in locals()
                    else []
                ),

                findings=(
                    findings
                    if "findings"
                    in locals()
                    else []
                ),
            )

            st.success(
                f"Report generated: {report}"
            )

        except Exception as exc:

            st.error(
                f"Report generation failed: {exc}"
            )
