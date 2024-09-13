import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.parametrize("operation,x,y,expected", [
    ("add", 5, 3, 8),
    ("subtract", 10, 4, 6),
    ("multiply", 6, 7, 42),
    ("divide", 1, 2, 0.5),
    ("add", -5, 3, -2),
    ("subtract", 0, 0, 0),
    ("multiply", -2, -3, 6),
])
def test_calculator_valid_operations(operation, x, y, expected):
    response = client.post("/calculate/", json={"operation": operation, "x": x, "y": y})
    assert response.status_code == 200
    assert response.json() == {"operation": operation, "x": x, "y": y, "result": expected}

def test_calculator_division_by_zero():
    response = client.post("/calculate/", json={"operation": "divide", "x": 10, "y": 0})
    assert response.status_code == 400
    assert "Division by zero is not allowed" in response.json()["detail"]

def test_calculator_invalid_operation():
    response = client.post("/calculate/", json={"operation": "power", "x": 2, "y": 3})
    assert response.status_code == 400
    assert "Invalid operation" in response.json()["detail"]

def test_calculator_float_input():
    response = client.post("/calculate/", json={"operation": "add", "x": 2.5, "y": 3.7})
    assert response.status_code == 200
    assert pytest.approx(response.json()["result"], 0.01) == 6.2

def test_calculator_string_input():
    response = client.post("/calculate/", json={"operation": "add", "x": "2", "y": "3"})
    assert response.status_code == 422  # Validation error

def test_calculator_missing_parameter():
    response = client.post("/calculate/", json={"operation": "add", "x": 2})
    assert response.status_code == 422  # Validation error

def test_calculator_extra_parameter():
    response = client.post("/calculate/", json={"operation": "add", "x": 2, "y": 3, "z": 4})
    assert response.status_code == 200
    assert response.json() == {"operation": "add", "x": 2, "y": 3, "result": 5}