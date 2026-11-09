import pytest
from app import create_app

@pytest.fixture()
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_list_tasks_returns_initial_task(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.get_json()) == 1

def test_create_task(client):
    response = client.post("/tasks", json={"title": "Build a pipeline"})
    assert response.status_code == 201
    assert response.get_json()["title"] == "Build a pipeline"

def test_create_task_requires_title(client):
    response = client.post("/tasks", json={"title": " "})
    assert response.status_code == 400

def test_update_task(client):
    response = client.patch("/tasks/1", json={"done": True})
    assert response.status_code == 200
    assert response.get_json()["done"] is True

def test_update_missing_task(client):
    response = client.patch("/tasks/999", json={"done": True})
    assert response.status_code == 404

def test_delete_task(client):
    response = client.delete("/tasks/1")
    assert response.status_code == 204
