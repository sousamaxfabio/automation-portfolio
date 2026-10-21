from unittest.mock import patch

from external_service import get_external_status


def test_external_status_success():
    fake_response = {
        "status": "ok",
        "service": "external-api"
    }

    with patch("external_service.httpx.get") as mock_get:
        mock_get.return_value.json.return_value = fake_response
        mock_get.return_value.raise_for_status.return_value = None

        result = get_external_status()

        assert result["status"] == "ok"
        assert result["service"] == "external-api"

        mock_get.assert_called_once()