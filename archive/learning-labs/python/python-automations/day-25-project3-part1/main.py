import os
import csv
import json
from dotenv import load_dotenv

# Load env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

print(f"DAY 25 — Project 3 Part 1")
print(f"Model: {model}")
print(f"Using Key: {api_key[:10]}... (from.env)" if api_key else "No API key found!")

# Check if openai library is installed, if not use fallback
try:
    from openai import OpenAI
    client = OpenAI(api_key=api_key)
    USE_OPENAI = True
    print("✅ OpenAI client ready\n")
except ImportError:
    print("⚠️ openai library not installed, will use mock classification")
    USE_OPENAI = False

INPUT_FILE = "input.csv"
OUTPUT_FILE = "results.csv"
REQUIRED_FIELDS = ["name", "description"]

# 1. Read CSV
rows = []
invalid_rows = []

print(f"📖 Reading {INPUT_FILE}...")
with open(INPUT_FILE, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader, start=1):
        # 2. Validate required fields
        missing = [field for field in REQUIRED_FIELDS if not row.get(field) or not row.get(field).strip()]
        if missing:
            print(f"❌ Row {i} INVALID — missing: {missing} -> {row}")
            invalid_rows.append({**row, "error": f"Missing fields: {missing}"})
            continue
        rows.append(row)

print(f"✅ Valid rows: {len(rows)} | Invalid: {len(invalid_rows)}\n")

# 3. Send to API + 4. Process JSON
results = []

for row in rows:
    name = row["name"]
    desc = row["description"]

    print(f"🚀 Sending to API: {name}...")

    category = "Unknown"
    try:
        if USE_OPENAI:
            # Real OpenAI classification
            prompt = f"""
Classify this product into ONE of these categories:
Electronics, Sports, Kitchen, Fitness, Education, Other.

Product: {name}
Description: {desc}

Respond ONLY with valid JSON like: {{"category": "Electronics", "confidence": 0.95}}
"""
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                timeout=15
            )
            # Parse JSON response
            content = response.choices[0].message.content.strip()
            # Clean markdown code block if present
            if content.startswith("```"):
                content = content.replace("```json", "").replace("```", "").strip()

            parsed = json.loads(content)
            category = parsed.get("category", "Other")
            confidence = parsed.get("confidence", 0)
            print(f" ✅ API SUCCESS -> {category} (conf: {confidence})")
        else:
            # Fallback mock logic
            desc_lower = desc.lower()
            if "mouse" in desc_lower or "battery" in desc_lower:
                category = "Electronics"
            elif "shoe" in desc_lower or "running" in desc_lower or "jogging" in desc_lower:
                category = "Sports"
            elif "coffee" in desc_lower or "kitchen" in desc_lower:
                category = "Kitchen"
            elif "yoga" in desc_lower or "workout" in desc_lower:
                category = "Fitness"
            elif "python" in desc_lower or "book" in desc_lower:
                category = "Education"
            else:
                category = "Other"
            print(f" ✅ MOCK SUCCESS -> {category}")

    except Exception as e:
        print(f" ❌ API FAILED -> {e}")
        category = f"ERROR: {e}"

    results.append({
        "id": row["id"],
        "name": name,
        "description": desc,
        "category": category,
        "status": "classified"
    })

# Add invalid rows to results too
for row in invalid_rows:
    results.append({
        "id": row.get("id", ""),
        "name": row.get("name", ""),
        "description": row.get("description", ""),
        "category": "INVALID",
        "status": row.get("error", "")
    })

# 5. Save results CSV
print(f"\n💾 Saving {OUTPUT_FILE}...")
with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "description", "category", "status"])
    writer.writeheader()
    writer.writerows(results)

print(f"✅ Done! Saved {len(results)} rows to {OUTPUT_FILE}")
print("\n--- Preview ---")
for r in results[:3]:
    print(r)