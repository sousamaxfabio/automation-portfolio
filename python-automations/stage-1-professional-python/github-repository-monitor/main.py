import logging

from app.api_client import fetch_repositories
from app.config import get_github_token, get_github_username
from app.exceptions import GitHubApiError
from app.logging_config import configure_logging
from app.storage import save_repositories
from app.transformers import transform_repository


configure_logging()
logger = logging.getLogger(__name__)

username = get_github_username()
token = get_github_token()

try:
    raw_repositories = fetch_repositories(
        username=username,
        token=token,
    )
except GitHubApiError as error:
    logger.error("GitHub API request failed: %s", error)
    raise SystemExit(1)

repositories = [
    transform_repository(data)
    for data in raw_repositories
]

logger.info(
    "Repositories returned: %s",
    len(repositories),
)

for repository in repositories:
    logger.info(
        "Repository=%s | Status=%s",
        repository.name,
        repository.status(),
    )

output_file = save_repositories(repositories)

logger.info(
    "Repository data saved: %s",
    output_file,
)