from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_status():
    response = client.get("/")
    assert response.status_code == 200

def test_root_content():
    response = client.get("/")
    assert response.json() == {"status": "healthy", "message": "Containerized microservice running on AWS!"}

def test_info_route():
    response = client.get("/info")
    assert response.status_code == 200

def test_invalid_route():
    response = client.get("/nonexistent")
    assert response.status_code == 404