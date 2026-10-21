# Day 23 — Airtable Integration: Invoice Processing

## Overview
Automates invoice validation and uploads valid invoices to Airtable table `Invoices-final`.
Filters non-invoice documents and invoices missing payment deadlines.

## Final Working State — 2026-09-08 ✅

**Airtable Table: `Invoices-final`**
- `Name` (Primary)
- `Vendor`
- `Amount`
- `Status`
- `notes` (lowercase)

Result: 2 records created, 2 filtered — exactly as required.

## Setup

### .env
> Use TABLE NAME `Invoices-final`, not Table ID `tbl6sJbb3oMuQR7Wj`. Prevents 403.

Token scopes:
- data.records:read
- data.records:write
- schema.bases:read

### Dependencies

## How It Works
1. `load_dotenv(override=True)` loads env
2. `Api(TOKEN).table(BASE_ID, TABLE_NAME)` connects
3. `table.schema()` gets real field names dynamically
4. `os.walk()` recursively finds PDFs in `day-19-production-improvements/sample-invoices/`
5. Validation: skips non-invoice and missing-deadline
6. Creates record with only existing fields:
```python
actual_fields = [f.name for f in schema.fields]
record = {k: v for k, v in full_record.items() if k in actual_fields}
table.create(record)

**3. Save: `Ctrl+S`**

You should now see the green checkmarks `✅ SUCCESS` preview in VSCode markdown preview (Ctrl+Shift+V).

Done — tell me when it's saved and I'll give you the git commit command for your usual docs pattern.