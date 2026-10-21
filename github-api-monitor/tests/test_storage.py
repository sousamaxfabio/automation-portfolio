import json

from app.models import Repository
from app.storage import save_repositories


def test_save_repositories(monkeypatch, tmp_path) -> None:
    temporary_output = tmp_path / "repositories.json"

    monkeypatch.setattr(
        "app.storage.OUTPUT_FILE",
        temporary_output,
    )

    repositories = [
        Repository(
            name="example",
            url="https://github.com/example/example",
            open_issues=2,
            archived=False,
        )
    ]

    saved_file = save_repositories(repositories)

    saved_data = json.loads(
        saved_file.read_text(encoding="utf-8")
    )

    assert saved_file == temporary_output
    assert saved_data == [
        {
            "name": "example",
            "url": "https://github.com/example/example",
            "open_issues": 2,
            "archived": False,
            "status": "active with open issues",
        }
    ]