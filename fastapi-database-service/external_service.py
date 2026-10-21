import httpx


def get_external_status():
    response = httpx.get(
        "https://example.com/status",
        timeout=5
    )

    response.raise_for_status()

    return response.json()