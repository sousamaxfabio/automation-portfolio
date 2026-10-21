import os
from pathlib import Path

from dotenv import load_dotenv


PROJECT_FOLDER = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_FOLDER / ".env"

load_dotenv(ENV_FILE)


def get_github_username() -> str:
    return os.getenv("GITHUB_USERNAME", "sousamaxfabio")


def get_github_token() -> str | None:
    return os.getenv("GITHUB_TOKEN")