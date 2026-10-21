service_requests = [
    {
        "id": "SR-001",
        "title": "Password reset",
        "priority": "low",
        "minutes_open": 15,
        "resolved": True,
    },
    {
        "id": "SR-002",
        "title": "Payment API unavailable",
        "priority": "critical",
        "minutes_open": 90,
        "resolved": False,
    },
    {
        "id": "SR-003",
        "title": "New employee access",
        "priority": "medium",
        "minutes_open": 45,
        "resolved": False,
    },
    {
        "id": "SR-004",
        "title": "Webhook authentication failure",
        "priority": "high",
        "minutes_open": 120,
        "resolved": False,
    },
]
def count_unresolved(requests):
    count = 0

    for request in requests:
        if request["resolved"] is False:
            count += 1

    return count


unresolved_total = count_unresolved(service_requests)
print(f"Unresolved requests: {unresolved_total}")

def count_resolved(requests):
    count = 0

    for request in requests:
        if request["resolved"] is True:
            count += 1

    return count

resolved_total = count_resolved(service_requests)
print(f"Resolved requests: {resolved_total}")


def get_unresolved_titles_short(requests):
    return [
        request["title"]
        for request in requests
        if not request["resolved"]
    ]


short_titles = get_unresolved_titles_short(service_requests)
print(f"Using comprehension: {short_titles}")
unresolved_priorities = {
    request["priority"]
    for request in service_requests
    if not request["resolved"]
}

print(f"Unresolved priorities: {sorted(unresolved_priorities)}")