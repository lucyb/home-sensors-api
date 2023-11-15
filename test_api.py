from api import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_post_default_accepts_payload():
    test_data = {
        "nickname": "weather-test",
        "model": "grow",
        "uid": "e6614c775b8c4035",
        "timestamp": "2022-09-04T10:40:24Z",
    }

    response = client.post("/", json=test_data)
    assert response.status_code == 200