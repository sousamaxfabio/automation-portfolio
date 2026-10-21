def create_status_message(title: str, resolved: bool) -> str:
    if resolved:
        return f"{title}: closed"
    else:
        return f"{title}: open"


def needs_attention(minutes_open: int) -> bool:
    return minutes_open >= 60    