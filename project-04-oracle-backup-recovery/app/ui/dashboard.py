import streamlit as st

from app.config import get_settings

from app.database.connection import (
    OracleConnectionManager,
)

from app.database.repository import (
    OracleRepository,
)

from app.backup.backup_monitor import (
    BackupMonitor,
)

from app.backup.recovery_monitor import (
    RecoveryMonitor,
)

from app.backup.archive_monitor import (
    ArchiveMonitor,
)

from app.backup.health import (
    BackupHealthMonitor,
)

from app.reports.generator import (
    BackupReportGenerator,
)


@st.cache_resource
def get_repository():

    manager = OracleConnectionManager()

    manager.initialize()

    return OracleRepository(manager)


def run_dashboard():

    settings = get_settings()

    st.set_page_config(
        page_title=(
            "Oracle Backup & Recovery"
        ),
        page_icon="💾",
        layout="wide",
    )

    st.title(
        "💾 Oracle Backup & Recovery Platform"
    )

    st.caption(
        "Enterprise Backup, Recovery and "
        "Disaster Recovery Monitoring"
    )

    repository = get_repository()

    backup_monitor = BackupMonitor(
        repository
    )

    recovery_monitor = RecoveryMonitor(
        repository
    )

    archive_monitor = ArchiveMonitor(
        repository
    )

    health_monitor = BackupHealthMonitor(
        repository
    )

    # =====================================================
    # BACKUP HEALTH
    # =====================================================

    st.header("Backup Health")

    try:

        health = health_monitor.evaluate()

        status = health.get(
            "status",
            "UNKNOWN",
        )

        if status == "HEALTHY":

            st.success(
                "Backup Status: HEALTHY"
            )

        elif status == "WARNING":

            st.warning(
                "Backup Status: WARNING"
            )

        elif status == "CRITICAL":

            st.error(
                "Backup Status: CRITICAL"
            )

        else:

            st.info(
                "Backup Status: UNKNOWN"
            )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Backup Status",
            status,
        )

        c2.metric(
            "Backup Age",
            f"{health.get('backup_age_hours', 0)} hours",
        )

        c3.metric(
            "Controlfile Backup",
            (
                "Available"
                if health.get(
                    "last_controlfile_backup"
                )
                else "Not Found"
            ),
        )

    except Exception as exc:

        st.error(
            f"Backup health check failed: {exc}"
        )

    st.divider()

    # =====================================================
    # BACKUP HISTORY
    # =====================================================

    st.header("RMAN Backup History")

    try:

        backups = (
            backup_monitor
            .get_backup_history()
        )

        st.dataframe(
            backups,
            use_container_width=True,
        )

    except Exception as exc:

        st.error(
            f"Backup history failed: {exc}"
        )

    st.divider()

    # =====================================================
    # BACKUP SUMMARY
    # =====================================================

    st.header("Backup Summary")

    try:

        summary = (
            backup_monitor
            .get_backup_summary()
        )

        st.dataframe(
            summary,
            use_container_width=True,
        )

    except Exception as exc:

        st.error(
            f"Backup summary failed: {exc}"
        )

    st.divider()

    # =====================================================
    # RECOVERY
    # =====================================================

    st.header("Recovery Status")

    try:

        recovery = (
            recovery_monitor
            .get_recovery_status()
        )

        database_role = (
            recovery_monitor
            .get_database_role()
        )

        instance = (
            recovery_monitor
            .get_instance_status()
        )

        tab1, tab2, tab3 = st.tabs(
            [
                "Recovery",
                "Database Role",
                "Instance",
            ]
        )

        with tab1:

            st.dataframe(
                recovery,
                use_container_width=True,
            )

        with tab2:

            st.dataframe(
                database_role,
                use_container_width=True,
            )

        with tab3:

            st.dataframe(
                instance,
                use_container_width=True,
            )

    except Exception as exc:

        st.error(
            f"Recovery monitoring failed: {exc}"
        )

    st.divider()

    # =====================================================
    # ARCHIVE LOG
    # =====================================================

    st.header("Archive Log Monitoring")

    try:

        archive_summary = (
            archive_monitor
            .get_archive_summary()
        )

        archive_destinations = (
            archive_monitor
            .get_archive_destinations()
        )

        archive_gaps = (
            archive_monitor
            .get_archive_gaps()
        )

        tab1, tab2, tab3 = st.tabs(
            [
                "Archive Summary",
                "Archive Destinations",
                "Archive Gaps",
            ]
        )

        with tab1:

            st.dataframe(
                archive_summary,
                use_container_width=True,
            )

        with tab2:

            st.dataframe(
                archive_destinations,
                use_container_width=True,
            )

        with tab3:

            if archive_gaps.empty:

                st.success(
                    "No archive log gaps detected."
                )

            else:

                st.error(
                    "Archive log gaps detected."
                )

                st.dataframe(
                    archive_gaps,
                    use_container_width=True,
                )

    except Exception as exc:

        st.error(
            f"Archive monitoring failed: {exc}"
        )

    st.divider()

    # =====================================================
    # REPORT
    # =====================================================

    st.header("Operational Report")

    if st.button(
        "Generate Backup & Recovery Report",
        type="primary",
    ):

        try:

            generator = (
                BackupReportGenerator()
            )

            report_path = generator.generate(

                health=health,

                backups=(
                    backups.to_dict(
                        orient="records"
                    )
                    if "backups" in locals()
                    else []
                ),

                recovery=(
                    recovery.to_dict(
                        orient="records"
                    )
                    if "recovery" in locals()
                    else []
                ),

                archive_logs=(
                    archive_summary.to_dict(
                        orient="records"
                    )
                    if "archive_summary"
                    in locals()
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
