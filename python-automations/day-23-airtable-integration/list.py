import os, requests
from dotenv import load_dotenv
load_dotenv(override=True)
token = os.getenv("AIRTABLE_TOKEN")
base = os.getenv("AIRTABLE_BASE_ID")
headers = {"Authorization": f"Bearer {token}"}
r = requests.get(f"https://api.airtable.com/v0/meta/bases/{base}/tables", headers=headers)
for t in r.json()['tables']:
    print(t['name'], "->", t['id'], "-> Fields:", [f['name'] for f in t['fields']])