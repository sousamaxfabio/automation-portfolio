class ServiceRequest:
    def __init__(
        self,
        request_id: str,
        title: str,
        priority: str,
        minutes_open: int,
        resolved: bool = False,
    ) -> None:
        self.request_id = request_id
        self.title = title
        self.priority = priority
        self.minutes_open = minutes_open
        self.resolved = resolved

    def needs_attention(self) -> bool:
        return not self.resolved and self.minutes_open >= 60

    def resolve(self) -> None:
        self.resolved = True


request = ServiceRequest(
    request_id="SR-001",
    title="Password reset",
    priority="low",
    minutes_open=90,
)

print(f"Before resolving: {request.needs_attention()}")

request.resolve()

print(f"After resolving: {request.needs_attention()}")
