class Repository:
    def __init__(
        self,
        name: str,
        url: str,
        open_issues: int,
        archived: bool,
    ) -> None:
        self.name = name
        self.url = url
        self.open_issues = open_issues
        self.archived = archived

    def status(self) -> str:
        if self.archived:
            return "archived"

        if self.open_issues > 0:
            return "active with open issues"

        return "active"

    def to_dict(self) -> dict[str, str | int | bool]:
        return {
            "name": self.name,
            "url": self.url,
            "open_issues": self.open_issues,
            "archived": self.archived,
            "status": self.status(),
        }