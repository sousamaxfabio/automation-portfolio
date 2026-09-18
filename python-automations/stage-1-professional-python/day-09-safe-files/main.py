import json
from pathlib import Path


folder = Path(__file__).parent

input_folder = folder / "input"
input_folder.mkdir(parents=True, exist_ok=True)
input_file = input_folder / "requests.json"

output_folder = folder / "output"
output_folder.mkdir(parents=True, exist_ok=True)
output_file = output_folder / "processed_requests.json"

if not input_file.exists():
    print(f"Input file not found: {input_file}")
elif output_file.exists():
    print(f"Output already exists. Nothing was overwritten: {output_file.name}")
else:
    with input_file.open("r", encoding="utf-8") as file:
        service_requests = json.load(file)

    with output_file.open("x", encoding="utf-8") as file:
        json.dump(service_requests, file, indent=4)

    print(f"Output created safely: {output_file.name}")