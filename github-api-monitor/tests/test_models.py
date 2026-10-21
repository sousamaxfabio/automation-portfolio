from app.models import Repository


def test_repository_is_active_without_open_issues() -> None:
    repository = Repository(
        name="example",
        url="https://github.com/example/example",
        open_issues=0,
        archived=False,
    )

    assert repository.status() == "active"


def test_repository_reports_open_issues() -> None:
    repository = Repository(
        name="example",
        url="https://github.com/example/example",
        open_issues=3,
        archived=False,
    )

    assert repository.status() == "active with open issues"


def test_archived_repository_status() -> None:
    repository = Repository(
        name="example",
        url="https://github.com/example/example",
        open_issues=3,
        archived=True,
    )

    assert repository.status() == "archived"