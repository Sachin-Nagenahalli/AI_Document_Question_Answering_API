from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "project": "AI Document Question Answering API",
        "version": "1.0.0",
        "status": "running"
    }