def show_welcome_message() -> None:
    print("Starting the service request checker")


show_welcome_message()
def show_request(title: str) -> None:
    print(f"Request: {title}")


show_request("Password reset")
def create_status_message(title: str, resolved: bool) -> str:
    if resolved:
        return f"{title}: closed"
    else:
        return f"{title}: open"


status_message = create_status_message("Password reset", True)
print(status_message)
def needs_attention(minutes_open: int) -> bool:
    return minutes_open >= 60


attention_required = needs_attention(30)
print(f"Needs attention: {attention_required}")
service_request = {
    "title": "Webhook authentication failure",
    "resolved": False,
    "minutes_open": 120,
}


def get_request_minutes(request: dict) -> int:
    return request["minutes_open"]


request_minutes = get_request_minutes(service_request)
print(f"Request minutes open: {request_minutes}")