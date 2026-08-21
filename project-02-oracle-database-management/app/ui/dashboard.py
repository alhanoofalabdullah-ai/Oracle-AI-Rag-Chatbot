import streamlit as st

from app.config import get_settings
from app.database.connection import OracleConnectionManager
from app.database.repository import OracleRepository

from app.monitoring.health import HealthMonitor
from app.monitoring.database_info import DatabaseInfoMonitor
from app.monitoring.storage import StorageMonitor
from app.monitoring.sessions import SessionMonitor
from app.monitoring.performance import PerformanceMonitor

from app.reports.generator import HealthReportGenerator


@st.cache_resource
def get_repository():

    manager = OracleConnectionManager()
    manager.initialize()

    return OracleRepository(manager)


def run_dashboard():

    settings = get_settings()

    st.set_page_config(
        page_title=settings.app_name,
        page_icon="🗄️",
        layout="wide",
    )

    st.title("🗄️ Oracle Database Management")
    st.caption(
        "Enterprise Database Health & Monitoring Dashboard"
    )

    repository = get_repository()

    health_monitor = HealthMonitor(repository)
    database_monitor = DatabaseInfoMonitor(repository)
    storage_monitor = StorageMonitor(repository)
    session_monitor = SessionMonitor(repository)
    performance_monitor = PerformanceMonitor(repository)

    # --------------------------------------------------
    # HEALTH
    # --------------------------------------------------

    st.header("Database Health")

    try:

        health = health_monitor.check_database()

        status = health["status"]

        if status == "HEALTHY":
            st.success("Database Status: HEALTHY")

        elif status == "WARNING":
            st.warning("Database Status: WARNING")

        else:
            st.error("Database Status: UNHEALTHY")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Database",
            health.get("database_name", "N/A"),
        )

        col2.metric(
            "Open Mode",
            health.get("open_mode", "N/A"),
        )

        col3.metric(
            "Role",
            health.get("database_role", "N/A"),
        )

        col4.metric(
            "Instance",
            health.get("instance_name", "N/A"),
        )

    except Exception as exc:

        st.error(
            f"Database health check failed: {exc}"
        )

        return

    st.divider()

    # --------------------------------------------------
    # DATABASE INFORMATION
    # --------------------------------------------------

    st.header("Database Information")

    try:

        database_info = (
            database_monitor.get_database_info()
        )

        instance_info = (
            database_monitor.get_instance_info()
        )

        st.subheader("Database")

        st.dataframe(
            database_info,
            use_container_width=True,
        )

        st.subheader("Instance")

        st.dataframe(
            instance_info,
            use_container_width=True,
        )

    except Exception as exc:

        st.error(
            f"Unable to retrieve database information: {exc}"
        )

    st.divider()

    # --------------------------------------------------
    # STORAGE
    # --------------------------------------------------

    st.header("Tablespace Monitoring")

    try:

        storage = (
            storage_monitor.get_tablespaces_with_status(
                warning=settings.tablespace_warning_percent,
                critical=settings.tablespace_critical_percent,
            )
        )

        if storage.empty:
            st.info("No tablespace information available.")

        else:

            st.dataframe(
                storage,
                use_container_width=True,
            )

    except Exception as exc:

        st.error(
            f"Storage monitoring failed: {exc}"
        )

    st.divider()

    # --------------------------------------------------
    # SESSIONS
    # --------------------------------------------------

    st.header("Session Monitoring")

    try:

        total_sessions = (
            session_monitor.get_total_sessions()
        )

        active_sessions = (
            session_monitor.get_active_session_count()
        )

        col1, col2 = st.columns(2)

        col1.metric(
            "Total Sessions",
            total_sessions,
        )

        col2.metric(
            "Active Sessions",
            active_sessions,
        )

        st.subheader("Session Summary")

        summary = (
            session_monitor.get_session_summary()
        )

        st.dataframe(
            summary,
            use_container_width=True,
        )

        st.subheader("Active Sessions")

        active = (
            session_monitor.get_active_sessions()
        )

        st.dataframe(
            active,
            use_container_width=True,
        )

    except Exception as exc:

        st.error(
            f"Session monitoring failed: {exc}"
        )

    st.divider()

    # --------------------------------------------------
    # PERFORMANCE
    # --------------------------------------------------

    st.header("Performance Monitoring")

    try:

        st.subheader("System Metrics")

        metrics = (
            performance_monitor.get_system_metrics()
        )

        st.dataframe(
            metrics,
            use_container_width=True,
        )

        st.subheader("Top SQL")

        top_sql = (
            performance_monitor.get_top_sql()
        )

        st.dataframe(
            top_sql,
            use_container_width=True,
        )

        st.subheader("Wait Events")

        waits = (
            performance_monitor.get_wait_events()
        )

        st.dataframe(
            waits,
            use_container_width=True,
        )

    except Exception as exc:

        st.error(
            f"Performance monitoring failed: {exc}"
        )

    st.divider()

    # --------------------------------------------------
    # REPORT
    # --------------------------------------------------

    st.header("Operational Report")

    if st.button(
        "Generate Health Report",
        type="primary",
    ):

        try:

            storage_records = (
                storage.to_dict(orient="records")
                if "storage" in locals()
                else []
            )

            session_records = (
                summary.to_dict(orient="records")
                if "summary" in locals()
                else []
            )

            performance_records = (
                metrics.to_dict(orient="records")
                if "metrics" in locals()
                else []
            )

            generator = HealthReportGenerator()

            report_path = generator.generate(
                health=health,
                storage=storage_records,
                sessions={
                    "total_sessions": total_sessions,
                    "active_sessions": active_sessions,
                    "summary": session_records,
                },
                performance={
                    "system_metrics": performance_records,
                    "top_sql": (
                        top_sql.to_dict(
                            orient="records"
                        )
                        if "top_sql" in locals()
                        else []
                    ),
                },
            )

            st.success(
                f"Report generated: {report_path}"
            )

        except Exception as exc:

            st.error(
                f"Report generation failed: {exc}"
            )
