import streamlit as st

from app.config import get_settings

from app.database.connection import (
    OracleConnectionManager,
)

from app.database.repository import (
    OracleRepository,
)

from app.monitoring.performance import (
    PerformanceMonitor,
)

from app.monitoring.sql_analysis import (
    SQLAnalysisMonitor,
)

from app.monitoring.wait_events import (
    WaitEventMonitor,
)

from app.monitoring.sessions import (
    SessionPerformanceMonitor,
)

from app.monitoring.system_metrics import (
    SystemMetricsMonitor,
)

from app.monitoring.health import (
    PerformanceHealthMonitor,
)

from app.reports.generator import (
    PerformanceReportGenerator,
)


@st.cache_resource
def get_repository():

    manager = OracleConnectionManager()

    manager.initialize()

    return OracleRepository(manager)


def run_dashboard():

    settings = get_settings()

    st.set_page_config(
        page_title=settings.app_name,
        page_icon="📊",
        layout="wide",
    )

    st.title(
        "📊 Oracle Performance Monitoring"
    )

    st.caption(
        "Enterprise Oracle Database Performance "
        "Monitoring & SQL Tuning Platform"
    )

    repository = get_repository()

    performance = PerformanceMonitor(
        repository
    )

    sql_monitor = SQLAnalysisMonitor(
        repository
    )

    wait_monitor = WaitEventMonitor(
        repository
    )

    session_monitor = (
        SessionPerformanceMonitor(
            repository
        )
    )

    metrics_monitor = (
        SystemMetricsMonitor(
            repository
        )
    )

    health_monitor = (
        PerformanceHealthMonitor(
            repository
        )
    )

    # =====================================================
    # HEALTH
    # =====================================================

    st.header("Database Performance Health")

    try:

        health = health_monitor.check()

        if health["status"] == "HEALTHY":

            st.success(
                "Database Performance Status: HEALTHY"
            )

        elif health["status"] == "WARNING":

            st.warning(
                "Database Performance Status: WARNING"
            )

        else:

            st.error(
                "Database Performance Status: UNHEALTHY"
            )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Database",
            health.get(
                "database_name",
                "N/A",
            ),
        )

        c2.metric(
            "Open Mode",
            health.get(
                "open_mode",
                "N/A",
            ),
        )

        c3.metric(
            "Instance",
            health.get(
                "instance_name",
                "N/A",
            ),
        )

        c4.metric(
            "Role",
            health.get(
                "database_role",
                "N/A",
            ),
        )

    except Exception as exc:

        st.error(
            f"Health check failed: {exc}"
        )

        return

    st.divider()

    # =====================================================
    # SYSTEM METRICS
    # =====================================================

    st.header("System Metrics")

    try:

        metrics = (
            performance.get_system_metrics()
        )

        st.dataframe(
            metrics,
            use_container_width=True,
        )

    except Exception as exc:

        st.error(
            f"System metrics failed: {exc}"
        )

    st.divider()

    # =====================================================
    # DATABASE STATISTICS
    # =====================================================

    st.header("Database Statistics")

    try:

        statistics = (
            metrics_monitor
            .get_database_statistics()
        )

        st.dataframe(
            statistics,
            use_container_width=True,
        )

    except Exception as exc:

        st.error(
            f"Database statistics failed: {exc}"
        )

    st.divider()

    # =====================================================
    # TOP SQL
    # =====================================================

    st.header("SQL Performance Analysis")

    try:

        tab1, tab2, tab3 = st.tabs(
            [
                "Top SQL - Elapsed Time",
                "Top SQL - CPU",
                "Top SQL - I/O",
            ]
        )

        with tab1:

            top_sql_elapsed = (
                sql_monitor
                .get_top_sql_by_elapsed()
            )

            st.dataframe(
                top_sql_elapsed,
                use_container_width=True,
            )

        with tab2:

            top_sql_cpu = (
                sql_monitor
                .get_top_sql_by_cpu()
            )

            st.dataframe(
                top_sql_cpu,
                use_container_width=True,
            )

        with tab3:

            top_sql_io = (
                sql_monitor
                .get_top_sql_by_io()
            )

            st.dataframe(
                top_sql_io,
                use_container_width=True,
            )

    except Exception as exc:

        st.error(
            f"SQL analysis failed: {exc}"
        )

    st.divider()

    # =====================================================
    # WAIT EVENTS
    # =====================================================

    st.header("Wait Event Analysis")

    try:

        waits = (
            wait_monitor.get_wait_events()
        )

        st.dataframe(
            waits,
            use_container_width=True,
        )

    except Exception as exc:

        st.error(
            f"Wait-event analysis failed: {exc}"
        )

    st.divider()

    # =====================================================
    # SESSIONS
    # =====================================================

    st.header("Session Performance")

    try:

        active_count = (
            session_monitor
            .get_active_count()
        )

        col1, col2 = st.columns(2)

        col1.metric(
            "Active Sessions",
            active_count,
        )

        long_running = (
            session_monitor
            .get_long_running_sessions(
                minimum_seconds=300
            )
        )

        col2.metric(
            "Long Running Sessions",
            len(long_running),
        )

        st.subheader(
            "Active Sessions"
        )

        active = (
            session_monitor
            .get_active_sessions()
        )

        st.dataframe(
            active,
            use_container_width=True,
        )

        st.subheader(
            "Long Running Sessions"
        )

        st.dataframe(
            long_running,
            use_container_width=True,
        )

    except Exception as exc:

        st.error(
            f"Session monitoring failed: {exc}"
        )

    st.divider()

    # =====================================================
    # REPORT
    # =====================================================

    st.header("Performance Report")

    if st.button(
        "Generate Performance Report",
        type="primary",
    ):

        try:

            generator = (
                PerformanceReportGenerator()
            )

            report_path = generator.generate(

                health=health,

                system_metrics=(
                    metrics.to_dict(
                        orient="records"
                    )
                    if "metrics" in locals()
                    else []
                ),

                top_sql=(
                    top_sql_elapsed.to_dict(
                        orient="records"
                    )
                    if "top_sql_elapsed"
                    in locals()
                    else []
                ),

                waits=(
                    waits.to_dict(
                        orient="records"
                    )
                    if "waits" in locals()
                    else []
                ),

                sessions=(
                    active.to_dict(
                        orient="records"
                    )
                    if "active" in locals()
                    else []
                ),
            )

            st.success(
                f"Report generated: {report_path}"
            )

        except Exception as exc:

            st.error(
                f"Report generation failed: {exc}"
            )
