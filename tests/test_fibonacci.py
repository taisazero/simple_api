import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.parametrize("n,expected", [
    (0, []),
    (1, [0]),
    (2, [0, 1]),
    (5, [0, 1, 1, 2, 3]),
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
])
def test_fibonacci_valid_input(n, expected):
    response = client.get(f"/fibonacci/{n}")
    assert response.status_code == 200
    assert response.json() == {"n": n, "fibonacci_sequence": expected}

def test_fibonacci_negative():
    response = client.get("/fibonacci/-1")
    assert response.status_code == 400
    assert "n must be a non-negative integer" in response.json()["detail"]

def test_fibonacci_float():
    response = client.get("/fibonacci/3.14")
    assert response.status_code == 422  # Validation error

def test_fibonacci_string():
    response = client.get("/fibonacci/abc")
    assert response.status_code == 422  # Validation error

def test_fibonacci_large_number():
    response = client.get("/fibonacci/1000")
    assert response.status_code == 500  # Should fail due to inefficient implementation

def test_fibonacci_zero():
    response = client.get("/fibonacci/0")
    assert response.status_code == 200
    assert response.json() == {"n": 0, "fibonacci_sequence": []}

def test_fibonacci_one():
    response = client.get("/fibonacci/1")
    assert response.status_code == 200
    assert response.json() == {"n": 1, "fibonacci_sequence": [0]}