from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_addition():
    response = client.post("/calculate", json={"operation": "add", "a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 8}