from app.models import Repository


REQUIRED_FIELDS = (
    "name",
    "html_url",
    "open_issues_count",
    "archived",
)


def transform_repository(data: dict) -> Repository:
    missing_fields = [
        field
        for field in REQUIRED_FIELDS
        if field not in data
    ]

    if missing_fields:
        missing_names = ", ".join(missing_fields)
        raise ValueError(f"Missing required repository fields: {missing_names}")

    return Repository(
        name=data["name"],
        url=data["html_url"],
        open_issues=data["open_issues_count"],
        archived=data["archived"],
    )