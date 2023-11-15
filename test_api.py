from api import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_post_default_accepts_payload():
    test_data = {
        "nickname": "weather-test",
    }

    response = client.post("/", json=test_data)
    assert response.status_code == 200