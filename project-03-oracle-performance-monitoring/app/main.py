from app.config import get_settings
from app.logging_config import configure_logging
from app.ui.dashboard import run_dashboard


def main():

    settings = get_settings()

    configure_logging(
        settings.log_level
    )

    run_dashboard()


if __name__ == "__main__":
    main()
