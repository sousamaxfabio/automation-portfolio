invoice_file = "valid-invoice-N8N-20260907-7F3C9A.pdf"
vendor_name = "Acme Corp"
amount = 1250
print(invoice_file)

# Step 2: Strings and Numbers
invoice_number = invoice_file.replace("valid-invoice-", "").replace(".pdf", "")
print(f"Invoice number: {invoice_number}")

total = amount * 1.21
print(f"Total with VAT: {total} EUR")

# Step 3: Lists
invoices = [
    "valid-invoice-N8N-20260907-7F3C9A.pdf",
    "missing-deadline-N8N-MISSING-20260907-3C8D.pdf",
    "incorrect-document-meeting-notes.pdf"
]
print(f"Total invoices: {len(invoices)}")

# Step 5: Conditions (Day 19 fix)
print("\n--- Validation fix ---")
for file in invoices:
    if "meeting-notes" in file:
        print(f"❌ {file} -> Validation Failed: incorrect document")
        print(f"   Trigger: Invoice Processing - Failure Notification")
    elif "MISSING" in file:
        print(f"⚠️ {file} -> Validation Failed: payment_deadline is missing")
        print(f"   Trigger: Invoice Processing - Failure Notification")
    else:
        print(f"✅ {file} -> Validation Passed -> Save to Airtable")

# Step 4: Dictionaries
invoice_record = {
    "invoice_number": invoice_number,
    "vendor": vendor_name,
    "amount": amount,
    "payment_deadline": "2026-09-30",
    "status": "pending_approval"
}
print(f"\nRecord: {invoice_record}")
print(f"Vendor from record: {invoice_record['vendor']}")
invoice_record["status"] = "approved"
print(f"Updated status: {invoice_record['status']}")

# Step 6: Loops - retry
print("\n--- Retry simulation ---")
attempt = 0
max_attempts = 3
while attempt < max_attempts:
    attempt += 1
    print(f"Attempt {attempt}/{max_attempts} to save to Airtable...")
    if attempt == 3:
        print("✅ Success!")
        break
    else:
        print("❌ Failed, retrying...")

# Step 7: Functions
print("\n--- Functions ---")
def process_invoice(file_name, vendor, amount):
    number = file_name.replace("valid-invoice-", "").replace(".pdf", "")
    total_vat = amount * 1.21
    record = {
        "invoice_number": number,
        "vendor": vendor,
        "amount": total_vat,
        "status": "processed"
    }
    return record

result = process_invoice("valid-invoice-N8N-20260907-7F3C9A.pdf", "Acme Corp", 1250)
print(f"Function result: {result}")