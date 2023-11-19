from api import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_get_default_returns_success():
    response = client.get("/")
    assert response.status_code == 200

def test_post_urban_accepts_payload():
    test_data = {
        "nickname": "weather-test",
        "model": "urban",
        "uid": "e6614c775b8c4035",
        "timestamp": "2022-09-04T10:40:24Z",
        "readings": {
            "temperature": 27.57,
            "humidity": 49.33,
            "pressure": 996.22,
            "noise": 0.87,
            "pm1": 9,
            "pm2_5": 4,
            "pm10": 2,
            "voltage": 4.035,
        }
    }

    response = client.post("/urban", json=test_data)
    assert response.status_code == 200