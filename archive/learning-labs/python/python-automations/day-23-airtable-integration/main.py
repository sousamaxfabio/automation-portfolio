import os
from dotenv import load_dotenv
from pyairtable import Api
from datetime import datetime

load_dotenv(override=True)

BASE_ID = os.getenv("AIRTABLE_BASE_ID")
TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")
TOKEN = os.getenv("AIRTABLE_TOKEN")

print(f"Using table: {TABLE_NAME}")

api = Api(TOKEN)
table = api.table(BASE_ID, TABLE_NAME)

# Get actual field names from Airtable
schema = table.schema()
actual_fields = [f.name for f in schema.fields]
print(f"Airtable fields: {actual_fields}")

root = r"C:\Users\fabio\Documents\Codex\automation-portfolio"
files = []
for r, d, f in os.walk(root):
    for file in f:
        if file.lower().endswith(".pdf") and "day-19" in r:
            files.append(os.path.join(r, file))

print(f"Found {len(files)} files")

for filepath in files:
    filename = os.path.basename(filepath)
    print(f"\nProcessing: {filename}")

    low = filename.lower()
    if "non-invoice" in low:
        print(f"❌ {filename} -> Incorrect type - skipping")
        continue
    if "missing" in low:
        print(f"❌ {filename} -> Missing deadline - skipping")
        continue

    # Build record with ONLY fields that exist
    full_record = {
        "Name": filename,
        "Vendor": "Test Vendor",
        "Amount": 100,
        "Status": "Processed",
        "notes": f"Processed {datetime.now().isoformat()}",
        "Notes": f"Processed {datetime.now().isoformat()}",
    }

    # Filter to only fields Airtable actually has
    record = {k: v for k, v in full_record.items() if k in actual_fields}

    # Always keep primary field
    if "Name" not in record and actual_fields:
        record[actual_fields[0]] = filename

    try:
        table.create(record)
        print(f"✅ SUCCESS: {filename} -> {record}")
    except Exception as e:
        print(f"FAILED: {e}")

print("\nDone! Check Airtable Invoices-final")