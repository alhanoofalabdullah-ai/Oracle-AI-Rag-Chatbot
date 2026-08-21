import logging
import subprocess
from pathlib import Path

from app.config import get_settings


logger = logging.getLogger(__name__)


class RMANCommandRunner:
    """
    Safely execute RMAN command files.

    Intended for controlled Oracle test environments.
    """

    def __init__(self) -> None:
        self.settings = get_settings()

    def execute(
        self,
        script_path: str,
    ) -> dict:

        path = Path(script_path)

        if not path.exists():
            raise FileNotFoundError(
                f"RMAN script not found: {path}"
            )

        logger.info(
            "Executing RMAN script: %s",
            path,
        )

        command = [
            self.settings.rman_executable,
            "target",
            "/",
            "cmdfile",
            str(path),
        ]

        process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
        )

        return {
            "return_code": process.returncode,
            "stdout": process.stdout,
            "stderr": process.stderr,
            "success": process.returncode == 0,
        }
