from api import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_post_default():
    response = client.post("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}