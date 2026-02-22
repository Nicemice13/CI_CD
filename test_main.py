from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "FastAPI on Railway"}

def test_read_root_status_field():
    response = client.get("/")
    assert "status" in response.json()
    assert response.json()["status"] == "ok"

def test_read_root_message_field():
    response = client.get("/")
    assert "message" in response.json()
    assert response.json()["message"] == "FastAPI on Railway"

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_health_check_status():
    response = client.get("/health")
    assert "status" in response.json()
    assert response.json()["status"] == "healthy"

def test_root_content_type():
    response = client.get("/")
    assert response.headers["content-type"] == "application/json"

def test_health_content_type():
    response = client.get("/health")
    assert response.headers["content-type"] == "application/json"

def test_invalid_endpoint():
    response = client.get("/invalid")
    assert response.status_code == 404

def test_root_method_get_only():
    response = client.post("/")
    assert response.status_code == 405

def test_health_method_get_only():
    response = client.post("/health")
    assert response.status_code == 405

def test_root_put_not_allowed():
    response = client.put("/")
    assert response.status_code == 405

def test_root_delete_not_allowed():
    response = client.delete("/")
    assert response.status_code == 405

def test_health_put_not_allowed():
    response = client.put("/health")
    assert response.status_code == 405

def test_health_delete_not_allowed():
    response = client.delete("/health")
    assert response.status_code == 405

def test_root_response_type():
    response = client.get("/")
    assert isinstance(response.json(), dict)

def test_health_response_type():
    response = client.get("/health")
    assert isinstance(response.json(), dict)

def test_multiple_root_calls():
    for _ in range(5):
        response = client.get("/")
        assert response.status_code == 200

def test_multiple_health_calls():
    for _ in range(5):
        response = client.get("/health")
        assert response.status_code == 200

def test_root_and_health_sequence():
    response1 = client.get("/")
    response2 = client.get("/health")
    assert response1.status_code == 200
    assert response2.status_code == 200
