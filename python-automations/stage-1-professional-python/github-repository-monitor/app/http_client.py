import logging
import time

import requests

from app.exceptions import GitHubApiError


logger = logging.getLogger(__name__)

RETRYABLE_STATUS_CODES = {
    429,
    500,
    502,
    503,
    504,
}


def get_with_retries(
    url: str,
    headers: dict[str, str],
    parameters: dict[str, object],
    timeout: int = 10,
    max_attempts: int = 3,
) -> requests.Response:
    for attempt in range(1, max_attempts + 1):
        try:
            response = requests.get(
                url,
                headers=headers,
                params=parameters,
                timeout=timeout,
            )
        except (requests.Timeout, requests.ConnectionError) as error:
            if attempt == max_attempts:
                raise GitHubApiError(
                    f"Request failed after {max_attempts} attempts"
                ) from error

            wait_seconds = 2 ** (attempt - 1)
            logger.warning(
                "Network failure | Attempt=%s/%s | RetryIn=%ss",
                attempt,
                max_attempts,
                wait_seconds,
            )
            time.sleep(wait_seconds)
            continue
        except requests.RequestException as error:
            raise GitHubApiError(
                "Unexpected HTTP request failure"
            ) from error

        if response.status_code not in RETRYABLE_STATUS_CODES:
            return response

        if attempt == max_attempts:
            raise GitHubApiError(
                f"HTTP {response.status_code} continued after "
                f"{max_attempts} attempts"
            )

        wait_seconds = 2 ** (attempt - 1)
        logger.warning(
            "Retryable HTTP status=%s | Attempt=%s/%s | "
            "RetryIn=%ss",
            response.status_code,
            attempt,
            max_attempts,
            wait_seconds,
        )
        time.sleep(wait_seconds)

    raise GitHubApiError("Request failed unexpectedly")