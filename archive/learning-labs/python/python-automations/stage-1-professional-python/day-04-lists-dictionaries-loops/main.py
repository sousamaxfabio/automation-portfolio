service_requests = [
    {
        "id": "SR-001",
        "title": "Password reset",
        "priority": "low",
        "resolved": True,
    },
    {
        "id": "SR-002",
        "title": "Payment API unavailable",
        "priority": "critical",
        "resolved": False,
    },
]

print(service_requests[0])
print(service_requests[0]["title"])
for request in service_requests:
    if not request["resolved"]:
        print(
            f"Open: {request['id']} - {request['title']}"
        )
open_count = 0

for request in service_requests:
    if not request["resolved"]:
        open_count += 1                           

print(f"Open requests: {open_count}")
def count_open_requests(requests: list) -> int:
    count = 0

    for request in requests:
        if not request["resolved"]:
            count += 1

    return count

service_requests.append(
    {
        "id": "SR-003",
        "title": "New employee access",
        "priority": "medium",
        "resolved": False,
    }
)
total_open = count_open_requests(service_requests)
print(f"Function result: {total_open}")