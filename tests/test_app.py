import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture
def client():
    return TestClient(app)


def test_unregister_participant_removes_email(client):
    # Arrange
    activity_name = "Chess Club"
    email = "student@example.com"
    activities[activity_name]["participants"] = [
        participant for participant in activities[activity_name]["participants"] if participant != email
    ]

    # Act
    client.post(f"/activities/{activity_name}/signup?email={email}")
    response = client.delete(f"/activities/{activity_name}/unregister?email={email}")

    # Assert
    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]
