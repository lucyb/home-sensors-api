from fastapi import FastAPI
from fastapi.testclient import TestClient

#TODO import from the app
app = FastAPI()

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}