import requests

from app.exceptions import GitHubApiError
from app.http_client import get_with_retries


GITHUB_API_URL = "https://api.github.com"


def fetch_repositories(
    username: str,
    token: str | None = None,
    per_page: int = 100,
) -> list[dict]:
    url = f"{GITHUB_API_URL}/users/{username}/repos"

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "github-repository-monitor",
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"
        print("Authentication: bearer token")
    else:
        print("Authentication: none")

    all_repositories = []
    page = 1

    while True:
        parameters = {
            "page": page,
            "per_page": per_page,
            "sort": "updated",
        }

        print(f"Fetching page: {page}")

        response = get_with_retries(
            url=url,
            headers=headers,
            parameters=parameters,
            timeout=10,
        )

        print(f"HTTP status: {response.status_code}")

        rate_limit = response.headers.get(
            "X-RateLimit-Limit",
            "unknown",
        )
        remaining = response.headers.get(
            "X-RateLimit-Remaining",
            "unknown",
        )

        print(f"Rate limit remaining: {remaining}/{rate_limit}")

        if response.status_code == 401:
            raise GitHubApiError(
                "Authentication failed: check the GitHub token"
            )

        if response.status_code == 403:
            if remaining == "0":
                reset_time = response.headers.get(
                    "X-RateLimit-Reset",
                    "unknown",
                )
                raise GitHubApiError(
                    f"API rate limit reached; reset time: {reset_time}"
                )

            raise GitHubApiError(
                "Access forbidden: check token permissions"
            )

        if response.status_code == 404:
            raise GitHubApiError(
                f"GitHub user not found: {username}"
            )

        try:
            response.raise_for_status()
        except requests.HTTPError as error:
            raise GitHubApiError(
                f"GitHub returned HTTP {response.status_code}"
            ) from error

        page_data = response.json()

        if not isinstance(page_data, list):
            raise GitHubApiError(
                "GitHub returned an unexpected response format"
            )

        all_repositories.extend(page_data)

        if len(page_data) < per_page:
            break

        page += 1

    return all_repositories