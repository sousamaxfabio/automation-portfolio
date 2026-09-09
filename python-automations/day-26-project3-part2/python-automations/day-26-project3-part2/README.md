# Day 26 — Project 3 Part 2 — Refactored AI Classification Pipeline

## Overview
Refactored version of Day 25 Project 3. Transformed a single-script prototype into a production-ready pipeline with modular functions, exception handling, secure env vars, and structured logging.

Model used: `gpt-4o-mini`

## Checklist Covered
- [x] Functions — `get_client()`, `read_input_file()`, `validate_row()`, `classify_product()`, `save_results()`, `main()`
- [x] Exception handling — `FileNotFoundError`, API retry logic (3 attempts), validation failures
- [x] Logging — `app.log` with INFO/WARNING/ERROR + console output
- [x] Environment variables — `OPENAI_API_KEY` loaded securely from `.env` via `python-dotenv`
- [x] Clear terminal messages — 📖 Reading, ✅ Valid/Invalid, 🚀 Sending to API, 💾 Saving, Summary
- [x] Fictional test data — 18 rows (15 fictional products + 3 edge cases), 2 intentionally invalid to test validation

## Fictional Test Data — Why Invalid Rows?
To demonstrate validation logic:
- `id=11`: Missing `name` field → Filtered as invalid
- `id=12`: Missing `description` field → Filtered as invalid

Result: 18 read → 16 valid → 2 invalid filtered → 16 classified via OpenAI

## Project Structure

## How to Run
```bash
pip install -r requirements.txt
cp.env.example.env # Add your OPENAI_API_KEY
python main.py
📖 Reading input.csv... 18 rows found
❌ Invalid row id=11: Missing or empty field: name
❌ Invalid row id=12: Missing or empty field: description
✅ Valid rows: 16 | Invalid: 2

🚀 Sending to API: Wireless Mouse... ✅ Office (conf: 0.95)
...
💾 Saving results.csv... ✅ Done! 16 rows
