import requests


url = "https://postman-echo.com/post"

payload = {
    "event": "repository_audit",
    "repository": "automation-portfolio",
    "status": "active",
}

response = requests.post(
    url,
    json=payload,
    timeout=10,
)

print(f"HTTP status: {response.status_code}")

response.raise_for_status()

response_data = response.json()
echoed_payload = response_data["json"]

print(f"Sent payload: {payload}")
print(f"Echoed payload: {echoed_payload}")

if echoed_payload != payload:
    raise ValueError("The echoed JSON does not match the sent payload")

print("JSON request body validated successfully")