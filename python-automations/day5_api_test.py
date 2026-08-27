import os

import requests
from dotenv import load_dotenv


load_dotenv()

API_URL = os.getenv("API_URL", "https://jsonplaceholder.typicode.com")

print("--- TESTING GET ---")
r = requests.get(f"{API_URL}/posts/1")
print(f"Status: {r.status_code}")
print(r.json())

print("\n--- TESTING POST ---")
data = {
	"title": "my first automation",
	"body": "learning APIs - Day 5",
	"userId": 1,
}
r2 = requests.post(f"{API_URL}/posts", json=data)
print(f"Status: {r2.status_code}")
print(r2.json())

if r2.status_code == 201:
	print("✅ POST SUCCESS!")
