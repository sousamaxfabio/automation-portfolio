import os
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from fastapi.testclient import TestClient


PROJECT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_DIR))

import app as app_module


client = TestClient(app_module.app)


class TestOpsPilotApi(unittest.TestCase):
    def test_health_endpoint(self):
        response = client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "healthy")
        self.assertEqual(response.json()["service"], "opspilot-ai")

    def test_rejects_invalid_input(self):
        response = client.post(
            "/triage",
            json={
                "requester": "Fabio",
                "title": "Hi",
                "description": "Too short",
            },
        )

        self.assertEqual(response.status_code, 422)

    def test_reports_missing_api_configuration(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY": ""}):
            response = client.post(
                "/triage",
                json={
                    "requester": "Fabio",
                    "title": "Printer not working",
                    "description": "The office printer has stopped responding.",
                },
            )

        self.assertEqual(response.status_code, 503)
        self.assertEqual(
            response.json()["detail"],
            "AI service is not configured",
        )

    def test_returns_structured_triage_result(self):
        fake_openai_response = Mock()
        fake_openai_response.output_text = (
            '{"category":"maintenance",'
            '"urgency":"critical",'
            '"summary":"Water leak near electrical equipment",'
            '"recommended_action":"Isolate the area and contact maintenance",'
            '"confidence":0.98}'
        )

        fake_client = Mock()
        fake_client.responses.create.return_value = fake_openai_response

        with (
            patch.dict(
                os.environ,
                {
                    "OPENAI_API_KEY": "test-key",
                    "OPENAI_MODEL": "test-model",
                },
            ),
            patch.object(app_module, "OpenAI", return_value=fake_client),
        ):
            response = client.post(
                "/triage",
                json={
                    "requester": "Maria",
                    "title": "Water leak in office",
                    "description": (
                        "Water is entering near an electrical socket."
                    ),
                },
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["category"], "maintenance")
        self.assertEqual(response.json()["urgency"], "critical")
        self.assertEqual(response.json()["confidence"], 0.98)
        self.assertTrue(response.json()["request_id"])


if __name__ == "__main__":
    unittest.main()