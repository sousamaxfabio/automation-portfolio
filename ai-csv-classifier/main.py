import csv
import os
import logging
import time
import json
from dotenv import load_dotenv
from openai import OpenAI

# --- SETUP ---
load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def get_client():
    """[ ] Environment variables - Securely load API key"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logging.error("OPENAI_API_KEY not found in.env")
        raise ValueError("Missing OPENAI_API_KEY")
    logging.info("OpenAI client ready")
    return OpenAI(api_key=api_key)

def read_input_file(filepath):
    """[ ] Functions - Read CSV with exception handling"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        logging.info(f"Read {len(rows)} rows from {filepath}")
        print(f"\n📖 Reading {filepath}... {len(rows)} rows found")
        return rows
    except FileNotFoundError:
        logging.error(f"File not found: {filepath}")
        print(f"❌ File not found: {filepath}")
        return []
    except Exception as e:
        logging.error(f"Error reading file: {e}")
        print(f"❌ Error reading file: {e}")
        return []

def validate_row(row):
    """[ ] Functions + [ ] Exception handling - Validate required fields"""
    required = ['id', 'name', 'description']
    for field in required:
        if not row.get(field) or not str(row.get(field)).strip():
            return False, f"Missing or empty field: {field}"
    return True, "valid"

def classify_product(client, product_name, description):
    """[ ] Functions + [ ] Exception handling - Call API with retry"""
    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Classify the product into ONE category: Electronics, Fitness, Kitchen, Education, Office, Lifestyle. Reply with JSON: {\"category\": \"...\", \"confidence\": 0.95}"},
                    {"role": "user", "content": f"Product: {product_name} - {description}"}
                ],
                response_format={"type": "json_object"},
                temperature=0.2
            )
            result = json.loads(response.choices[0].message.content)
            return result.get("category", "Unknown"), result.get("confidence", 0.0)

        except Exception as e:
            logging.warning(f"Attempt {attempt}/{max_retries} failed for '{product_name}': {e}")
            print(f" ⚠️ Retry {attempt}/{max_retries} for {product_name}...")
            if attempt == max_retries:
                logging.error(f"Failed to classify '{product_name}' after {max_retries} retries: {e}")
                return "Error", 0.0
            time.sleep(2)

def save_results(results, filepath):
    """[ ] Functions - Save results"""
    try:
        fieldnames = ['id', 'name', 'description', 'price', 'category', 'confidence', 'status']
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        logging.info(f"Saved {len(results)} rows to {filepath}")
        print(f"\n💾 Saving {filepath}... ✅ Done! {len(results)} rows")
        return True
    except Exception as e:
        logging.error(f"Error saving results: {e}")
        print(f"❌ Error saving: {e}")
        return False

def main():
    """[ ] Clear terminal messages - Main flow"""
    print("\n" + "="*50)
    print("DAY 26 — Project 3 Part 2 — Refactored Pipeline")
    print("Model: gpt-4o-mini")
    print("="*50)

    try:
        client = get_client()
        print("✅ OpenAI client ready\n")
    except Exception as e:
        print(f"❌ Cannot continue: {e}")
        return

    raw_rows = read_input_file("input.csv")
    if not raw_rows:
        return

    valid_rows = []
    invalid_count = 0

    for row in raw_rows:
        is_valid, msg = validate_row(row)
        if is_valid:
            valid_rows.append(row)
        else:
            invalid_count += 1
            logging.warning(f"Invalid row id={row.get('id','?')}: {msg}")
            print(f" ❌ Invalid row id={row.get('id','?')}: {msg}")

    print(f"✅ Valid rows: {len(valid_rows)} | Invalid: {invalid_count}\n")
    logging.info(f"Validation complete - Valid: {len(valid_rows)}, Invalid: {invalid_count}")

    results = []
    for row in valid_rows:
        print(f"🚀 Sending to API: {row['name']}... ", end="")
        category, conf = classify_product(client, row['name'], row['description'])
        status = "classified" if category!= "Error" else "failed"
        print(f"{'✅' if status=='classified' else '❌'} {category} (conf: {conf})")
        results.append({
            'id': row['id'],
            'name': row['name'],
            'description': row['description'],
            'price': row.get('price',''),
            'category': category,
            'confidence': conf,
            'status': status
        })

    save_results(results, "results.csv")

    print("\n--- Summary ---")
    print(f"Total read: {len(raw_rows)}")
    print(f"Valid: {len(valid_rows)}")
    print(f"Invalid: {invalid_count}")
    print(f"Classified: {len([r for r in results if r['status']=='classified'])}")
    print(f"Check app.log for detailed logs")
    print("="*50)

if __name__ == "__main__":
    main()