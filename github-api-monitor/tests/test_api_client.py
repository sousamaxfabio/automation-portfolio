from unittest.mock import Mock

import pytest

from app.api_client import fetch_repositories
from app.exceptions import GitHubApiError


def create_response(
    status_code: int,
    data: list | None = None,
    remaining: str = "4999",
) -> Mock:
    response = Mock()
    response.status_code = status_code
    response.headers = {
        "X-RateLimit-Limit": "5000",
        "X-RateLimit-Remaining": remaining,
        "X-RateLimit-Reset": "1234567890",
    }
    response.json.return_value = data if data is not None else []
    return response


def test_fetch_repositories_success(monkeypatch) -> None:
    api_data = [
        {
            "name": "example",
            "html_url": "https://github.com/example/example",
            "open_issues_count": 0,
            "archived": False,
        }
    ]
    response = create_response(200, api_data)

    monkeypatch.setattr(
        "app.api_client.get_with_retries",
        lambda **kwargs: response,
    )

    result = fetch_repositories(
        username="example",
        token=None,
    )

    assert result == api_data


def test_fetch_repositories_uses_pagination(monkeypatch) -> None:
    first_page = create_response(
        200,
        [{"name": "first"}],
    )
    empty_page = create_response(200, [])
    responses = iter([first_page, empty_page])
    call_count = 0

    def fake_request(**kwargs):
        nonlocal call_count
        call_count += 1
        return next(responses)

    monkeypatch.setattr(
        "app.api_client.get_with_retries",
        fake_request,
    )

    result = fetch_repositories(
        username="example",
        per_page=1,
    )

    assert result == [{"name": "first"}]
    assert call_count == 2


def test_fetch_repositories_rejects_invalid_token(
    monkeypatch,
) -> None:
    response = create_response(401)

    monkeypatch.setattr(
        "app.api_client.get_with_retries",
        lambda **kwargs: response,
    )

    with pytest.raises(
        GitHubApiError,
        match="Authentication failed",
    ):
        fetch_repositories("example", token="invalid")


def test_fetch_repositories_detects_rate_limit(
    monkeypatch,
) -> None:
    response = create_response(
        403,
        remaining="0",
    )

    monkeypatch.setattr(
        "app.api_client.get_with_retries",
        lambda **kwargs: response,
    )

    with pytest.raises(
        GitHubApiError,
        match="API rate limit reached",
    ):
        fetch_repositories("example")


def test_fetch_repositories_rejects_unknown_user(
    monkeypatch,
) -> None:
    response = create_response(404)

    monkeypatch.setattr(
        "app.api_client.get_with_retries",
        lambda **kwargs: response,
    )

    with pytest.raises(
        GitHubApiError,
        match="GitHub user not found",
    ):
        fetch_repositories("missing-user")