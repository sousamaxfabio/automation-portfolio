import json
import csv
from pathlib import Path


folder = Path(__file__).parent
json_file = folder / "requests.json"

with json_file.open("r", encoding="utf-8") as file:
    service_requests = json.load(file)

print(service_requests)
for request in service_requests:
    print(f"{request['id']}: {request['title']}")
    unresolved_requests = [
    request
    for request in service_requests
    if not request["resolved"]
]

output_file = folder / "unresolved_requests.json"

with output_file.open("w", encoding="utf-8") as file:
    json.dump(unresolved_requests, file, indent=4)

print(f"Saved unresolved requests to: {output_file.name}")
csv_file = folder / "requests.csv"

with csv_file.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    csv_requests = list(reader)

for request in csv_requests:
    request["resolved"] = request["resolved"].lower() == "true"

print(csv_requests)
unresolved_csv_requests = [
    request
    for request in csv_requests
    if not request["resolved"]
]

output_csv_file = folder / "unresolved_requests.csv"
columns = ["id", "title", "priority", "resolved"]

with output_csv_file.open("w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(unresolved_csv_requests)

print(f"Saved unresolved CSV requests to: {output_csv_file.name}")