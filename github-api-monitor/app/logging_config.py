import logging
from pathlib import Path


PROJECT_FOLDER = Path(__file__).resolve().parent.parent
LOG_FOLDER = PROJECT_FOLDER / "logs"
LOG_FILE = LOG_FOLDER / "github_monitor.log"


def configure_logging() -> None:
    LOG_FOLDER.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s | %(levelname)s | "
            "%(name)s | %(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(
                LOG_FILE,
                encoding="utf-8",
            ),
        ],
        force=True,
    )