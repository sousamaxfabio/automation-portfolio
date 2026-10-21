import requests, os
from dotenv import load_dotenv
load_dotenv(override=True)
token = os.getenv("AIRTABLE_TOKEN")
r = requests.get("https://api.airtable.com/v0/meta/whoami", headers={"Authorization": f"Bearer {token}"})
print(r.text)