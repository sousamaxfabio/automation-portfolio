import json
from pathlib import Path

from app.models import Repository


PROJECT_FOLDER = Path(__file__).resolve().parent.parent
DATA_FOLDER = PROJECT_FOLDER / "data"
OUTPUT_FILE = DATA_FOLDER / "repositories.json"


def save_repositories(
    repositories: list[Repository],
) -> Path:
    DATA_FOLDER.mkdir(parents=True, exist_ok=True)

    output_data = [
        repository.to_dict()
        for repository in repositories
    ]

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            output_data,
            file,
            indent=4,
            ensure_ascii=False,
        )

    return OUTPUT_FILE