import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_DIR))

from main import read_input_file, save_results, validate_row


class TestValidation(unittest.TestCase):
    def test_accepts_complete_row(self):
        row = {
            "id": "1",
            "name": "Wireless Mouse",
            "description": "Ergonomic office mouse",
        }

        is_valid, message = validate_row(row)

        self.assertTrue(is_valid)
        self.assertEqual(message, "valid")

    def test_rejects_missing_name(self):
        row = {
            "id": "1",
            "name": "",
            "description": "Ergonomic office mouse",
        }

        is_valid, message = validate_row(row)

        self.assertFalse(is_valid)
        self.assertEqual(message, "Missing or empty field: name")


class TestCsvFiles(unittest.TestCase):
    def test_reads_csv_input(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_path = Path(temp_dir) / "input.csv"
            input_path.write_text(
                "id,name,description,price\n"
                "1,Wireless Mouse,Ergonomic office mouse,25.99\n",
                encoding="utf-8",
            )

            rows = read_input_file(input_path)

            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["name"], "Wireless Mouse")

    def test_saves_csv_output(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "results.csv"
            results = [
                {
                    "id": "1",
                    "name": "Wireless Mouse",
                    "description": "Ergonomic office mouse",
                    "price": "25.99",
                    "category": "Office",
                    "confidence": "0.95",
                    "status": "classified",
                }
            ]

            saved = save_results(results, output_path)

            self.assertTrue(saved)
            self.assertTrue(output_path.exists())
            self.assertIn("Wireless Mouse", output_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()