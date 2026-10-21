import pytest

from app.transformers import transform_repository


def test_transform_repository() -> None:
    api_data = {
        "name": "automation-portfolio",
        "html_url": "https://github.com/example/automation-portfolio",
        "open_issues_count": 2,
        "archived": False,
    }

    repository = transform_repository(api_data)

    assert repository.name == "automation-portfolio"
    assert repository.url == "https://github.com/example/automation-portfolio"
    assert repository.open_issues == 2
    assert repository.archived is False


def test_transform_repository_rejects_missing_data() -> None:
    incomplete_api_data = {
        "name": "automation-portfolio",
        "html_url": "https://github.com/example/automation-portfolio",
        "archived": False,
    }

    with pytest.raises(ValueError, match="open_issues_count"):
        transform_repository(incomplete_api_data)