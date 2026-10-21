import os
from unittest.mock import Mock, patch

from fastapi.testclient import TestClient

from main import app


client = TestClient(app)

API_KEY = os.getenv("API_KEY")


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_readiness_success():
    fake_cursor = Mock()
    fake_cursor.fetchone.return_value = (1,)

    fake_connection = Mock()
    fake_connection.cursor.return_value = fake_cursor

    with patch(
        "main.get_connection",
        return_value=fake_connection,
    ):
        response = client.get("/readiness")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ready",
        "database": "connected",
    }

    fake_cursor.execute.assert_called_once_with("SELECT 1")
    fake_cursor.close.assert_called_once()
    fake_connection.close.assert_called_once()


def test_readiness_database_failure():
    with patch(
        "main.get_connection",
        side_effect=Exception("Database unavailable"),
    ):
        response = client.get("/readiness")

    assert response.status_code == 503
    assert response.json() == {
        "detail": "Database not available"
    }


def test_requests_without_api_key():
    response = client.get("/requests")

    assert response.status_code == 422


def test_requests_with_wrong_api_key():
    response = client.get(
        "/requests",
        headers={"x-api-key": "wrong-key"},
    )

    assert response.status_code == 401


def test_requests_with_correct_api_key():
    response = client.get(
        "/requests",
        headers={"x-api-key": API_KEY},
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_request_success():
    response = client.post(
        "/requests",
        headers={"x-api-key": API_KEY},
        json={
            "customer_id": 1,
            "category": "billing",
            "priority": "medium",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["customer_id"] == 1
    assert data["category"] == "billing"
    assert data["priority"] == "medium"
    assert "id" in data


def test_create_request_invalid_priority():
    response = client.post(
        "/requests",
        headers={"x-api-key": API_KEY},
        json={
            "customer_id": 1,
            "category": "billing",
            "priority": "urgent",
        },
    )

    assert response.status_code == 422


def test_create_request_unknown_customer():
    response = client.post(
        "/requests",
        headers={"x-api-key": API_KEY},
        json={
            "customer_id": 999,
            "category": "billing",
            "priority": "high",
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Customer not found"