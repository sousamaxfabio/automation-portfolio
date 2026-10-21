from unittest.mock import Mock

import pytest
import requests

from app.exceptions import GitHubApiError
from app.http_client import get_with_retries


def test_request_succeeds_after_two_timeouts(monkeypatch) -> None:
    call_count = 0
    successful_response = Mock(status_code=200)

    def fake_get(*args, **kwargs):
        nonlocal call_count
        call_count += 1

        if call_count < 3:
            raise requests.Timeout

        return successful_response

    monkeypatch.setattr(
        "app.http_client.requests.get",
        fake_get,
    )
    monkeypatch.setattr(
        "app.http_client.time.sleep",
        lambda seconds: None,
    )

    response = get_with_retries(
        url="https://example.com",
        headers={},
        parameters={},
        timeout=1,
        max_attempts=3,
    )

    assert response.status_code == 200
    assert call_count == 3


def test_request_fails_after_final_timeout(monkeypatch) -> None:
    def always_timeout(*args, **kwargs):
        raise requests.Timeout

    monkeypatch.setattr(
        "app.http_client.requests.get",
        always_timeout,
    )
    monkeypatch.setattr(
        "app.http_client.time.sleep",
        lambda seconds: None,
    )

    with pytest.raises(
        GitHubApiError,
        match="Request failed after 3 attempts",
    ):
        get_with_retries(
            url="https://example.com",
            headers={},
            parameters={},
            timeout=1,
            max_attempts=3,
        )