import logging
import sys

from app.config import get_settings


def configure_logging() -> None:
    """
    Configure application-wide logging.
    """

    settings = get_settings()

    level = getattr(
        logging,
        settings.log_level.upper(),
        logging.INFO,
    )

    logging.basicConfig(
        level=level,
        format=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        ),
        handlers=[
            logging.StreamHandler(sys.stdout)
        ],
        force=True,
    )
