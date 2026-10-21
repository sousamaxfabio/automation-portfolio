import os
import requests
from dotenv import load_dotenv

# [ ] Environment variables + .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL", "https://jsonplaceholder.typicode.com")
TIMEOUT = int(os.getenv("TIMEOUT", "5"))

print(f"Using API: {API_URL}")
print(f"Using Key: {API_KEY[:5]}... (from .env)\n")

# --- 1. GET request with Auth + Timeout + Parse JSON ---
print("--- [GET] Testing GET request ---")
try:
    headers = {
        "Authorization": f"Bearer {API_KEY}"  # [ ] Authentication
    }
    # [ ] GET requests + [ ] requests + [ ] Timeouts + [ ] Parse JSON responses
    response = requests.get(
        f"{API_URL}/posts/1",
        headers=headers,
        timeout=TIMEOUT
    )
    response.raise_for_status()  # will raise for 4xx/5xx
    
    data = response.json()  # [ ] Parse JSON responses
    print(f"✅ GET SUCCESS: {data}\n")

except requests.exceptions.Timeout:
    print(f"❌ GET Failed: Timeout after {TIMEOUT}s")
except requests.exceptions.RequestException as e:
    print(f"❌ GET Failed: {e}\n")

# --- 2. Failed request handling ---
print("--- [FAILED] Testing failed request ---")
try:
    # Intentional wrong URL to show error handling
    bad_response = requests.get(
        f"{API_URL}/invalid-endpoint-xyz",
        timeout=TIMEOUT
    )
    bad_response.raise_for_status()
    
except requests.exceptions.HTTPError as e:
    print(f"✅ Correctly handled failed request: {e}")
    print(f"Status Code: {e.response.status_code} -> Failed request logic works!\n")
except requests.exceptions.RequestException as e:
    print(f"✅ Correctly handled failed request: {e}\n")

# --- 3. POST request with Auth + JSON ---
print("--- [POST] Testing POST request ---")
try:
    payload = {
        "title": "Day 24 Test",
        "body": "Learning APIs with Python",
        "userId": 1
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    # [ ] POST requests
    post_response = requests.post(
        f"{API_URL}/posts",
        json=payload,
        headers=headers,
        timeout=TIMEOUT
    )
    post_response.raise_for_status()
    
    post_data = post_response.json()
    print(f"✅ POST SUCCESS: Created -> {post_data}")

except requests.exceptions.Timeout:
    print(f"❌ POST Failed: Timeout after {TIMEOUT}s")
except requests.exceptions.RequestException as e:
    print(f"❌ POST Failed: {e}")

print("\nDone! All Day 24 checks passed.")